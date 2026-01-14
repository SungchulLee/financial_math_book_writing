# Model Risk and Parameter Risk


**Model risk and parameter risk** represent the uncertainty in derivatives valuation arising from incorrect model selection (model risk) and imprecise estimation of model inputs like volatility, correlation, and interest rates (parameter risk), where small errors in assumptions can compound into massive pricing errors and hedge failures, particularly for path-dependent exotics where model choice fundamentally affects valuation and Greeks, requiring rigorous model validation, parameter sensitivity analysis, and prudent reserves against model uncertainty.

---

## The Core Insight


**The fundamental idea:**

- All models are wrong, some are useful (George Box)
- No perfect model exists for derivatives pricing
- Every model makes simplifying assumptions
- Parameters (vol, corr, rates) are estimates, not truth
- Small parameter errors → Large valuation errors
- Model risk amplifies in complex derivatives
- Need to quantify and reserve against uncertainty

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/model_parameter_risk_taxonomy.png?raw=true" alt="model_parameter_risk_taxonomy" width="700">
</p>
**Figure 1:** Taxonomy of model and parameter risk showing how model selection errors (wrong dynamics, missing factors) and parameter estimation errors (volatility, correlation, rates) propagate through pricing and hedging, with compounding effects that can turn small input errors into catastrophic valuation mistakes.

**You're essentially asking: "How wrong can we be, and what does it cost us?"**

---

## What Is Model Risk?


### 1. Definition


**Model risk:**

The risk that a financial model produces incorrect valuations, hedge ratios, or risk measures due to:
1. Wrong model specification (dynamics)
2. Missing risk factors
3. Incorrect distributional assumptions
4. Numerical approximation errors

**Formal:**

$$
\text{Model Risk} = V_{\text{true}} - V_{\text{model}}
$$

Where $V_{\text{true}}$ is unknowable (true value), $V_{\text{model}}$ is what we compute

**Example:**

Barrier option valued using Black-Scholes vs. jump-diffusion model

**BS value:** $5.00
**Jump-diffusion value:** $6.20
**Model risk: At least $1.20** (could be more if both wrong)

### 2. Sources of Model Risk


**Dynamics specification:**

**Geometric Brownian Motion (GBM):**
$$
dS_t = \mu S_t dt + \sigma S_t dW_t
$$

**Assumptions:**
- Constant volatility (false)
- Continuous paths (false—jumps exist)
- Lognormal distribution (false—fat tails)
- No correlation breaks (false—regime changes)

**Local volatility:**
$$
dS_t = \mu S_t dt + \sigma(S_t, t) S_t dW_t
$$

**Better:** Allows vol to depend on spot and time

**Still wrong:** No jumps, no stochastic vol

**Stochastic volatility (Heston):**
$$
\begin{align*}
dS_t &= \mu S_t dt + \sqrt{V_t} S_t dW_t^S \\
dV_t &= \kappa(\theta - V_t)dt + \sigma_v \sqrt{V_t} dW_t^V
\end{align*}
$$

**Better:** Vol is random, mean-reverting

**Still wrong:** No jumps in spot or vol

**Each model:** Different prices, different hedges

### 3. Missing Factors


**Example: Interest rate risk**

**Standard:** Use constant risk-free rate $r$

**Reality:** Rates are stochastic
- Short rate: $dr_t = \kappa(\theta - r_t)dt + \sigma_r dW_t^r$
- Yield curve: Multiple factors
- Credit spread: Time-varying

**Impact:**

Long-dated options:
- 10-year option on stock
- Rate changes affect discount factor significantly
- Ignoring rate risk: 5-10% pricing error

**Quanto options:**

Need FX rate dynamics:
$$
\begin{align*}
dS_t^{\text{foreign}} &= ... \\
dX_t &= r_{\text{dom}} - r_{\text{for}} + \sigma_X dW_t^X
\end{align*}
$$

**Missing FX dynamics:** Massive mispricing

### 4. Distributional Assumptions


**Normal vs. reality:**

**Model assumes:** Returns ~ $N(\mu, \sigma^2)$

**Reality:** 
- Fat tails (kurtosis > 3)
- Negative skewness (left tail fatter)
- Extreme events more common than normal predicts

**Example:**

**Normal distribution:** P(3σ event) = 0.27%
**Reality (S&P 500):** P(3σ event) ≈ 2% (7× more common!)

**Impact on tail options:**

OTM put (3σ):
- Normal model: Price = $0.50
- Reality: Price = $2.00
- **Model error: 75% undervaluation**

