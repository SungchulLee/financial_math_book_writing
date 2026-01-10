# Correlation and Factor Exposure

**Correlation and factor exposure** measure how assets move together (correlation) and their sensitivity to common underlying drivers (factors), where correlations are unstable and spike to one during crises while factor models decompose returns into systematic components like market beta, size, value, and momentum, allowing investors to understand true diversification, identify hidden concentrated risks, and construct portfolios that isolate desired exposures while hedging unwanted systematic risk.

---

## The Core Insight

**The fundamental idea:**

- Assets don't move independently
- Common factors drive correlated moves
- Correlation ≠ causation (but suggests common drivers)
- Factor exposure explains why assets correlate
- Crisis → correlations spike (diversification fails when needed)
- Understanding factors = understanding risk
- Can hedge systematic, keep idiosyncratic

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/correlation_factor_structure.png?raw=true" alt="correlation_factor_structure" width="700">
</p>
**Figure 1:** Hierarchical structure of correlations and factors showing how asset returns decompose into systematic factor exposures (market, size, value, momentum) and idiosyncratic risk, with correlations arising from shared factor loadings and crisis periods exhibiting correlation convergence to one across all asset classes.

**You're essentially asking: "Why do assets move together, and how can I measure and manage this co-movement?"**

---

## What Is Correlation?

### 1. Definition

**Statistical measure of co-movement:**

$$
\rho_{X,Y} = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y} = \frac{E[(X - \mu_X)(Y - \mu_Y)]}{\sigma_X \sigma_Y}
$$

Where:
- $\rho$ = Correlation coefficient (-1 to +1)
- $\text{Cov}(X,Y)$ = Covariance
- $\sigma_X, \sigma_Y$ = Standard deviations

**Interpretation:**

- $\rho = +1$: Perfect positive correlation (move together exactly)
- $\rho = 0$: No linear relationship (independent)
- $\rho = -1$: Perfect negative correlation (move opposite exactly)

**Example:**

S&P 500 and Nasdaq:
- Daily returns over 1 year
- S&P return: $\mu_{\text{SPX}} = 0.05\%$, $\sigma_{\text{SPX}} = 1.2\%$
- Nasdaq return: $\mu_{\text{NDX}} = 0.08\%$, $\sigma_{\text{NDX}} = 1.5\%$
- Covariance: $\text{Cov} = 0.015\%$

$$
\rho = \frac{0.015\%}{1.2\% \times 1.5\%} = \frac{0.015}{1.8} = 0.83
$$

**Strong positive correlation** (83%)

### 2. Sample vs. True Correlation

**Estimation uncertainty:**

**Sample correlation (what we compute):**

$$
\hat{\rho} = \frac{\sum_{i=1}^n (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^n (x_i - \bar{x})^2 \sum_{i=1}^n (y_i - \bar{y})^2}}
$$

**Standard error:**

$$
SE(\hat{\rho}) \approx \frac{1 - \rho^2}{\sqrt{n}}
$$

**Example:**

Estimate $\rho = 0.6$ using 100 observations

$$
SE = \frac{1 - 0.36}{\sqrt{100}} = \frac{0.64}{10} = 0.064
$$

**95% confidence interval:** $[0.47, 0.73]$

**Wide range!** Correlation estimates are noisy

### 3. Time-Varying Correlation

**Correlations are not constant:**

**Periods of stability:** $\rho \approx 0.5$ (normal times)
**Periods of crisis:** $\rho \to 1$ (everything falls together)

**Example—2008 financial crisis:**

**Pre-crisis (2007):**
- US stocks vs. EM stocks: $\rho = 0.55$
- US stocks vs. Commodities: $\rho = 0.35$
- US stocks vs. US bonds: $\rho = -0.20$

**Crisis (Q4 2008):**
- US stocks vs. EM stocks: $\rho = 0.95$ (spiked!)
- US stocks vs. Commodities: $\rho = 0.80$ (spiked!)
- US stocks vs. US bonds: $\rho = -0.40$ (strengthened flight to quality)

**Implication:** Diversification fails in crisis when you need it most

### 4. Conditional Correlation

**Correlation depends on regime:**

**Conditional on market state:**

$$
\rho | (\text{Market Down > 2\%}) \neq \rho | (\text{Market Up > 2\%})
$$

**Example:**

Tech stocks (AAPL, MSFT, GOOGL):

**Normal days:** $\rho \approx 0.6$
**Market up >2%:** $\rho \approx 0.5$ (dispersion increases)
**Market down >2%:** $\rho \approx 0.9$ (all fall together)

