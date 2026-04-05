# Correlation and Systemic Risk


Credit risk is inherently correlated across firms and sectors. Ignoring **correlation and systemic risk** is a major source of model error, especially for portfolio credit products.

---

## Sources of correlation


Credit correlations arise from:
- macroeconomic shocks,
- sectoral dependencies,
- financial contagion and feedback loops.

These effects intensify during crises.

---

## Modeling correlation


Approaches include:
- copula-based default correlation,
- factor models for intensities,
- structural multi-firm asset models.

Each approach balances tractability and realism.

---

## Systemic risk


Systemic risk refers to:
- joint default events,
- cascading failures,
- breakdown of diversification.

Single-name models cannot capture these effects.

---

## Implications for pricing


Ignoring correlation leads to:
- underpricing of portfolio credit risk,
- severe losses in stress scenarios,
- misleading diversification benefits.

This was evident during the global financial crisis.

---

## Key takeaways


- Credit risk is strongly correlated.
- Systemic risk dominates in crises.
- Correlation modeling is unavoidable for portfolios.

---

## Further reading


- Li, Gaussian copula model.
- Duffie et al., correlated defaults.

---

## Exercises

**Exercise 1.** In a one-factor Gaussian copula model, each firm's latent variable is $X_i = \sqrt{\rho}\,Z + \sqrt{1-\rho}\,\epsilon_i$ where $Z$ and $\epsilon_i$ are independent standard normals. Compute the pairwise correlation $\text{Corr}(X_i, X_j) = \rho$ for $i \neq j$. Explain why this single-parameter structure may be insufficient for capturing heterogeneous correlation patterns across sectors.

??? success "Solution to Exercise 1"

    **Computing the pairwise correlation:**

    Given $X_i = \sqrt{\rho}\,Z + \sqrt{1 - \rho}\,\epsilon_i$ where $Z$ and $\epsilon_i$ are independent standard normals, we compute:

    $$
    \text{Cov}(X_i, X_j) = \text{Cov}\!\left(\sqrt{\rho}\,Z + \sqrt{1-\rho}\,\epsilon_i,\; \sqrt{\rho}\,Z + \sqrt{1-\rho}\,\epsilon_j\right)
    $$

    Since $Z$, $\epsilon_i$, $\epsilon_j$ are mutually independent:

    $$
    \text{Cov}(X_i, X_j) = \rho\,\text{Var}(Z) + \sqrt{(1-\rho)(1-\rho)}\,\underbrace{\text{Cov}(\epsilon_i, \epsilon_j)}_{=0} = \rho
    $$

    Also, $\text{Var}(X_i) = \rho\,\text{Var}(Z) + (1-\rho)\,\text{Var}(\epsilon_i) = \rho + (1-\rho) = 1$.

    Therefore:

    $$
    \text{Corr}(X_i, X_j) = \frac{\text{Cov}(X_i, X_j)}{\sqrt{\text{Var}(X_i)\,\text{Var}(X_j)}} = \frac{\rho}{1} = \rho
    $$

    **Why a single-parameter structure is insufficient:**

    The one-factor model forces *all* pairs of firms to share the same correlation $\rho$. In reality, credit correlations are heterogeneous:

    1. **Within-sector correlations are higher** than cross-sector correlations. Two banks have much higher default correlation than a bank and a utility company.
    2. **Geographic clustering** matters: firms in the same region share local economic risks.
    3. **Supply chain dependencies** create firm-specific correlation patterns (e.g., an auto manufacturer and its parts suppliers).
    4. **Size and leverage effects** mean that correlation varies with firm characteristics.

    A single $\rho$ cannot capture this rich structure. It forces a trade-off: calibrating to average correlation understates within-sector risk and overstates cross-sector risk. Multi-factor models (with sector-specific factors, regional factors, etc.) address this by introducing multiple latent variables with different factor loadings per firm.

---

**Exercise 2.** Consider a portfolio of 100 identical firms, each with 5-year default probability $p = 3\%$. Under zero correlation ($\rho = 0$), compute the expected number of defaults and approximate the standard deviation using the binomial model. Repeat for perfect correlation ($\rho = 1$). Compare the shapes of the two loss distributions.