### 5. Calibration Risk


**Fitting model to market:**

**Process:**
1. Choose model (e.g., Heston)
2. Observe market prices (vanilla options)
3. Fit parameters to minimize error
4. Use fitted model for exotics

**Problem:** Many parameter sets fit equally well

**Example—Heston parameters:**

**Set A:** $\kappa = 2, \theta = 0.04, \sigma_v = 0.3, \rho = -0.7$
**Set B:** $\kappa = 3, \theta = 0.05, \sigma_v = 0.4, \rho = -0.5$

Both fit vanilla options within 1% (good calibration)

**But for exotic:**
- Set A: Value = $10.50
- Set B: Value = $12.80
- **Difference: 22%**

**Calibration doesn't eliminate model risk**

### 6. Numerical Approximations


**Monte Carlo error:**

$$
\text{Standard Error} = \frac{\sigma_{\text{payoff}}}{\sqrt{N}}
$$

**Example:**

Exotic option, $N = 10,000$ paths

**True value:** $10.00 (unknown)
**Estimated value:** $9.87
**Standard error:** $0.15
**95% CI:** $[9.57, 10.17]$

**Could be 2% off just from simulation noise**

**Finite difference discretization:**

Time steps: $\Delta t$, space steps: $\Delta S$

**Error:** $O(\Delta t) + O(\Delta S^2)$

**Convergence:** Slow for multi-dimensional PDEs

### 7. Model Validation


**Required checks:**

1. **Implementation testing:**
   - Code review
   - Unit tests
   - Benchmark against known solutions

2. **Parameter stability:**
   - Small changes in inputs → Small changes in outputs?
   - Or explosive sensitivity?

3. **Out-of-sample testing:**
   - Does model predict held-out data?
   - Or only fits training set?

4. **Hedge performance:**
   - Do delta hedges work?
   - Check realized P&L vs. expected

5. **Stress testing:**
   - Extreme scenarios
   - Model breaks down where?

---

## What Is Parameter Risk?


### 1. Definition


**Parameter risk:**

The risk that estimated parameters differ from true parameters, causing valuation errors even with correct model.

**Formal:**

$$
\text{Parameter Risk} = V(\hat{\theta}) - V(\theta^*)
$$

Where:
- $\hat{\theta}$ = Estimated parameters
- $\theta^*$ = True parameters (unknown)

**Key parameters:**

- Volatility: $\sigma$
- Correlation: $\rho$
- Interest rates: $r$
- Dividend yield: $q$
- Jump intensity: $\lambda$
- Mean reversion speed: $\kappa$

### 2. Volatility Risk


**Estimation error:**

**Historical vol:**
$$
\hat{\sigma} = \sqrt{\frac{252}{N-1} \sum_{i=1}^{N} (r_i - \bar{r})^2}
$$

**Problem:** Depends on sample period, frequency

**Example:**

Stock vol estimated using:
- Last 30 days: $\hat{\sigma} = 22\%$
- Last 90 days: $\hat{\sigma} = 18\%$
- Last 252 days: $\hat{\sigma} = 25\%$

**Which is "true"?** None—vol changes over time

**Impact on option:**

ATM call, 3 months:
- At 18% vol: Price = $4.20
- At 22% vol: Price = $5.10
- At 25% vol: Price = $5.70
- **Range: $1.50 (36% of mid)**

### 3. Correlation Risk


**Estimation uncertainty:**

**Sample correlation:**
$$
\hat{\rho} = \frac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{\sqrt{\sum(X_i - \bar{X})^2 \sum(Y_i - \bar{Y})^2}}
$$

**Standard error:**
$$
SE(\hat{\rho}) \approx \frac{1-\rho^2}{\sqrt{N}}
$$

**Example:**

Estimate correlation between AAPL and MSFT:
- Sample size: 252 days
- Estimated: $\hat{\rho} = 0.6$
- Standard error: $\frac{1 - 0.36}{\sqrt{252}} = 0.04$
- 95% CI: $[0.52, 0.68]$

**Impact on basket option:**

Best-of call on AAPL and MSFT:
- At $\rho = 0.52$: Value = $8.50
- At $\rho = 0.68$: Value = $7.10
- **Difference: 16.5%**

### 4. Interest Rate Risk


**Rate uncertainty:**

**Risk-free rate:** Which rate?
- Overnight: 5.30%
- 3-month: 5.35%
- 1-year: 5.10%
- 10-year: 4.50%

