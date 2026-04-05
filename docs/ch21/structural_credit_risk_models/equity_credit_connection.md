# Equity–Credit Connection

Structural models provide a unified framework linking **equity and credit markets** through their common dependence on firm value. This connection has profound implications for relative value trading, risk management, and understanding market dynamics. While theoretically elegant, the equity-credit link also reveals important empirical puzzles.

---

## Theoretical Foundation

### Common Driver: Firm Value

In structural models, both equity and debt are contingent claims on the same underlying—the firm's asset value $V_t$:

- **Equity:** Call option on firm value with strike equal to debt
- **Debt:** Risk-free bond minus put option on firm value

Since both securities derive their value from $V_t$, their prices must move together in predictable ways.

### Equity as a Leveraged Position

From Merton's model, equity value is:

$$
E = V N(d_1) - D e^{-rT} N(d_2)
$$

with delta (sensitivity to firm value):

$$
\Delta_E = \frac{\partial E}{\partial V} = N(d_1) > 0
$$

Equity is a **leveraged long position** in firm value. When $V$ increases:
- Equity value rises
- Default probability falls
- Credit spreads tighten

---

## Equity Volatility and Credit Spreads

### Leverage Effect on Volatility

Applying Itô's lemma to $E(V_t, t)$:

$$
dE = \frac{\partial E}{\partial V} dV + \frac{\partial E}{\partial t} dt + \frac{1}{2}\frac{\partial^2 E}{\partial V^2} (dV)^2
$$

The instantaneous equity volatility is:

$$
\sigma_E = \frac{\partial E}{\partial V} \cdot \frac{V}{E} \cdot \sigma_V = \frac{V N(d_1)}{E} \cdot \sigma_V
$$

Define **leverage ratio** $L = V/E$:

$$
\sigma_E = L \cdot N(d_1) \cdot \sigma_V
$$

### Implications

1. **Equity volatility exceeds asset volatility:** Since $L > 1$ for levered firms, $\sigma_E > \sigma_V$
2. **Leverage amplification:** Higher leverage $\implies$ higher equity volatility
3. **Volatility feedback:** Falling equity prices $\implies$ rising leverage $\implies$ rising equity volatility

This creates the empirical **leverage effect**: negative correlation between equity returns and volatility changes.

---

## Credit Spread Dynamics

### Spread-Equity Relationship

The credit spread depends on:

$$
s = f(V_0/D, \sigma_V, T) = g(E, \sigma_E, D, T)
$$

Since equity prices embed information about $V$ and $\sigma_V$, spreads can be inferred from equity markets.

### Directional Relationship

**When equity prices fall:**
- Firm value $V$ decreases
- Leverage $D/V$ increases  
- Default probability rises
- Credit spreads widen

**When equity volatility rises:**
- Higher probability of extreme outcomes
- Increased chance of hitting default barrier
- Credit spreads widen

These relationships are:
- Negative between equity price and credit spread
- Positive between equity volatility and credit spread

---

## Quantitative Relationships

### Distance to Default

The **distance to default** (DD) provides a normalized measure:

$$
DD = \frac{\ln(V/D) + (\mu - \sigma_V^2/2)T}{\sigma_V\sqrt{T}}
$$

where $\mu$ is the physical drift of asset value.

In terms of observables:

$$
DD \approx \frac{\ln(E + D) - \ln(D) + (\mu - \sigma_V^2/2)T}{\sigma_V\sqrt{T}}
$$

**KMV/Moody's Analytics approach:**
1. Estimate $V$ and $\sigma_V$ from equity data
2. Compute DD
3. Map DD to expected default frequency (EDF) using historical data

### Spread Approximation

For small spreads and near-the-money situations:

$$
s \approx (1 - R) \cdot \lambda \approx (1 - R) \cdot \frac{N(-DD)}{T}
$$

where $R$ is recovery rate and $\lambda$ is an implied intensity.

---

## Empirical Evidence

### Equity-Credit Correlation

Empirical studies find:
- Strong negative correlation between equity returns and CDS spread changes
- Correlation strengthens during market stress
- Lead-lag relationships vary by market conditions

Typical correlations: $\rho(dE/E, ds) \approx -0.3$ to $-0.6$

### Information Flow