**Asymmetry:** Downside correlation >> Upside correlation

### 5. Copulas

**Beyond linear correlation:**

**Correlation measures only linear dependence**
**Copulas capture full dependence structure**

**Gaussian copula:**
- Assumes joint normal distribution
- Specified by correlation matrix
- Tail dependence symmetric

**t-copula:**
- Fatter tails than Gaussian
- Tail dependence asymmetric
- Better for financial assets

**Example:**

Two assets with returns:
- Marginals: Both Student-t (fat tails)
- Copula: t-copula with $\rho = 0.6$, $\nu = 5$ df

**Tail dependence:** P(both crash together) >> Gaussian copula predicts

**Crisis:** t-copula captures "crash together" better than Gaussian

### 6. Realized Correlation

**From high-frequency data:**

$$
\rho_{\text{realized}} = \frac{\sum_{i=1}^{n} r_{1,i} r_{2,i}}{\sqrt{\sum_{i=1}^{n} r_{1,i}^2 \sum_{i=1}^{n} r_{2,i}^2}}
$$

Using intraday returns (e.g., 5-minute bars)

**Advantage:** More precise estimate (more data points)
**Disadvantage:** Microstructure noise

**Example:**

Daily estimate (1 day): $\hat{\rho} = 0.65$ with SE = 0.10
Realized (288 5-min bars): $\hat{\rho} = 0.68$ with SE = 0.04

**3× reduction in standard error**

### 7. Correlation Matrices

**For $n$ assets, need $n(n-1)/2$ correlations**

**Example—10 assets:**

$$
\text{Correlations needed} = \frac{10 \times 9}{2} = 45
$$

**Correlation matrix $\mathbf{R}$:**

$$
\mathbf{R} = \begin{bmatrix}
1 & \rho_{12} & \rho_{13} & \cdots \\
\rho_{21} & 1 & \rho_{23} & \cdots \\
\vdots & \vdots & \ddots & \vdots \\
\end{bmatrix}
$$

**Properties:**
- Symmetric: $\rho_{ij} = \rho_{ji}$
- Diagonal = 1 (asset perfectly correlated with itself)
- Positive semi-definite (eigenvalues ≥ 0)

**Challenge:** Need to estimate 45 parameters from limited data
**Solution:** Factor models (reduce dimensionality)

---

## Key Terminology

**Correlation:**
- Linear co-movement measure
- Ranges from -1 to +1
- Time-varying, regime-dependent
- Estimation error significant

**Factor:**
- Systematic source of return
- Common driver across assets
- Examples: Market, size, value
- Cannot be diversified away

**Factor Loading (Beta):**
- Sensitivity to factor
- $\beta_i = \frac{\text{Cov}(R_i, F)}{\text{Var}(F)}$
- Measures exposure magnitude
- Can be hedged with derivatives

**Idiosyncratic Risk:**
- Asset-specific component
- Uncorrelated across assets
- Can be diversified
- Also called "alpha" source

**Systematic Risk:**
- Factor-driven component
- Correlated across assets
- Cannot be diversified
- Priced in equilibrium

**Factor Model:**
- Decomposes returns into factors
- Linear combination of exposures
- Examples: CAPM, Fama-French
- Used for attribution and hedging

**Covariance Matrix:**
- All pairwise covariances
- $n \times n$ matrix for $n$ assets
- Contains correlations and volatilities
- Essential for portfolio optimization

---

## Factor Models

### 1. Single-Factor CAPM

**Market model:**

$$
R_i = \alpha_i + \beta_i R_M + \epsilon_i
$$