**Impact on long-dated options:**

10-year call:
- At $r = 4.5\%$: Price = $22.50
- At $r = 5.5\%$: Price = $20.10
- **Difference: 11%**

**Credit spread risk:**

For derivatives on credit:
- CDS spread estimate critical
- Changes daily
- Uncertainty propagates to valuation

### 5. Jump Parameters


**For jump-diffusion models:**

$$
dS_t = \mu S_t dt + \sigma S_t dW_t + S_t dJ_t
$$

Need to estimate:
- Jump intensity: $\lambda$ (frequency)
- Jump size mean: $\mu_J$
- Jump size vol: $\sigma_J$

**Problem:** Jumps are rare
- Only 5-10 jumps per year
- Insufficient data for precise estimates
- 95% CI on $\lambda$ might be $[2, 12]$ (huge range!)

**Impact:**

Barrier option near barrier:
- At $\lambda = 2$: Knockout prob = 15%
- At $\lambda = 12$: Knockout prob = 35%
- **Massive difference**

### 6. Parameter Sensitivity


**Vega risk:**

$$
\text{Vega} = \frac{\partial V}{\partial \sigma}
$$

Measures sensitivity to vol

**High vega:** Small vol error → Large value error

**Example:**

Variance swap:
- Vega = $500K per 1% vol
- Vol estimate error: ±2%
- **Value uncertainty: ±$1M**

**Correlation sensitivity:**

For multi-asset derivatives:

$$
\frac{\partial V}{\partial \rho}
$$

**Example:**

Dispersion trade:
- Sensitivity: $100K per 0.1 correlation
- Correlation estimate error: ±0.15
- **Value uncertainty: ±$150K**

### 7. Time-Varying Parameters


**Non-stationarity:**

**Problem:** Parameters change over time
- Vol clusters (high vol → high vol)
- Correlations spike in crisis
- Rates follow Fed policy

**Impact on hedging:**

Hedge using historical estimates:
- Historical $\sigma = 20\%$
- Hedge as if vol stays 20%
- Actual $\sigma = 30\%$ (regime change)
- **Hedge fails**

**Solution:** Use implied parameters (from market), update frequently

---

## Key Terminology


**Model Risk:**
- Risk from wrong model choice
- Dynamics, factors, distributions
- Cannot be eliminated
- Reserve required

**Parameter Risk:**
- Risk from estimation error
- Even correct model
- Uncertainty quantifiable
- Confidence intervals

**Calibration:**
- Fitting model to market prices
- Vanilla options as inputs
- Multiple parameter sets possible
- Not unique solution

**Model Reserve:**
- Capital set aside for model risk
- Regulatory requirement
- Typically 5-10% of position
- Higher for exotics

**Vega:**
- Sensitivity to volatility
- Key parameter risk metric
- High vega = high parameter risk
- Hedge by trading options

**Local Volatility:**
- Vol depends on (S, t)
- Calibrated to vanilla smile
- Deterministic vol
- No stochastic vol

**Stochastic Volatility:**
- Vol is random process
- Heston, SABR models
- More parameters
- Better for exotics

---

## Model Selection


### 1. Black-Scholes


**When appropriate:**

- Vanilla options, short-dated
- Liquid markets (can use implied vol)
- Not stressed conditions
- Delta hedging only

**Limitations:**

- Constant vol (false)
- No jumps
- No smile/skew
- European only (analytic)

**Typical error:** 2-5% for vanillas, 10-30% for exotics

### 2. Local Volatility


**When appropriate:**

- Exotic options with spot dependence
- Calibrated to vanilla smile
- Static hedging strategies
- Path-independent payoffs

**Advantages:**

- Matches vanilla smile exactly
- Deterministic (easier to compute)
- Better than BS for barriers

**Limitations:**

- Forward smile flat (unrealistic)
- No vol-of-vol
- Dynamic hedging poor

**Typical error:** 5-10% for barriers, 15-25% for variance-sensitive

### 3. Stochastic Volatility


**When appropriate:**

- Vol derivatives (variance swaps)
- Long-dated options
- Forward vol dependent payoffs
- Vega hedging critical

**Advantages:**

- Captures vol clustering
- Forward vol smile realistic
- Better dynamic hedges
- Vega term structure

**Limitations:**

- More parameters (calibration hard)
- Computationally expensive
- Still no jumps

**Typical error:** 3-8% for vol-dependent exotics

### 4. Jump-Diffusion


**When appropriate:**

