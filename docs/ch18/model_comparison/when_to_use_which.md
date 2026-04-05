# When to Use Which Model

Selecting a short rate model is not merely a theoretical exercise: the choice has direct consequences for derivative prices, hedging strategies, and risk management outputs. This section provides a practical decision framework for choosing among the Vasicek, CIR, Hull-White, and Black-Karasinski models, organized by use case rather than by model.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Match specific pricing and risk management tasks to the appropriate short rate model
    2. Apply a structured decision framework based on product type, market environment, and computational constraints
    3. Identify situations where model limitations create material pricing risk
    4. Justify model selection choices in a production setting

---

## Decision Framework

The model selection decision depends on five dimensions, each carrying different weight depending on the application.

| Dimension | Key Question | Models Affected |
|:---|:---|:---|
| **Curve fit** | Must the model reprice all observed bonds exactly? | Time-homogeneous models fail; Hull-White and Black-Karasinski succeed |
| **Rate positivity** | Can the product tolerate negative rates? | Vasicek and Hull-White allow negative rates; CIR and Black-Karasinski do not |
| **Analytical tractability** | Are closed-form prices needed for speed or calibration? | Vasicek, CIR, Hull-White offer formulas; Black-Karasinski requires numerics |
| **Volatility structure** | Does the volatility depend on the rate level? | CIR ($\sigma\sqrt{r}$) and Black-Karasinski ($\sigma r$) are level-dependent |
| **Computational budget** | How much time is available for pricing? | Analytical models are fastest; trees and Monte Carlo add cost |

---

## Use Case 1: Pricing Vanilla Interest Rate Derivatives

**Products:** Caps, floors, European swaptions, bond options

**Recommended model: Hull-White**

The Hull-White model is the standard production model for vanilla rate derivatives because it simultaneously achieves:

1. **Exact fit to the initial yield curve**, ensuring no-arbitrage against observed bond prices
2. **Closed-form pricing** for caps, floors, and European swaptions via Black-type formulas
3. **Fast calibration** to at-the-money cap or swaption volatilities with only two parameters ($a$, $\sigma$)

The cap price in the Hull-White model decomposes into a sum of caplets, each priced analytically:

$$
\text{Caplet}(T_{i-1}, T_i, K) = (1 + \delta K)\,\text{Put}\!\left(\frac{1}{1 + \delta K},\, T_{i-1},\, T_i\right)
$$

where $\delta = T_i - T_{i-1}$ and the put on a zero-coupon bond has the Black-type formula with volatility $\sigma_P = \frac{\sigma}{a}(1 - e^{-a\delta})\sqrt{\frac{1 - e^{-2aT_{i-1}}}{2a}}$.

!!! tip "When to Deviate"
    Consider CIR instead of Hull-White when the interest rate environment makes negative rates extremely unlikely (e.g., emerging market currencies with high rate levels) and level-dependent volatility improves the cap smile fit.

---

## Use Case 2: Pricing Path-Dependent and Early-Exercise Derivatives

**Products:** Bermudan swaptions, callable bonds, range accruals, TARNs

**Recommended model: Hull-White (tree) or Black-Karasinski (tree)**

Path-dependent and early-exercise products require backward induction on a lattice or simulation with regression. The Hull-White trinomial tree provides:

1. **Exact curve fit** via the deterministic shift $\alpha(t_i)$ at each time step
2. **Efficient backward induction** with recombining nodes
3. **Early exercise** handled by comparing continuation and exercise values at each node

For products where log-normal rate dynamics better match the market (e.g., when cap implied volatilities exhibit a pronounced smile), the Black-Karasinski trinomial tree is preferred despite the loss of analytical bond pricing.

!!! info "Proposition: Tree Complexity"
    For an $N$-step trinomial tree with $J$ nodes per time slice:

    - **Hull-White tree:** bond prices at each node computed analytically via $P(t_i, T) = A(t_i, T)e^{-B(t_i, T)r_{ij}}$
    - **Black-Karasinski tree:** bond prices at each node require backward induction through the tree, adding $O(N \cdot J)$ operations per bond

---

## Use Case 3: Risk Management and Scenario Analysis

**Products:** Value-at-Risk, stress testing, scenario generation, economic capital

**Recommended model: Vasicek or CIR under the physical measure**

For risk management, the model must capture the real-world dynamics of rates, not just risk-neutral pricing. The key requirements are:

1. **Stationary distribution** for long-horizon scenarios
2. **Interpretable parameters** ($\kappa$, $\theta$, $\sigma$) with clear economic meaning
3. **Efficient simulation** for large Monte Carlo engines

The Vasicek model under the physical measure $\mathbb{P}$ provides the conditional distribution

$$
r(t+\Delta) \mid r(t) \sim \mathcal{N}\!\left(\theta^{\mathbb{P}} + (r(t) - \theta^{\mathbb{P}})e^{-\kappa^{\mathbb{P}}\Delta},\; \frac{(\sigma^{\mathbb{P}})^2}{2\kappa^{\mathbb{P}}}(1 - e^{-2\kappa^{\mathbb{P}}\Delta})\right)
$$

which supports exact sampling without discretization error.

!!! warning "Physical vs Risk-Neutral Parameters"
    The parameters under $\mathbb{P}$ and $\mathbb{Q}$ differ by the market price of risk $\lambda$:

    $$
    \kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \lambda, \qquad \theta^{\mathbb{Q}} = \frac{\kappa^{\mathbb{P}}\theta^{\mathbb{P}}}{\kappa^{\mathbb{P}} + \lambda}
    $$

    Risk management models must be calibrated to historical data (physical measure), while pricing models are calibrated to market prices (risk-neutral measure).

---

## Use Case 4: Pedagogical and Prototyping Applications

**Products:** Teaching, research prototypes, benchmark computations

**Recommended model: Vasicek**

The Vasicek model is the natural starting point because:

1. Every formula is available in closed form (bond prices, yields, options, caps, swaptions)
2. The Ornstein-Uhlenbeck process has well-known mathematical properties
3. Parameter estimation from historical data is straightforward (regression on $\Delta r$)
4. The model illustrates all key concepts (mean reversion, affine structure, Riccati equations) without the complications of time-dependent parameters

Once the theoretical framework is understood via Vasicek, extending to Hull-White (add $\theta(t)$) or CIR (change diffusion to $\sigma\sqrt{r}$) is a natural next step.

---

## Use Case 5: Positive-Rate Environments and Inflation Modeling

**Products:** Real rate derivatives, inflation-linked bonds, emerging market rates

**Recommended model: CIR**

When negative rates are economically meaningless (e.g., modeling real interest rates or rates in high-yield economies), the CIR model is preferred because:

1. **Rate positivity** is guaranteed under the Feller condition $2\kappa\theta \ge \sigma^2$
2. **Level-dependent volatility** $\sigma\sqrt{r}$ ensures that volatility vanishes as rates approach zero, preventing the model from pushing rates negative
3. The **non-central chi-squared** transition density provides exact simulation

The variance of $r(t)$ in CIR is

$$
\text{Var}^{\mathbb{Q}}[r(t)] = r(0)\,\frac{\sigma^2}{\kappa}(e^{-\kappa t} - e^{-2\kappa t}) + \theta\,\frac{\sigma^2}{2\kappa}(1 - e^{-\kappa t})^2
$$

which depends on the current rate level -- a feature absent from Gaussian models.

---

## Use Case 6: Cap/Floor Smile Calibration

**Products:** Caps and floors across multiple strikes, exotic products sensitive to the smile

**Recommended model: Black-Karasinski or shifted Hull-White**

A single Hull-White model with constant $\sigma$ produces flat caplet implied volatilities across strikes (the smile is trivial because the forward rate is log-normal under the forward measure). To capture the observed smile:

- **Black-Karasinski** naturally produces a volatility smile because the rate distribution is log-normal, not normal. The smile shape depends on the level of rates and the mean reversion speed.
- **Shifted Hull-White** adds a displacement parameter $\delta$ so that $r(t) + \delta$ follows a Hull-White process, combining analytical tractability with a non-trivial smile.

!!! tip "Trade-off"
    Black-Karasinski requires numerical pricing (trees or Monte Carlo) for every instrument, making calibration slower. If the smile is not a primary concern, Hull-White with its analytical formulas is preferable.

---

## Decision Flowchart

The following logic summarizes the model selection process:

1. **Is exact curve fit required?**
    - No $\to$ Vasicek or CIR (time-homogeneous models)
    - Yes $\to$ Continue to step 2

