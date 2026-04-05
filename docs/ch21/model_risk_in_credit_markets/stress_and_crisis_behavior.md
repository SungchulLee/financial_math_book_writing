# Stress and Crisis Behavior


Credit models calibrated in normal markets often fail during **stress and crisis periods**. Understanding these breakdowns is central to credit model risk.

---

## Regime dependence


During crises:
- default intensities jump,
- correlations spike,
- liquidity evaporates.

Static models cannot capture these regime shifts.

---

## Model breakdown mechanisms


Common failure modes include:
- extrapolation beyond calibration data,
- frozen liquidity invalidating market prices,
- violated independence assumptions.

Models appear stable until stress occurs.

---

## Stress testing


Robust credit risk management relies on:
- scenario analysis,
- extreme but plausible stresses,
- reverse stress testing.

Stress tests complement, not replace, models.

---

## Lessons from crises


Historical crises show:
- tail risk dominates averages,
- diversification benefits vanish,
- conservative assumptions outperform complex models.

---

## Key takeaways


- Crisis behavior differs qualitatively from normal markets.
- Stress testing is indispensable.
- Model humility is essential in credit markets.

---

## Further reading


- BIS, stress testing frameworks.
- Cont, model uncertainty and crises.

---

## Exercises

**Exercise 1.** A credit model is calibrated to CDS spreads during a period when the average BBB spread is 120 bp. During a crisis, spreads widen to 500 bp. Explain why simply re-calibrating the model to crisis spreads may not be sufficient. What structural features of the model (e.g., constant correlation, fixed recovery) might break down?

??? success "Solution to Exercise 1"

    **Why re-calibration to crisis spreads may be insufficient:**

    Simply updating CDS spreads from 120 bp to 500 bp within the existing model framework addresses only the *marginal* default probabilities (higher spreads imply higher individual default rates). However, a crisis changes the *entire structure* of credit risk, not just its level. Several structural features of the model may break down:

    **1. Constant correlation assumption:**

    Most credit portfolio models (Gaussian copula, factor models) use a fixed correlation parameter calibrated during normal periods. During crises, correlations increase dramatically — often from 15--20% to 50--70%. Re-calibrating individual spreads while holding correlation constant understates portfolio tail risk because it misses the increased clustering of defaults. The model predicts losses as if defaults are as dispersed as in normal times, just more frequent, when in reality defaults become highly concentrated.

    **2. Fixed recovery rate assumption:**

    Models typically assume a constant recovery rate (e.g., $R = 40\%$ for senior unsecured). During crises, recovery rates decline significantly — in 2008, average recovery rates for defaulted bonds fell to 20--25%. Lower recovery means higher loss-given-default, amplifying losses beyond what the re-calibrated default probabilities alone would suggest.

    **3. Independence between recovery and default rates:**

    In practice, recovery rates are negatively correlated with default rates (more defaults occur precisely when the economy is weak and distressed asset values are depressed). The standard model's independence assumption misses this "double hit" effect.

    **4. Liquidity breakdown:**

    Crisis spreads of 500 bp may reflect both genuine credit deterioration and illiquidity premia. The model cannot distinguish between the two. If the model interprets the entire spread as credit risk, it may overstate default probabilities while still missing the liquidity risk component (inability to trade, margin calls, forced selling).

    **5. Contagion and feedback effects:**

    Static models assume that each firm's default probability is exogenous. During crises, defaults are endogenous: one firm's default can trigger others through counterparty exposure, funding withdrawal, or confidence effects. Re-calibrating to current spreads captures the *current* state but not the *dynamic* — the possibility that conditions will deteriorate further through feedback loops.

    **6. Non-stationarity of factor loadings:**

    The sensitivity of individual firms to the common factor may change during stress. Firms that were previously idiosyncratic may become highly systematic when, for example, all depend on the same stressed funding market. The factor model structure itself may be misspecified during crises.

---

**Exercise 2.** Describe three specific mechanisms through which credit models fail during stress periods. For each mechanism, provide a concrete example from the 2008 financial crisis or the 2020 COVID-19 market disruption.

