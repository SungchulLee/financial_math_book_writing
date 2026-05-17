# Case Studies in Model Failure

Quantitative models drive decision-making in modern finance, but models occasionally fail dramatically. Examining historical failures—Long-Term Capital Management (LTCM), Barings Bank, the London Whale trading loss, and the 2008 financial crisis—reveals recurring patterns: excessive leverage, model over-confidence, organizational breakdowns, and market regime changes.

## Key Concepts

**Long-Term Capital Management (1998)**
LTCM operated a "market-neutral" convergence trading strategy using sophisticated mathematical models:

- **Model logic**: historical spreads reliably mean-revert; pairs trading hedges directional risk
- **Capital**: \$5 billion with 25:1 leverage on a \$125 billion portfolio
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
- **Losses**: \$1.3 billion, more than Barings' equity; bank collapsed

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

- **Notional exposure**: \$100 billion in credit derivatives
- **Strategy**: intended as hedge but became speculative position
- **Trigger**: market volatility increased; position moved against the bank
- **Losses**: \$6 billion (officially), possibly \$9 billion including unwinding costs

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
The 2008 crisis combined housing-price, CDO/Gaussian-copula, liquidity, and counterparty-risk model failures simultaneously. Recall (see [§ Model Risk in Credit Markets](../../ch21/model_risk_in_credit_markets/wrong_way_risk.md)) for the Gaussian-copula and CDO-tranche breakdown in detail. Distinct systemic features of 2008:

- **Calibration to normal times**: parameters estimated 1990--2007 excluded prior crises
- **Regulatory arbitrage** under Basel II: capital minimized through model exploits
- **Procyclicality**: low VaR in good times encouraged risk-taking; high VaR in bad times forced deleveraging
- **Interconnectedness**: Lehman's $\sim$930{,}000 derivative contracts revealed hidden systemic linkages

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

---

## Exercises

**Exercise 1.** In the LTCM crisis, convergence trades between on-the-run and off-the-run Treasury bonds widened dramatically instead of converging. Explain how the use of historical correlation assumptions in the risk model led to a severe underestimation of portfolio risk. What specific model assumption was violated, and how could a robust framework (e.g., worst-case volatility or stress testing) have flagged this risk?

??? success "Solution to Exercise 1"

    **LTCM Convergence Trade Failure and Correlation Assumptions**

    LTCM's convergence trades relied on the assumption that spreads between on-the-run and off-the-run Treasury bonds would narrow over time. The risk model estimated portfolio risk using a historical variance-covariance matrix $\Sigma$ computed from normal-period data (approximately 1990--1997).

    **The Core Model Assumption**

    The portfolio variance was computed as:

    $$
    \sigma_P^2 = \mathbf{w}^\top \Sigma \mathbf{w}
    $$

    where $\mathbf{w}$ is the vector of position weights. If the portfolio consisted of $n$ convergence trades with individual variance $\sigma^2$ and pairwise correlation $\rho$, then:

    $$
    \sigma_P^2 = \sigma^2 \left[ \sum_{i=1}^n w_i^2 + \rho \sum_{i \neq j} w_i w_j \right] = \sigma^2 \left[ \|\mathbf{w}\|^2 + \rho \left( (\mathbf{1}^\top \mathbf{w})^2 - \|\mathbf{w}\|^2 \right) \right]
    $$

    For equally weighted positions with $w_i = 1/n$, this simplifies to:

    $$
    \sigma_P^2 = \frac{\sigma^2}{n} \left[ 1 + (n-1)\rho \right]
    $$

    During normal periods, $\rho \approx 0.2$, so for $n = 20$ trades, $\sigma_P^2 \approx \sigma^2 \cdot (1 + 19 \cdot 0.2)/20 = \sigma^2 \cdot 4.8/20 = 0.24\sigma^2$. The model reported substantial diversification benefit.

    **The Violated Assumption**

    The specific assumption violated was **correlation stationarity**. During the Russian default crisis, all convergence trades moved adversely simultaneously because of a common risk factor: flight to quality. The crisis correlation rose to $\rho^{\text{crisis}} \approx 0.8$, giving:

    $$
    \sigma_P^{2,\text{crisis}} = \frac{\sigma^2}{20}(1 + 19 \cdot 0.8) = \frac{16.2 \sigma^2}{20} = 0.81\sigma^2
    $$

    The ratio of crisis-to-normal portfolio variance is $0.81/0.24 \approx 3.4$, meaning the portfolio standard deviation was approximately $\sqrt{3.4} \approx 1.84$ times what the model predicted. With 25:1 leverage, this translated to a leveraged loss factor of approximately $25 \times 1.84 = 46$ times the expected volatility per unit of equity.

    **How a Robust Framework Would Have Helped**

    A **worst-case volatility** framework would replace the single estimate $\Sigma$ with a set of plausible covariance matrices $\mathcal{U}$:

    $$
    \text{VaR}_{\text{robust}} = \max_{\Sigma \in \mathcal{U}} \sqrt{\mathbf{w}^\top \Sigma \mathbf{w}} \cdot z_\alpha
    $$

    This could include stress scenarios with $\rho \in [0.5, 0.9]$ based on prior crisis episodes (e.g., the 1992 ERM crisis or 1994 bond market selloff). Alternatively, **reverse stress testing** would ask: "What correlation level would cause insolvency?" The answer, given 25:1 leverage, would have been a relatively modest correlation increase, clearly flagging the fragility of the strategy.

