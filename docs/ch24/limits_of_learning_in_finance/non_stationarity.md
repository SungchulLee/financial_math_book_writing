# Non-Stationarity


A fundamental limitation of learning in finance is **non-stationarity**: the statistical properties of financial data change over time.

---

## What is non-stationarity?


A process is non-stationary if:

- distributions evolve over time,
- parameters drift,
- structural breaks occur.

Most financial time series exhibit non-stationarity.

---

## Sources in financial markets


Non-stationarity arises from:

- changing market regimes,
- regulatory and institutional shifts,
- technological innovation,
- endogenous feedback from trading strategies.

These changes invalidate static models.

---

## Impact on learning algorithms


Non-stationarity causes:

- degradation of predictive performance,
- instability of parameter estimates,
- misleading backtests.

Models trained on past data may fail abruptly.

---

## Mitigation strategies


Common approaches: rolling-window estimation, adaptive / online learning (Recall (see [§ Online Learning and Adaptive Calibration](../online_learning_and_adaptive_calibration/filtering_and_bayesian_updating.md))), regime-switching models, and stress testing beyond historical data. No method fully eliminates the problem.

---

## Key takeaways


- Financial data is inherently non-stationary.
- Learning performance degrades over time.
- Continuous monitoring is essential.

---

## Further reading


- Cont, model uncertainty and instability.
- Hamilton, regime changes in economics.

---

## Exercises

**Exercise 1.** A GARCH(1,1) model $\sigma_t^2 = \omega + \alpha r_{t-1}^2 + \beta \sigma_{t-1}^2$ is estimated on 10 years of daily equity returns. After a major market regime change (e.g., a financial crisis), the estimated parameters shift significantly. Compute the half-life of the GARCH variance process $h = -\log(2)/\log(\alpha + \beta)$ and explain how the persistence parameter $\alpha + \beta$ relates to non-stationarity.

??? success "Solution to Exercise 1"
    **GARCH(1,1) half-life and persistence.**

    The GARCH(1,1) model is:

    $$
    \sigma_t^2 = \omega + \alpha r_{t-1}^2 + \beta \sigma_{t-1}^2
    $$

    The unconditional (long-run) variance exists if and only if $\alpha + \beta < 1$ and is given by:

    $$
    \bar{\sigma}^2 = \frac{\omega}{1 - \alpha - \beta}
    $$

    The variance process mean-reverts toward $\bar{\sigma}^2$ at a rate governed by the persistence parameter $\rho = \alpha + \beta$. Specifically, defining $h_t = \sigma_t^2 - \bar{\sigma}^2$, the deviation from the long-run mean satisfies approximately:

    $$
    \mathbb{E}[h_{t+k} \mid h_t] \approx (\alpha + \beta)^k \, h_t
    $$

    The **half-life** is the number of periods $h$ for which $(\alpha + \beta)^h = 1/2$, yielding:

    $$
    h = \frac{-\log 2}{\log(\alpha + \beta)}
    $$

    **Numerical example.** Suppose $\alpha = 0.05$ and $\beta = 0.93$, so $\alpha + \beta = 0.98$. Then:

    $$
    h = \frac{-\log 2}{\log(0.98)} = \frac{0.6931}{0.0202} \approx 34.3 \text{ trading days}
    $$

    **Relation to non-stationarity.** When $\alpha + \beta$ is close to 1, the half-life is very long, meaning the variance process is highly persistent --- shocks to volatility decay slowly. In the limit $\alpha + \beta \to 1$, the process approaches an IGARCH (integrated GARCH), which is non-stationary in the sense that the unconditional variance is undefined (it diverges). After a regime change (e.g., a financial crisis), the estimated parameters $\alpha$ and $\beta$ shift because the new data has fundamentally different volatility dynamics. A model estimated on pre-crisis data with $\alpha + \beta = 0.98$ will be too slow to adapt to a crisis where realized volatility jumps by a factor of 3--5, and too slow to revert after the crisis ends. This parameter instability is a direct manifestation of non-stationarity: the data-generating process has changed, invalidating the assumption that $\omega$, $\alpha$, and $\beta$ are constants.