??? success "Solution to Exercise 2"

    **Three mechanisms of credit model failure during stress:**

    **Mechanism 1: Correlation regime shift**

    *Description*: Models calibrated to normal-period correlations dramatically underestimate the probability of joint defaults during stress. Correlations are not constant parameters but regime-dependent quantities that spike during crises.

    *2008 example*: The Gaussian copula model for CDO pricing used base correlations calibrated during 2004--2006, a period of historically low default correlations (10--20%). When the housing crisis hit, actual default correlations surged to 50--80% as the common factor (housing market collapse) affected virtually all mortgage borrowers simultaneously. Senior CDO tranches that models rated as AAA experienced defaults because the model never considered correlations at crisis levels.

    *2020 example*: During the initial COVID-19 market shock in March 2020, investment-grade and high-yield credit spreads widened simultaneously across all sectors — even sectors not directly affected by lockdowns (like technology). The pandemic acted as a universal systematic shock, creating near-perfect correlation in credit spread movements that exceeded any historical calibration period.

    **Mechanism 2: Liquidity evaporation invalidating market prices**

    *Description*: Credit models rely on market prices (CDS spreads, bond prices) for calibration. When liquidity disappears, quoted prices no longer reflect fundamental credit risk — they reflect the absence of buyers and forced selling. Models calibrated to these distorted prices produce unreliable outputs.

    *2008 example*: The CDO market became completely illiquid in 2007--2008. There were no buyers for structured credit products at any price. "Mark-to-market" valuations were essentially model marks (Level 3 under FAS 157), but the models themselves required market prices for calibration — a circularity that produced meaningless valuations. The ABX index (a synthetic index of subprime mortgage bonds) traded at prices implying 100% cumulative default rates for some vintages, which was clearly impossible but reflected pure illiquidity rather than fundamental value.

    *2020 example*: In March 2020, even the US Treasury market — the world's most liquid — experienced severe dislocations. Corporate bond markets froze, and ETF prices diverged from NAVs by 5--8%. Credit models that depended on orderly market prices for calibration produced unreliable results until the Federal Reserve's intervention restored liquidity.

    **Mechanism 3: Violated independence assumptions (contagion)**

    *Description*: Standard intensity models assume that each firm's default intensity is driven by exogenous factors. They do not capture feedback effects where one default triggers others through counterparty chains, funding withdrawal, or confidence loss. During crises, these contagion effects dominate.

    *2008 example*: The collapse of Lehman Brothers on September 15, 2008 triggered a chain reaction: the Reserve Primary Fund "broke the buck" due to Lehman exposure, causing a run on money market funds. This froze the commercial paper market, cutting off short-term funding for non-financial corporations. The resulting credit crunch pushed firms that were previously healthy toward distress. No standard credit model captured this cascade — each firm's default was treated independently, but in reality defaults were causally linked through the financial network.

    *2020 example*: In the initial COVID-19 shock, companies that drew down revolving credit lines (to hoard cash) strained bank balance sheets, which reduced banks' willingness to lend to other firms, which increased those firms' credit risk. This feedback loop between corporate credit stress and bank lending capacity was not captured by models that treated corporate and financial credit risk independently.

---

**Exercise 3.** A risk manager conducts a stress test by shifting all default intensities up by a factor of 3 while keeping correlations constant. Explain why this "parallel shift" stress test may underestimate portfolio credit losses. What additional stressed parameters should be considered?

??? success "Solution to Exercise 3"

    **Why a parallel shift in default intensities is insufficient:**

    The stress test shifts all default intensities by a factor of 3 (e.g., from $\lambda_i$ to $3\lambda_i$), which increases individual default probabilities. For a 5-year horizon with initial $\lambda = 1\%$ per annum:

    - Base case: $P(\text{default}) = 1 - e^{-0.01 \times 5} \approx 4.88\%$
    - Stressed: $P(\text{default}) = 1 - e^{-0.03 \times 5} \approx 13.93\%$

    While this captures higher individual default rates, it may **significantly underestimate portfolio losses** for several reasons:

    **1. Correlation is not stressed:**

    Keeping correlations constant while raising intensities treats the crisis as "more defaults but same dispersion." In reality, crises feature *correlated* increases in default rates — the defaults cluster together rather than being spread evenly across the portfolio. A stressed intensity with constant correlation produces a portfolio loss distribution with a higher mean but similar shape, while the true crisis distribution has a dramatically fatter tail.

    *Example*: Under the base case with $\rho = 15\%$, the 99.9th percentile of portfolio losses might be 8%. Under stressed intensities but same $\rho$, it might rise to 18%. But with stressed intensities *and* stressed correlation ($\rho = 50\%$), it could reach 35% — nearly double the constant-correlation stressed estimate.

    **2. Recovery rates should be stressed:**

    Crisis periods feature lower recovery rates because:

    - Distressed assets flood the market simultaneously, depressing prices.
    - Bankruptcy courts and restructuring processes are overwhelmed.
    - Collateral values decline with the broader economy.

    Recovery might decline from 40% to 20%, effectively doubling the loss-given-default.

    **3. Sector concentration risk:**

    A parallel shift assumes all sectors are equally stressed. In reality, crises often hit specific sectors disproportionately (housing in 2008, energy in 2015, hospitality in 2020). Sector-specific stress tests with concentrated intensity increases would reveal concentration risk that a uniform shift masks.

    **Additional parameters that should be stressed:**

    | Parameter | Base | Suggested Stress |
    |---|---|---|
    | Default intensity | $\lambda$ | $3\lambda$ to $5\lambda$ |
    | Pairwise correlation | $\rho$ | $2\rho$ to $3\rho$ (capped at reasonable level) |
    | Recovery rate | 40% | 15--25% |
    | Sector concentration | Uniform | Sector-specific shocks |
    | Liquidity | Normal | Bid-ask widening, margin calls |
    | Contagion | None | Default of largest exposure triggers secondary defaults |

    A comprehensive stress test should simultaneously stress multiple parameters, as the interaction effects (high default rates *plus* high correlation *plus* low recovery) are much worse than the sum of individual stresses.