---

**Exercise 2.** During the 2007-2008 financial crisis, CDO tranches experienced losses far beyond what Gaussian copula models predicted. Explain the role of correlation assumptions in the Gaussian copula model, and describe quantitatively how a change from $\rho = 0.3$ to $\rho = 0.8$ in the default correlation would affect the expected loss on a mezzanine tranche. What alternative copula structures better capture tail dependence?

??? success "Solution to Exercise 2"

    **Gaussian Copula, Correlation, and Mezzanine Tranche Losses**

    **The Gaussian Copula Model**

    In the one-factor Gaussian copula model, each obligor $i$ defaults when a latent variable $X_i$ falls below a threshold $c_i$:

    $$
    X_i = \sqrt{\rho}\, Z + \sqrt{1 - \rho}\, \epsilon_i
    $$

    where $Z \sim N(0,1)$ is the systematic factor, $\epsilon_i \sim N(0,1)$ is the idiosyncratic factor, and $\rho$ is the (common) default correlation. The conditional default probability given the systematic factor is:

    $$
    p(Z) = \Phi\left(\frac{\Phi^{-1}(p_i) - \sqrt{\rho}\, Z}{\sqrt{1-\rho}}\right)
    $$

    where $p_i$ is the marginal default probability and $\Phi$ is the standard normal CDF.

    **Effect of Correlation on Mezzanine Tranche**

    Consider a pool of 100 homogeneous obligors with individual default probability $p = 0.05$ and recovery rate $R = 0.40$. The mezzanine tranche covers losses between attachment point $a = 3\%$ and detachment point $d = 7\%$ of the pool notional.

    At **low correlation** ($\rho = 0.3$): Defaults are relatively independent. The loss distribution is concentrated around the expected loss $\text{EL} = p(1 - R) = 0.05 \times 0.60 = 3\%$. The mezzanine tranche has moderate expected loss because the bulk of the loss distribution falls near the attachment point. Conditional on the systematic factor $Z$, most scenarios produce losses near the expected value, with modest probability of reaching into the mezzanine region.

    At **high correlation** ($\rho = 0.8$): The loss distribution becomes bimodal. Either the systematic factor is favorable and almost no one defaults, or the systematic factor is adverse and a large fraction of the pool defaults simultaneously. The conditional default probability $p(Z)$ swings widely with $Z$:

    - For $Z = 1$ (favorable): $p(Z) = \Phi\left(\frac{-1.645 - 0.894}{0.447}\right) \approx \Phi(-5.68) \approx 0$
    - For $Z = -2$ (adverse): $p(Z) = \Phi\left(\frac{-1.645 + 1.789}{0.447}\right) \approx \Phi(0.32) \approx 0.63$

    In the adverse scenario, portfolio loss $\approx 0.63 \times 0.60 = 37.8\%$, far exceeding the detachment point. The mezzanine tranche is completely wiped out.

    **Quantitative Impact**

    The expected loss on the mezzanine tranche can be approximated by:

    $$
    \text{EL}_{\text{mezz}} = \frac{1}{d - a} \int_{-\infty}^{\infty} \left[\min(L(z), d) - \min(L(z), a)\right]^+ \phi(z)\, dz
    $$

    where $L(z) = p(z)(1 - R)$ is the conditional portfolio loss. Numerically, the expected loss on the mezzanine tranche approximately doubles or triples when moving from $\rho = 0.3$ to $\rho = 0.8$, and the probability of complete tranche wipeout increases dramatically.

    **Alternative Copulas with Better Tail Dependence**

    The Gaussian copula has zero upper tail dependence coefficient $\lambda_U = 0$, meaning it underestimates joint extreme events. Alternatives include:

    1. **Student-$t$ copula**: Has positive upper and lower tail dependence $\lambda_U > 0$, controlled by the degrees of freedom parameter $\nu$. As $\nu \to \infty$, it converges to the Gaussian copula.

    2. **Clayton copula**: Captures lower tail dependence ($\lambda_L > 0$), appropriate for joint downside risk, but has no upper tail dependence.

    3. **Marshall-Olkin copula**: Models common shocks (e.g., a systemic event that causes all defaults simultaneously), naturally generating clustered defaults.

    4. **Dynamic copulas**: Allow $\rho_t$ to vary over time, capturing the empirical phenomenon of correlation increasing during crises.