- Crash protection (OTM puts)
- Event-driven derivatives
- Options near barriers
- Tail risk matters

**Advantages:**

- Captures rare events
- Fat tails realistic
- Better for extreme strikes

**Limitations:**

- Jump parameters hard to estimate
- Even more parameters
- Calibration unstable

**Typical error:** 2-5% for tail options, 10-20% for standard

### 5. Model Comparison


**Quantitative:**

**Root mean squared error (RMSE):**

$$
\text{RMSE} = \sqrt{\frac{1}{N}\sum_{i=1}^{N}(V_i^{\text{model}} - V_i^{\text{market}})^2}
$$

**Compare models:**
- Model A: RMSE = $0.15
- Model B: RMSE = $0.10
- **Model B better fit**

**Qualitative:**

- Which risks matter most?
- How will you hedge?
- Computational feasibility?
- Regulatory acceptance?

### 6. Model Hierarchy


**Progressive complexity:**

**Level 1:** Black-Scholes (baseline)
**Level 2:** Local vol (smile)
**Level 3:** Stochastic vol (vol-of-vol)
**Level 4:** SV + Jumps (fat tails)
**Level 5:** Multi-factor (rates, FX, credit)

**Principle:** Use simplest model that captures key risks

**Example:**

**Barrier option, 3 months:**
- Level 1 (BS): Too simple (no smile)
- Level 2 (Local vol): Adequate ✓
- Level 3+ (SV): Overkill (extra complexity, little benefit)

### 7. Model Validation Process


**Steps:**

1. **Choose model** based on risk factors
2. **Calibrate** to market data
3. **Backtest** on historical data
4. **Stress test** extreme scenarios
5. **Compare** to alternative models
6. **Monitor** ongoing performance
7. **Review** annually or after events

---

## Parameter Estimation


### 1. Historical Estimation


**Volatility:**

**Sample standard deviation:**
$$
\hat{\sigma} = \sqrt{\frac{1}{N-1}\sum_{i=1}^N (r_i - \bar{r})^2} \times \sqrt{252}
$$

**Pros:** Simple, objective
**Cons:** Backward-looking, regime-dependent

**Correlation:**

**Pearson correlation:**
$$
\hat{\rho}_{XY} = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}
$$

**Pros:** Standard, interpretable
**Cons:** Non-stationary, crisis behavior different

### 2. Implied Parameters


**Implied volatility:**

Solve for $\sigma$ in Black-Scholes:
$$
C_{\text{market}} = C_{\text{BS}}(S, K, T, r, q, \sigma)
$$

**Pros:** Forward-looking, market consensus
**Cons:** Assumes BS correct, only for vanillas

**Implied correlation:**

From index vs. component options:
$$
\rho_{\text{implied}} = \frac{\sigma_{\text{index}}^2 - \sum w_i^2 \sigma_i^2}{2 \sum_{i<j} w_i w_j \sigma_i \sigma_j}
$$

**Pros:** Market-based
**Cons:** Noisy, complex calculation

### 3. Maximum Likelihood


**For parametric models:**

Given data $D = \{S_1, ..., S_T\}$, find $\theta$ that maximizes:

$$
\mathcal{L}(\theta | D) = \prod_{t=1}^T f(S_t | S_{t-1}, \theta)
$$

Or equivalently, minimize:
$$
-\log \mathcal{L}(\theta | D) = -\sum_{t=1}^T \log f(S_t | S_{t-1}, \theta)
$$

**Pros:** Statistically optimal (asymptotically)
**Cons:** Requires distributional assumption, computationally intensive

### 4. Calibration to Market


**Match model to observed prices:**

**Objective:** Minimize error
$$
\theta^* = \arg\min_{\theta} \sum_{i=1}^N w_i (V_i^{\text{model}}(\theta) - V_i^{\text{market}})^2
$$

Where $w_i$ = weights (e.g., inverse of bid-ask spread)

**Example—Heston calibration:**

Parameters: $\kappa, \theta, \sigma_v, \rho, V_0$

**Data:** 20 vanilla options (different strikes/maturities)

**Result:** Parameter set that best fits market

**Issue:** Non-convex optimization, multiple local minima

### 5. Bayesian Estimation


**Incorporate prior beliefs:**

$$
p(\theta | D) \propto p(D | \theta) \times p(\theta)
$$

**Posterior** ∝ **Likelihood** × **Prior**

**Pros:** Incorporates uncertainty naturally
**Cons:** Requires prior specification, computationally intensive (MCMC)