??? success "Solution to Exercise 2"

    **Portfolio of $n = 100$ firms, each with $p = 3\%$ default probability over 5 years.**

    **Case 1: Zero correlation ($\rho = 0$)**

    When defaults are independent, the number of defaults $D$ follows a Binomial$(100, 0.03)$ distribution.

    - **Expected number of defaults:**

    $$
    E[D] = np = 100 \times 0.03 = 3
    $$

    - **Standard deviation:**

    $$
    \text{SD}(D) = \sqrt{np(1-p)} = \sqrt{100 \times 0.03 \times 0.97} = \sqrt{2.91} \approx 1.71
    $$

    The loss distribution is concentrated around 3 defaults. By normal approximation, there is less than a 0.1% chance of more than about 8 defaults ($3 + 3 \times 1.71 \approx 8.1$). The distribution is roughly bell-shaped (slightly skewed due to low $p$).

    **Case 2: Perfect correlation ($\rho = 1$)**

    Under perfect correlation, all firms share the same latent variable: $X_i = Z$ for all $i$. Either *all* firms default or *none* do:

    - With probability $p = 3\%$: all 100 firms default (100 defaults).
    - With probability $1 - p = 97\%$: no firms default (0 defaults).

    - **Expected number of defaults:**

    $$
    E[D] = 100 \times 0.03 = 3 \quad \text{(unchanged)}
    $$

    - **Standard deviation:**

    $$
    \text{SD}(D) = \sqrt{E[D^2] - (E[D])^2}
    $$

    $$
    E[D^2] = 0.03 \times 100^2 + 0.97 \times 0 = 300
    $$

    $$
    \text{SD}(D) = \sqrt{300 - 9} = \sqrt{291} \approx 17.06
    $$

    **Comparison:**

    | Metric | $\rho = 0$ | $\rho = 1$ |
    |---|---|---|
    | $E[D]$ | 3 | 3 |
    | $\text{SD}(D)$ | 1.71 | 17.06 |
    | Distribution shape | Concentrated near mean | Binary: 0 or 100 |
    | $P(D > 10)$ | $\approx 0.003\%$ | $3\%$ |

    The expected number of defaults is the same in both cases — correlation does not affect the mean. However, the standard deviation increases by a factor of 10, and the loss distribution changes from a concentrated bell shape to a bimodal (binary) distribution. Under perfect correlation, the probability of catastrophic loss (all 100 defaults) is 3%, whereas under independence it is astronomically small ($\approx 0.03^{100}$). This is why correlation is the key driver of tail risk in credit portfolios.

---

**Exercise 3.** Explain why credit correlation increases during financial crises. Identify at least three channels through which correlated defaults propagate: (a) macroeconomic, (b) direct financial linkages, and (c) information contagion.

??? success "Solution to Exercise 3"

    **Why credit correlation increases during financial crises:**

    Credit correlations are not constant — they increase sharply during periods of financial stress. Three key propagation channels are:

    **(a) Macroeconomic channel:**

    During recessions, all firms face the same adverse macroeconomic environment: declining GDP, rising unemployment, falling consumer demand, and tightening credit conditions. These common shocks simultaneously weaken the creditworthiness of many firms. In the one-factor model, this corresponds to a large negative realization of the systematic factor $Z$, which pushes all firms' latent variables $X_i$ toward the default threshold. The effective correlation is higher because the common factor dominates idiosyncratic differences.

    *Example*: During the 2008 recession, corporate default rates rose across virtually all sectors — manufacturing, retail, financial services, real estate — because all were exposed to the same aggregate demand collapse and credit freeze.

    **(b) Direct financial linkages (counterparty contagion):**

    Financial institutions are connected through chains of obligations: interbank lending, derivatives contracts, repo financing, and payment systems. When one institution defaults, its counterparties suffer losses, which may push them toward default as well, creating a cascade.

    *Example*: The collapse of Lehman Brothers in September 2008 triggered a chain reaction. Money market funds that held Lehman commercial paper "broke the buck," causing a run on money markets. Banks that had written CDS protection on Lehman faced massive payouts. Lehman's prime brokerage clients lost access to collateral. Each of these channels transmitted the initial default to other institutions, raising correlations far above historical norms.

    **(c) Information contagion (sentiment and herding):**

    When one firm in a sector defaults, the market reassesses the creditworthiness of all similar firms, even those without direct financial linkages to the defaulted entity. This "guilt by association" effect widens spreads across the sector and can trigger a self-fulfilling prophecy: widening spreads increase borrowing costs, which genuinely weakens firms' credit profiles.

    *Example*: After the failure of Bear Stearns in March 2008, CDS spreads on all major investment banks widened dramatically, even those with different business models and risk exposures. The market treated the entire sector as correlated, and the resulting funding stress made other banks genuinely weaker — a case where the perceived correlation *created* actual correlation.

    These three channels reinforce each other during crises, creating a feedback loop where economic weakness causes defaults, defaults cause financial contagion, and contagion creates panic that further weakens the economy.

---

**Exercise 4.** A risk manager assumes a portfolio default correlation of $\rho = 15\%$ based on pre-crisis data. During a crisis, realized correlations rise to $\rho = 50\%$. Describe qualitatively how the portfolio loss distribution changes and why diversification benefits are reduced. What implications does this have for the pricing of senior CDO tranches?