---

**Exercise 3.** The "London Whale" incident at JPMorgan in 2012 involved a VaR model change that halved the reported risk of a large credit derivatives portfolio. Discuss how model governance failures (changing the VaR model mid-stream, using Excel-based calculations) contributed to the loss. What organizational controls would have prevented or detected this issue earlier?

??? success "Solution to Exercise 3"

    **London Whale: Model Governance Failures**

    **The VaR Model Change**

    In early 2012, JPMorgan's Chief Investment Office (CIO) changed its VaR model for the Synthetic Credit Portfolio. The key changes included:

    1. **New model halved reported VaR**: The old model reported VaR of approximately \$132 million; the new model reported approximately \$67 million. This reduction was not due to actual risk reduction but to methodological changes in how correlations and volatilities were estimated.

    2. **Excel-based calculations**: Critical risk calculations were performed in spreadsheets rather than robust, version-controlled systems. A specific error involved a formula that divided by a sum instead of an average, systematically underestimating volatility.

    3. **Mid-stream model change**: The model was changed while the portfolio was being built up, making it impossible to track whether risk was genuinely changing or just being reported differently.

    **How Governance Failures Contributed**

    *Lack of independent validation*: The model change was not independently validated before deployment. Under SR 11-7, any material model change should undergo independent review by a model validation team that does not report to the business line.

    *Override of risk warnings*: The CIO's risk management team raised concerns about the growing position, but these were dismissed by the business. The VaR limit was effectively adjusted by changing the model rather than reducing the position.

    *Inadequate documentation*: The rationale for the model change was poorly documented. There was no formal comparison showing that the new model was more accurate than the old one.

    *Missing backtesting*: The new model was not backtested against historical data to verify that its lower VaR estimates were justified. Proper backtesting would have shown the new model had more exceptions (actual losses exceeding VaR) than the old model.

    **Organizational Controls That Would Have Prevented the Issue**

    1. **Model change committee**: Any model change must be approved by an independent committee including risk management, model validation, and senior management. Changes to models for positions exceeding a materiality threshold require additional scrutiny.

    2. **Parallel running**: When a model is changed, both old and new models should run in parallel for a minimum period (e.g., 90 days). Any material difference in outputs must be explained and documented.

    3. **Independent recalculation**: Risk metrics should be independently recalculated by a team outside the business line, using independently maintained systems (not Excel spreadsheets shared with the trading desk).

    4. **P&L attribution**: Daily P&L should be decomposed into components explained by risk factors. Unexplained P&L (the residual) is a warning sign. Large unexplained P&L in the CIO would have triggered investigation.

    5. **Position limits independent of VaR**: In addition to VaR limits, hard notional limits and gross/net exposure limits should constrain position size regardless of what the VaR model reports.

    6. **Whistleblower protection and escalation**: Traders and risk managers who raise concerns should have a clear escalation path to senior management and the board, with protection against retaliation.