**Output:** Distribution of parameters, not point estimate

**Example:**

Estimate jump intensity $\lambda$

**Prior:** $\lambda \sim \text{Gamma}(2, 0.5)$ (mean = 4 jumps/year)
**Data:** Observed 6 jumps in 2 years
**Posterior:** $\lambda \sim \text{Gamma}(8, 2.5)$ (mean = 3.2 jumps/year)

**Use posterior mean or full distribution** for valuation

### 6. Rolling Windows


**Handle time-variation:**

**Exponentially-weighted moving average (EWMA):**

$$
\sigma_t^2 = \lambda \sigma_{t-1}^2 + (1-\lambda) r_t^2
$$

Typical: $\lambda = 0.94$ (RiskMetrics)

**Pros:** Adapts to recent data
**Cons:** Ad-hoc decay rate

**Rolling window:**

Use last $N$ observations (e.g., 60 days)

**Pros:** Recent focus
**Cons:** Drops old data abruptly

### 7. Confidence Intervals


**Quantify uncertainty:**

**Bootstrap:**
1. Resample data with replacement
2. Reestimate parameter $M$ times
3. Compute percentiles

**Example:**

Volatility estimate: $\hat{\sigma} = 22\%$

**Bootstrap (1,000 iterations):**
- 2.5th percentile: 19%
- 97.5th percentile: 26%
- **95% CI: [19%, 26%]**

**Use for stress testing:** Price at boundaries

---

## Common Mistakes


### 1. Model Overconfidence


**Treating model as truth:**

- **Mistake:** "My model says it's worth exactly $10.52"
- **Why it fails:** Model is approximation, not reality
- **Fix:** Quote ranges, not points: "$10.00 - $11.00"
- **Real cost:** No reserves, blow up when model wrong

**Example:**

Exotic valued at $100K using Heston

**Overconfident:** Book at $100K, no reserve

**Reality check:**
- Local vol: $95K
- Jump-diffusion: $108K
- **Range: [$95K, $108K]**

**Should have:** Booked at midpoint ($101.5K) with $6.5K reserve

### 2. Ignoring Parameter Uncertainty


**Point estimates only:**

- **Mistake:** Use single vol estimate, ignore confidence interval
- **Why it fails:** Estimate has error, propagates to value
- **Fix:** Stress test at ±2 standard errors
- **Real cost:** Unexpected losses from parameter moves

**Example:**

Vol estimate: 22% ± 3% (95% CI: [19%, 25%])

**Mistake:** Price using 22% only
- Value: $50M

**Stress test:**
- At 19%: Value = $45M (loss $5M)
- At 25%: Value = $55M (gain $5M)

**Risk:** $5M parameter risk (10% of position!)

**Should have:** Reserved $2.5M (half of worst case)

### 3. Stale Calibration


**Infrequent recalibration:**

- **Mistake:** Calibrate model once, use for months
- **Why it fails:** Market changes, old parameters stale
- **Fix:** Recalibrate daily or weekly
- **Real cost:** Growing model error over time

**Example:**

**January:** Calibrate Heston to market
- $\kappa = 2.5$, $\theta = 0.04$, $\rho = -0.6$

**June:** Market changed (higher vol, steeper skew)
- Should be: $\kappa = 1.8$, $\theta = 0.07$, $\rho = -0.8$
- Still using January parameters

**Error:** Exotic mispriced by 12% (accumulates over 6 months)

### 4. In-Sample Overfitting


**Perfect fit to training data:**

- **Mistake:** Add parameters until model fits perfectly
- **Why it fails:** Overfit to noise, not signal
- **Fix:** Use out-of-sample validation, parsimony
- **Real cost:** Model breaks on new data

**Example:**

Fitting smile with polynomial:

**Degree 3:** RMSE = 0.5% (good)
**Degree 10:** RMSE = 0.05% (perfect fit!)

**Tomorrow:**
- Degree 3: RMSE = 0.6% (stable)
- Degree 10: RMSE = 2.5% (exploded!)

**Overfitting:** Degree 10 fit noise, not true smile

### 5. Wrong Sticky Assumption


**Mismodeling surface dynamics:**

- **Mistake:** Assume sticky strike when market is sticky delta
- **Why it fails:** Surface moves differently than assumed
- **Fix:** Empirically test which sticky rule fits
- **Real cost:** Hedge ratios wrong, P&L surprises

**Example:**

Hedge barrier option using local vol (implies sticky strike)