---

**Exercise 2.** Describe the rolling-window estimation approach for a mean-variance portfolio. If the window size is $W = 252$ trading days, explain the trade-off: a larger window provides more data (reducing estimation error) but may include stale data from a different regime (increasing misspecification). How would you choose $W$ optimally?

??? success "Solution to Exercise 2"
    **Rolling-window estimation trade-off.**

    In a rolling-window mean-variance portfolio, at each date $t$ we estimate the mean vector $\hat{\mu}_t$ and covariance matrix $\hat{\Sigma}_t$ using the most recent $W$ observations:

    $$
    \hat{\mu}_t = \frac{1}{W}\sum_{s=t-W+1}^{t} r_s, \qquad \hat{\Sigma}_t = \frac{1}{W-1}\sum_{s=t-W+1}^{t} (r_s - \hat{\mu}_t)(r_s - \hat{\mu}_t)^\top
    $$

    **Trade-off analysis:**

    - **Estimation error** (favors large $W$): The standard error of $\hat{\mu}$ scales as $\sigma/\sqrt{W}$ and the estimation error of $\hat{\Sigma}$ scales as $O(1/\sqrt{W})$. A larger window reduces sampling noise.
    - **Misspecification error** (favors small $W$): If the true parameters changed $\tau$ periods ago, observations older than $\tau$ come from a different regime. Including stale data introduces bias. The misspecification error grows with $W$ when $W > \tau$.

    The total error can be decomposed as:

    $$
    \text{Total Error} \approx \underbrace{\frac{c_1}{\sqrt{W}}}_{\text{estimation error}} + \underbrace{c_2 \cdot W \cdot |\delta|}_{\text{misspecification bias}}
    $$

    where $|\delta|$ is the magnitude of parameter drift per period and $c_1, c_2$ are constants.

    **Optimal $W$:** Minimizing total error by differentiating with respect to $W$ and setting to zero:

    $$
    \frac{\partial}{\partial W}\left(\frac{c_1}{\sqrt{W}} + c_2 W |\delta|\right) = -\frac{c_1}{2W^{3/2}} + c_2 |\delta| = 0
    $$

    $$
    W^* = \left(\frac{c_1}{2 c_2 |\delta|}\right)^{2/3}
    $$

    This shows that the optimal window is shorter when the drift rate $|\delta|$ is larger (i.e., during turbulent periods) and longer when data is stable. For $W = 252$, the window covers one trading year. This is a common default, but it may be too long during crises and too short during stable regimes. In practice, one can use an adaptive window that shortens automatically when structural break tests (e.g., CUSUM) detect instability, or use exponential weighting as a smooth alternative.

---

**Exercise 3.** The Augmented Dickey-Fuller (ADF) test examines whether a time series has a unit root (a form of non-stationarity). For the model $\Delta x_t = \alpha + \beta x_{t-1} + \sum_{j=1}^p \gamma_j \Delta x_{t-j} + \varepsilon_t$, explain what the null hypothesis $\beta = 0$ means and how rejection (or non-rejection) informs the choice of learning algorithm for return prediction.