Where:
- $R_i$ = Asset return
- $R_M$ = Market return
- $\beta_i$ = Market beta (factor loading)
- $\alpha_i$ = Intercept (Jensen's alpha)
- $\epsilon_i$ = Idiosyncratic error

**Beta estimation:**

$$
\beta_i = \frac{\text{Cov}(R_i, R_M)}{\text{Var}(R_M)}
$$

**Example:**

Stock returns: $R_i$
Market returns (S&P 500): $R_M$

**Regression:**
- Slope: $\beta = 1.2$ (stock moves 1.2× market)
- Intercept: $\alpha = 0.5\%$ (outperformance)
- R²: 0.65 (65% explained by market)

**Interpretation:**
- Market rises 10% → Stock expected to rise 12% (1.2 × 10%)
- Systematic component: 65%
- Idiosyncratic component: 35%

### 2. Fama-French Three-Factor

**Extended model:**

$$
R_i = \alpha_i + \beta_{i,M} R_M + \beta_{i,\text{SMB}} \text{SMB} + \beta_{i,\text{HML}} \text{HML} + \epsilon_i
$$

**Factors:**
- **Market (M):** Excess return of market over risk-free
- **SMB (Size):** Small minus Big (small-cap - large-cap)
- **HML (Value):** High minus Low (value - growth)

**Example:**

Value stock regression:
- $\beta_M = 0.9$ (slightly defensive)
- $\beta_{\text{SMB}} = 0.3$ (small-cap tilt)
- $\beta_{\text{HML}} = 0.8$ (strong value exposure)
- R²: 0.78 (78% explained)

**Interpretation:**
- When value stocks outperform by 10%, this stock gains 8% (0.8 × 10%)
- Three factors explain 78% vs. 65% for market alone
- Remaining 22% is idiosyncratic

### 3. Carhart Four-Factor

**Add momentum:**

$$
R_i = \alpha + \beta_M R_M + \beta_{\text{SMB}} \text{SMB} + \beta_{\text{HML}} \text{HML} + \beta_{\text{MOM}} \text{MOM} + \epsilon
$$

**Fourth factor:**
- **MOM (Momentum):** Winners minus Losers (past 12-month return)

**Example:**

Momentum stock:
- $\beta_M = 1.1$ (aggressive)
- $\beta_{\text{SMB}} = 0.0$ (neutral size)
- $\beta_{\text{HML}} = -0.3$ (growth tilt)
- $\beta_{\text{MOM}} = 0.9$ (strong momentum)
- R²: 0.82

**Interpretation:** This is a growth momentum stock

### 4. Fama-French Five-Factor

**Add profitability and investment:**

$$
R_i = \alpha + \beta_M R_M + \beta_{\text{SMB}} \text{SMB} + \beta_{\text{HML}} \text{HML} + \beta_{\text{RMW}} \text{RMW} + \beta_{\text{CMA}} \text{CMA} + \epsilon
$$

**Additional factors:**
- **RMW:** Robust minus Weak (profitability)
- **CMA:** Conservative minus Aggressive (investment)

**Modern best practice:** Explains ~85% of stock return variation

### 5. Macro Factors

**Economy-wide drivers:**

**Factors:**
- GDP growth
- Inflation (CPI, PPI)
- Interest rate changes (Fed policy)
- Credit spreads (TED spread, high-yield)
- Oil price changes
- USD strength

**Example—Fixed income:**

$$
R_{\text{bond}} = \alpha + \beta_1 \Delta r + \beta_2 \Delta \text{spread} + \beta_3 \Delta \text{inflation} + \epsilon
$$

**Corporate bond:**
- $\beta_{\Delta r} = -7$ (duration effect)
- $\beta_{\Delta \text{spread}} = -4$ (credit spread sensitivity)
- $\beta_{\Delta \text{inflation}} = -2$ (real rate effect)

**Interpretation:** 10 bps rate rise → -70 bps bond return

### 6. Statistical Factors (PCA)

**Principal Component Analysis:**

**No economic interpretation, purely statistical**

**Process:**
1. Compute covariance matrix of returns
2. Find eigenvectors (principal components)
3. Project returns onto components

**Example—10 stocks:**

- PC1: Explains 60% of variance (market factor)
- PC2: Explains 15% (sector factor)
- PC3: Explains 8% (style factor)
- PC4-10: Explain 17% (idiosyncratic)

**Advantage:** Orthogonal factors (no multicollinearity)
**Disadvantage:** Hard to interpret economically

### 7. Custom Factor Models

**Industry-specific:**

**Energy stocks:**

$$
R_{\text{energy}} = \alpha + \beta_M R_M + \beta_{\text{oil}} \Delta \text{Oil} + \beta_{\text{natural gas}} \Delta \text{NG} + \epsilon
$$

**Tech stocks:**

$$
R_{\text{tech}} = \alpha + \beta_M R_M + \beta_{\text{NASDAQ}} R_{\text{NASDAQ}} + \beta_{\text{chip}} R_{\text{SOX}} + \epsilon
$$

**Banks:**

$$
R_{\text{bank}} = \alpha + \beta_M R_M + \beta_{\text{rates}} \Delta \text{10Y} + \beta_{\text{curve}} \Delta \text{(10Y-2Y)} + \epsilon
$$

---

## Decomposing Portfolio Risk

### 1. Total Risk Decomposition

**Variance formula:**

$$
\text{Var}(R_p) = \sum_{i=1}^{n} w_i^2 \sigma_i^2 + \sum_{i=1}^{n} \sum_{j \neq i} w_i w_j \rho_{ij} \sigma_i \sigma_j
$$

**Two components:**
- First term: Idiosyncratic risk (individual variances)
- Second term: Systematic risk (correlations)

**As $n \to \infty$:** First term → 0, second term dominates

**Implication:** Cannot diversify away systematic risk

### 2. Factor Risk vs. Specific Risk

**Factor model variance:**

$$
\text{Var}(R_i) = \beta_i^2 \text{Var}(F) + \text{Var}(\epsilon_i)
$$

**Systematic risk:** $\beta_i^2 \text{Var}(F)$ (cannot diversify)
**Idiosyncratic risk:** $\text{Var}(\epsilon_i)$ (can diversify)

**Example:**

Stock with $\beta = 1.2$, market vol = 20%, idiosyncratic vol = 25%

**Total variance:**
$$
\sigma^2 = (1.2)^2 \times (0.20)^2 + (0.25)^2 = 0.0576 + 0.0625 = 0.1201
$$

**Total vol:** $\sqrt{0.1201} = 34.7\%$

**Decomposition:**
- Systematic: $0.0576 / 0.1201 = 48\%$
- Idiosyncratic: $0.0625 / 0.1201 = 52\%$

### 3. Portfolio Factor Exposure

**Weighted average of individual betas:**

$$
\beta_p = \sum_{i=1}^{n} w_i \beta_i
$$

**Example:**

Portfolio:
- 40% Stock A ($\beta = 0.8$)
- 30% Stock B ($\beta = 1.3$)
- 30% Stock C ($\beta = 1.0$)

**Portfolio beta:**
$$
\beta_p = 0.4 \times 0.8 + 0.3 \times 1.3 + 0.3 \times 1.0 = 0.32 + 0.39 + 0.30 = 1.01
$$

**Market-neutral:** Portfolio moves ~1:1 with market

### 4. Marginal Risk Contribution

**How much does asset $i$ contribute to portfolio risk?**

$$
\text{MRC}_i = \frac{\partial \sigma_p}{\partial w_i} = \frac{\sum_{j=1}^{n} w_j \rho_{ij} \sigma_i \sigma_j}{\sigma_p}
$$

**Risk contribution:**

$$
\text{RC}_i = w_i \times \text{MRC}_i
$$

**Sum property:**

$$
\sum_{i=1}^{n} \text{RC}_i = \sigma_p
$$

**Example:**

- Portfolio vol: 15%
- Stock A weight: 30%, MRC = 18%
- Risk contribution: 30% × 18% = 5.4%

**Interpretation:** Stock A contributes 5.4% to total 15% portfolio vol

### 5. Risk Parity

**Equal risk contribution:**

**Objective:** Each asset contributes equally to portfolio risk

$$
\text{RC}_1 = \text{RC}_2 = ... = \text{RC}_n = \frac{\sigma_p}{n}
$$

**Implementation:** Inverse-volatility weighting (approximately)

$$
w_i \propto \frac{1}{\sigma_i}
$$

**Example:**

- Asset A: $\sigma = 10\%$ → Weight = 40%
- Asset B: $\sigma = 20\%$ → Weight = 20%
- Asset C: $\sigma = 40\%$ → Weight = 10%

**Result:** Each contributes ~5% to portfolio risk

### 6. Factor Risk Contribution

**Decompose by factor:**

$$
\text{Var}(R_p) = \sum_{k=1}^{K} \beta_{p,k}^2 \text{Var}(F_k) + \text{Var}(\epsilon_p)
$$

**Risk attribution:**
- Factor 1 (Market): 60%
- Factor 2 (Value): 15%
- Factor 3 (Momentum): 10%
- Idiosyncratic: 15%

**Insight:** Market risk dominates (60% of total risk)

### 7. Stress Testing

**Scenario-based factor shocks:**

**Scenario: 2008-style crisis**
- Market factor: -40%
- Value factor: -20%
- Credit spread: +500 bps

**Portfolio impact:**

$$
\Delta R_p = \beta_{M} \times (-40\%) + \beta_{\text{HML}} \times (-20\%) + \beta_{\text{credit}} \times 500\text{ bps}
$$

**If $\beta_M = 1.2$, $\beta_{\text{HML}} = 0.5$, $\beta_{\text{credit}} = -3$:**

$$
\Delta R_p = 1.2 \times (-40\%) + 0.5 \times (-20\%) + (-3) \times 5\% = -48\% - 10\% - 15\% = -73\%
$$

**Catastrophic stress loss: -73%**

---

## Common Mistakes

### 1. Assuming Stable Correlation

**Using historical average:**

- **Mistake:** Estimate $\rho = 0.5$ from 5-year history, assume constant
- **Why it fails:** Correlations spike in crisis
- **Fix:** Use time-varying models (GARCH, DCC)
- **Real cost:** Diversification fails when needed most

**Example:**

Portfolio: 50% US stocks, 50% EM stocks
- Historical $\rho = 0.55$
- Portfolio vol: 14% (based on historical)

**Crisis:** $\rho \to 0.95$
- Actual portfolio vol: 19%
- **35% more risk than expected**

### 2. Ignoring Tail Correlation

**Normal periods vs. extremes:**

- **Mistake:** Measure correlation using all data (including normal times)
- **Why it fails:** Tail correlation >> average correlation
- **Fix:** Compute correlation conditional on large moves
- **Real cost:** Underestimate crisis risk

**Example:**

- Overall $\rho = 0.6$
- Conditional $\rho | (\text{Market down >3\%}) = 0.9$

**Crisis:** Both assets fall together much more than average suggests

### 3. Collinearity in Factors

**Correlated factors:**

- **Mistake:** Include value, quality, profitability (all correlated)
- **Why it fails:** Can't separate individual contributions
- **Fix:** Use orthogonalized factors or PCA
- **Real cost:** Unstable betas, poor out-of-sample

**Example:**

**Value and quality factors:**
- Both select similar stocks (value = cheap, quality = profitable cheap)
- Correlation: 0.7
- Regression: Betas flip signs (multicollinearity)

### 4. Sample Size Issues

**Too few observations:**

- **Mistake:** Estimate 100-stock correlation matrix from 1 year data
- **Why it fails:** Need $(n(n-1)/2)$ correlations, have only 252 data points
- **Fix:** Use factor models (reduce dimensionality)
- **Real cost:** Noisy estimates, unstable portfolios

**Example:**

- 100 stocks: Need 4,950 correlations
- 1 year: 252 daily returns
- **Vastly underdetermined** (20× more parameters than data)

### 5. Survivorship Bias

**Only using surviving assets:**

- **Mistake:** Build factor model using current S&P 500 constituents
- **Why it fails:** Ignores stocks that went bankrupt, got delisted
- **Fix:** Use point-in-time data
- **Real cost:** Overestimate returns, underestimate risk

**Example:**

Fama-French SMB factor:
- With survivorship bias: Return = 5% annually
- Without bias: Return = 3% annually
- **Overestimate by 67%**

### 6. Look-Ahead Bias

**Using future information:**

- **Mistake:** Use end-of-year financials available in March for January portfolio
- **Why it fails:** Wouldn't have known data in January
- **Fix:** Lag all accounting data appropriately
- **Real cost:** Backtest looks great, live trading fails

**Example:**

Value factor using P/B ratios:
- December 31 financials released March 31
- Mistake: Use for January 1 portfolio
- Reality: Use prior year's data (9-month lag)

### 7. Factor Timing

**Thinking you can time factors:**

- **Mistake:** "Value is cheap now, let's load up"
- **Why it fails:** Factor timing extremely difficult
- **Fix:** Long-term exposure, rebalance mechanically
- **Real cost:** Whipsaw, underperform constant exposure

**Example:**

Value factor underperforms 2017-2020 (growth rally)
- Investor exits value in 2020
- Value outperforms 2021-2022 (value comeback)
- **Missed the reversal**

---

## Best vs. Worst Case

### 1. Best Case: Success

**Factor-based risk management:**

**Setup:**
- Institutional portfolio manager
- Uses Fama-French 5-factor model
- Systematic rebalancing

**Portfolio (2015):**
- 100 stocks, $500M AUM
- Target: Market-neutral, value tilt
- Constraints: $\beta_M = 0$, $\beta_{\text{HML}} = 0.5$

**Factor exposures (achieved):**
- Market: $\beta_M = 0.02$ (near zero) ✓
- Value: $\beta_{\text{HML}} = 0.48$ ✓
- Size: $\beta_{\text{SMB}} = 0.10$ (slight small-cap)
- Momentum: $\beta_{\text{MOM}} = -0.05$ (near zero)
- Profitability: $\beta_{\text{RMW}} = 0.30$ (profitable companies)

**2015-2020 Performance:**

**Value factor:** Underperformed by -15% (growth rally)

**Portfolio:**
- Return: +45%
- Benchmark (market): +60%
- **Underperformed by 15%** as expected (short market, long value)

**But in 2021-2022 (value comeback):**
- Value factor: Outperformed by +25%
- Portfolio: +30%
- Benchmark: +10%
- **Outperformed by 20%**

**Total (2015-2022):**
- Portfolio: +94%
- Benchmark: +74%
- **Outperformed by 20%** (alpha from value exposure)

**Success factors:**
1. Clear factor objectives (not style drift)
2. Disciplined rebalancing (monthly)
3. Low turnover (minimize costs)
4. Stayed the course (didn't abandon value in 2020)
5. Factor model explained 85% of returns (well understood risk)

### 2. Worst Case: Disaster

**Correlation meltdown:**

**Setup:**
- Multi-strategy hedge fund
- "Diversified" across 10 strategies
- Assumed low correlation

**Strategies:**
1. Equity long-short (market-neutral)
2. Convertible arbitrage
3. Merger arbitrage
4. Volatility arbitrage
5. Fixed income relative value
6. Emerging markets
7. Commodities
8. Event-driven
9. Distressed debt
10. Macro trading

**Historical correlations (2005-2007):**
- Average pairwise: $\rho = 0.25$ (low!)
- Believed to be well-diversified

**2008 Financial Crisis:**

**Q4 2008:**

**All strategies crashed together:**
1. Equity L/S: -35% (longs down, shorts up)
2. Convert arb: -40% (credit spreads exploded)
3. Merger arb: -25% (deals broke)
4. Vol arb: -50% (short vol blew up)
5. Fixed income RV: -30% (liquidity crisis)
6. EM: -45% (capital flight)
7. Commodities: -35% (demand collapsed)
8. Event-driven: -30% (events canceled)
9. Distressed: -40% (no bids)
10. Macro: -20% (wrong-footed)

**Crisis correlations:**
- Average pairwise: $\rho = 0.85$ (spiked!)
- All strategies had same factor: **Liquidity**

**Portfolio loss:**

**Naive calculation (assumed $\rho = 0.25$):**
- Expected vol: 12%
- Expected 3σ loss: 36%

**Actual (with $\rho = 0.85$):**
- Realized vol: 40%
- Actual loss: -38%

**Leverage 4:1:**
- Equity: -38% × 4 = **-152%** (complete wipeout)

**Aftermath:**
- Fund lost 100% of equity
- Additional 52% owed to creditors
- Liquidated
- Lawsuits from investors
- "Diversification" was illusory

**Root causes:**
1. Hidden common factor (liquidity risk)
2. Correlation instability (changed in crisis)
3. Leverage amplified (4× turned -38% into -152%)
4. Liquidation spiral (forced selling worsened)
5. Factor model missed key risk (liquidity not measured)

**Lesson:** Correlations spike to 1 in crisis—all diversification disappears

---

## Risk Management Rules

### 1. Correlation Stress Testing

**Required scenarios:**

1. **Crisis:** All correlations → 0.9
2. **Contagion:** Regional correlations → 1
3. **Sector:** Industry correlations → 1
4. **Factor:** Common factor exposure → 3× normal

**Maximum stress loss:**

$$
\text{Stress Loss} \leq 30\% \text{ of Capital}
$$

### 2. Factor Exposure Limits

**Per factor:**

$$
|\beta_{p,k}| \leq 0.5 \text{ (for non-market factors)}
$$

$$
0.7 \leq \beta_{p,M} \leq 1.3 \text{ (for market factor, if not market-neutral)}
$$

**Example:**

Market-neutral fund:
- $\beta_M$: [-0.1, +0.1] ✓
- $\beta_{\text{value}}$: [-0.5, +0.5] ✓
- $\beta_{\text{momentum}}$: [-0.5, +0.5] ✓

### 3. Diversification Minimum

**Number of positions:**

$$
n \geq \frac{1}{1 - R^2} \times 10
$$

Where $R^2$ = Average factor model fit

**Example:**

If $R^2 = 0.70$ (factor model explains 70%):

$$
n \geq \frac{1}{0.30} \times 10 = 33 \text{ positions minimum}
$$

**Rationale:** Need enough stocks to diversify remaining 30% idiosyncratic risk

### 4. Rebalancing Frequency

**Factor exposures:**

- Check daily
- Rebalance if drift > 0.1 from target
- Monthly scheduled rebalance (regardless)

**Example:**

Target $\beta_M = 0$, actual $\beta_M = 0.12$

**Action:** Rebalance to bring back to 0

### 5. Model Validation

**Out-of-sample testing:**

- Estimate factor model on first half of data
- Test on second half
- Check if R² similar (should be within 10%)

**Example:**

- In-sample (2010-2015): R² = 0.75
- Out-of-sample (2016-2020): R² = 0.68
- **Acceptable** (within 10% = 0.075)

### 6. Rolling Correlation

**Estimate using rolling windows:**

$$
\rho_t = f(\text{returns}_{t-N:t})
$$

**Typical:** $N = 60$ days (3 months)

**Update daily:** Fresh correlation estimate each day

**Monitor changes:** Alert if $|\Delta \rho| > 0.2$

### 7. Maximum Leverage

**Based on correlation:**

$$
\text{Max Leverage} = \frac{1}{1 + \bar{\rho}}
$$

**Example:**

Average correlation $\bar{\rho} = 0.5$:

$$
\text{Max Leverage} = \frac{1}{1.5} = 0.67 \times 2 = 1.33
$$

Wait, let me recalculate:

Better rule:

$$
\text{Max Leverage} = 4 - 3\bar{\rho}
$$

**If $\bar{\rho} = 0$:** Max leverage = 4×
**If $\bar{\rho} = 0.5$:** Max leverage = 2.5×
**If $\bar{\rho} = 1$:** Max leverage = 1× (no leverage!)

---

## Real-World Examples

### 1. Quant Quake (August 2007)

**Correlation convergence:**

**Setup:**
- Many quant funds using similar factor models
- All long value, short momentum
- Crowded trades

**August 6-10, 2007:**
- Massive unwinding (unknown trigger)
- All quant funds hit at once
- Correlations spiked

**Losses:**
- Goldman Sachs: -30%
- Renaissance: -8.7%
- AQR: -13%
- D.E. Shaw: -10%

**Cause:** Common factor exposure (crowded trade)

**Recovery:** Most recovered within months (factors mean-reverted)

**Lesson:** Factor crowding creates systemic risk

### 2. LTCM (1998)

**Correlation misjudgment:**

**Strategy:** Convergence trades (spread arbitrage)

**Assumption:** Diversified (100+ strategies)

**Reality:** All had common factor—liquidity

**Crisis:** Russia defaulted, liquidity dried up

**Correlations:**
- Normal: 0.3-0.5
- Crisis: 0.9+

**Losses:** 90% in 4 months

**Leverage:** 25:1 (amplified correlation spike)

### 3. Risk Parity 2020

**COVID crash then recovery:**

**Strategy:** Risk parity (60% bonds, 40% stocks for equal risk)

**March 2020:**
- Stocks: -35%
- Bonds: -10% (unusual—both fell!)
- Correlation changed from -0.3 to +0.5

**Risk parity funds:**
- Expected: Bonds cushion stock fall
- Reality: Both fell (correlation flip)
- Losses: 15-20% (worse than 60/40)

**Recovery:**
- Both rallied (correlation stabilized)
- Recovered by year-end

**Lesson:** Even negative correlation can break

### 4. Factor ETF Proliferation

**2010s: Factor investing boom:**

**Products:**
- MTUM (Momentum ETF): $15B AUM
- VLUE (Value ETF): $8B AUM
- SIZE (Small-Cap ETF): $5B AUM
- QUAL (Quality ETF): $10B AUM

**Concern:** Factor crowding

**2020 value crash:**
- Value factor: -20% underperformance
- VLUE outflows: $2B (25% of AUM)
- Forced selling worsened decline

**2021 value recovery:**
- Value factor: +30% outperformance
- VLUE inflows: $3B
- Too late (missed bottom)

**Lesson:** Retail factor timing creates volatility

---

## Practical Steps

### 1. Estimate Factors

**Choose model:**

- Academic: Fama-French 5-factor
- Practitioner: Barra, Axioma (commercial)
- Custom: Industry-specific

**Run regressions:**

For each asset $i$:

$$
R_i = \alpha_i + \sum_{k=1}^{K} \beta_{i,k} F_k + \epsilon_i
$$

**Output:** Factor loadings $\beta_{i,k}$ for each asset

### 2. Construct Portfolio

**Optimization with factor constraints:**

$$
\min_w w^T \Sigma w
$$

Subject to:
- $\sum w_i = 1$ (fully invested)
- $\beta_{p,M} = \text{target}$ (market exposure)
- $\beta_{p,\text{value}} = \text{target}$ (value tilt)
- etc.

**Example:**

Target: Market-neutral, value tilt

**Constraints:**
- $\beta_M = 0$
- $\beta_{\text{HML}} = 0.5$
- $w_i \in [0, 0.05]$ (max 5% per stock)

### 3. Monitor Exposures

**Daily factor exposure calculation:**

$$
\beta_{p,k} = \sum_{i=1}^{n} w_i \beta_{i,k}
$$

**Track drift from targets:**

$$
\text{Drift}_k = \beta_{p,k} - \beta_{\text{target},k}
$$

**Alert if:** $|\text{Drift}_k| > 0.1$

### 4. Rebalance

**When drift exceeds threshold:**

1. Recalculate optimal weights (with current betas)
2. Generate trade list (buys/sells)
3. Optimize execution (minimize market impact)
4. Execute trades
5. Verify new factor exposures

**Frequency:**
- Scheduled: Monthly
- Event-driven: When drift > threshold

### 5. Attribution

**Decompose return:**

$$
R_p = \sum_{k=1}^{K} \beta_{p,k} F_k + \epsilon_p
$$

**Attribution:**
- Market factor: $\beta_{p,M} \times F_M$
- Value factor: $\beta_{p,\text{HML}} \times F_{\text{HML}}$
- Selection (alpha): $\epsilon_p$

**Example:**

Month return: +2.5%

**Attribution:**
- Market: $1.0 \times 3\% = 3.0\%$
- Value: $0.5 \times (-2\%) = -1.0\%$
- Momentum: $0.1 \times 1\% = 0.1\%$
- Selection: $0.4\%$
- **Total: 3.0 - 1.0 + 0.1 + 0.4 = 2.5\%** ✓

**Insight:** Market positive, value negative, but selection added value

### 6. Risk Reporting

**Daily/weekly report:**

- Factor exposures (current vs. target)
- Factor risk contribution (%)
- Correlation matrix (rolling 3-month)
- Stress test results
- VaR (95%, 99%)

### 7. Model Review

**Quarterly:**

- Reestimate factor model
- Check R² (in-sample and out-of-sample)
- Update factor definitions if needed
- Validate against new data

**Annually:**

- Full factor model review
- Consider new factors
- Benchmark against alternatives
- Document changes

---

## Final Wisdom

> "Correlation and factor exposure are the hidden architecture of portfolio risk—the invisible threads that connect asset returns and ensure that 'diversification' is often an illusion. The correlation coefficient is a seductive number: ρ = 0.5 suggests moderate co-movement, implying diversification works. But correlations are unstable, regime-dependent, and asymmetric—they spike to 1 precisely when you need diversification most (crashes). Worse, observed correlation is just the manifestation of deeper common factors: when you think you're diversified across 10 strategies, you might actually have one exposure (liquidity risk) expressed 10 different ways. Factor models are the antidote: they decompose returns into systematic components (market, value, size) and idiosyncratic noise, revealing true diversification. The tragedy of modern finance: retail chases 'diversification' by adding more stocks, while institutions know the truth—you need uncorrelated *factors*, not uncorrelated *stocks*. With 30 stocks, you've diversified idiosyncratic risk (the easy part); the hard part is managing systematic factor exposure (the part that matters). Every major blow-up—LTCM, quant quake, 2008 crisis—traces back to hidden factor concentration masked by apparent diversification. The golden rule: measure factor exposures explicitly, stress test correlations to 1, and never lever beyond 2-3× when correlations are high. Modern portfolio theory promised risk reduction through diversification; modern portfolio reality shows that in crisis, correlations converge and diversification disappears. Know your factors, respect correlation instability, and remember that 'market-neutral' doesn't mean 'risk-neutral'—it just means you've neutralized one factor while keeping all the others."

**Key to success:**

- Use factor models to understand true exposures (not just correlations)
- Stress test correlations → 1 (always assume worst case in crisis)
- Monitor factor drift daily (exposures change as prices move)
- Diversify across factors, not just assets (30 tech stocks = 1 factor)
- Limit leverage inversely to correlation (high ρ → low leverage)
- Rebalance systematically (monthly minimum for factors)
- Accept that perfect diversification impossible (some systematic risk remains)
- Remember: correlation ≠ causation, but reveals common factors (dig deeper)
