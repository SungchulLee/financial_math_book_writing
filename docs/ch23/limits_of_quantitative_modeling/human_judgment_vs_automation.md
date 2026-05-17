# Human Judgment vs Automation


## Introduction


The relationship between human judgment and automated quantitative models is one of the central tensions in modern finance. Pure automation offers consistency, speed, and freedom from emotional bias, but lacks adaptability to novel situations. Human judgment provides flexibility and contextual understanding, but is subject to cognitive biases and limited processing capacity.

Effective financial decision-making typically requires a thoughtful combination of both, with clear protocols for when human override is appropriate and when automated systems should be trusted.

## Comparative Strengths


### 1. Advantages of Automated Models


**Consistency**: Models apply the same rules every time.

$$
f(x_t) = f(x_{t'}) \quad \text{when } x_t = x_{t'}
$$

No mood effects, fatigue, or recency bias.

**Speed**: Process thousands of instruments in milliseconds.

**Scalability**: Same model handles 10 or 10,000 positions.

**Documentation**: Model logic is explicit and auditable.

**Emotional Neutrality**: No fear or greed influencing decisions.

### 2. Advantages of Human Judgment


**Pattern Recognition**: Identify novel situations not in training data.

**Contextual Understanding**: Incorporate soft information (news, relationships, intuition).

**Adaptability**: Quickly adjust to regime changes.

**Creative Problem-Solving**: Generate solutions outside model framework.

**Accountability**: Humans can explain and justify decisions.

### 3. Comparative Analysis


| Dimension | Automation | Human Judgment |
|-----------|------------|----------------|
| Consistency | High | Variable |
| Speed | Very High | Limited |
| Novel situations | Poor | Strong |
| Emotional bias | None | Present |
| Scalability | Excellent | Limited |
| Accountability | Model audit | Personal |

## Cognitive Biases in Financial Decision-Making


### 1. Overconfidence


**Definition**: Excessive certainty in own predictions.

**Manifestation**: 

- Underestimate forecast uncertainty
- Overweight own analysis vs. market prices
- Insufficient diversification

**Quantification**: Compare stated confidence intervals to realized outcomes.

### 2. Anchoring


**Definition**: Over-reliance on initial information.

**Example**: Analyst forecasts anchored to previous estimates despite new information.

**Impact**: Slow adjustment to changing conditions.

### 3. Confirmation Bias


**Definition**: Seeking information that confirms existing beliefs.

**Example**: Selectively reading research that supports current positions.

**Risk**: Miss disconfirming evidence of model failure.

### 4. Herding


**Definition**: Following crowd rather than independent analysis.

**Mechanism**: Career risk from being wrong alone exceeds risk from being wrong with everyone.

**Consequence**: Crowded trades, correlated failures.

### 5. Loss Aversion


**Definition**: Losses loom larger than equivalent gains.

$$
|U(-x)| > U(x) \quad \text{for } x > 0
$$

**Impact**: Hold losing positions too long, cut winners too early.

### 6. Recency Bias


**Definition**: Overweight recent observations.

**Example**: After calm period, underestimate tail risk.

**Model Analog**: Rolling window estimation naturally creates recency bias.

## Model-Human Interaction Protocols


### 1. Decision Framework


**Level 1 - Full Automation**: Model executes without human involvement.

- Use for: High-frequency, standardized decisions
- Example: Market-making spread adjustments

**Level 2 - Human-in-the-Loop**: Model recommends, human approves.

- Use for: Material decisions with moderate complexity
- Example: Daily rebalancing of large portfolio

**Level 3 - Human-on-the-Loop**: Model executes, human monitors.

- Use for: Time-sensitive decisions requiring rapid execution
- Example: Algorithm trading with human oversight

**Level 4 - Model-Assisted**: Human decides, model provides input.

- Use for: Novel or complex situations
- Example: Strategic asset allocation review

### 2. Override Protocols


**Conditions for Override**:

1. Model output clearly inconsistent with known facts
2. Unusual market conditions not in model training data
3. Material soft information not captured by model
4. Model malfunction or data error suspected

**Documentation Requirements**:

- Reason for override
- Expected vs. model-recommended action
- Post-hoc review of override decision

### 3. Escalation Procedures


**Automated Alerts**: Trigger when:

- Model outputs exceed historical ranges
- Key assumptions violated
- Performance degrades significantly

**Escalation Path**:

1. Alert to model user
2. Escalate to risk management
3. Escalate to senior management
4. Emergency procedures if critical

## Optimal Allocation of Tasks


### 1. Tasks Best Suited for Automation


**High-Frequency Decisions**: Too fast for human processing.

**Routine Calculations**: Greeks, VaR, margin calculations.

**Data Processing**: Cleaning, aggregation, basic analytics.

**Compliance Checks**: Rule-based validation.

**Execution**: Order routing, algorithmic execution.

### 2. Tasks Requiring Human Judgment


**Strategy Development**: Identifying new opportunities.

**Crisis Management**: Novel situations without historical precedent.

**Relationship Management**: Client interaction, negotiations.

**Ethical Decisions**: Situations with moral dimensions.

**Model Development**: Specifying model structure and assumptions.

### 3. Collaborative Tasks


**Model Validation**: Combine automated tests with expert review.

**Risk Assessment**: Quantitative metrics plus qualitative judgment.

**Investment Decisions**: Model-generated ideas vetted by humans.

**Calibration**: Automated optimization with human reasonableness checks.

## Case Studies in Model-Human Interaction


### 1. Quant Fund Model Override


**Situation**: Model signals aggressive short position; portfolio manager has concerns.

**Process**:

1. PM documents concerns (market structure change, new regulation)
2. Risk committee reviews
3. Decision: Reduce position size, monitor closely

**Outcome**: Position would have been profitable, but risk was appropriate.

**Lesson**: Override process should not require being "right" — appropriate risk management is the goal.

### 2. Trading Algorithm Malfunction


**Situation**: Algorithm generating excessive orders, moving market.

**Response**:

1. Automated circuit breaker triggers
2. Human operator notified
3. Manual review identifies bug
4. System shut down, positions unwound manually

**Lesson**: Human oversight essential for automated systems; must have kill switch.

### 3. Crisis Decision-Making


**Situation**: 2008 financial crisis; standard models failing.

**Adaptation**:

1. Suspended automated rebalancing
2. Senior management direct involvement
3. Scenario analysis replaced VaR
4. Increased liquidity buffers manually

**Lesson**: During regime changes, human judgment must dominate.

## Designing Effective Human-Model Systems


### 1. Transparency


**Model Explainability**: Users should understand model logic.

**Interpretable Outputs**: Provide intuition, not just numbers.

**Uncertainty Communication**: Show confidence intervals, not just point estimates.

### 2. Appropriate Trust Calibration


**Avoid Over-Trust**: Automation bias — excessive reliance on model.

**Avoid Under-Trust**: Rejection of valid model insights due to unfamiliarity.

**Calibration Tools**: Track model performance, build appropriate confidence.

### 3. Feedback Loops


**Performance Tracking**: Compare model recommendations to outcomes.

**Override Analysis**: Review override decisions for patterns.

**Continuous Improvement**: Use feedback to improve both model and protocols.

### 4. Training


**Model Literacy**: Users understand model assumptions and limitations.

**Override Training**: Practice identifying when override is appropriate.

**Bias Awareness**: Education on cognitive biases.

## Regulatory Expectations

Recall (see [§ Model Risk and Governance](../../ch22/model_risk_and_governance/model_validation.md)) for the SR 11-7 framework (effective challenge, independent validation, documentation). Two further regimes constrain the human/automation boundary specifically:

- **GDPR**: right to explanation of automated decisions and right to human review (affects credit scoring, trading access, insurance pricing).
- **MiFID II**: mandated kill switches, designated responsible persons for algorithms, stress testing of automated systems.

## Future Directions


### 1. Machine Learning Integration


**Opportunity**: ML can capture nonlinear patterns humans miss.

**Challenge**: Black-box models harder to interpret and override.

**Approach**: Explainable AI (XAI) methods for interpretability.

### 2. Human-AI Collaboration


**Augmented Intelligence**: AI enhances human capabilities rather than replacing.

**Example**: AI identifies anomalies, human investigates and decides.

### 3. Adaptive Automation


**Dynamic Allocation**: System adjusts automation level based on conditions.

**Calm Markets**: Higher automation.

**Stressed Markets**: More human involvement automatically.

## Summary


### Key Principles


1. **Complementarity**: Humans and models have different strengths
2. **Clear Protocols**: Define when each should dominate
3. **Override Capability**: Always maintain human override option
4. **Bias Awareness**: Recognize limitations of both human and model
5. **Continuous Learning**: Improve allocation over time

### Best Practices


1. Match task to decision-maker (human vs. model)
2. Document override decisions and rationale
3. Train users on model limitations and bias
4. Maintain kill switches for automated systems
5. Review performance of human-model allocation regularly

The optimal balance between human judgment and automation depends on the specific task, market conditions, and organizational capabilities. Effective risk management requires thoughtful design of this interaction.

---

## Exercises

**Exercise 1.** A quantitative trading desk uses an automated hedging system that rebalances delta-neutral positions every 5 minutes. During a flash crash, the system generates a cascade of sell orders. Describe how a human override protocol should be designed: what triggers should pause automated trading, what information should be presented to the human decision-maker, and what decision framework should guide the override?

??? success "Solution to Exercise 1"

    **Human Override Protocol for Automated Hedging During a Flash Crash**

    **Trigger Design: When to Pause Automated Trading**

    The override protocol should operate on a hierarchy of triggers, each with increasing urgency:

    *Tier 1 -- Caution (Yellow Alert)*:

    - Price moves exceed 3 standard deviations of recent 5-minute returns within any 5-minute window.
    - Order book depth falls below 50% of its trailing 1-hour average.
    - The system's own order flow exceeds a threshold fraction (e.g., 10%) of total market volume.

    *Tier 2 -- Warning (Orange Alert)*:

    - Price moves exceed 5 standard deviations in any 5-minute window.
    - Bid-ask spread widens to more than 3 times its trailing average.
    - Multiple correlated instruments move simultaneously beyond normal ranges.
    - The system begins to trigger: automated position sizing is reduced by 50%, and the human decision-maker is paged.

    *Tier 3 -- Halt (Red Alert)*:

    - Circuit breaker conditions: price decline exceeds a hard limit (e.g., 5% in 10 minutes).
    - Order book becomes one-sided (no bids or no offers at reasonable levels).
    - The system generates self-referential feedback: its own orders are a significant fraction of the best bid/offer.
    - Action: all automated trading halts immediately (kill switch activates).

    **Information for the Human Decision-Maker**

    When a Tier 2 or Tier 3 alert fires, the human should receive a concise dashboard showing:

    1. **Current portfolio exposure**: Net delta, gamma, vega, and total notional, compared to limits.
    2. **Recent order flow**: What the algorithm has been doing in the last 5--15 minutes (buys/sells, size, fill rates).
    3. **Market context**: Price charts, volume, bid-ask spread, and order book depth for the primary instrument and correlated instruments.
    4. **P&L impact**: Estimated mark-to-market P&L under current prices and under stress scenarios (e.g., further 5% decline).
    5. **System status**: Whether the algorithm is operating normally, has been throttled, or has been halted.

    **Decision Framework for Override**

    The human decision-maker should follow a structured protocol:

    *Step 1 -- Assess*: Is this a genuine market dislocation or a data/system error? Check whether other data sources confirm the price moves.

    *Step 2 -- Contain*: If genuine, prevent the system from amplifying the move. Cancel all pending orders. Do not place new orders until the situation is assessed.

    *Step 3 -- Evaluate*: Assess current exposure. Can the portfolio survive a further adverse move of equal magnitude? If not, begin reducing exposure manually, prioritizing liquid instruments.

    *Step 4 -- Communicate*: Notify risk management and senior management. Document the situation and decisions.

    *Step 5 -- Resume or Unwind*: Only resume automated trading once market conditions normalize (bid-ask spreads return to within 2x normal, order book depth recovers). If the flash crash has materially changed the portfolio, conduct a full risk review before restarting.

    The key principle is that during extreme events, speed of response matters less than avoiding catastrophic losses. The human override should prioritize capital preservation over profit optimization.

---

**Exercise 2.** Compare the strengths and weaknesses of human judgment versus algorithmic models in the following tasks: (a) calibrating a volatility surface, (b) identifying a regime change in market dynamics, (c) pricing a bespoke structured product, and (d) managing a large portfolio during a liquidity crisis. For each task, recommend the appropriate balance between human and automated decision-making.

??? success "Solution to Exercise 2"

    **Human vs. Algorithmic Strengths Across Financial Tasks**

    **(a) Calibrating a Volatility Surface**

    - **Automation strengths**: Calibration is an optimization problem (minimizing the distance between model and market prices). Algorithms can solve this consistently, quickly, and across thousands of strike-maturity pairs. Numerical methods (Levenberg-Marquardt, differential evolution) handle the high-dimensional parameter space efficiently.
    - **Human strengths**: Humans can identify when calibration is producing unreasonable parameters (e.g., negative vol-of-vol, extreme mean reversion), detect data errors in market quotes, and apply judgment about which instruments to weight more heavily based on liquidity.
    - **Recommendation**: **Level 3 (Human-on-the-Loop)**. Automation performs the calibration; human reviews outputs for reasonableness. Automated checks flag parameter values outside historical ranges. Human approves or adjusts before parameters enter the pricing system.

    **(b) Identifying a Regime Change in Market Dynamics**

    - **Automation strengths**: Statistical tests (CUSUM, Markov regime-switching models) can detect structural breaks in time series. Algorithms can monitor hundreds of indicators simultaneously and compute filtered regime probabilities in real time.
    - **Human strengths**: Humans excel at interpreting the *cause* of a regime change (new policy, geopolitical event, pandemic) and assessing whether it is temporary or permanent. Humans can incorporate soft information (news, expert commentary) that statistical models cannot process.
    - **Recommendation**: **Level 4 (Model-Assisted)**. Models provide statistical signals and regime probabilities; human analysts interpret the signals in context and decide on the appropriate response. This is because false positives in regime detection are costly (premature position changes), and the consequences of missing a true regime change are severe.

    **(c) Pricing a Bespoke Structured Product**

    - **Automation strengths**: Monte Carlo simulation, PDE solvers, and characteristic function methods can price complex payoffs accurately, given a model specification.
    - **Human strengths**: Bespoke products require understanding the client's specific needs, legal terms, and risk transfer structure. The choice of model (which assumptions to make) is a judgment call. Humans can identify terms in the contract that create non-standard risks (e.g., knock-in barriers, early termination clauses).
    - **Recommendation**: **Level 2 (Human-in-the-Loop)**. Human structures the product, selects the model, and reviews the price. Automation performs the computation. Human performs sanity checks (e.g., does the price satisfy put-call parity-like bounds? Is it between the prices of simpler products that bound its payoff?).

    **(d) Managing a Large Portfolio During a Liquidity Crisis**

    - **Automation strengths**: Can rapidly compute exposures, P&L, and margin requirements. Can execute unwinding strategies according to pre-programmed rules.
    - **Human strengths**: During a liquidity crisis, standard models fail (bid-ask spreads are not reflected in mid-market models, correlations spike, liquidity disappears). Humans can negotiate with counterparties, make strategic decisions about which positions to prioritize for unwinding, and assess systemic considerations that models ignore.
    - **Recommendation**: **Level 4 or Full Human Override**. During a liquidity crisis, automated systems should be largely suspended or severely constrained. Human decision-makers should lead, using model outputs only as one input among many. The 2008 crisis demonstrated that firms that relied heavily on automated risk management (following VaR-based rules mechanically) often made the worst decisions (forced selling at the worst prices).

---

**Exercise 3.** The concept of "automation bias" describes the tendency for humans to over-rely on automated systems. In a risk management context, a trader consistently approves model-generated hedge ratios without independent verification. Design an organizational process that mitigates automation bias while preserving the efficiency benefits of automated systems.

??? success "Solution to Exercise 3"

    **Mitigating Automation Bias in Risk Management**

    **The Problem**

    Automation bias occurs when humans trust automated outputs without sufficient scrutiny. In this scenario, a trader rubber-stamps model-generated hedge ratios, potentially missing errors in the model, stale inputs, or regime changes that invalidate the model's assumptions. This creates a dangerous situation where the apparent safety of hedging masks actual unhedged risk.

    **Organizational Process Design**

    *Component 1 -- Mandatory Independent Checks (Random Sampling)*:

    - Each day, a randomly selected subset (e.g., 10--20%) of model-generated hedge ratios are flagged for mandatory independent verification.
    - The trader must compute or verify the hedge ratio using an independent method (e.g., a different model, a Bloomberg calculator, or a hand calculation for simple cases) before the hedge is executed.
    - The selection is random and unpredictable, so the trader cannot anticipate which ratios will be checked. This maintains vigilance across all positions.

    *Component 2 -- Structured Attestation*:

    - Before approving any hedge ratio, the trader must complete a brief checklist:
        - Are the market data inputs current (within the last 15 minutes)?
        - Is the implied volatility used by the model consistent with the current market?
        - Does the hedge ratio have the expected sign and approximate magnitude?
        - Has the model been recalibrated today?
    - This takes 30--60 seconds per position but forces active engagement rather than passive approval.

    *Component 3 -- Anomaly Detection Layer*:

    - An automated pre-screen compares today's hedge ratios to yesterday's and to a simple benchmark (e.g., Black-Scholes delta).
    - If the change exceeds a threshold (e.g., delta changes by more than 0.05, or the model delta differs from Black-Scholes delta by more than 0.10), the system flags the position for enhanced review.
    - This preserves efficiency: most positions pass the screen automatically, and only anomalous positions require detailed human attention.

    *Component 4 -- Periodic "Fire Drills"*:

    - Monthly, the risk management team intentionally introduces a known error into the model inputs (e.g., a stale volatility, an incorrect interest rate) and observes whether the trader detects it.
    - Results are tracked and discussed (not punitively, but as a learning exercise).
    - This maintains awareness that model outputs can be wrong.

    *Component 5 -- Performance Tracking and Feedback*:

    - Track hedging P&L attribution: decompose into delta P&L (explained by the hedge), gamma P&L (residual from discrete rebalancing), and unexplained P&L (model error).
    - If unexplained P&L consistently exceeds expectations, this is evidence that the model is not performing well and the trader's unquestioning acceptance of its outputs is costly.
    - Present this data to the trader regularly to build appropriate calibration of trust.

    **Preserving Efficiency**

    The design avoids requiring the trader to independently verify every hedge ratio (which would negate the benefit of automation). Instead, it uses targeted interventions (random sampling, anomaly detection, fire drills) to maintain alertness while allowing routine positions to flow through efficiently.

---

**Exercise 4.** Consider a model that predicts credit default probabilities using machine learning. The model's outputs are used to set credit limits. A credit analyst notices that the model assigns low default probability to a company despite qualitative warning signs (management turnover, accounting irregularities). Formalize a decision framework that combines the quantitative model output with qualitative analyst judgment, including explicit rules for when analyst overrides are warranted.

??? success "Solution to Exercise 4"

    **Decision Framework Combining Quantitative Model and Qualitative Analyst Judgment**

    **Formalizing the Problem**

    Let $p_M \in [0, 1]$ denote the model's estimated default probability and $s_A \in \{-2, -1, 0, +1, +2\}$ denote the analyst's qualitative signal, where negative values indicate concern and positive values indicate confidence above the model estimate. The goal is to produce a combined default probability $p_C$ and a credit limit decision.

    **Bayesian Combination Framework**

    One principled approach treats the model and analyst as two signals about the true default probability $p^*$.

    *Step 1 -- Prior*: Start with the model estimate $p_M$ as the prior, reflecting the model's processing of quantitative data (financial ratios, market prices, macroeconomic variables).

    *Step 2 -- Analyst signal as likelihood*: The analyst's qualitative assessment shifts the estimate based on soft information. Define an adjustment factor $\alpha(s_A)$:

    $$
    \log\left(\frac{p_C}{1 - p_C}\right) = \log\left(\frac{p_M}{1 - p_M}\right) + \alpha(s_A)
    $$

    where $\alpha(s_A)$ maps the analyst's signal to a log-odds adjustment. For example:

    | $s_A$ | Interpretation | $\alpha(s_A)$ |
    |-------|---------------|----------------|
    | $-2$ | Strong concern | $+1.0$ (doubles odds of default) |
    | $-1$ | Moderate concern | $+0.5$ |
    | $0$ | Neutral | $0$ |
    | $+1$ | Moderate confidence | $-0.5$ |
    | $+2$ | Strong confidence | $-1.0$ |

    For the given scenario, $p_M$ is low (say 0.02) but $s_A = -2$ (management turnover, accounting irregularities). Then:

    $$
    \log\left(\frac{p_C}{1 - p_C}\right) = \log\left(\frac{0.02}{0.98}\right) + 1.0 = -3.89 + 1.0 = -2.89
    $$

    $$
    p_C = \frac{e^{-2.89}}{1 + e^{-2.89}} = \frac{0.056}{1.056} \approx 0.053
    $$

    The combined default probability increases from 2% to approximately 5.3%, which may now exceed the threshold for the assigned credit limit.

    **Explicit Rules for Override**

    An analyst override of the model is warranted when:

    1. **Material non-public qualitative information**: The analyst has information that the model structurally cannot process (e.g., knowledge of pending litigation, management fraud indicators, supplier relationship breakdown).

    2. **Model input staleness**: The model uses financial data that is several months old, but the analyst knows of material recent developments.

    3. **Structural model limitation**: The model does not include a relevant risk factor (e.g., the model does not account for country risk, and the company has significant exposure to a country experiencing political turmoil).

    4. **Pattern recognition**: The analyst recognizes a pattern consistent with historical defaults that the model has not been trained on (e.g., rapid management turnover followed by accounting restatements is a classic pre-default pattern).

    **Override Process Requirements**

    - The analyst must document the specific qualitative factors motivating the override.
    - The override must be reviewed by a senior credit officer within 24 hours.
    - All overrides are tracked, and their outcomes (did the company actually default or deteriorate?) are reviewed quarterly to calibrate the analyst's judgment over time.
    - The calibration parameters $\alpha(s_A)$ should be updated periodically based on the historical accuracy of analyst overrides versus model-only assessments.

    **Credit Limit Decision Rule**

    Given the combined probability $p_C$ and the exposure amount $E$, the expected loss is:

    $$
    \text{EL} = p_C \times \text{LGD} \times E
    $$

    The credit limit is set such that EL does not exceed the allocated risk budget. When the analyst override increases $p_C$ significantly, the credit limit should be reduced proportionally, or additional collateral/covenants should be required.

---

**Exercise 5.** During the COVID-19 market dislocation in March 2020, many quantitative models produced signals that were historically unprecedented. Describe how a well-designed human-automation system should handle such situations. What specific thresholds or indicators should trigger a shift from automated to human-led decision-making?

??? success "Solution to Exercise 5"

    **Human-Automation System Design for Unprecedented Market Dislocations (COVID-19 March 2020)**

    **What Made March 2020 Unprecedented**

    - The VIX rose from 14 to 82 in four weeks, a magnitude and speed without precedent in the VIX's history.
    - Cross-asset correlations spiked: equities, credit, commodities, and even Treasury markets experienced simultaneous stress.
    - Liquidity disappeared across asset classes, including traditionally safe assets (Treasury off-the-runs, investment-grade corporate bonds).
    - The economic cause (a pandemic) was entirely outside the scope of standard financial models.
    - Central bank interventions (emergency rate cuts, unlimited QE) created discontinuous policy shifts.

    **Thresholds and Indicators for Shifting to Human-Led Decision-Making**

    *Category 1 -- Volatility Regime Indicators*:

    - VIX exceeds its 99th historical percentile (approximately 40 based on post-1990 data). This indicates the market has entered an extreme regime.
    - Realized volatility over any trailing 5-day window exceeds 3 times its trailing 60-day average.
    - Implied volatility term structure inverts (short-term IV exceeds long-term IV by more than 10 vol points), indicating acute near-term fear.

    *Category 2 -- Liquidity Indicators*:

    - Bid-ask spreads in core instruments (S&P 500 futures, 10-year Treasury, investment-grade credit indices) exceed 3 times their trailing 20-day average.
    - Market depth (quantity available at best bid/offer) falls below 25% of its trailing average.
    - Repo rates spike or funding markets show stress (LIBOR-OIS spread exceeds 50 bps).

    *Category 3 -- Correlation Indicators*:

    - Rolling 10-day correlation between equities and bonds exceeds +0.5 (normally negative, indicating diversification failure).
    - Average pairwise correlation among S&P 500 stocks exceeds 0.7 (indicating undifferentiated selling).
    - Cross-asset volatility (equities, credit, rates, FX) all exceed 90th percentile simultaneously.

    *Category 4 -- Model Performance Indicators*:

    - Backtesting violations: model VaR exceeded more than 3 times in a 10-day window (at 99% confidence, expect approximately 1 violation per 100 days).
    - Hedge P&L attribution shows unexplained P&L exceeding 50% of total P&L.
    - Calibration failure: model cannot fit current market prices within acceptable tolerance.

    **How the System Should Respond**

    *Phase 1 -- Heightened Monitoring* (any Category 1 or 2 threshold breached):

    - Reduce automation level from Level 1/3 to Level 2 (human-in-the-loop).
    - Reduce automated position sizing by 50%.
    - Increase reporting frequency from daily to intraday.
    - Convene risk management meeting within 2 hours.

    *Phase 2 -- Human-Led Decision-Making* (multiple categories breached or Category 4 triggered):

    - Suspend automated rebalancing and hedging.
    - Senior management assumes direct control of portfolio decisions.
    - Replace VaR-based risk limits with scenario-based limits (e.g., "portfolio must survive a further 20% decline").
    - Prioritize liquidity: build cash buffers, unwind illiquid positions if possible.
    - Use model outputs only as one reference among many; do not rely on any single model.

    *Phase 3 -- Recovery* (indicators return below thresholds for 5 consecutive days):

    - Gradually reintroduce automated systems, starting with Level 3 (human-on-the-loop).
    - Recalibrate models using data that includes the crisis period.
    - Conduct post-mortem analysis of model performance during the crisis.
    - Update thresholds and protocols based on lessons learned.

    **Key Principle**: The system should fail safe -- when in doubt about whether conditions are unprecedented, default to more human involvement rather than less. The cost of temporarily reduced efficiency is far less than the cost of algorithmic decisions in conditions the algorithm was never designed to handle.

---

**Exercise 6.** A bank's model validation team must decide whether to approve a new AI-based pricing model that outperforms traditional models on backtests but is largely unexplainable (a "black box"). Discuss the trade-off between model accuracy and interpretability, and propose a framework for evaluating whether the model should be deployed, including the role of human oversight in monitoring its ongoing performance.

??? success "Solution to Exercise 6"

    **Accuracy vs. Interpretability Trade-Off for AI Pricing Models**

    **The Fundamental Trade-Off**

    Model accuracy and interpretability often exist in tension:

    | Property | Traditional Models | AI/ML Models |
    |----------|-------------------|--------------|
    | Accuracy (backtest) | Moderate | High |
    | Interpretability | High | Low |
    | Extrapolation reliability | Known (via theory) | Unknown |
    | Regulatory acceptance | Established | Uncertain |
    | Failure modes | Understood | Opaque |

    A traditional model (e.g., Heston for option pricing) may have lower backtest accuracy but its failures are well-characterized: we know it assumes constant parameters, and we know how to stress-test those assumptions. A neural network may achieve lower pricing errors on historical data but could fail catastrophically in novel market conditions without warning.

    **Proposed Evaluation Framework**

    *Criterion 1 -- Accuracy Assessment (Necessary but Not Sufficient)*:

    - Out-of-sample backtesting across multiple time periods, including crisis periods.
    - Comparison to multiple benchmark models (not just one traditional model).
    - Accuracy must be evaluated on economically meaningful metrics: hedging P&L, not just pricing error. A model that prices well but hedges poorly is dangerous.
    - Statistical significance: is the improvement over traditional models statistically significant, or could it be due to overfitting?

    *Criterion 2 -- Interpretability Assessment*:

    - Apply explainability methods: SHAP values, LIME, attention maps, or partial dependence plots to understand which inputs drive the model's outputs.
    - Verify that the model's sensitivities (Greeks) have economically reasonable signs and magnitudes. For example, does the model's delta satisfy $0 \leq \Delta_{\text{call}} \leq 1$? Does vega have the correct sign? Is gamma positive for vanilla options?
    - Identify failure modes: construct adversarial inputs (extreme parameter values, unusual market conditions) and examine whether the model's outputs remain reasonable.

    *Criterion 3 -- Robustness Assessment*:

    - Sensitivity to training data: retrain on different subsets and measure output variation.
    - Sensitivity to architecture: does the model's performance change significantly with minor architecture changes (number of layers, activation functions)?
    - Out-of-distribution detection: can the model identify when its inputs are outside the training distribution and flag reduced confidence?

    *Criterion 4 -- Operational Risk Assessment*:

    - Can the model be independently replicated by the validation team?
    - Is the training pipeline reproducible?
    - What happens if the model fails silently (produces plausible but incorrect outputs)?

    **Deployment Decision Framework**

    *Approve for production use if*:

    - All four criteria are satisfactory.
    - Adequate human oversight is in place (see below).
    - The model is not the sole pricing/risk model; a traditional model runs in parallel.

    *Approve for shadow mode only if*:

    - Accuracy is demonstrated but interpretability or robustness concerns remain.
    - The model runs alongside the production model, and outputs are compared daily, but the traditional model's outputs are used for actual decisions.
    - Shadow mode continues until interpretability and robustness concerns are resolved (minimum 6 months).

    *Reject if*:

    - The model cannot be shown to satisfy basic economic constraints (arbitrage-free, correct Greeks signs).
    - The model's performance degrades significantly in crisis periods.
    - The model cannot be independently replicated.

    **Human Oversight in Ongoing Monitoring**

    If the model is deployed:

    1. **Daily monitoring**: Compare AI model outputs to traditional model outputs. Investigate any divergence exceeding a threshold (e.g., pricing difference > 1% of option value).

    2. **Monthly backtesting**: Compute formal backtesting statistics (Kupiec test for VaR, hedging P&L tracking for pricing models).

    3. **Quarterly model review**: The validation team conducts a comprehensive review including re-running interpretability analyses on recent data to check for drift in the model's behavior.

    4. **Kill switch**: If the model produces outputs that violate no-arbitrage bounds (e.g., negative call prices, call prices exceeding spot price, put-call parity violations), it is automatically switched off and the traditional model takes over.

    5. **Regulatory reporting**: All model decisions, overrides, and performance metrics are documented for regulatory review. Under SR 11-7, the bank must demonstrate effective challenge of the model, which is harder for black-box models and requires more intensive ongoing monitoring.