---

**Exercise 4.** Define reverse stress testing. For a portfolio of 50 investment-grade corporate bonds, describe how you would implement a reverse stress test to find the minimum set of conditions (e.g., default rate, correlation, recovery) that would cause a 10% portfolio loss.

??? success "Solution to Exercise 4"

    **Definition of reverse stress testing:**

    Reverse stress testing starts from a specified adverse outcome and works backward to identify the scenarios that would cause it. Unlike conventional stress testing (which starts from a scenario and computes losses), reverse stress testing answers: "What would have to go wrong for us to lose X?"

    Formally, given a loss threshold $L^*$, reverse stress testing seeks the set of risk factor realizations $\boldsymbol{\theta}^* = (\lambda^*, \rho^*, R^*, \ldots)$ such that:

    $$
    \text{Portfolio Loss}(\boldsymbol{\theta}^*) \ge L^*
    $$

    subject to a plausibility constraint (the scenario should be unlikely but not impossible).

    **Implementation for a portfolio of 50 investment-grade corporate bonds with target loss of 10%:**

    **Step 1: Define the loss function.**

    For a portfolio of 50 bonds with equal notional $N_i$, the portfolio loss fraction is:

    $$
    L = \frac{1}{50}\sum_{i=1}^{50}(1 - R_i)\,\mathbf{1}_{\{\tau_i \le T\}}
    $$

    The target is $L \ge 10\%$.

    **Step 2: Identify the risk factor space.**

    The key parameters to vary are:

    - Default rate $p$ (or equivalently default intensity $\lambda$)
    - Default correlation $\rho$
    - Recovery rate $R$
    - Sector concentration (which sectors are hit)

    **Step 3: Determine minimum conditions.**

    With $R = 40\%$ (loss given default = 60%), achieving $L = 10\%$ requires:

    $$
    \frac{1}{50}\sum_{i=1}^{50} 0.60 \times \mathbf{1}_{\{\tau_i \le T\}} \ge 0.10 \implies \text{number of defaults} \ge \frac{50 \times 0.10}{0.60} \approx 8.33
    $$

    So at least 9 defaults out of 50 are needed. With $R = 20\%$, only $\lceil 50 \times 0.10 / 0.80 \rceil = 7$ defaults suffice.

    **Step 4: Find the "least unlikely" scenario.**

    Use optimization to find the parameter combination that achieves the 10% loss with the highest probability (i.e., the most plausible crisis scenario):

    $$
    \boldsymbol{\theta}^* = \arg\max_{\boldsymbol{\theta}} P(\boldsymbol{\theta}) \quad \text{subject to} \quad E[L \mid \boldsymbol{\theta}] \ge 10\%
    $$

    For example, using the Vasicek large-pool approximation, the expected loss fraction is:

    $$
    E[L] = (1-R)\,p
    $$

    and the probability that $L \ge 10\%$ depends on $\rho$. The reverse stress test finds the boundary in $(\rho, p, R)$ space.

    **Step 5: Explore specific scenarios.**

    Candidate reverse stress scenarios for a 10% portfolio loss:

    | Scenario | Default rate $p$ | Correlation $\rho$ | Recovery $R$ | Defaults needed |
    |---|---|---|---|---|
    | High default, moderate corr | 15% | 30% | 40% | $\ge 9$ |
    | Moderate default, high corr | 8% | 60% | 40% | $\ge 9$ |
    | Moderate default, low recovery | 10% | 30% | 20% | $\ge 7$ |
    | Combined stress | 12% | 50% | 25% | $\ge 7$ |

    For each scenario, compute the probability using the credit portfolio model and assess plausibility against historical experience.

    **Step 6: Report and act.**

    The output is a set of "breaking point" scenarios. For each, the risk manager should assess:

    - Is this scenario historically unprecedented, or has something similar occurred?
    - What early warning indicators would signal movement toward this scenario?
    - Are there concentrated exposures (sector, geography, counterparty) that make certain scenarios more likely?
    - What hedging or de-risking actions could be taken preemptively?