??? success "Solution to Exercise 3"
    **ADF test and unit roots.**

    The ADF regression model is:

    $$
    \Delta x_t = \alpha + \beta x_{t-1} + \sum_{j=1}^{p} \gamma_j \Delta x_{t-j} + \varepsilon_t
    $$

    **Null hypothesis $H_0: \beta = 0$:** This means $x_t$ has a unit root. Under the null, the model reduces to:

    $$
    \Delta x_t = \alpha + \sum_{j=1}^p \gamma_j \Delta x_{t-j} + \varepsilon_t
    $$

    which is an AR($p$) model for the *changes* $\Delta x_t$. The level $x_t$ is a random walk with drift (non-stationary), meaning shocks have permanent effects and the process does not revert to a fixed mean.

    **Alternative hypothesis $H_1: \beta < 0$:** The process is (trend-)stationary. Shocks decay over time and $x_t$ reverts toward a long-run level.

    **Implications for learning algorithms:**

    - **Non-rejection (unit root present):** The raw series $x_t$ (e.g., log-prices) is non-stationary. A learning algorithm should *not* use levels as features, since the distribution of $x_t$ is time-varying and standard regression assumptions break down (spurious regression problem). Instead, use returns $\Delta x_t$ or other stationary transformations.

    - **Rejection (stationary):** The series mean-reverts, making level-based prediction meaningful. Mean-reversion strategies (e.g., pairs trading, cointegration-based strategies) require stationarity of the spread. If the ADF test rejects, there is statistical support for mean-reversion.

    The ADF test statistic does not follow a standard $t$-distribution under the null --- it follows the Dickey-Fuller distribution, which has heavier left tails. Critical values (e.g., $-2.86$ at 5% for a model with intercept) are obtained from simulation. Practitioners should also be aware that the ADF test has low power in small samples: it frequently fails to reject the null when the true process is stationary but highly persistent ($\beta$ close to 0).

---

**Exercise 4.** In a two-regime Hamilton regime-switching model, returns follow $r_t | s_t = i \sim N(\mu_i, \sigma_i^2)$ with transition matrix $P = \begin{pmatrix} p_{11} & 1-p_{11} \\ 1-p_{22} & p_{22} \end{pmatrix}$. If $p_{11} = 0.98$ and $p_{22} = 0.90$, compute the expected duration of each regime and the stationary probability of being in each regime. Explain why models trained on data predominantly from regime 1 may fail catastrophically in regime 2.

??? success "Solution to Exercise 4"
    **Hamilton regime-switching model: expected durations and stationary probabilities.**

    In the two-regime model, the transition matrix is:

    $$
    P = \begin{pmatrix} p_{11} & 1 - p_{11} \\ 1 - p_{22} & p_{22} \end{pmatrix} = \begin{pmatrix} 0.98 & 0.02 \\ 0.10 & 0.90 \end{pmatrix}
    $$

    **Expected duration of each regime.** The duration in regime $i$ is geometrically distributed with success probability $1 - p_{ii}$ (probability of leaving), so:

    $$
    \mathbb{E}[D_1] = \frac{1}{1 - p_{11}} = \frac{1}{1 - 0.98} = \frac{1}{0.02} = 50 \text{ days}
    $$

    $$
    \mathbb{E}[D_2] = \frac{1}{1 - p_{22}} = \frac{1}{1 - 0.90} = \frac{1}{0.10} = 10 \text{ days}
    $$

    Regime 1 (e.g., low volatility, "normal") persists for an average of 50 days, while regime 2 (e.g., high volatility, "crisis") persists for an average of 10 days.

    **Stationary probabilities.** The stationary distribution $\pi = (\pi_1, \pi_2)$ satisfies $\pi P = \pi$ and $\pi_1 + \pi_2 = 1$. From the balance equation:

    $$
    \pi_1(1 - p_{11}) = \pi_2(1 - p_{22})
    $$

    $$
    \pi_1 \cdot 0.02 = \pi_2 \cdot 0.10
    $$

    $$
    \pi_1 = 5\pi_2
    $$

    Combined with $\pi_1 + \pi_2 = 1$:

    $$
    \pi_1 = \frac{1 - p_{22}}{(1 - p_{11}) + (1 - p_{22})} = \frac{0.10}{0.02 + 0.10} = \frac{0.10}{0.12} = \frac{5}{6} \approx 0.833
    $$

    $$
    \pi_2 = \frac{0.02}{0.12} = \frac{1}{6} \approx 0.167
    $$

    **Why models fail across regimes.** The market spends approximately 83.3% of the time in regime 1. A model trained on historical data will be dominated by regime-1 observations. If regime 2 has dramatically different parameters (e.g., $\mu_2 \ll \mu_1$ and $\sigma_2 \gg \sigma_1$), the model will be poorly calibrated for regime 2. Specifically:

    - The estimated mean and variance reflect primarily regime-1 characteristics.
    - Risk management based on regime-1 volatility severely underestimates tail risk during regime 2.
    - The model may interpret regime-2 returns as anomalies rather than draws from a different distribution, leading to catastrophic position sizing.

    This is a fundamental manifestation of non-stationarity: the data is a mixture, and the mixture weights (regime occupancy) mean that rare but important regimes are underrepresented in training data.