Research on price discovery shows:
- CDS and equity markets both incorporate information
- No consistent leader—depends on firm and time period
- Credit markets may lead for distressed firms
- Equity markets may lead for investment-grade firms

### Credit Spread Puzzle

**The puzzle:** Structural models significantly underpredict observed credit spreads, especially for:
- Short maturities
- Investment-grade debt

**Possible explanations:**
1. Liquidity premiums in corporate bonds
2. Tax effects
3. Jump risk not captured by diffusion models
4. Recovery rate uncertainty
5. Systematic risk premiums

Huang and Huang (2012) estimate that credit risk explains only 20-30% of investment-grade spreads.

---

## Applications

### Relative Value Trading

The equity-credit link enables arbitrage strategies:

**Capital Structure Arbitrage:**
- If CDS spreads are "too wide" relative to equity-implied spreads:
  - Sell CDS protection (receive spread)
  - Short equity (hedge firm value exposure)
- If CDS spreads are "too tight":
  - Buy CDS protection
  - Go long equity

**Implementation challenges:**
- Transaction costs
- Model uncertainty
- Liquidity differences
- Jump risk exposure

### Credit Spread Forecasting

Equity information predicts credit spreads:
1. Estimate firm value and volatility from equity
2. Compute model-implied spread
3. Compare to market spread
4. Trade on deviations

**Evidence:** Equity-implied spreads have predictive power for future spread changes, with strongest effects for speculative-grade firms.

### Risk Management

Integrated equity-credit models for:
- Portfolio VaR including both asset classes
- Stress testing across capital structure
- Counterparty credit risk (CVA with equity correlation)

---

## Model-Based Spread Decomposition

### Components of Observed Spreads

Observed spread = Default risk + Liquidity premium + Tax effect + Risk premium

$$
s^{\text{observed}} = s^{\text{Merton}} + s^{\text{liquidity}} + s^{\text{tax}} + s^{\text{risk premium}}
$$

### Structural Model Contribution

The Merton model captures the **expected loss** component:

$$
s^{\text{Merton}} \approx (1-R) \cdot \text{Default Probability}/T
$$

This is typically 20-50% of observed spreads.

### Residual Spread

The residual (observed minus model-implied) reflects:
- Compensation for bearing systematic credit risk
- Illiquidity costs
- Model misspecification

---

## Joint Calibration

### Simultaneous Fit

To calibrate structural models consistently:

1. **Equity constraint:** $E^{\text{model}} = E^{\text{market}}$
2. **Equity volatility constraint:** $\sigma_E^{\text{model}} = \sigma_E^{\text{market}}$
3. **CDS/bond constraint:** $s^{\text{model}} \approx s^{\text{market}}$

With 3 equations and 3 unknowns ($V_0$, $\sigma_V$, and possibly barrier $B$), the system may be:
- Over-determined (no exact solution)
- Perfectly determined (unique solution)
- Under-determined (need additional constraints)

### Typical Findings

Joint calibration often reveals:
- Asset volatility $\sigma_V$ lower than equity volatility $\sigma_E$
- Implied barriers significantly above naive debt value
- Residual model errors for short-term spreads

---

## Practical Considerations

### Data Requirements

Equity-credit analysis requires:
- Equity prices (liquid, continuous)
- Equity option implied volatilities (for $\sigma_E$)
- CDS spreads or corporate bond prices
- Balance sheet data for $D$
- Interest rate curves

### Model Selection

| Firm Type | Recommended Approach |
|-----------|---------------------|
| Investment-grade, stable | Simple Merton sufficient |
| Speculative-grade | First-passage or jump models |
| Distressed | Reduced-form with equity signal |
| Financial firms | Specialized models needed |

### Limitations

1. **Assumption violations:** Constant volatility, simple capital structure
2. **Unobservable inputs:** Asset value, asset volatility
3. **Market frictions:** Liquidity differences, short-sale constraints
4. **Model risk:** Multiple models fit data equally well

---

## Hybrid Models

### Combining Structural and Reduced-Form

Modern approaches blend:
- **Structural intuition:** Equity-credit link, economic drivers
- **Reduced-form tractability:** Intensity-based pricing, easy calibration

**Example:** Set intensity as function of equity price:

$$
\lambda_t = f(S_t, \sigma_t) = a + b \cdot (S^*/S_t)^c
$$

This captures structural intuition in reduced-form framework.

### Credit-Equity Hybrid Derivatives