---

**Exercise 4.** Compare the model failures in the 1987 Black Monday crash and the 2020 COVID-19 market crash. In both cases, implied volatilities spiked far beyond historical levels. Discuss whether a model incorporating regime-switching (with a "crisis" regime) would have provided adequate hedging, and identify the fundamental challenge of calibrating rare-event models from limited historical data.

??? success "Solution to Exercise 4"

    **Comparing Model Failures: 1987 Black Monday vs. 2020 COVID-19 Crash**

    **1987 Black Monday**

    - On October 19, 1987, the Dow Jones fell 22.6% in a single day.
    - Implied volatility spiked from roughly 20% to over 150% intraday.
    - Portfolio insurance strategies (synthetic puts via dynamic delta hedging) amplified the crash through feedback: as prices fell, delta-hedging required selling more stock, pushing prices down further.
    - Models assumed continuous trading and liquidity; both failed.

    **2020 COVID-19 Crash**

    - Between February 19 and March 23, 2020, the S&P 500 fell 34%.
    - VIX spiked from 14 to over 82 (the highest since 2008).
    - The cause was exogenous (pandemic) rather than endogenous (trading strategy feedback).
    - Models calibrated to post-2008 data had not seen a pandemic-driven selloff.

    **Regime-Switching Model Assessment**

    A two-regime model specifies:

    $$
    \text{Regime 1 (Normal):} \quad r_t \sim N(\mu_1, \sigma_1^2), \quad \mu_1 > 0, \quad \sigma_1 \approx 0.15
    $$

    $$
    \text{Regime 2 (Crisis):} \quad r_t \sim N(\mu_2, \sigma_2^2), \quad \mu_2 < 0, \quad \sigma_2 \approx 0.40
    $$

    with transition matrix:

    $$
    P = \begin{pmatrix} 1 - p_{12} & p_{12} \\ p_{21} & 1 - p_{21} \end{pmatrix}
    $$

    **Would Regime-Switching Have Provided Adequate Hedging?**

    *Partial yes*: A regime-switching model would have assigned non-zero probability to a crisis state, leading to:

    - Higher option-implied volatilities (reflecting the mixture distribution).
    - Larger VaR estimates that account for possible regime shifts.
    - Delta-hedging strategies that incorporate the possibility of jumping to the crisis regime, resulting in more conservative hedge ratios.

    The hedge ratio in a regime-switching model incorporates regime probabilities:

    $$
    \Delta_{\text{RS}} = \pi_1(t) \Delta_1 + \pi_2(t) \Delta_2
    $$

    where $\pi_i(t)$ is the filtered probability of being in regime $i$ at time $t$, and $\Delta_i$ is the hedge ratio conditional on regime $i$.

    *Fundamental limitations*:

    1. **Calibration from limited data**: The transition probability $p_{12}$ (normal to crisis) is estimated from historical crises. With perhaps 5--10 crisis episodes in 50 years of data, the estimate is highly uncertain. A small change in $p_{12}$ (e.g., from 0.01 to 0.03) dramatically changes the model's risk assessment.

    2. **Crisis severity is variable**: The 1987 crash was a one-day event driven by endogenous feedback; the 2020 crash was a multi-week event driven by an exogenous pandemic. A two-state model with fixed $\mu_2, \sigma_2$ cannot capture this heterogeneity.

    3. **Novel crisis types**: Each crisis has unique features. The 1987 crash involved portfolio insurance feedback loops. The 2020 crash involved a global pandemic. A model calibrated to one type of crisis may not protect against the next.

    4. **Timing of regime detection**: The model must infer regime shifts in real time via filtering. During the early stages of a crash, the filtered probability $\pi_2(t)$ increases gradually, meaning the model reacts *after* significant losses have already occurred.

    **Conclusion**: Regime-switching improves upon single-regime models by acknowledging the possibility of crises, but it cannot fully solve the problem because the nature, timing, and severity of future crises are fundamentally unpredictable from historical data. The model provides a framework for thinking about tail risk, not a precise prediction of it.