---

**Exercise 5.** An online learning algorithm uses exponential weighting with decay parameter $\lambda$: $\hat{\mu}_t = (1-\lambda)\hat{\mu}_{t-1} + \lambda r_t$. Show that this is equivalent to a weighted average with exponentially declining weights. For what value of $\lambda$ does the effective window size equal approximately 60 days? How does $\lambda$ trade off responsiveness to regime changes against noise sensitivity?

??? success "Solution to Exercise 5"
    **Exponential weighting and effective window size.**

    The online learning update is:

    $$
    \hat{\mu}_t = (1 - \lambda)\hat{\mu}_{t-1} + \lambda r_t
    $$

    **Equivalence to exponentially weighted average.** By recursive substitution:

    $$
    \hat{\mu}_t = \lambda r_t + (1 - \lambda)\hat{\mu}_{t-1}
    $$

    $$
    = \lambda r_t + (1 - \lambda)[\lambda r_{t-1} + (1 - \lambda)\hat{\mu}_{t-2}]
    $$

    $$
    = \lambda r_t + \lambda(1 - \lambda)r_{t-1} + (1 - \lambda)^2 \hat{\mu}_{t-2}
    $$

    Continuing the recursion:

    $$
    \hat{\mu}_t = \lambda \sum_{k=0}^{t-1} (1-\lambda)^k r_{t-k} + (1-\lambda)^t \hat{\mu}_0
    $$

    For large $t$, the initialization term vanishes and:

    $$
    \hat{\mu}_t \approx \lambda \sum_{k=0}^{\infty} (1-\lambda)^k r_{t-k}
    $$

    This is a weighted average with weights $w_k = \lambda(1-\lambda)^k$ that decay exponentially. The weights sum to 1:

    $$
    \sum_{k=0}^{\infty} w_k = \lambda \sum_{k=0}^{\infty}(1-\lambda)^k = \lambda \cdot \frac{1}{1-(1-\lambda)} = 1
    $$

    **Effective window size.** The effective window size is the number of observations that receive "meaningful" weight. A standard definition is the reciprocal of the sum of squared weights:

    $$
    W_{\text{eff}} = \frac{1}{\sum_{k=0}^\infty w_k^2} = \frac{1}{\lambda^2 \sum_{k=0}^\infty (1-\lambda)^{2k}} = \frac{1}{\lambda^2 \cdot \frac{1}{1-(1-\lambda)^2}} = \frac{1-(1-\lambda)^2}{\lambda^2} = \frac{2-\lambda}{\lambda}
    $$

    An alternative common definition uses the "center of mass" interpretation: $W_{\text{eff}} = (1-\lambda)/\lambda$, which represents the mean lag of the weights.

    **Finding $\lambda$ for $W_{\text{eff}} \approx 60$ days.** Using the center-of-mass definition:

    $$
    \frac{1-\lambda}{\lambda} = 60 \implies 1 - \lambda = 60\lambda \implies \lambda = \frac{1}{61} \approx 0.0164
    $$

    Using the sum-of-squares definition:

    $$
    \frac{2 - \lambda}{\lambda} = 60 \implies 2 - \lambda = 60\lambda \implies \lambda = \frac{2}{61} \approx 0.0328
    $$

    Either convention gives $\lambda$ on the order of $1/60$ to $2/61$.

    **Trade-off between responsiveness and noise sensitivity:**

    - **Large $\lambda$** (short effective window): The estimator responds quickly to regime changes, tracking new dynamics rapidly. However, it is highly sensitive to noise --- each individual observation receives large weight, so the estimate fluctuates substantially.
    - **Small $\lambda$** (long effective window): The estimator is smooth and stable, averaging out noise effectively. However, it responds slowly to regime changes, continuing to use stale data for many periods after the true parameters have shifted.

    This is the same bias-variance trade-off as in the rolling-window approach, but with a smooth (exponential) weighting rather than a sharp (rectangular) window.