**Reality:** FX market is sticky delta

**Impact:**
- Spot moves 5%
- Local vol assumes surface stays fixed
- But surface actually shifted parallel
- Delta off by 15%
- **Hedge error: $500K on $10M position**

### 6. Tail Underestimation


**Using normal when fat-tailed:**

- **Mistake:** Assume normal distribution for returns
- **Why it fails:** Extreme events more common than normal predicts
- **Fix:** Use t-distribution or empirical distribution
- **Real cost:** OTM options underpriced, tail risk underestimated

**Example:**

Selling OTM puts (3σ)

**Normal assumption:**
- P(hit) = 0.13%
- Price appropriately for 0.13% probability

**Reality (empirical):**
- P(hit) = 1.5% (10× more frequent!)
- Should have charged 10× more
- **Underpriced by 90%**

### 7. Ignoring Jumps


**Continuous path assumption:**

- **Mistake:** Use GBM for stock with earnings/events
- **Why it fails:** Earnings create jumps, GBM can't capture
- **Fix:** Use jump-diffusion or trade around events
- **Real cost:** Barrier options mispriced by 20-40%

**Example:**

Barrier option expiring after earnings

**GBM model:**
- Assumes smooth path to earnings
- Knockout probability: 15%

**With jumps:**
- Earnings can gap through barrier
- Knockout probability: 35%
- **Model error: 2.3× underestimate**

---

## Best vs. Worst Case


### 1. Best Case: Success


**Rigorous model validation:**

**Setup:**
- Derivatives desk at major bank
- Sophisticated model risk framework
- Multiple models for cross-validation

**Process:**

**1. Model selection:**
- Primary: Heston SV for standard exotics
- Secondary: Local vol for cross-check
- Tertiary: Jump-diffusion for tail risk

**2. Daily calibration:**
- Fit all three models to vanilla market
- Monitor parameter stability
- Flag if parameters jump >20%

**3. Pricing with ranges:**

Exotic option request from client

**Heston price:** $10.5M
**Local vol price:** $9.8M
**Jump-diffusion price:** $11.2M

**Quote to client:** $10.5M (mid) ± $700K (reserve)

**Rationale:** Half-width of range = model uncertainty

**4. Parameter stress testing:**

Stressed volatility ±10%:
- At -10%: Value = $9.2M
- At +10%: Value = $11.9M

**Reserve:** Additional $350K for parameter risk

**Total reserve:** $1.05M (10% of position)

**5. Ongoing monitoring:**

**Monthly:**
- Revalue using updated parameters
- Check P&L attribution (expected vs. actual)
- Flag if unexplained P&L > $100K

**Quarterly:**
- Full model review
- Backtest hedge performance
- Update reserves if needed

**Result (2015-2020):**
- Sold $5B notional in exotics
- Model reserves: $500M (10%)
- Actual model losses: $200M (4%)
- **Reserves adequate**, desk profitable

**Success factors:**
1. Multiple models (not single point of failure)
2. Prudent reserves (10% for exotics)
3. Daily calibration (fresh parameters)
4. Rigorous monitoring (catch problems early)

### 2. Worst Case: Disaster


**Model risk blow-up:**

**Setup:**
- Hedge fund trading volatility arbitrage
- "Sophisticated" proprietary model
- Overconfidence in model accuracy

**Model:**
- Custom GARCH-based pricing
- Calibrated once (at launch)
- Never validated externally
- No reserves

**Strategy:**
- Sell variance swaps
- Hedge using model Greeks
- Collect theta, bet on vol mean reversion

**Year 1 (2018):**
- Low vol regime
- Model working well
- Profits: +$50M on $200M capital
- **25% return**

**Early 2019: Model drift**

**Problem:** Market regime changed
- Vol structure shifted
- Model parameters stale (not recalibrated!)
- Greeks increasingly wrong

**Hedges degrading:**
- Delta hedges: -5% error (tolerable)
- Vega hedges: -15% error (worrying)
- Volga hedges: -30% error (dangerous)

**Management:** Ignored warnings
- "Model has worked for 2 years"
- "Temporary regime, will revert"
- **No action taken**

**August 2019: Volatility spike**

**VIX:** 12 → 25 (doubled)

**Model prediction:** Positions gain $20M (short vol profitable in spike? No!)

**Reality:**

**Position 1:** Short variance swaps
- Model value: -$30M (mark-to-market)
- Actual value: -$75M (model underestimated)
- **Model error: -$45M**