---

**Exercise 5.** The Barings Bank collapse (1995) involved unauthorized trading by Nick Leeson. While primarily an operational risk failure, discuss how the absence of model-based position monitoring and real-time risk aggregation contributed to the loss. Design a model-based alert system that would have detected the growing exposure.

??? success "Solution to Exercise 5"

    **Barings Bank: Operational Risk and Model-Based Detection**

    **How Absence of Model-Based Monitoring Contributed**

    Nick Leeson accumulated unauthorized positions in Nikkei 225 futures and options on the Singapore and Osaka exchanges, hiding losses in a secret account (error account 88888). The key failures were:

    1. **No real-time position aggregation**: Barings did not have a system that aggregated Leeson's positions across exchanges in real time. A position monitoring system would have shown that the net exposure was far larger than authorized.

    2. **No independent margin reconciliation**: The margin calls from the exchanges should have been reconciled against authorized trading limits. Instead, Leeson controlled both execution and back-office reconciliation.

    3. **No Greeks monitoring**: Leeson's short straddle positions had large negative gamma exposure:

        $$
        \Gamma_{\text{portfolio}} = \sum_i n_i \Gamma_i < 0
        $$

        A model computing portfolio Greeks would have shown that a significant market move in either direction would generate large losses. The vega exposure was also large and negative, meaning any volatility spike (such as from the Kobe earthquake) would be devastating.

    4. **No P&L verification**: Daily P&L should have been independently computed from market prices and known positions. The hidden losses would have appeared as discrepancies.

    **Design of a Model-Based Alert System**

    *Layer 1 -- Position Monitoring (Real-Time)*:

    - Aggregate all positions by trader, desk, and entity across all exchanges.
    - Alert triggers: (a) net delta exposure exceeds authorized limit, (b) notional value exceeds threshold, (c) any position in unauthorized instruments.
    - Data: real-time trade feeds from exchanges, position database.

    *Layer 2 -- Risk Metrics (Intraday)*:

    - Compute portfolio VaR, delta, gamma, vega, and theta at least every hour.
    - Alert triggers: (a) VaR exceeds limit, (b) gamma exceeds limit (indicating concentrated directional bet), (c) vega exposure exceeds limit.
    - For Leeson's position, the VaR alert would have triggered when Nikkei futures notional exceeded approximately \$3--5 billion.

    *Layer 3 -- P&L Reconciliation (Daily)*:

    - Independently compute theoretical P&L from market moves and known positions: $\text{P\&L} \approx \Delta \cdot \Delta S + \frac{1}{2}\Gamma (\Delta S)^2 + \Theta \Delta t + \text{vega} \cdot \Delta \sigma$.
    - Compare to reported P&L.
    - Alert trigger: unexplained P&L exceeding a threshold (e.g., more than 10% of theoretical P&L).
    - This would have detected the hidden losses accumulating in account 88888.

    *Layer 4 -- Margin and Funding Flows (Daily)*:

    - Monitor margin calls from exchanges and reconcile against authorized positions.
    - Alert trigger: margin calls inconsistent with reported positions.
    - Barings was sending hundreds of millions in margin to Singapore; this should have triggered investigation.

    *Layer 5 -- Segregation of Duties (Structural)*:

    - No individual should control both trade execution and trade confirmation/settlement.
    - System-enforced separation: different login credentials, different reporting lines, mandatory dual authorization for transfers above threshold.

    This layered system would have detected Leeson's growing exposure within days, well before losses reached the level that destroyed the bank.

---