Products like:
- Equity default swaps
- Convertible bonds
- Contingent convertibles (CoCos)

require joint equity-credit modeling with consistent dynamics.

---

## Key Takeaways

- Structural models create a natural equity-credit link through common firm value driver
- Equity prices, volatility, and credit spreads are theoretically connected
- The leverage effect explains equity volatility dynamics
- Credit spread puzzles suggest model incompleteness—observed spreads exceed model predictions
- Equity-credit relative value trading exploits mispricings
- Joint calibration is essential but challenging
- Modern practice blends structural intuition with reduced-form tractability

---

## Further Reading

- Duffie, D., & Singleton, K. J. (2003). *Credit Risk: Pricing, Measurement, and Management*. Princeton University Press, Chapter 6.
- Huang, J.-Z., & Huang, M. (2012). How much of the corporate-treasury yield spread is due to credit risk? *Review of Asset Pricing Studies*, 2(2), 153–202.
- Cremers, M., Driessen, J., & Maenhout, P. (2008). Explaining the level of credit spreads: Option-implied jump risk premia in a firm value model. *Review of Financial Studies*, 21(5), 2209–2242.
- Bielecki, T. R., & Rutkowski, M. (2004). *Credit Risk: Modeling, Valuation and Hedging*. Springer, Chapter 3.

---

## Exercises

**Exercise 1.** In the Merton model, equity is a call option on firm value: $E = V_0\,N(d_1) - De^{-rT}\,N(d_2)$. A firm has equity value $E_0 = 40$, debt face value $D = 60$, risk-free rate $r = 4\%$, maturity $T = 5$, and equity volatility $\sigma_E = 40\%$. Set up the system of two equations (equity pricing and volatility matching) needed to solve for $V_0$ and $\sigma_V$. Describe how you would solve this system numerically.