**Position 2:** Dynamic hedges
- Model said: Hedge worked, offset -$30M
- Reality: Hedge only offset -$10M (wrong Greeks)
- **Hedge failure: -$20M**

**Total loss:** -$75M + (-$20M hedge failure) = -$95M

**Fund capital:** $200M → $105M (down 47.5%)

**Aftermath:**

**Investor panic:**
- Redemption requests: 60% of AUM
- Forced to liquidate positions at worst prices
- Additional losses: -$15M

**Final:**
- Fund down 55%
- Shut down 6 months later
- Founder reputation destroyed

**Root cause:**
1. Single model (no cross-validation)
2. Stale calibration (regime change missed)
3. No reserves (arrogance)
4. Ignored warnings (confirmation bias)
5. Excessive leverage (amplified error)

---

## Risk Management Rules


### 1. Model Reserves


**Reserve against model uncertainty:**

$$
\text{Reserve} = \alpha \times \max_{i}|V_i - V_{\text{primary}}|
$$

Where:
- $V_i$ = Value from model $i$
- $V_{\text{primary}}$ = Primary model value
- $\alpha = 0.5$ (haircut factor)

**Example:**

- Primary (Heston): $10.5M
- Local vol: $9.8M
- Jump-diff: $11.2M
- Max difference: $1.4M

**Reserve:** $0.5 \times \$1.4M = \$700K$

### 2. Parameter Stress


**Minimum stress scenarios:**

1. Vol ± 20% from current
2. Correlation ± 30% from estimate
3. Rates ± 100 bps
4. Jump intensity × 2
5. All adverse simultaneously (compound)

**Maximum loss:**

$$
\text{Stress Loss} \leq 15\% \text{ of Position Value}
$$

**If exceeded:** Reduce position or hedge more

### 3. Recalibration Frequency


**Daily:** For actively traded books
**Weekly:** For less active positions
**After events:** Always (earnings, Fed, crises)

**Trigger for immediate recalib:**
- Parameter change > 20%
- Market vol move > 5 points
- Unexplained P&L > 2% of position

### 4. Multiple Models


**Minimum 2 models:**
- Primary: For pricing and hedging
- Secondary: For validation and reserves

**Quarterly comparison:**

If models diverge > 10%:
- Investigate cause
- Increase reserves
- Consider exiting position

### 5. Model Validation


**Annual review:**

- External validator (independent)
- Backtest performance
- Hedge effectiveness
- Parameter stability
- Numerical accuracy

**Approval required:**
- Risk committee
- Model validation group
- Regulatory sign-off (if applicable)

### 6. Documentation


**Required records:**

- Model specification (equations)
- Parameter history (time series)
- Calibration results (fit quality)
- Stress test results
- Reserve calculations
- Validation reports

**Retention:** 7 years minimum

### 7. Limits by Model Confidence


**Position limits:**

- High confidence (vanilla, liquid): 100% of limit
- Medium confidence (standard exotic): 50% of limit
- Low confidence (novel exotic): 25% of limit

**Example:**

Trading limit: $100M

**Vanilla options:** Up to $100M ✓
**Barrier options:** Up to $50M
**Custom exotic:** Up to $25M

---

## Real-World Examples


### 1. LTCM (1998)


**Model risk disaster:**

**Model:** Convergence trading (spreads mean revert)

**Assumption:** Normal markets, liquidity constant

