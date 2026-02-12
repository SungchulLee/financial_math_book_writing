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
E = V N(d_1) - D e^{-rT} N(d_2),
$$

with delta (sensitivity to firm value):

$$
\Delta_E = \frac{\partial E}{\partial V} = N(d_1) > 0.
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
dE = \frac{\partial E}{\partial V} dV + \frac{\partial E}{\partial t} dt + \frac{1}{2}\frac{\partial^2 E}{\partial V^2} (dV)^2.
$$

The instantaneous equity volatility is:

$$
\sigma_E = \frac{\partial E}{\partial V} \cdot \frac{V}{E} \cdot \sigma_V = \frac{V N(d_1)}{E} \cdot \sigma_V.
$$

Define **leverage ratio** $L = V/E$:

$$
\sigma_E = L \cdot N(d_1) \cdot \sigma_V.
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
s = f(V_0/D, \sigma_V, T) = g(E, \sigma_E, D, T).
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
DD = \frac{\ln(V/D) + (\mu - \sigma_V^2/2)T}{\sigma_V\sqrt{T}},
$$

where $\mu$ is the physical drift of asset value.

In terms of observables:

$$
DD \approx \frac{\ln(E + D) - \ln(D) + (\mu - \sigma_V^2/2)T}{\sigma_V\sqrt{T}}.
$$

**KMV/Moody's Analytics approach:**
1. Estimate $V$ and $\sigma_V$ from equity data
2. Compute DD
3. Map DD to expected default frequency (EDF) using historical data

### Spread Approximation

For small spreads and near-the-money situations:

$$
s \approx (1 - R) \cdot \lambda \approx (1 - R) \cdot \frac{N(-DD)}{T},
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
s^{\text{Merton}} \approx (1-R) \cdot \text{Default Probability}/T.
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