---

**Exercise 5.** During the 2008 crisis, diversification benefits "vanished" for many credit portfolios. Explain this phenomenon using the concept of correlation regime switching. If pre-crisis correlation is $\rho = 15\%$ and crisis correlation is $\rho = 50\%$, describe qualitatively how the portfolio loss distribution changes.

??? success "Solution to Exercise 5"

    **The vanishing of diversification benefits during crises:**

    Diversification works by offsetting losses on some positions with gains (or smaller losses) on others. The benefit depends on imperfect correlation: if assets move independently, losses on some are offset by stability on others. When correlation increases toward 1, all assets move together and diversification provides no protection.

    **Correlation regime switching framework:**

    Consider a credit portfolio in a two-regime model:

    - **Pre-crisis regime**: pairwise default correlation $\rho = 15\%$. Defaults are relatively independent. In a portfolio of $n$ firms with individual default probability $p$, the portfolio loss distribution is well-approximated by the mean, and extreme losses are very rare.

    - **Crisis regime**: pairwise default correlation $\rho = 50\%$. The common factor dominates. Conditional on a bad realization of the systematic factor, all firms simultaneously face elevated default risk.

    **How the portfolio loss distribution changes:**

    **1. The mean loss is unchanged** (correlation does not affect expected loss):

    $$
    E[L] = (1-R) \times p \quad \text{regardless of } \rho
    $$

    **2. The variance increases dramatically.** For a large homogeneous portfolio, the variance of the loss rate scales approximately as:

    $$
    \text{Var}(L) \propto \rho \quad \text{(for small } p \text{)}
    $$

    Moving from $\rho = 15\%$ to $\rho = 50\%$ roughly triples the variance and increases the standard deviation by a factor of about $\sqrt{50/15} \approx 1.83$.

    **3. The tail becomes much heavier.** Using the Vasicek large-pool formula, the $q$-th quantile of the portfolio loss rate is:

    $$
    L_q = (1-R)\,\Phi\!\left(\frac{\Phi^{-1}(p) + \sqrt{\rho}\,\Phi^{-1}(q)}{\sqrt{1-\rho}}\right)
    $$

    For $p = 3\%$, $R = 40\%$, and $q = 99.9\%$:

    - $\rho = 15\%$: $L_{99.9\%} = 0.6 \times \Phi\!\left(\frac{-1.881 + 0.387 \times 3.09}{0.922}\right) = 0.6 \times \Phi\!\left(\frac{-1.881 + 1.196}{0.922}\right) = 0.6 \times \Phi(-0.743) \approx 0.6 \times 0.229 = 13.7\%$

    - $\rho = 50\%$: $L_{99.9\%} = 0.6 \times \Phi\!\left(\frac{-1.881 + 0.707 \times 3.09}{0.707}\right) = 0.6 \times \Phi\!\left(\frac{-1.881 + 2.185}{0.707}\right) = 0.6 \times \Phi(0.430) \approx 0.6 \times 0.666 = 40.0\%$

    The 99.9th percentile loss nearly triples — from 13.7% to 40.0%.

    **4. Diversification benefit is reduced.** Define the diversification benefit as the ratio of portfolio standard deviation to the sum of individual standard deviations. Under independence ($\rho = 0$), this ratio scales as $1/\sqrt{n}$, approaching zero for large portfolios. Under high correlation, the ratio approaches 1 (no diversification). The shift from $\rho = 15\%$ to $\rho = 50\%$ substantially reduces the effective number of independent risk factors in the portfolio, concentrating risk in the common factor.

    **Practical implication:** Portfolios that appeared well-diversified under pre-crisis correlations ($\rho = 15\%$) suffered concentrated losses during the crisis ($\rho = 50\%$). Risk models that used pre-crisis calibration dramatically underestimated tail risk, leading to inadequate capital reserves and the failure of instruments (senior CDO tranches) that were designed to be protected by diversification.

---

**Exercise 6.** Compare the effectiveness of three stress testing approaches for credit portfolios: (a) historical simulation using past crisis data, (b) hypothetical scenario analysis, and (c) model-based stressed calibration. For each approach, discuss strengths, weaknesses, and the types of risks it can and cannot capture.