**Exercise 6.** After each major model failure, regulators have responded with new requirements (e.g., Basel II after LTCM, Basel III after 2008, FRTB after 2008). Discuss the phenomenon of "regulatory model risk"---the risk that models designed to satisfy regulations become targets for regulatory arbitrage. Give a specific example of how a bank might exploit the VaR framework to reduce reported risk without reducing actual risk.

??? success "Solution to Exercise 6"

    **Regulatory Model Risk and VaR Arbitrage**

    **The Phenomenon of Regulatory Model Risk**

    Regulatory model risk arises from a fundamental tension: regulators prescribe specific models or frameworks for computing capital requirements, but the regulated entities have strong economic incentives to minimize capital. When the regulatory framework specifies a particular model structure (e.g., VaR at 99% confidence over 10 days), banks can exploit the known weaknesses of that structure to reduce reported risk without genuinely reducing actual risk.

    This creates a cycle:

    1. Crisis occurs, revealing model inadequacy.
    2. Regulators impose new model-based requirements.
    3. Banks optimize against the new requirements.
    4. New risks accumulate in areas not captured by the regulatory model.
    5. Next crisis reveals new inadequacy.

    **Historical Examples of the Regulatory Cycle**

    - **Post-LTCM (Basel II)**: Introduced internal models for market risk (VaR). Banks optimized portfolios to minimize VaR, leading to concentrated positions in instruments with low measured volatility but high tail risk (e.g., senior CDO tranches, which had low VaR but catastrophic crisis losses).

    - **Post-2008 (Basel III)**: Introduced leverage ratio, liquidity coverage ratio, and stressed VaR. Banks shifted risk to unregulated entities (shadow banking) or used instruments not well captured by stressed VaR.

    - **FRTB**: Introduced expected shortfall replacing VaR, non-modellable risk factors, and desk-level approval. Banks are now optimizing desk structures and risk factor classifications.

    **Specific Example: VaR Arbitrage via Short Volatility**

    Consider a bank that sells deep out-of-the-money put options on the S&P 500. Under a historical simulation VaR at 99% confidence:

    $$
    \text{VaR}_{0.99} = -\text{Quantile}_{0.01}(\text{P\&L distribution})
    $$

    Using 250 trading days of historical data, the 99% VaR corresponds to approximately the 2.5th worst day. If none of the last 250 days includes a market crash, the short put position shows:

    - **Daily P&L**: Small positive (premium collection) on 245+ days.
    - **VaR**: Very low, because the 2.5th worst historical loss is small.
    - **Capital requirement**: Minimal.

    However, the **actual risk** is enormous: a market crash of 10--20% would produce losses many times the reported VaR. The position is essentially selling insurance against rare events, collecting premiums that look like profits while accumulating catastrophic tail risk.

    **Quantitative Illustration**

    Suppose the bank sells 1-month 90% strike puts, collecting \$2 per contract daily in time decay. Historical simulation VaR (250-day window, no crash in window):

    $$
    \text{VaR}_{0.99}^{\text{reported}} \approx \$5 \text{ per contract}
    $$

    But the true worst-case loss (conditional on a 2008-like crash) could be:

    $$
    \text{Loss}_{\text{crisis}} \approx \$50\text{--}\$100 \text{ per contract}
    $$

    The ratio of actual tail risk to reported VaR is 10--20x, meaning the bank holds 10--20 times less capital than the actual risk warrants.

    **Mitigating Regulatory Model Risk**

    1. **Expected Shortfall (ES)** instead of VaR: ES = $\mathbb{E}[\text{Loss} \mid \text{Loss} > \text{VaR}_\alpha]$ captures the severity of tail losses, not just their frequency. This partially addresses the short-volatility arbitrage.

    2. **Stressed calibration windows**: Require models to include crisis periods in calibration data.

    3. **Non-modellable risk factors (NMRF)**: FRTB identifies risk factors with insufficient data and applies conservative capital charges.

    4. **Multiple metrics**: Use VaR, ES, stress tests, leverage ratio, and notional limits simultaneously, so that gaming one metric does not reduce overall capital.

    5. **Regulatory skepticism**: Regulators should be suspicious when reported risk decreases without corresponding reduction in position sizes or notional exposures.