2. **Are negative rates acceptable?**
    - Yes $\to$ Hull-White
    - No $\to$ CIR with time-dependent $\theta(t)$ (extended CIR) or Black-Karasinski

3. **Are closed-form option prices needed?**
    - Yes $\to$ Hull-White
    - No $\to$ Black-Karasinski (if log-normal dynamics needed)

4. **Is the volatility smile important?**
    - No $\to$ Hull-White
    - Yes $\to$ Black-Karasinski or shifted Hull-White

5. **Is this for risk management (physical measure)?**
    - Yes $\to$ Vasicek or CIR with $\mathbb{P}$-calibrated parameters

---

## Common Pitfalls in Model Selection

!!! warning "Pitfall 1: Using Time-Homogeneous Models for Derivative Pricing"
    Vasicek and CIR cannot match the observed yield curve exactly. Using them for derivative pricing introduces a static calibration error that contaminates all prices. The error is largest for long-dated products and products sensitive to the entire curve shape.

!!! warning "Pitfall 2: Ignoring Negative Rates in Hull-White"
    In low-rate environments, the Hull-White model can generate significantly negative rates. For products with payoffs that depend on $\max(r, 0)$ (e.g., floored floaters), this creates pricing artifacts. Monitor the probability $\mathbb{P}(r(t) < 0)$ and consider displaced or log-normal alternatives if it exceeds a few percent.

!!! warning "Pitfall 3: Over-Parameterizing with Time-Dependent Volatility"
    Making $\sigma(t)$ time-dependent in Hull-White allows perfect calibration to the entire cap volatility curve, but the resulting model may be unstable: small changes in market data can produce large swings in $\sigma(t)$, degrading hedge ratios and forward-starting derivative prices.

!!! warning "Pitfall 4: Confusing Physical and Risk-Neutral Calibration"
    A model calibrated to market option prices (risk-neutral) should not be used for scenario generation (physical measure), and vice versa. The mean reversion speed and long-run mean differ between measures.

---

## Summary

Model selection in short rate modeling is driven by the specific application rather than by inherent model superiority. Hull-White is the default for vanilla derivative pricing due to its exact curve fit and analytical tractability. CIR is preferred when rate positivity and level-dependent volatility are essential. Vasicek serves as the pedagogical foundation and is adequate for risk management scenario generation. Black-Karasinski fills the niche where log-normal dynamics and smile calibration outweigh the cost of numerical pricing. The decision framework above provides a structured approach, but practitioners should validate any model choice against the specific products, market conditions, and computational constraints of their application.

---

## Exercises

**Exercise 1.** A bank needs to price a portfolio of European caps on 3-month SOFR for maturities 1Y through 10Y. The portfolio is ATM and must be priced within 1 second for real-time risk. Using the decision flowchart, justify why Hull-White is the recommended model. What would change if the caps were deep OTM?

??? success "Solution to Exercise 1"
    Following the decision flowchart:

    1. **Is exact curve fit required?** Yes. The caps must be priced consistently with observed bond prices to avoid arbitrage. Each caplet is a put option on a zero-coupon bond, and any mismatch between model and market discount factors would contaminate all cap prices. $\to$ Proceed to step 2.

    2. **Are negative rates acceptable?** For USD SOFR rates (currently positive), modest negative rate probability is acceptable for ATM caps since the payoff $\max(L - K, 0)$ is not distorted unless rates go deeply negative. $\to$ Hull-White.

    3. **Are closed-form option prices needed?** Yes. The portfolio has caps for maturities 1Y--10Y, and real-time risk requires repricing within 1 second. Hull-White provides analytical caplet prices via the Black-type formula:

    $$
    \text{Caplet}(T_{i-1}, T_i, K) = (1 + \delta K)\,\text{Put}\!\left(\frac{1}{1+\delta K},\,T_{i-1},\,T_i\right)
    $$

    For 10 cap maturities with quarterly caplets ($\sim$40 caplets total), the computation requires $\sim$40 evaluations of the normal CDF $\Phi$, completing in well under 1 ms. Adding Greeks (delta, vega) requires only analytical derivatives, keeping total time far below 1 second.

    4. **Is the volatility smile important?** For ATM caps, no. The ATM cap price depends primarily on the ATM implied volatility, which Hull-White matches well.

    **Conclusion:** Hull-White satisfies all requirements: exact curve fit, analytical pricing, and sub-second computation.

    **What changes for deep OTM caps:** Deep OTM caps depend on the tails of the rate distribution. Hull-White (Gaussian rates) assigns too much probability to negative rates and too little to very high rates, producing a symmetric "smile" that underestimates the market's OTM cap smile (which is typically skewed). For deep OTM caps, the decision flowchart would reach step 4 ("Is the volatility smile important? Yes"), leading to Black-Karasinski or shifted Hull-White. The computational constraint becomes binding: BK requires tree-based pricing ($\sim$50 ms per caplet), so 40 caplets $\times$ 50 ms = 2 seconds, which may exceed the 1-second budget depending on how many OTM strikes are needed.