??? success "Solution to Exercise 6"

    **(a) Historical simulation using past crisis data:**

    *Method*: Apply actual risk factor changes from past crisis periods (e.g., 2008 GFC, 2011 European sovereign crisis, 2020 COVID-19) to the current portfolio. Compute portfolio losses under each historical episode.

    *Strengths*:

    - Realistic: the scenarios actually happened, so they capture genuine cross-asset dependencies and nonlinear effects.
    - No model required for scenario generation — the data speaks for itself.
    - Captures complex interactions (correlation spikes, liquidity effects, contagion) that models may miss.
    - Easy to communicate: "What would happen if 2008 repeated?"

    *Weaknesses*:

    - **Backward-looking**: can only test against crises that have already occurred. The next crisis may look nothing like past ones (e.g., a pandemic was not in most historical databases before 2020).
    - **Portfolio mismatch**: the current portfolio may contain instruments or exposures that did not exist during past crises, making direct application difficult.
    - **Limited sample**: there are very few genuine crisis episodes in the historical record, providing poor statistical coverage of tail events.
    - **Survivorship bias**: historical data only includes firms that existed during past crises, missing risks from new types of entities.

    *Risks captured*: Market risk, credit spread risk, correlation regime shifts, liquidity risk (to the extent captured in historical prices).

    *Risks not captured*: Novel risk types, risks from new financial instruments, future structural changes in the financial system.

    **(b) Hypothetical scenario analysis:**

    *Method*: Experts construct plausible but severe scenarios (e.g., "simultaneous sovereign default in three European countries," "major cyberattack on financial infrastructure," "sudden 300bp rise in interest rates with credit spread widening"). The portfolio is repriced under each scenario.

    *Strengths*:

    - **Forward-looking**: can test against crises that have never occurred but are plausible.
    - **Flexible**: scenarios can be tailored to the specific portfolio and its known vulnerabilities.
    - **Regulatory requirement**: Basel III and other frameworks mandate hypothetical stress testing.
    - **Captures unprecedented events**: unlike historical simulation, not limited to past experience.

    *Weaknesses*:

    - **Subjective**: scenario design depends on human judgment, which may be biased or limited by imagination.
    - **Internal consistency**: ensuring that all risk factors in the scenario are mutually consistent is difficult (e.g., if GDP falls by 5%, what happens to credit spreads, interest rates, equity markets, and FX simultaneously?).
    - **Incomplete**: any finite set of scenarios cannot cover the full space of possible crises.
    - **Anchoring bias**: scenarios may be anchored to past experience, defeating the purpose of forward-looking analysis.

    *Risks captured*: Concentration risk, specific vulnerability analysis, emerging risks (climate, cyber, geopolitical).

    *Risks not captured*: Risks outside the scenario designers' imagination, second-order effects, dynamic feedback.

    **(c) Model-based stressed calibration:**

    *Method*: Re-calibrate the credit model (e.g., Gaussian copula, intensity model) to stressed parameters: higher default intensities, higher correlations, lower recovery rates. Run the model under these stressed inputs to generate a stressed loss distribution.

    *Strengths*:

    - **Systematic**: covers the entire loss distribution, not just specific scenarios.
    - **Quantitative**: produces numerical outputs (VaR, Expected Shortfall, tail probabilities) that can be compared directly to risk limits.
    - **Parametric exploration**: can sweep through parameter space (e.g., correlation from 10% to 80%) to map the sensitivity surface.
    - **Consistent with pricing framework**: uses the same model as day-to-day risk management, enabling direct comparison between base and stressed results.

    *Weaknesses*:

    - **Model-dependent**: the stressed outputs are only as reliable as the model. If the model is structurally wrong (e.g., Gaussian copula with zero tail dependence), stressed calibration merely pushes a flawed model to extremes.
    - **Parameter uncertainty**: choosing "stressed" parameters is itself subjective. How much should correlation be stressed? What is a "plausible" stressed recovery rate?
    - **Misses structural breaks**: the model may not capture regime changes, contagion, or liquidity effects that dominate during actual crises.
    - **False precision**: produces precise numerical outputs that may convey unwarranted confidence in the stressed estimates.

    *Risks captured*: Systematic parameter sensitivity, tail behavior within the model's framework, correlation risk.

    *Risks not captured*: Model misspecification risk, liquidity risk, contagion effects, operational disruptions.

    **Overall assessment:** No single approach is sufficient. Best practice combines all three: historical simulation provides calibration anchors, hypothetical scenarios address forward-looking risks, and model-based stressed calibration provides systematic quantitative analysis. The results should be triangulated — if all three approaches indicate a vulnerability, it is highly credible; if they disagree, the discrepancy itself is informative about model uncertainty.