---

**Exercise 6.** Non-stationarity can be structural (permanent regime change) or transient (temporary dislocation). Design a monitoring system that distinguishes between these two cases using: (a) CUSUM tests for detecting structural breaks, and (b) mean-reversion tests for detecting transient dislocations. Explain why the appropriate response differs: recalibration for structural breaks versus patience for transient dislocations.

??? success "Solution to Exercise 6"
    **Monitoring system for structural vs. transient non-stationarity.**

    **(a) CUSUM test for structural breaks.**

    The CUSUM (Cumulative Sum) test detects persistent shifts in the mean of a process. Define the cumulative sum of standardized residuals:

    $$
    C_t = \sum_{s=1}^{t} \frac{r_s - \hat{\mu}}{\hat{\sigma}}
    $$

    where $\hat{\mu}$ and $\hat{\sigma}$ are estimated from a reference (in-control) period. Under the null of no structural change, $C_t$ behaves like a random walk with zero drift. Under a structural break at time $\tau$ that shifts the mean by $\delta$:

    $$
    \mathbb{E}[C_t] = \begin{cases} 0 & t < \tau \\ (t - \tau)\delta/\hat{\sigma} & t \geq \tau \end{cases}
    $$

    The CUSUM test signals a break when $|C_t|$ exceeds a threshold $h$ (often calibrated so that the average run length under the null is a specified value, e.g., 500 days). A **V-shape** in the CUSUM plot indicates a permanent level shift, while a **return to zero** indicates a transient deviation.

    A more sensitive variant is the **Page CUSUM**, which resets after each detection:

    $$
    S_t^+ = \max(0, S_{t-1}^+ + (r_t - \hat{\mu} - k)), \quad S_t^- = \min(0, S_{t-1}^- + (r_t - \hat{\mu} + k))
    $$

    where $k > 0$ is a reference value (typically $\delta/2$ for a shift of size $\delta$). A signal is raised when $S_t^+$ or $|S_t^-|$ exceeds threshold $h$.

    **(b) Mean-reversion tests for transient dislocations.**

    To detect transient dislocations, use tests for mean-reversion:

    - **Ornstein-Uhlenbeck fit:** Estimate $dx_t = \kappa(\theta - x_t)dt + \sigma dW_t$ on the deviation series $x_t = r_t - \hat{\mu}$. If $\kappa > 0$ is significantly positive, the deviation is transient (mean-reverting). A confidence interval for $\kappa$ quantifies how quickly the dislocation is expected to dissipate.

    - **Variance ratio test:** Compute $VR(q) = \text{Var}(x_{t+q} - x_t)/(q \cdot \text{Var}(x_{t+1} - x_t))$. Under a random walk (structural break), $VR(q) \approx 1$. Under mean-reversion (transient dislocation), $VR(q) < 1$ for large $q$.

    **Monitoring system design:**

    1. Continuously compute the CUSUM statistic $C_t$.
    2. When $|C_t|$ breaches the threshold $h$, flag a potential non-stationarity event.
    3. Upon flagging, run the mean-reversion test on the post-flag data.
    4. **Classification:**
        - If $C_t$ continues to diverge and the variance ratio is near 1: **structural break** --- the mean has permanently shifted.
        - If $C_t$ reverses toward zero and $\kappa > 0$ is significant: **transient dislocation** --- the deviation is temporary.

    **Why the response differs:**

    - **Structural break:** The old model is invalid. The correct response is to **recalibrate** the model using only post-break data, discarding (or down-weighting) pre-break observations. Continuing to use the old model will produce systematically biased predictions.

    - **Transient dislocation:** The old model is still valid; the market has temporarily deviated from equilibrium. The correct response is **patience** --- wait for the dislocation to resolve. Recalibrating to the transient regime would introduce noise into the estimates and cause the model to "chase" temporary fluctuations. In fact, transient dislocations may represent trading opportunities (e.g., mean-reversion strategies) rather than model failures.
