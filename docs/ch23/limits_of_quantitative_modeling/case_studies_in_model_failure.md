# Case Studies in Model Failure

Quantitative models drive decision-making in modern finance, but models occasionally fail dramatically. Examining historical failures—Long-Term Capital Management (LTCM), Barings Bank, the London Whale trading loss, and the 2008 financial crisis—reveals recurring patterns: excessive leverage, model over-confidence, organizational breakdowns, and market regime changes.

## Key Concepts

**Long-Term Capital Management (1998)**
LTCM operated a "market-neutral" convergence trading strategy using sophisticated mathematical models:
- **Model logic**: historical spreads reliably mean-revert; pairs trading hedges directional risk
- **Capital**: $5 billion with 25:1 leverage on a $125 billion portfolio
- **Trigger**: Russian default (August 1998) caused emerging market flight to quality

**Failure mechanisms**:
1. **Correlation breakdown**: portfolio positions that should be uncorrelated moved together
2. **Leverage amplification**: 25:1 leverage turned small losses into existential threat
3. **Liquidity misjudgment**: "liquid" positions became illiquid; bid-ask spreads exploded
4. **Model regime change**: 1998 was unlike historical data; models trained on normal times

**Lessons**:
- Leverage magnifies model error
- Correlation assumptions fail during stress
- Liquidity assumptions are behavioral, not technological
- Tail events can be much worse than VaR models predict

**Barings Bank (1995)**
Rogue trader Nick Leeson used unauthorized derivatives to mask trading losses:
- **Mechanism**: Leeson had control of both trading and back-office, circumventing controls
- **Strategy**: short straddles (sold volatility) on Nikkei, betting on low volatility
- **Trigger**: January 1995 Kobe earthquake; Nikkei fell sharply
- **Losses**: $1.3 billion, more than Barings' equity; bank collapsed

**Failure mechanisms**:
1. **Operational risk**: single person controlled both execution and settlement
2. **Risk measurement failure**: losses hidden through accounting manipulation
3. **Segregation of duties**: not enforced despite risk management theory
4. **Escalation**: trader doubled down (sunk cost fallacy) rather than admitting loss

**Lessons**:
- Quantitative models are only valid if operational controls work
- Segregation of duties and three-line defense essential
- Risk infrastructure must catch losses early
- Regulatory oversight of operational risk as important as market risk

**London Whale Trading Loss (2012)**
JP Morgan's Chief Investment Office (CIO) took large credit-hedging positions:
- **Notional exposure**: $100 billion in credit derivatives
- **Strategy**: intended as hedge but became speculative position
- **Trigger**: market volatility increased; position moved against the bank
- **Losses**: $6 billion (officially), possibly $9 billion including unwinding costs

**Failure mechanisms**:
1. **Model misuse**: Value-at-Risk model used positions outside scope (correlations unstable)
2. **Portfolio complexity**: internal models couldn't capture risks in complex synthetic indices
3. **Risk measurement errors**: models underestimated tail risk by factor of 2-3x
4. **Organizational culture**: risk warnings were overridden by revenue incentives

**Specific math failures**:
$$\text{VaR}_{\text{model}} = f(\text{volatility}, \text{correlation}) \text{ but correlation unstable in stress}$$

**Lessons**:
- Even sophisticated large banks fail to measure model risk
- Back-office infrastructure critical to detecting unusual positions
- Multi-risk-type positions need stress testing across scenarios
- Independent risk governance necessary

**2008 Financial Crisis: Systemic Model Failure**
The financial crisis involved multiple simultaneous model failures:

1. **Housing model failures**:
   - Models assumed housing prices would never decline nationally
   - Regional correlations underestimated (everyone exposed to housing)
   - Default correlations exploded (unemployment contagion)

2. **CDO model failures** (Gaussian copula):
   - Assumed constant correlation; correlation jumped during crisis
   - Assumed mortgages independent; defaults clustered
   - Senior tranches rated AAA despite hidden leverage

3. **Liquidity model failures**:
   - Models assumed assets could always be sold at mid-market prices
   - Actual: bid-ask spreads exploded, positions became illiquid
   - Fire sales became spiral: forced sales compressed prices

4. **Counterparty risk failures**:
   - CDS allowed leverage without capital charges (regulatory arbitrage)
   - Interconnectedness hidden (Lehman bankruptcy had 930,000 contracts counterparties)
   - Systemic risk ignored

**Failure mechanisms**:
- **Model calibration to normal times**: parameters estimated 1990-2007, excluded prior crises
- **Regulatory arbitrage**: models exploited to minimize capital (Basel II)
- **Incentive misalignment**: originators had no loss exposure; buyers had misaligned info
- **Procyclicality**: low VaR in good times encouraged risk-taking; high VaR in bad times forced deleveraging

**Systemic lessons**:
- Models trained on limited data (normal times only) fail in crises
- Interconnectedness and systemic risk not captured in individual firm models
- Regulatory arbitrage incentivizes model exploits
- Market prices can become detached from fundamentals (feedback loops)

**Common Themes Across Failures**

| Factor | LTCM | Barings | London Whale | 2008 Crisis |
|--------|------|---------|--------------|-------------|
| Model misspecification | Correlation | N/A | Tail risk | Regime change |
| Leverage | Extreme (25:1) | Moderate | Moderate | System-wide |
| Operational weakness | Internal models | Controls breach | Risk override | Regulatory gaps |
| Data period | 40 years | N/A | 10 years | 15 years |
| Liquidity misjudged | Yes | No | Yes | Yes |
| Tail risk ignored | Yes | No | Yes | Yes |
| Contagion/correlation | Yes | No | Yes | Yes |
| Incentive misalignment | No | Yes | Yes | Yes |

**Modern Risk Governance Responses**

1. **Regulatory reform**:
   - Basel III: higher capital, leverage ratios, stress testing
   - Dodd-Frank: systemic risk oversight, derivatives clearing
   - Stress testing: annual CCAR/DFAST scenarios

2. **Structural improvements**:
   - Separate investment and commercial banking (Volcker rule)
   - Bail-in mechanisms (CoCo bonds)
   - Resolution authorities for orderly failure

3. **Modeling best practices**:
   - Robust optimization instead of point estimates
   - Reverse stress testing: what shocks break the model?
   - Ensemble methods across multiple models
   - Regular backtesting and crisis scenario testing

4. **Organizational changes**:
   - Chief Risk Officer independence and authority
   - Separation of front/middle/back office
   - Whistleblower protections
   - Compensation alignment with risk outcomes

!!! warning "Enduring Model Risk"
    Despite improvements, model risk remains:
    - New products and strategies exploit old model gaps
    - Regulatory models can become targets for arbitrage
    - Behavioral factors (herd behavior, fear) amplify mathematical models
    - Model sophistication can mask rather than illuminate risks
    - Humility about model limitations essential for risk management