??? success "Solution to Exercise 1"
    **Given:** $E_0 = 40$, $D = 60$, $r = 0.04$, $T = 5$, $\sigma_E = 0.40$.

    **Step 1: The two-equation system.**

    The unknowns are $(V_0, \sigma_V)$. The two equations are:

    **Equation 1 (Equity pricing -- equity is a call on firm value):**

    $$
    E_0 = V_0 N(d_1) - De^{-rT} N(d_2) \implies 40 = V_0 N(d_1) - 60 e^{-0.20} N(d_2)
    $$

    $$
    40 = V_0 N(d_1) - 49.12 \, N(d_2)
    $$

    where:

    $$
    d_1 = \frac{\ln(V_0/60) + (0.04 + \sigma_V^2/2) \times 5}{\sigma_V\sqrt{5}}, \quad d_2 = d_1 - \sigma_V\sqrt{5}
    $$

    **Equation 2 (Volatility linkage via Ito's lemma):**

    $$
    \sigma_E E_0 = N(d_1) \sigma_V V_0 \implies 0.40 \times 40 = N(d_1) \sigma_V V_0
    $$

    $$
    16 = N(d_1) \sigma_V V_0
    $$

    **Step 2: Numerical solution procedure.**

    **Method 1: Fixed-point iteration.**

    1. **Initialize:** $V_0^{(0)} = E_0 + De^{-rT} = 40 + 49.12 = 89.12$.

    2. **Compute $\sigma_V^{(0)}$:** We need an initial $d_1$ estimate. Use $\sigma_V \approx \sigma_E \cdot E_0 / V_0^{(0)} = 0.40 \times 40/89.12 \approx 0.18$. Then:

        $$
        d_1^{(0)} = \frac{\ln(89.12/60) + (0.04 + 0.0162) \times 5}{0.18\sqrt{5}} = \frac{0.396 + 0.281}{0.402} = 1.684
        $$

        $N(d_1^{(0)}) = 0.9539$.

        $$
        \sigma_V^{(0)} = \frac{16}{0.9539 \times 89.12} = \frac{16}{85.01} = 0.1882
        $$

    3. **Update $V_0^{(1)}$:** Solve Equation 1 for $V_0$ given $\sigma_V = 0.1882$ using one-dimensional root finding (e.g., Newton's method or bisection on $V_0$).

    4. **Iterate** steps 2--3 until $|V_0^{(k+1)} - V_0^{(k)}| < \varepsilon$ and $|\sigma_V^{(k+1)} - \sigma_V^{(k)}| < \varepsilon$.

    **Method 2: Newton's method in 2D.**

    Define $F: \mathbb{R}^2 \to \mathbb{R}^2$:

    $$
    F_1(V, \sigma) = V N(d_1) - 49.12 \, N(d_2) - 40
    $$

    $$
    F_2(V, \sigma) = N(d_1) \sigma V - 16
    $$

    Compute the Jacobian $J_F$ with entries $\partial F_i / \partial x_j$ (where $x_1 = V$, $x_2 = \sigma$), and iterate:

    $$
    \begin{pmatrix} V \\ \sigma \end{pmatrix}^{(k+1)} = \begin{pmatrix} V \\ \sigma \end{pmatrix}^{(k)} - J_F^{-1} F\left(\begin{pmatrix} V \\ \sigma \end{pmatrix}^{(k)}\right)
    $$

    The Jacobian entries involve derivatives of $N(d_1)$ and $N(d_2)$ with respect to $V$ and $\sigma$ (through $d_1$ and $d_2$). Convergence is typically rapid (quadratic) with a good initial guess.

    After convergence, typical results for these parameters are approximately $V_0 \approx 89$--$90$ and $\sigma_V \approx 0.18$--$0.19$.

---

**Exercise 2.** Explain why, in the Merton framework, equity and credit are negatively correlated: when firm value $V_t$ decreases, equity value falls and credit spreads widen. Derive the sensitivity of the credit spread to changes in $V_t$ using the structural model.

??? success "Solution to Exercise 2"
    **Negative correlation between equity and credit in the Merton framework:**

    **Step 1: Equity sensitivity to firm value.**

    In the Merton model, equity is a call option on firm value:

    $$
    E = V N(d_1) - De^{-rT} N(d_2)
    $$

    The equity delta is:

    $$
    \frac{\partial E}{\partial V} = N(d_1) > 0
    $$

    When $V$ decreases, $E$ decreases. This is the direct equity-firm value link.

    **Step 2: Credit spread sensitivity to firm value.**

    The credit spread is:

    $$
    s = -\frac{1}{T}\ln\left[N(d_2) + \frac{1}{L}N(-d_1)\right]
    $$

    where $L = De^{-rT}/V$.

    Differentiating with respect to $V$:

    $$
    \frac{\partial s}{\partial V} = -\frac{1}{T} \cdot \frac{1}{N(d_2) + \frac{1}{L}N(-d_1)} \cdot \frac{\partial}{\partial V}\left[N(d_2) + \frac{V}{De^{-rT}}N(-d_1)\right]
    $$

    Computing the derivative of the bracketed expression:

    $$
    \frac{\partial}{\partial V}\left[N(d_2) + \frac{V}{De^{-rT}}N(-d_1)\right] = N'(d_2)\frac{\partial d_2}{\partial V} + \frac{N(-d_1)}{De^{-rT}} + \frac{V}{De^{-rT}}N'(-d_1)\left(-\frac{\partial d_1}{\partial V}\right)
    $$

    Since $\frac{\partial d_1}{\partial V} = \frac{\partial d_2}{\partial V} = \frac{1}{V\sigma_V\sqrt{T}} > 0$, and using the identity $VN'(d_1) = De^{-rT}N'(d_2)$ (from the Black-Scholes framework), the net effect simplifies. The key result is:

    $$
    \frac{\partial s}{\partial V} < 0
    $$

    **Interpretation:** When $V$ increases:

    - Equity $E$ increases (positive delta)
    - Credit spread $s$ decreases (negative sensitivity)

    Therefore $\frac{\partial E}{\partial V} > 0$ and $\frac{\partial s}{\partial V} < 0$, giving:

    $$
    \text{Corr}(\Delta E, \Delta s) < 0
    $$

    **Economic intuition:** Both equity and credit are claims on the same firm value $V$. When $V$ rises:

    - **Equity gains:** The call option on $V$ becomes more in-the-money, increasing equity value.
    - **Default risk falls:** The firm moves further from the default barrier, reducing the probability of default and the expected loss on debt.
    - **Spread tightens:** With lower default risk, creditors require less compensation, so spreads decrease.

    The negative equity-credit correlation is a fundamental prediction of structural models and is strongly supported by empirical evidence, with correlations typically in the range $-0.3$ to $-0.6$.

---

**Exercise 3.** A firm's equity price drops by 30% in one month. Using the equity-credit connection from the Merton model, describe qualitatively how the firm's CDS spread, distance to default, and credit rating would be affected. Why are these changes correlated?

??? success "Solution to Exercise 3"
    **A firm's equity drops 30% in one month.**

    If equity falls from $E_0$ to $0.70 E_0$, this signals a significant decline in firm value.

    **CDS spread:** The CDS spread will **widen** (increase) substantially. In the Merton framework:

    - Falling equity implies falling $V$ (since $\partial E / \partial V = N(d_1) > 0$).
    - Lower $V$ increases leverage $L = De^{-rT}/V$ and default probability $N(-d_2)$.
    - The credit spread $s = -\frac{1}{T}\ln[N(d_2) + \frac{1}{L}N(-d_1)]$ increases as $L$ rises.
    - A 30% equity decline for a leveraged firm can correspond to a 10--15% decline in $V$ (since equity is a leveraged position), which can dramatically increase spreads. For example, if the firm goes from $L = 0.60$ to $L = 0.70$, spreads might double or triple.

    **Distance to default:** DD will **decrease** sharply. Since:

    $$
    DD = \frac{\ln(V/\text{DP}) + (\mu - \sigma_V^2/2)T}{\sigma_V\sqrt{T}}
    $$

    the decline in $V$ directly reduces $\ln(V/\text{DP})$. Additionally, asset volatility $\sigma_V$ typically increases during distress (through the leverage effect $\sigma_E = (V/E)N(d_1)\sigma_V$, a 30% equity drop with fixed $\sigma_E$ implies higher $\sigma_V$), further reducing DD through both the numerator and denominator.

    A firm with initial $DD = 4$ might drop to $DD = 2.5$--$3.0$ after a 30% equity decline, depending on leverage.

    **Credit rating:** The credit rating would face **downgrade pressure**. However, the response depends on the rating agency's methodology:

    - Rating agencies use a "through-the-cycle" approach, meaning they may wait to see if the decline is temporary.
    - A 30% equity decline is serious enough to likely trigger at least a **negative outlook** or **credit watch negative** placement.
    - If the decline reflects fundamental deterioration (not just market sentiment), a downgrade of 1--3 notches could follow within weeks to months.
    - If the firm was borderline investment-grade (BBB-), this could trigger a downgrade to speculative-grade ("fallen angel"), with forced selling by index-tracking investors.

    **Why these changes are correlated:** All three measures -- CDS spread, DD, and credit rating -- are driven by the same fundamental variable: the firm's asset value $V_t$. In the structural model:

    $$
    V \downarrow \implies E \downarrow, \; s \uparrow, \; DD \downarrow, \; \text{Rating} \downarrow
    $$

    The equity-credit connection ensures that any information reflected in equity prices (which update continuously) will eventually be reflected in credit spreads and ratings. The CDS market typically reacts within hours to days (incorporating the same information as equity), while rating agencies respond with a lag of weeks to months.

---

**Exercise 4.** The "capital structure arbitrage" strategy exploits mispricings between equity and credit markets. Describe a trade where a CDS is overpriced relative to the model-implied spread from equity data. What risks does this strategy face (e.g., model risk, convergence risk, liquidity risk)?

??? success "Solution to Exercise 4"
    **Capital structure arbitrage when CDS is overpriced relative to equity-implied spread:**

    **Setup:** A structural model calibrated to equity data ($E_0, \sigma_E$) produces a model-implied CDS spread $s^{\text{model}}$ that is lower than the market CDS spread $s^{\text{market}}$. The CDS appears "overpriced" (protection is too expensive relative to what equity markets imply).

    **The trade:**

    1. **Sell CDS protection** (receive the spread $s^{\text{market}}$): This is equivalent to going long credit risk -- you profit if the firm does not default.
    2. **Short equity** to hedge firm value exposure: The equity short provides a hedge against firm value declines. The hedge ratio is determined by the model:

    $$
    \text{Equity hedge ratio} = \frac{\partial s}{\partial E} \cdot \frac{\text{CDS notional}}{\text{Equity position}}
    $$

    In practice, the hedge involves shorting a dollar amount of equity proportional to the CDS notional, scaled by the model-implied delta.

    **Profit mechanism:** If the CDS spread converges toward the equity-implied spread (either CDS tightens or equity falls enough to justify the wide CDS), the combined position profits. The equity short provides protection if the spread widening was justified by fundamental deterioration.

    **Risks faced by this strategy:**

    1. **Model risk:** The structural model may be wrong. If the equity-implied spread is too low (because the model underestimates default risk), the CDS spread may be correctly priced, and the trade will lose money. Different models give different implied spreads.

    2. **Convergence risk:** Even if the mismatch is genuine, there is no guarantee that prices will converge within the trade's horizon. The basis (CDS spread minus equity-implied spread) can widen before narrowing, requiring the trader to sustain mark-to-market losses.

    3. **Liquidity risk:**
        - CDS may become illiquid during stress, with wide bid-ask spreads.
        - Equity borrowing costs for the short position can increase.
        - Margin calls on both the CDS and equity positions may force premature unwinding.

    4. **Jump-to-default risk:** If the firm suddenly defaults (e.g., due to fraud), the CDS loss is the full notional minus recovery ($\approx 60\%$ of notional), while the equity short gains only the remaining equity value. The mismatch creates a net loss on the jump event.

    5. **Basis risk:** The equity hedge is imperfect because the equity-credit relationship is based on a model, and the actual sensitivity may differ. During stress, the correlation between equity returns and CDS spread changes may break down.

    6. **Carry and timing:** The trade involves carrying the CDS position (receiving periodic spread payments) against borrowing costs for the equity short. If convergence takes a long time, the carry may be insufficient to compensate for the capital tied up in the trade.

    7. **Counterparty risk:** The CDS seller faces counterparty risk on the CDS contract, though this is mitigated by collateral agreements.

---

**Exercise 5.** Using the Merton model relationship $\sigma_E = \sigma_V \cdot (V_0/E_0) \cdot N(d_1)$, explain why equity volatility is always higher than asset volatility for leveraged firms. If $V_0 = 100$, $E_0 = 30$, $\sigma_V = 20\%$, and $N(d_1) = 0.85$, compute $\sigma_E$.

??? success "Solution to Exercise 5"
    **Given:** $V_0 = 100$, $E_0 = 30$, $\sigma_V = 0.20$, $N(d_1) = 0.85$.

    **Step 1: Apply the volatility linkage formula.**

    From Ito's lemma applied to the Merton model, the relationship between equity and asset volatility is:

    $$
    \sigma_E = \sigma_V \cdot \frac{V_0}{E_0} \cdot N(d_1)
    $$

    **Step 2: Compute.**

    $$
    \sigma_E = 0.20 \times \frac{100}{30} \times 0.85 = 0.20 \times 3.333 \times 0.85 = 0.20 \times 2.833 = 0.5667
    $$

    $$
    \sigma_E \approx 56.7\%
    $$

    **Step 3: Explain why $\sigma_E > \sigma_V$ for leveraged firms.**

    The equity volatility ($56.7\%$) is nearly three times the asset volatility ($20\%$). This amplification arises from **financial leverage**:

    The leverage multiplier is $V_0/E_0 = 100/30 = 3.33$. Since equity is a residual claim (call option on firm value), a 1% change in $V$ does not produce a 1% change in $E$. Instead:

    $$
    \frac{dE}{E} = \frac{(\partial E/\partial V) \cdot dV}{E} = N(d_1) \cdot \frac{V}{E} \cdot \frac{dV}{V}
    $$

    The factor $N(d_1) \cdot V/E$ is the **equity elasticity** (omega) with respect to firm value. Since $V > E$ for any levered firm (because $V = E + B$ and $B > 0$), this elasticity exceeds 1, and equity returns are amplified versions of asset returns.

    **Key factors driving the amplification:**

    - **Leverage ratio** $V/E$: Higher leverage means equity absorbs a disproportionate share of firm value fluctuations. If $V/E = 10$ (extreme leverage), equity volatility would be roughly 10 times asset volatility.

    - **Option moneyness** $N(d_1)$: This factor, between 0 and 1, represents the option delta. For deep in-the-money equity ($V \gg D$), $N(d_1) \approx 1$, and the amplification is purely $V/E$. For at-the-money or out-of-the-money equity, $N(d_1) < 1$ partially offsets the leverage effect.

    - In our example, $N(d_1) = 0.85$ (moderately in-the-money), so the effective multiplier is $0.85 \times 3.33 = 2.83$.

    This relationship has an important dynamic consequence: as the firm's equity declines (increasing leverage $V/E$), equity volatility rises. This is the **leverage effect**, which explains the empirically observed negative correlation between equity returns and volatility changes.

---

**Exercise 6.** Discuss the empirical puzzle that equity-implied credit spreads (from structural models) are often lower than market-observed CDS spreads for investment-grade firms. What factors (liquidity premium, jump risk, model misspecification) might explain this gap?

??? success "Solution to Exercise 6"
    **The credit spread puzzle for investment-grade firms:**

    **The empirical observation:** When structural models (Merton, Black-Cox) are calibrated to equity market data, the model-implied credit spreads are substantially lower than observed market CDS or corporate bond spreads. Huang and Huang (2012) estimate that credit risk accounts for only 20--30% of investment-grade spreads and 60--80% of speculative-grade spreads.

    For example, a typical BBB-rated firm might have:

    - Model-implied spread: 30--50 bp
    - Observed CDS spread: 100--150 bp
    - Gap: 50--120 bp

    **Factors explaining the gap:**

    **1. Liquidity premium (estimated: 30--60 bp for IG).**

    Corporate bonds are significantly less liquid than government bonds:

    - Corporate bonds trade infrequently (many bonds trade only a few times per month).
    - Bid-ask spreads on corporate bonds are 2--10 times wider than for Treasuries.
    - During market stress, corporate bond liquidity evaporates, creating large price dislocations.

    Investors demand compensation for bearing this illiquidity risk. The liquidity premium is present in all corporate bonds, regardless of credit quality, and is a major contributor to the IG spread gap. CDS spreads also contain a liquidity component, though typically smaller.

    **2. Jump risk (estimated: 10--30 bp for IG).**

    Structural models with continuous diffusion (GBM) cannot generate sudden defaults for firms far from the barrier. In reality:

    - Accounting fraud can cause overnight collapse (Enron went from IG to default in weeks).
    - Sudden regulatory actions can impair asset value.
    - Catastrophic losses (litigation, natural disasters) create jump-to-default risk.

    Models with jumps (e.g., Merton jump-diffusion, Zhou 2001) generate higher spreads by allowing for instantaneous large drops in firm value. This partially closes the gap, especially at short maturities.

    **3. Model misspecification (estimated: 10--20 bp for IG).**

    The Merton model's assumptions introduce systematic bias:

    - **Constant volatility:** Stochastic volatility increases the variance of asset returns, fattening tails and raising default probabilities.
    - **Simple capital structure:** Real firms have complex, state-dependent liabilities that may trigger default more easily than the single-class debt assumption suggests.
    - **Constant interest rates:** Ignoring rate-credit correlation (typically negative) leads to underestimation of spreads.
    - **Log-normal returns:** Real asset returns have heavier tails than log-normal, increasing expected losses.

    **4. Systematic risk premium (estimated: 10--30 bp for IG).**

    Default events are correlated across firms (systemic risk). Investors demand compensation not just for expected losses but for bearing the risk that defaults cluster during bad economic times:

    - Defaults increase during recessions when investors' marginal utility is high.
    - The CAPM-like risk premium for credit exposure is not captured by the actuarial default probability.
    - This is analogous to the equity risk premium: expected returns exceed the risk-free rate as compensation for systematic risk.

    **5. Tax effects (estimated: 5--15 bp for IG).**

    Corporate bond income is taxed at higher rates than Treasury income in some jurisdictions, requiring higher pre-tax yields on corporate bonds. This tax wedge shows up as an apparent credit spread even in the absence of default risk.

    **Summary of decomposition for a typical BBB credit:**

    | Component | Estimated Contribution (bp) |
    |-----------|----------------------------|
    | Expected default loss (Merton) | 20--40 |
    | Liquidity premium | 30--60 |
    | Jump/tail risk premium | 10--30 |
    | Systematic risk premium | 10--30 |
    | Tax effects | 5--15 |
    | Model misspecification | 10--20 |
    | **Total observed spread** | **100--150** |

    The credit spread puzzle is not a single phenomenon but the sum of multiple factors, each individually significant. No single explanation is sufficient, and the relative importance of each factor varies by credit quality, maturity, and market conditions.