---

**Exercise 2.** An insurance company models long-term real interest rates for liability valuation. Rates must be positive (negative real rates are considered unrealistic for this application). The company needs to simulate rate paths over 30-year horizons. Apply the decision framework to recommend a model. Which dimension of the framework is most important here?

??? success "Solution to Exercise 2"
    Applying the decision framework dimension by dimension:

    1. **Curve fit:** For liability valuation, the model must be consistent with the current real yield curve, but exact fit is less critical than for derivative pricing (liabilities are not marked to market at individual bond prices). An approximate fit via constant parameters is acceptable. $\to$ Time-homogeneous models (Vasicek, CIR) are adequate.

    2. **Rate positivity:** This is the **most important dimension**. Negative real interest rates are considered unrealistic for this application (the insurance company's economic assumptions exclude negative real rates). The model must guarantee $r_t > 0$ for all $t$, especially over 30-year simulation horizons where tail events are explored. $\to$ CIR (with Feller condition) or Black-Karasinski.

    3. **Analytical tractability:** Closed-form bond prices are not required (the company runs Monte Carlo for scenario generation). However, exact simulation (drawing $r_{t+\Delta}$ without discretization error) is highly valuable for 30-year paths to avoid accumulated discretization bias.

    4. **Volatility structure:** Level-dependent volatility ($\sigma\sqrt{r}$ in CIR) is empirically realistic for real rates: when real rates are high, rate changes tend to be larger.

    5. **Computational budget:** Monte Carlo simulation over 30 years with monthly steps requires $360$ steps per path, times $10{,}000$+ paths. CIR allows exact simulation via the non-central chi-squared distribution, avoiding discretization error over long horizons.

    **Recommendation: CIR** under the physical measure $\mathbb{P}$, with parameters estimated from historical real rate data.

    **Most important dimension:** Rate positivity. Over a 30-year horizon, a Gaussian model (Vasicek) with typical parameters would generate paths with $r_t < 0$ with substantial probability, producing economically meaningless liability valuations. The Feller condition in CIR eliminates this entirely.

---

**Exercise 3.** A quant researcher is building a prototype to study the effect of mean reversion on bond option prices. She needs closed-form formulas for rapid experimentation. Why is Vasicek the best choice despite its inability to fit the market curve? Under what conditions would she need to switch to a more complex model?

??? success "Solution to Exercise 3"
    The Vasicek model is the best choice for prototyping because:

    1. **Closed-form formulas for everything:** Bond prices $P(t,T) = e^{A(\tau) + B(\tau)r}$, bond option prices (Black-type), cap prices (sum of caplet formulas), and swaption prices (Jamshidian decomposition) are all available in elementary closed form involving only exponentials and the normal CDF $\Phi$. The researcher can implement and test any formula in minutes.

    2. **Transparent parameter effects:** The mean reversion speed $\kappa$ directly controls the term structure slope, $\theta$ sets the long rate, and $\sigma$ scales all option prices. These effects can be studied analytically:

    $$
    \frac{\partial P}{\partial \kappa}, \quad \frac{\partial P}{\partial \theta}, \quad \frac{\partial P}{\partial \sigma}
    $$

    are all available in closed form, enabling systematic sensitivity analysis.

    3. **No calibration overhead:** The researcher does not need to match a market curve (she is studying theoretical relationships, not pricing real trades), so Hull-White's $\theta(t)$ calibration adds complexity without benefit.

    4. **Inability to fit the market curve is irrelevant:** For studying the effect of mean reversion on bond option prices, the researcher needs a model where $\kappa$ appears explicitly and its effect is isolated. Vasicek provides exactly this.

    **When to switch to a more complex model:**

    - If the study involves products where negative rates materially affect the payoff (e.g., studying knockout barriers near zero), the researcher should switch to CIR for rate positivity.
    - If the study requires comparison with market prices, Hull-White is needed for the exact curve fit.
    - If the study examines level-dependent volatility effects, CIR or a general CEV model ($\sigma r^\gamma$) is necessary since Vasicek has constant volatility by construction.
    - If the study involves multi-factor effects (e.g., decorrelation between short and long rates), a two-factor extension is required.

---

**Exercise 4.** Consider Pitfall 2 (negative rates in Hull-White). For Hull-White parameters $a = 0.05$, $\sigma = 0.01$, and current rate $r_0 = 0.5\%$, estimate the probability $\mathbb{P}(r_1 < 0)$ using the Gaussian transition density. Is this probability material? What remedy would you suggest?

??? success "Solution to Exercise 4"
    In the Hull-White model, the conditional distribution is

    $$
    r(t+\Delta) \mid r(t) \sim \mathcal{N}\!\left(\mu,\; \frac{\sigma^2}{2a}(1 - e^{-2a\Delta})\right)
    $$

    where $\mu = r(t)e^{-a\Delta} + \alpha(t+\Delta) - \alpha(t)e^{-a\Delta}$ and $\alpha(t)$ is determined by the market curve. For the given parameters $a = 0.05$, $\sigma = 0.01$, $r_0 = 0.005$, and $\Delta = 1$:

    **Conditional mean:** For a flat or near-flat curve at $r_0 = 0.5\%$, the drift will keep rates near the current level. Approximately:

    $$
    \mu \approx r_0\,e^{-a} + \theta_{\text{eff}}(1 - e^{-a}) \approx 0.005 \times 0.9512 + 0.005 \times 0.0488 \approx 0.005
    $$

    **Conditional variance:**

    $$
    \nu^2 = \frac{\sigma^2}{2a}(1 - e^{-2a}) = \frac{0.0001}{0.1}(1 - e^{-0.1}) = 0.001 \times 0.09516 = 9.516 \times 10^{-5}
    $$

    $$
    \nu = \sqrt{9.516 \times 10^{-5}} \approx 0.009755 = 0.976\%
    $$

    **Probability of negative rates:**

    $$
    \mathbb{P}(r_1 < 0) = \Phi\!\left(\frac{0 - \mu}{\nu}\right) = \Phi\!\left(\frac{-0.005}{0.009755}\right) = \Phi(-0.5126) \approx 30.4\%
    $$

    **Is this material?** Extremely material. A 30% probability of negative rates after just one year means that roughly one-third of all simulated paths will involve negative short rates. For products with rate-dependent payoffs (floored floaters, range accruals, etc.), this severely distorts prices.

    **Remedies:**

    1. **Shifted Hull-White:** Model $r_t + \delta$ as a Hull-White process with $\delta$ chosen so that the shifted rate is always positive in typical scenarios. With $\delta = -0.01$ (allowing rates down to $-1\%$), the effective floor is reasonable for the current environment.
    2. **Black-Karasinski:** Switch to BK where $r_t = e^{x_t} > 0$ by construction. This guarantees positivity at the cost of analytical tractability.
    3. **Floored Hull-White:** Apply $r_t^+ = \max(r_t, 0)$ at each simulation step. This is ad hoc and breaks the Gaussian analytics but prevents negative rates in practice.

    Given that $r_0 = 0.5\%$ is very low relative to the volatility ($\sigma = 1\%$ annualized), the model is in a regime where the Gaussian assumption is problematic. The desk should strongly consider Black-Karasinski or shifted Hull-White for this parameterization.

---

**Exercise 5.** A desk prices callable range accrual notes in JPY (where rates are near zero) and needs to calibrate to the cap volatility smile. Apply the flowchart: is exact curve fit needed? Are negative rates acceptable? Is the smile important? What model do you recommend, and what computational method would be used?

??? success "Solution to Exercise 5"
    Applying the flowchart step by step:

    1. **Is exact curve fit required?** Yes. Callable range accrual notes are marked to market against the JPY yield curve, and any curve mismatch propagates into the coupon accrual probabilities and the call decision. $\to$ Hull-White or Black-Karasinski.

    2. **Are negative rates acceptable?** In JPY with rates near zero, allowing negative rates is risky: the range accrual coupon accrues when the reference rate is within a specified range (e.g., 0% to 1%). If the model generates negative rates, the accrual probability is reduced, distorting the coupon estimate. For rates near zero, the probability of negative rates in Hull-White can be substantial (see Exercise 4). Negative rates are **not acceptable** for this product. $\to$ Black-Karasinski (or extended CIR).

    3. **Are closed-form option prices needed?** Not strictly: range accruals require tree-based or Monte Carlo pricing regardless (they are path-dependent with early exercise). Closed-form bond prices at tree nodes would speed up the computation, but this is a secondary concern.

    4. **Is the smile important?** Yes. The accrual probability depends on the distribution of rates near the range boundaries, and cap implied volatility smiles in JPY are significant. The log-normal distribution of BK provides a better match to the market smile than the normal distribution of HW, particularly near the lower boundary.

    **Recommendation: Black-Karasinski.**

    **Computational method:** Trinomial tree with backward induction. At each node $(t_i, r_{ij})$:

    - Check if $r_{ij}$ falls within the accrual range and accumulate the coupon
    - At call dates, compare the continuation value with the call price and apply the optimal exercise rule
    - Discount backward using the tree transition probabilities

    The tree must be calibrated to match the JPY yield curve (via $\theta(t_i)$ at each time step) and the cap/swaption volatilities (via $\sigma$ and $a$). Typical tree parameters: 50--200 steps per year, with computation time on the order of seconds for a single note.

---

**Exercise 6.** Pitfall 3 warns about over-parameterizing $\sigma(t)$ in Hull-White. Suppose calibrating to 10 cap maturities gives $\sigma(t)$ values $\{2.5, 1.8, 1.2, 0.9, 0.7, 0.6, 0.55, 0.5, 0.48, 0.45\}$ (in %). The next day, with slightly different market data, the values shift to $\{2.3, 2.0, 1.0, 0.85, 0.75, 0.58, 0.52, 0.51, 0.49, 0.44\}$. Compute the day-over-day percentage change for each bucket. Which buckets are most unstable, and how does this affect forward-starting swaption prices?

??? success "Solution to Exercise 6"
    Computing the day-over-day percentage change for each bucket:

    | Bucket | Day 1 (%) | Day 2 (%) | $\Delta$ (%) | Pct Change |
    |:------:|:---------:|:---------:|:------------:|:----------:|
    | 1 | 2.50 | 2.30 | $-$0.20 | $-$8.0% |
    | 2 | 1.80 | 2.00 | +0.20 | +11.1% |
    | 3 | 1.20 | 1.00 | $-$0.20 | $-$16.7% |
    | 4 | 0.90 | 0.85 | $-$0.05 | $-$5.6% |
    | 5 | 0.70 | 0.75 | +0.05 | +7.1% |
    | 6 | 0.60 | 0.58 | $-$0.02 | $-$3.3% |
    | 7 | 0.55 | 0.52 | $-$0.03 | $-$5.5% |
    | 8 | 0.50 | 0.51 | +0.01 | +2.0% |
    | 9 | 0.48 | 0.49 | +0.01 | +2.1% |
    | 10 | 0.45 | 0.44 | $-$0.01 | $-$2.2% |

    **Most unstable buckets:** Buckets 2 and 3 show the largest percentage changes (+11.1% and $-$16.7%, respectively). These are the intermediate-maturity buckets (roughly 2Y--3Y), which correspond to the peak of the volatility hump. Small changes in market data shift the hump location, causing large relative changes in $\sigma(t)$ at these maturities.

    Bucket 1 also shows a large absolute change ($-$8.0%), but this is partly because the short-end $\sigma(t)$ is most sensitive to the current rate level and the shape of the very short end of the curve.

    **Effect on forward-starting swaption prices:** A forward-starting swaption with start date $T_s$ and maturity $T_m$ depends primarily on $\sigma(t)$ for $t \in [T_s, T_m]$. If $T_s$ falls in the unstable buckets (2Y--3Y), the swaption price inherits the instability of $\sigma(t)$ in that region. Specifically:

    - Day-over-day P&L on forward-starting swaptions will be noisy, with unexplained P&L ("P&L leakage") driven by recalibration rather than market moves.
    - Hedge ratios computed from $\sigma(t)$ will oscillate, leading to frequent rebalancing and increased transaction costs.
    - The vega profile of the forward-starting swaption will be poorly hedged because the model's $\sigma(t)$ does not reliably represent the market's forward volatility structure.

    This is why the practical recommendation is to regularize $\sigma(t)$ (e.g., by smoothing, using fewer buckets, or imposing monotonicity constraints) rather than fitting every cap maturity independently.

---

**Exercise 7.** Pitfall 4 distinguishes physical and risk-neutral calibration. A risk manager estimates CIR parameters from 5 years of daily rate data and obtains $\kappa^{\mathbb{P}} = 0.15$, $\theta^{\mathbb{P}} = 0.04$. A trader calibrates to the swaption market and obtains $\kappa^{\mathbb{Q}} = 0.50$, $\theta^{\mathbb{Q}} = 0.06$. Compute the implied market price of risk $\lambda$. Why would using the physical parameters for derivative pricing lead to systematic mispricing?

??? success "Solution to Exercise 7"
    The relationship between physical and risk-neutral parameters involves the market price of risk $\lambda$:

    $$
    \kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \lambda
    $$

    From the given values:

    $$
    \lambda = \kappa^{\mathbb{Q}} - \kappa^{\mathbb{P}} = 0.50 - 0.15 = 0.35
    $$

    **Verification via $\theta$:** The relationship $\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}} / \kappa^{\mathbb{Q}}$ (which holds for the standard CIR market price of risk specification $\lambda(r) = \lambda\sqrt{r}/\sigma$, yielding $\kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \lambda$ and $\kappa^{\mathbb{Q}}\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}$) gives:

    $$
    \theta^{\mathbb{Q}} = \frac{\kappa^{\mathbb{P}}\theta^{\mathbb{P}}}{\kappa^{\mathbb{Q}}} = \frac{0.15 \times 0.04}{0.50} = \frac{0.006}{0.50} = 0.012
    $$

    However, the problem states $\theta^{\mathbb{Q}} = 0.06$, which is inconsistent with the simple specification above. This suggests the market price of risk has a more general form (e.g., $\lambda(r) = \lambda_0 + \lambda_1 r$), or equivalently that the drift transformation affects both $\kappa$ and $\kappa\theta$ independently. Under the more general specification where $\kappa^{\mathbb{Q}}\theta^{\mathbb{Q}}$ need not equal $\kappa^{\mathbb{P}}\theta^{\mathbb{P}}$, we simply accept both calibrations as given and note $\lambda = 0.35$.

    **Why physical parameters lead to systematic mispricing:**

    1. **Mean reversion is too slow:** $\kappa^{\mathbb{P}} = 0.15$ implies a half-life of $\ln 2/0.15 \approx 4.6$ years under $\mathbb{P}$, while the risk-neutral $\kappa^{\mathbb{Q}} = 0.50$ implies a half-life of $\ln 2/0.50 \approx 1.4$ years under $\mathbb{Q}$. Using $\kappa^{\mathbb{P}}$ for pricing produces rate distributions that are too dispersed (too slow to revert to the mean), overestimating the volatility of long-dated rates and hence **overpricing** long-dated options (caps, swaptions).

    2. **Long-run mean is too low:** $\theta^{\mathbb{P}} = 0.04$ vs $\theta^{\mathbb{Q}} = 0.06$. Using the lower physical $\theta$ shifts the entire rate distribution downward under the pricing measure, underpricing receiver swaptions and overpricing payer swaptions.

    3. **The risk premium is ignored:** The market price of risk $\lambda = 0.35$ represents the compensation that investors demand for bearing interest rate risk. It is embedded in market option prices and reflected in $\kappa^{\mathbb{Q}}$, $\theta^{\mathbb{Q}}$. Ignoring it (by using $\mathbb{P}$-parameters) systematically misprices all derivatives because the pricing measure does not reflect the market's risk preferences.

    4. **Quantitative impact:** The bond price under $\mathbb{Q}$ involves $B(\tau)$ computed with $\kappa^{\mathbb{Q}} = 0.50$, giving $B(10) = (1-e^{-5})/0.5 \approx 1.987$. Under $\mathbb{P}$ with $\kappa^{\mathbb{P}} = 0.15$, $B(10) = (1-e^{-1.5})/0.15 \approx 5.18$. The $\mathbb{P}$-based bond sensitivity is $2.6\times$ larger, producing dramatically different option prices and hedge ratios.
