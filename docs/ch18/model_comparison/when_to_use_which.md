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

---

**Exercise 2.** An insurance company models long-term real interest rates for liability valuation. Rates must be positive (negative real rates are considered unrealistic for this application). The company needs to simulate rate paths over 30-year horizons. Apply the decision framework to recommend a model. Which dimension of the framework is most important here?

---

**Exercise 3.** A quant researcher is building a prototype to study the effect of mean reversion on bond option prices. She needs closed-form formulas for rapid experimentation. Why is Vasicek the best choice despite its inability to fit the market curve? Under what conditions would she need to switch to a more complex model?

---

**Exercise 4.** Consider Pitfall 2 (negative rates in Hull-White). For Hull-White parameters $a = 0.05$, $\sigma = 0.01$, and current rate $r_0 = 0.5\%$, estimate the probability $\mathbb{P}(r_1 < 0)$ using the Gaussian transition density. Is this probability material? What remedy would you suggest?

---

**Exercise 5.** A desk prices callable range accrual notes in JPY (where rates are near zero) and needs to calibrate to the cap volatility smile. Apply the flowchart: is exact curve fit needed? Are negative rates acceptable? Is the smile important? What model do you recommend, and what computational method would be used?

---

**Exercise 6.** Pitfall 3 warns about over-parameterizing $\sigma(t)$ in Hull-White. Suppose calibrating to 10 cap maturities gives $\sigma(t)$ values $\{2.5, 1.8, 1.2, 0.9, 0.7, 0.6, 0.55, 0.5, 0.48, 0.45\}$ (in %). The next day, with slightly different market data, the values shift to $\{2.3, 2.0, 1.0, 0.85, 0.75, 0.58, 0.52, 0.51, 0.49, 0.44\}$. Compute the day-over-day percentage change for each bucket. Which buckets are most unstable, and how does this affect forward-starting swaption prices?

---

**Exercise 7.** Pitfall 4 distinguishes physical and risk-neutral calibration. A risk manager estimates CIR parameters from 5 years of daily rate data and obtains $\kappa^{\mathbb{P}} = 0.15$, $\theta^{\mathbb{P}} = 0.04$. A trader calibrates to the swaption market and obtains $\kappa^{\mathbb{Q}} = 0.50$, $\theta^{\mathbb{Q}} = 0.06$. Compute the implied market price of risk $\lambda$. Why would using the physical parameters for derivative pricing lead to systematic mispricing?