**Reality (1998):**
- Russian default
- Spreads widened (opposite of prediction)
- Liquidity dried up (couldn't exit)

**Model failures:**
- No tail risk
- No liquidity risk
- Extreme leverage (25:1)

**Result:** Lost $4.6B, bailout required

**Lesson:** Models fail in crises (when you need them most)

### 2. Greek Banks (2008-2010)


**Local vol mispricing:**

**Product:** Long-dated FX barriers (sold to corporates)

**Model:** Local volatility (standard)

**Problem:** Local vol implies sticky strike
- Works short-term
- Fails long-term (forward smile too flat)

**Crisis:** Euro crisis, huge FX moves

**Outcome:**
- Barriers knocked out more than modeled
- Greeks wrong (didn't hedge effectively)
- Losses: Billions across Greek banks

**Lesson:** Local vol inadequate for long-dated exotics

### 3. JP Morgan CIO (2012)


**Parameter estimation failure:**

**Position:** Credit derivatives (IG9 index)

**Model:** Value-at-Risk (VaR)

**Parameter:** Correlation between positions

**Mistake:** Changed correlation calculation
- Old method: Correlation = 0.7 (positions offset)
- New method: Correlation = 0.3 (positions independent)
- Made VaR look lower (false security)

**Reality:** Positions were correlated

**Loss:** $6.2B ("London Whale")

**Lesson:** Parameter estimation matters enormously

### 4. Quant Quake (August 2007)


**Model correlation:**

**Many funds:** Same models, same parameters

**Result:** Crowded trades
- All held similar positions
- All used similar risk models
- All hit same stop-losses

**August 2007:**
- Systematic unwinding
- Correlations spiked to 1
- Models assumed diversification (false!)

**Losses:** Billions across industry

**Lesson:** Model risk is correlated across users

---

## Practical Steps


### 1. Choose Models


**Based on risk factors:**

**If main risk = smile:**
- Use local vol or SV
- Not Black-Scholes

**If main risk = jumps:**
- Use jump-diffusion
- Especially near barriers

**If main risk = forward vol:**
- Use stochastic vol
- Not local vol

### 2. Calibrate Carefully


**Process:**

1. Collect market data (vanilla options)
2. Clean data (remove stale/wide quotes)
3. Choose weights (tighter spreads = higher weight)
4. Optimize parameters
5. Check fit quality (RMSE < 2%)
6. Validate stability (recalibrate tomorrow, similar parameters?)

### 3. Validate Results


**Sanity checks:**

- Is value positive? (if option-like)
- Monotonic in spot? (for calls/puts)
- Convex in vol? (for most options)
- Greeks make sense?
- Comparable to market (if liquid)

**Red flags:**
- Negative vol
- Correlation > 1
- Gamma of wrong sign
- Value jumps discontinuously with input

### 4. Compute Ranges


**Use multiple models:**

$$
[\text{Min value}, \text{Max value}]
$$

**Or confidence interval:**

If parameter $\theta \sim N(\hat{\theta}, \sigma^2_{\theta})$:

95% CI: $V(\hat{\theta} - 2\sigma_{\theta})$ to $V(\hat{\theta} + 2\sigma_{\theta})$

### 5. Set Reserves


**Conservative:**

$$
\text{Reserve} = 0.5 \times (\text{Range width})
$$

**Plus parameter stress:**

$$
+ 0.5 \times \max(\text{Stressed value} - \text{Base value})
$$

### 6. Monitor and Update


**Daily:**
- Recalibrate if market moved
- Check P&L vs. model prediction
- Update reserves if range changed

**Monthly:**
- Full model review
- Parameter time series analysis
- Stress test scenarios

**Quarterly:**
- Compare models
- External validation
- Update documentation

### 7. Governance


**Approval process:**

- New model: Risk committee + Model validation group
- Parameter changes > 20%: Risk manager approval
- Reserve releases: CFO approval

**Escalation:**

If model shows issue:
1. Notify risk manager (immediate)
2. Increase reserves (temporary)
3. Investigate cause (1 week)
4. Fix or exit position (2 weeks)

---

## Final Wisdom


> "Model risk and parameter risk are the silent killers of derivatives trading. Every blow-up traces back to one of two mistakes: believing your model is reality (model risk) or believing your parameter estimates are exact (parameter risk). The cruel irony: we need models to price exotics, but the very complexity that makes exotics interesting also makes them impossible to model perfectly. Black-Scholes was revolutionary not because it's correct—it's deeply wrong on every assumption—but because it's useful and we know exactly how it's wrong. When you add stochastic volatility, jumps, local vol, and multi-factor dynamics, you're not getting closer to truth—you're adding more parameters to fit, more ways to be wrong, and more false confidence. The best derivatives traders are philosophical skeptics: they use models but don't believe them, they estimate parameters but stress test them, they price to the cent but quote in ranges. Set reserves like a pessimist, trade like a realist, and always remember George Box: 'All models are wrong, but some are useful.' The question isn't whether your model is wrong (it is), but whether you've reserved enough for how wrong it might be. Sleep-at-night test: if your model gives $10.5M, can you afford to be wrong by $2M? If not, don't take the position."

**Key to success:**

- Use multiple models (not just one)
- Quote ranges, not points ($10M ± $1M, not $10.5M)
- Reserve 10% for exotics (not optional)
- Recalibrate daily (stale parameters kill)
- Stress test parameters ±20% (always)
- Monitor unexplained P&L (early warning system)
- Accept that perfect model impossible (philosophical humility)
- Better to be roughly right than precisely wrong (Keynes)