??? success "Solution to Exercise 4"

    **Qualitative change in the portfolio loss distribution:**

    When correlation increases from $\rho = 15\%$ to $\rho = 50\%$, the portfolio loss distribution undergoes a fundamental transformation:

    **1. The mean is unchanged.** Correlation does not affect the expected loss — the expected number of defaults remains $n \times p$ regardless of $\rho$. However, the distribution's *shape* changes dramatically.

    **2. The variance increases substantially.** In the one-factor model, the variance of the number of defaults for a homogeneous portfolio of $n$ names is approximately:

    $$
    \text{Var}(D) \approx n\,p(1-p) + n(n-1)\left[\Phi_2(\Phi^{-1}(p), \Phi^{-1}(p); \rho) - p^2\right]
    $$

    where $\Phi_2$ is the bivariate normal CDF. Higher $\rho$ increases the second term, which represents the covariance between default indicators. The standard deviation can increase by a factor of 2--3 or more.

    **3. The distribution becomes more heavy-tailed and skewed.** Under low correlation, the law of large numbers applies approximately, and the loss distribution is concentrated around the mean. Under high correlation, the systematic factor dominates and the distribution develops a long right tail — large losses become much more probable.

    **4. Diversification benefits are reduced.** The key insight: diversification works by exploiting the cancellation of independent risks. When correlation rises, risks become more aligned, and diversification provides less protection. In the limit $\rho \to 1$, there is no diversification benefit at all.

    **Implications for senior CDO tranches:**

    Senior tranches are only hit by extreme loss events. Their pricing is dominated by the right tail of the loss distribution. When correlation increases:

    - The probability of losses reaching the senior attachment point increases dramatically (as computed in the Gaussian copula exercise using the Vasicek formula).
    - Senior tranche spreads widen significantly — a tranche that was "virtually risk-free" under $\rho = 15\%$ may have meaningful default probability under $\rho = 50\%$.
    - The AAA ratings assigned to senior tranches based on pre-crisis correlations become invalid.
    - Hedging senior tranches becomes more expensive and less reliable, as the sensitivity to correlation (a parameter that is difficult to hedge) increases.

    This is exactly what happened during the 2008 crisis: the shift from benign to stressed correlations caused catastrophic repricing of senior CDO tranches.

---

**Exercise 5.** Compare three approaches to modeling default correlation: (a) copula-based models, (b) multi-name intensity factor models, and (c) structural multi-firm asset models. For each, describe the main advantages and limitations.

??? success "Solution to Exercise 5"

    **Comparison of three approaches to modeling default correlation:**

    **(a) Copula-based models:**

    *Description*: Copulas separate marginal default distributions from the dependence structure. The marginal default probabilities $p_i$ are modeled individually (e.g., from CDS spreads), and a copula function $C(u_1, \ldots, u_n)$ captures all dependence.

    *Advantages*:

    - Flexibility: any marginal distributions can be combined with any copula.
    - Tractability: the Gaussian copula allows semi-analytical CDO pricing via the large-pool approximation.
    - Calibration: implied copula parameters can be extracted from tranche spreads.
    - Scalability: factor copulas reduce dimensionality for large portfolios.

    *Limitations*:

    - Static: copulas describe dependence at a single point in time, not its dynamics.
    - Choice of copula is consequential but difficult to validate — different copulas give very different tail behavior.
    - Single-parameter copulas (Gaussian with one $\rho$) cannot capture heterogeneous correlation.
    - No economic mechanism: copulas are purely statistical, offering no insight into *why* defaults are correlated.

    **(b) Multi-name intensity factor models:**

    *Description*: Each firm's default intensity $\lambda_i(t)$ is driven by common and idiosyncratic factors:

    $$
    \lambda_i(t) = a_i(t) + b_i\,Y(t) + c_i\,Z_i(t)
    $$

    where $Y(t)$ is a common (systematic) factor and $Z_i(t)$ is an idiosyncratic factor.

    *Advantages*:

    - Dynamic: correlation evolves over time as factors evolve.
    - Economic interpretation: the common factor represents macroeconomic conditions.
    - Flexible: heterogeneous factor loadings $b_i$ allow sector-specific correlations.
    - Consistent with single-name CDS pricing through the intensity framework.

    *Limitations*:

    - Computationally intensive for large portfolios.
    - Calibration requires specifying factor dynamics (mean reversion, volatility, jumps), adding many parameters.
    - Joint calibration to multiple names and multiple tenors is difficult.
    - Default contagion (where one default changes other firms' intensities) requires additional modeling.

    **(c) Structural multi-firm asset models:**

    *Description*: Extending the Merton model, each firm's asset value $V_i(t)$ follows a correlated diffusion, and default occurs when $V_i$ hits a barrier $D_i$:

    $$
    dV_i(t) = \mu_i V_i(t)\,dt + \sigma_i V_i(t)\,dW_i(t)
    $$

    with $\text{Corr}(dW_i, dW_j) = \rho_{ij}$.

    *Advantages*:

    - Strong economic foundation: default is linked to firm fundamentals (asset value vs. liabilities).
    - Natural correlation structure: firms are correlated through their asset returns.
    - Observable inputs: equity prices provide information about asset values and correlations.
    - Rich dynamics: the model generates time-varying default probabilities as asset values evolve.

    *Limitations*:

    - Asset values are not directly observable — must be inferred from equity prices.
    - Diffusion-based models underestimate short-term default probabilities (need jumps).
    - High-dimensional correlation matrix $(\rho_{ij})$ is difficult to estimate for large portfolios.
    - Computational cost is high for portfolio credit derivatives (many correlated paths needed).

---

**Exercise 6.** Define systemic risk and distinguish it from idiosyncratic credit risk. Explain why a portfolio with zero expected loss at the individual name level can still suffer large losses due to systemic risk. Give a numerical example using a simple two-state model (normal vs crisis) with correlation $\rho_{\text{normal}} = 10\%$ and $\rho_{\text{crisis}} = 60\%$.

??? success "Solution to Exercise 6"

    **Definitions:**

    **Systemic risk** is the risk of widespread failure across the financial system, where the distress of individual institutions or markets propagates to the entire system through interconnections, common exposures, and feedback mechanisms. It is a *collective* phenomenon that cannot be understood by analyzing individual entities in isolation.

    **Idiosyncratic credit risk** is the risk of default specific to a single firm, driven by firm-specific factors (management decisions, product failures, fraud) that are independent of the broader market. It can be diversified away in a large portfolio.

    **Why a portfolio with low individual-level expected loss can suffer large systemic losses:**

    Consider a portfolio where each firm has very low default probability (say $p = 1\%$) in normal times. If defaults are independent, the portfolio's loss distribution is tightly concentrated around the mean. However, if there is a latent systemic risk — a low-probability state of the world in which many firms default simultaneously — then the unconditional portfolio loss distribution has a hidden fat tail.

    The key insight is that the *unconditional* expected loss may be low, but the *conditional* loss in the crisis state can be enormous. Diversification, which works well in normal states, breaks down in the crisis state because all firms are affected by the same systemic shock.

    **Numerical example with a two-state model:**

    Consider a portfolio of $n = 100$ firms, each with unconditional default probability $p = 3\%$. The economy has two regimes:

    - **Normal state** (probability $\pi_N = 80\%$): correlation $\rho_N = 10\%$, conditional default probability $p_N$.
    - **Crisis state** (probability $\pi_C = 20\%$): correlation $\rho_C = 60\%$, conditional default probability $p_C$.

    We need $\pi_N p_N + \pi_C p_C = p = 3\%$. For illustration, suppose $p_N = 1\%$ and $p_C = 11\%$ (so $0.8 \times 0.01 + 0.2 \times 0.11 = 0.008 + 0.022 = 0.03$, which checks out).

    **Normal state ($\rho = 10\%$, $p_N = 1\%$):**

    Defaults are nearly independent. The number of defaults is approximately Binomial$(100, 0.01)$ with mean $1$ and standard deviation $\approx 1$. The probability of more than 5 defaults is negligible. Losses are small and well-diversified.

    **Crisis state ($\rho = 60\%$, $p_C = 11\%$):**

    High correlation means the systematic factor dominates. The expected number of defaults is $11$, but the distribution is highly dispersed. Using the Vasicek approximation, the probability of more than 30 defaults (30% of the portfolio) is substantial:

    $$
    z^* = \frac{\Phi^{-1}(0.11) - \sqrt{1-0.6}\;\Phi^{-1}(0.30)}{\sqrt{0.6}} = \frac{-1.227 - 0.632 \times (-0.524)}{0.775} = \frac{-1.227 + 0.331}{0.775} \approx -1.156
    $$

    $$
    P(D/n > 30\%) = \Phi(-1.156) \approx 12.4\%
    $$

    So conditional on being in the crisis state, there is a 12.4% probability of losing more than 30% of the portfolio.

    **Unconditional tail risk:**

    The unconditional probability of more than 30 defaults is:

    $$
    P(D > 30) \approx 0.80 \times \underbrace{P(D > 30 \mid \text{Normal})}_{\approx 0} + 0.20 \times 0.124 \approx 2.5\%
    $$

    A single-regime model with $\rho = 10\%$ and $p = 3\%$ would estimate this probability as essentially zero. The two-state model reveals that systemic risk creates a hidden 2.5% probability of catastrophic loss — entirely driven by the crisis state in which diversification collapses.

    This example illustrates why systemic risk cannot be captured by models calibrated exclusively to normal-times data: the tail risk is generated by a different regime with fundamentally different correlation dynamics.
