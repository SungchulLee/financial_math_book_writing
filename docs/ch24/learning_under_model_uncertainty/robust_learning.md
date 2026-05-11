# Robust Learning


**Robust learning** addresses uncertainty and misspecification in models by designing algorithms that perform well even when assumptions are violated.

---

## Motivation


Financial environments are characterized by:

- model misspecification,
- non-stationarity,
- limited and noisy data.

Robust learning seeks stability rather than optimality under idealized assumptions.

---

## Robust optimization perspective


Robust learning often adopts a min–max formulation:

$$
\min_{\pi} \max_{\mathbb{P} \in \mathcal{P}} \mathbb{E}_{\mathbb{P}}[L(\pi)]
$$


where $\mathcal{P}$ represents a set of plausible models.

This guards against worst-case scenarios.

---

## Applications in finance


Robust learning is applied to:

- portfolio allocation under uncertainty,
- hedging with ambiguous dynamics,
- risk-sensitive control.

It aligns naturally with regulatory and risk-management objectives.

---

## Trade-offs


Robustness typically:

- reduces sensitivity to estimation error,
- sacrifices some performance in benign regimes,
- improves tail behavior.

This mirrors the bias–variance trade-off.

---

## Key takeaways


- Robust learning hedges against model uncertainty.
- Worst-case thinking improves stability.
- Conservative strategies often outperform long-term.

---

## Further reading


- Hansen & Sargent, robust control.
- Bertsimas et al., robust optimization.

---

## Exercises

**Exercise 1.** A portfolio manager estimates the mean return vector $\hat{\mu}$ from $n = 60$ monthly observations of $d = 10$ assets. The estimation error is $\|\hat{\mu} - \mu\| \le \delta$ with high probability. The robust portfolio problem is $\min_x \max_{\mu : \|\mu - \hat{\mu}\| \le \delta} \{-\mu^\top x + \frac{\gamma}{2} x^\top \Sigma x\}$. (a) Show that the inner maximization has the closed-form solution $-\hat{\mu}^\top x + \delta \|x\| + \frac{\gamma}{2} x^\top \Sigma x$. (b) Interpret the term $\delta \|x\|$ as a shrinkage penalty on the portfolio weights. (c) For $\gamma = 2$, $\delta = 0.02$, $\hat{\mu} = (0.01, \ldots, 0.01)^\top$, and $\Sigma = 0.04 I_{10}$, solve for the optimal robust portfolio and compare with the standard mean-variance solution.

??? success "Solution to Exercise 1"
    **(a)** We solve the inner maximization:

    $$
    \max_{\mu : \|\mu - \hat{\mu}\| \le \delta} \left\{-\mu^\top x + \frac{\gamma}{2} x^\top \Sigma x\right\}
    $$

    Since $\frac{\gamma}{2} x^\top \Sigma x$ does not depend on $\mu$, this reduces to:

    $$
    \max_{\mu : \|\mu - \hat{\mu}\| \le \delta} (-\mu^\top x) + \frac{\gamma}{2} x^\top \Sigma x
    $$

    Write $\mu = \hat{\mu} + \Delta$ where $\|\Delta\| \le \delta$. Then $-\mu^\top x = -\hat{\mu}^\top x - \Delta^\top x$. We need to maximize $-\Delta^\top x$ subject to $\|\Delta\| \le \delta$. By the Cauchy-Schwarz inequality:

    $$
    -\Delta^\top x \le |\Delta^\top x| \le \|\Delta\| \cdot \|x\| \le \delta \|x\|
    $$

    The maximum is achieved when $\Delta = -\delta \frac{x}{\|x\|}$ (assuming $x \ne 0$). Therefore the inner maximization yields:

    $$
    -\hat{\mu}^\top x + \delta \|x\| + \frac{\gamma}{2} x^\top \Sigma x
    $$

    **(b)** The robust outer problem is:

    $$
    \min_x \left\{-\hat{\mu}^\top x + \delta \|x\| + \frac{\gamma}{2} x^\top \Sigma x\right\}
    $$

    The term $\delta \|x\|$ is a **norm penalty** (specifically an $\ell_2$ penalty) on the portfolio weights. This acts as a shrinkage or regularization term that:

    - Penalizes large portfolio positions, because concentrated portfolios (large $\|x\|$) are more sensitive to estimation error in $\mu$.
    - Shrinks the robust portfolio toward the origin (or toward the minimum-variance portfolio if there is a budget constraint $\mathbf{1}^\top x = 1$).
    - Functions identically to Tikhonov / Ridge regularization in regression, providing a **robustness interpretation of shrinkage**: the penalty arises naturally from hedging against the worst-case mean within the uncertainty set.

    **(c)** With $\gamma = 2$, $\delta = 0.02$, $\hat{\mu} = 0.01 \cdot \mathbf{1}_{10}$, and $\Sigma = 0.04 I_{10}$, the standard mean-variance (unconstrained) solution is:

    $$
    x^{\text{MV}} = \frac{1}{\gamma} \Sigma^{-1} \hat{\mu} = \frac{1}{2} \cdot \frac{1}{0.04} \cdot 0.01 \cdot \mathbf{1}_{10} = 0.125 \cdot \mathbf{1}_{10}
    $$

    For the robust problem, the first-order condition (using subdifferential for $\|x\|$ at $x \ne 0$) is:

    $$
    -\hat{\mu} + \delta \frac{x}{\|x\|} + \gamma \Sigma x = 0
    $$

    By symmetry, the solution has the form $x^* = \alpha \mathbf{1}_{10}$ for some $\alpha > 0$. Then $\|x^*\| = \alpha\sqrt{10}$ and $\frac{x^*}{\|x^*\|} = \frac{\mathbf{1}_{10}}{\sqrt{10}}$. Substituting:

    $$
    -0.01 + \frac{0.02}{\sqrt{10}} + 2 \cdot 0.04 \cdot \alpha = 0
    $$

    $$
    0.08 \alpha = 0.01 - \frac{0.02}{\sqrt{10}} = 0.01 - 0.006325 = 0.003675
    $$

    $$
    \alpha = \frac{0.003675}{0.08} \approx 0.04594
    $$

    So $x^{\text{robust}} \approx 0.046 \cdot \mathbf{1}_{10}$, compared with $x^{\text{MV}} = 0.125 \cdot \mathbf{1}_{10}$. The robust portfolio is significantly **smaller** (about 37% of the mean-variance solution), reflecting the shrinkage induced by parameter uncertainty. The robustness penalty reduces aggressive positions that rely on the estimated mean being correct.

---

**Exercise 2.** Hansen and Sargent's robust control framework uses a penalty on the relative entropy (KL divergence) between the reference model $\mathbb{P}_0$ and an alternative $\mathbb{P}$: $\min_\pi \max_{\mathbb{P}: D_{\text{KL}}(\mathbb{P} \| \mathbb{P}_0) \le \eta} \mathbb{E}_\mathbb{P}[L(\pi)]$. (a) Using the dual of the KL constraint, show this is equivalent to $\min_\pi \{\mathbb{E}_{\mathbb{P}_0}[L(\pi)] + \theta \ln \mathbb{E}_{\mathbb{P}_0}[e^{L(\pi)/\theta}]\}$ for some multiplier $\theta > 0$. (b) Recognize the second term as related to the entropic risk measure. (c) Explain why the parameter $\theta$ controls the degree of robustness: small $\theta$ corresponds to high robustness (fear of model misspecification), while $\theta \to \infty$ recovers the standard expected-loss criterion.

??? success "Solution to Exercise 2"
    **(a)** Consider the constrained problem:

    $$
    \min_\pi \max_{\mathbb{P}: D_{\text{KL}}(\mathbb{P} \| \mathbb{P}_0) \le \eta} \mathbb{E}_\mathbb{P}[L(\pi)]
    $$

    Using the Lagrangian dual of the KL constraint, for any $\theta > 0$:

    $$
    \max_{\mathbb{P}} \left\{\mathbb{E}_\mathbb{P}[L(\pi)] - \theta D_{\text{KL}}(\mathbb{P} \| \mathbb{P}_0)\right\}
    $$

    Write $\frac{d\mathbb{P}}{d\mathbb{P}_0} = \frac{e^{L(\pi)/\theta}}{\mathbb{E}_{\mathbb{P}_0}[e^{L(\pi)/\theta}]}$ as the optimal tilted measure (by calculus of variations, the optimizer of a linear functional minus KL divergence is the exponentially tilted measure). Substituting back:

    $$
    \mathbb{E}_\mathbb{P}[L(\pi)] - \theta D_{\text{KL}}(\mathbb{P} \| \mathbb{P}_0)
    $$

    At the optimal $\mathbb{P}^*$, $D_{\text{KL}}(\mathbb{P}^* \| \mathbb{P}_0) = \frac{1}{\theta}\mathbb{E}_{\mathbb{P}^*}[L(\pi)] - \ln \mathbb{E}_{\mathbb{P}_0}[e^{L(\pi)/\theta}]$. After substitution and simplification, the worst-case expected loss equals:

    $$
    \theta \ln \mathbb{E}_{\mathbb{P}_0}[e^{L(\pi)/\theta}]
    $$

    Therefore the robust problem becomes:

    $$
    \min_\pi \left\{\theta \ln \mathbb{E}_{\mathbb{P}_0}\!\left[e^{L(\pi)/\theta}\right]\right\}
    $$

    This can also be written as $\min_\pi \{\mathbb{E}_{\mathbb{P}_0}[L(\pi)] + \theta \ln \mathbb{E}_{\mathbb{P}_0}[e^{(L(\pi) - \mathbb{E}_{\mathbb{P}_0}[L(\pi)])/\theta}]\}$, where $\theta$ plays the role of a Lagrange multiplier for the KL constraint with bound $\eta$.

    **(b)** The **entropic risk measure** at level $\theta$ is defined as:

    $$
    \rho_\theta(X) = \theta \ln \mathbb{E}[e^{X/\theta}]
    $$

    This is exactly the expression appearing above. The entropic risk measure is a coherent risk measure (for suitable sign conventions) that penalizes the tails of $L(\pi)$ exponentially. It interpolates between the expected value ($\theta \to \infty$) and the worst case ($\theta \to 0^+$). The robust control problem is therefore equivalent to minimizing the entropic risk of the loss.

    **(c)** The parameter $\theta$ controls the degree of robustness:

    - **Small $\theta$**: The exponential tilting $e^{L/\theta}$ amplifies large losses dramatically. The worst-case measure $\mathbb{P}^*$ places heavy weight on catastrophic scenarios. The KL constraint is tight (large $\eta$ is effectively used), meaning the adversary has great latitude to distort the model. This corresponds to **high robustness** (extreme fear of model misspecification).
    - **Large $\theta$**: The exponential tilting becomes nearly linear: $e^{L/\theta} \approx 1 + L/\theta$. The worst-case measure is close to $\mathbb{P}_0$. The entropic risk measure converges to $\mathbb{E}_{\mathbb{P}_0}[L(\pi)]$, recovering the standard expected-loss criterion with no robustness.
    - **$\theta \to \infty$**: By Taylor expansion, $\theta \ln \mathbb{E}[e^{L/\theta}] \to \mathbb{E}[L] + \frac{\text{Var}(L)}{2\theta} + \cdots \to \mathbb{E}[L]$, which is the classical (non-robust) objective.

---

**Exercise 3.** Consider robust hedging of a European call option when the true volatility $\sigma$ is unknown but lies in the interval $[\sigma_{\min}, \sigma_{\max}]$. (a) The worst-case loss for a delta-hedger depends on the realized volatility through the gamma term: $\text{P\&L} \approx \frac{1}{2}\Gamma S^2 (\sigma_{\text{realized}}^2 - \sigma_{\text{hedge}}^2) \Delta t$. Explain why the worst case is $\sigma_{\text{realized}} = \sigma_{\max}$ when the hedger is short gamma and $\sigma_{\text{realized}} = \sigma_{\min}$ when long gamma. (b) Describe the Avellaneda-Levy-Paras uncertain volatility model: the robust price is the solution to a nonlinear PDE where $\sigma$ is chosen adversarially at each point. (c) Discuss the conservatism cost: how much wider are robust option prices compared to Black-Scholes with mid-volatility?

??? success "Solution to Exercise 3"
    **(a)** The hedging P&L for a delta-hedged option position over a small interval $\Delta t$ is approximately:

    $$
    \text{P\&L} \approx \frac{1}{2}\Gamma S^2 (\sigma_{\text{realized}}^2 - \sigma_{\text{hedge}}^2) \Delta t
    $$

    where $\Gamma = \frac{\partial^2 V}{\partial S^2}$ is the option's gamma.

    - **Short gamma** ($\Gamma < 0$, e.g., the hedger has sold options): The P&L is $\frac{1}{2}|\Gamma| S^2 (\sigma_{\text{hedge}}^2 - \sigma_{\text{realized}}^2) \Delta t$. This is minimized (worst case) when $\sigma_{\text{realized}}$ is as large as possible, i.e., $\sigma_{\text{realized}} = \sigma_{\max}$. High realized volatility causes losses for short-gamma positions.
    - **Long gamma** ($\Gamma > 0$, e.g., the hedger has bought options): The P&L is $\frac{1}{2}\Gamma S^2 (\sigma_{\text{realized}}^2 - \sigma_{\text{hedge}}^2) \Delta t$. This is minimized when $\sigma_{\text{realized}}$ is as small as possible, i.e., $\sigma_{\text{realized}} = \sigma_{\min}$. Low realized volatility means the purchased optionality is wasted.

    **(b)** The **Avellaneda-Levy-Paras (ALP) uncertain volatility model** addresses this by letting the volatility be chosen adversarially at each point in $(S, t)$ space. The robust option price $V(S, t)$ satisfies the nonlinear PDE:

    $$
    \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^*(S,t)^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0
    $$

    where $\sigma^*$ is chosen to maximize the loss at each point:

    $$
    \sigma^*(S,t) = \begin{cases} \sigma_{\max} & \text{if } \Gamma(S,t) > 0 \quad (\text{long gamma region}) \\ \sigma_{\min} & \text{if } \Gamma(S,t) < 0 \quad (\text{short gamma region}) \end{cases}
    $$

    Wait -- from the perspective of the option writer (who is pricing the option to sell), the **upper bound** on the price uses $\sigma_{\max}$ where $\Gamma > 0$ and $\sigma_{\min}$ where $\Gamma < 0$. The **lower bound** uses the opposite. For a vanilla call, $\Gamma > 0$ everywhere, so the upper robust price is simply the Black-Scholes price at $\sigma_{\max}$.

    The PDE is nonlinear because $\sigma^*$ depends on the sign of $\Gamma = \frac{\partial^2 V}{\partial S^2}$, which itself depends on the solution.

    **(c)** The conservatism cost is the difference between the robust price and the Black-Scholes price at mid-volatility $\bar{\sigma} = (\sigma_{\min} + \sigma_{\max})/2$.

    For a vanilla European call with $\Gamma > 0$ everywhere, the robust upper price is $\text{BS}(\sigma_{\max})$ and the mid-vol price is $\text{BS}(\bar{\sigma})$. The spread is approximately:

    $$
    \text{BS}(\sigma_{\max}) - \text{BS}(\bar{\sigma}) \approx \text{Vega} \cdot \frac{\sigma_{\max} - \sigma_{\min}}{2}
    $$

    For ATM options with large vega, this can be substantial. For example, with $\sigma_{\min} = 0.15$, $\sigma_{\max} = 0.25$, and an ATM 1-year call on a stock at \$100, the vega is roughly \$40 per unit vol, giving a spread of about $40 \times 0.05 = \$2$, which is roughly 2% of the stock price. For exotic options (barriers, digitals) where gamma can change sign, the robust pricing bands are wider still because the nonlinearity of the PDE amplifies the uncertainty.

---

**Exercise 4.** The min-max formulation $\min_\pi \max_{\mathbb{P} \in \mathcal{P}} \mathbb{E}_\mathbb{P}[L(\pi)]$ can be excessively conservative when $\mathcal{P}$ is too large. (a) Explain the bias-variance tradeoff in robust learning: a larger ambiguity set increases bias (more conservative) but reduces variance (less sensitive to estimation error). (b) For a moment-based ambiguity set $\mathcal{P} = \{\mathbb{P} : \|\mathbb{E}_\mathbb{P}[\xi] - \hat{\mu}\| \le \delta, \text{Cov}_\mathbb{P}(\xi) \preceq \Sigma_{\max}\}$, describe how the parameters $\delta$ and $\Sigma_{\max}$ control the conservatism. (c) Argue that in illiquid markets with limited data, robust approaches outperform because estimation error dominates, while in liquid markets with abundant data, standard approaches suffice.

??? success "Solution to Exercise 4"
    **(a)** The **bias-variance tradeoff** in robust learning operates as follows. Let $\mathcal{P}$ be the ambiguity set:

    - **Larger $\mathcal{P}$** (more uncertainty): The min-max objective $\min_\pi \max_{\mathbb{P} \in \mathcal{P}} \mathbb{E}_\mathbb{P}[L(\pi)]$ becomes more conservative. The optimal policy $\pi^*$ is biased toward worst-case scenarios and away from the true optimal. However, because the solution is less sensitive to which specific $\mathbb{P}$ is true, the **variance** of out-of-sample performance is lower. The solution is stable across different realizations of training data.
    - **Smaller $\mathcal{P}$**: The solution is closer to the optimal for the estimated model (less bias) but more sensitive to estimation error (higher variance). If $\mathcal{P}$ is too small and the true $\mathbb{P}$ falls outside $\mathcal{P}$, the guarantees break down entirely.

    The optimal size of $\mathcal{P}$ minimizes the total error (bias + variance), analogous to the regularization parameter in penalized regression.

    **(b)** For the moment-based ambiguity set $\mathcal{P} = \{\mathbb{P} : \|\mathbb{E}_\mathbb{P}[\xi] - \hat{\mu}\| \le \delta, \text{Cov}_\mathbb{P}(\xi) \preceq \Sigma_{\max}\}$:

    - **$\delta$ controls mean uncertainty**: Larger $\delta$ means the robust solution trusts the estimated mean less. This shrinks portfolio weights (as in Exercise 1), reducing performance when $\hat{\mu}$ is accurate but protecting when it is not.
    - **$\Sigma_{\max}$ controls covariance uncertainty**: $\Sigma_{\max} \succ \hat{\Sigma}$ inflates the perceived risk, leading to more diversified portfolios. The gap $\Sigma_{\max} - \hat{\Sigma}$ represents the additional risk budget for covariance estimation error.

    Both parameters should be calibrated to the level of estimation uncertainty: $\delta \propto \|\hat{\mu} - \mu\|$ (which scales as $O(1/\sqrt{n})$) and $\Sigma_{\max}$ should contain the true covariance with high probability.

    **(c)** In **illiquid markets with limited data**:

    - The number of observations $n$ is small relative to the dimension $d$.
    - Estimation error in $\hat{\mu}$ is large (the standard error of the sample mean is $\sigma / \sqrt{n}$, which is substantial for small $n$).
    - The mean-variance optimizer amplifies these errors through $\hat{\Sigma}^{-1}\hat{\mu}$, especially when $\hat{\Sigma}$ is poorly conditioned.
    - Robust approaches dominate because the regularization / shrinkage they impose reduces the catastrophic impact of estimation error.

    In **liquid markets with abundant data**:

    - Large $n$ means $\hat{\mu}$ and $\hat{\Sigma}$ are well-estimated.
    - The bias introduced by robustness is not compensated by variance reduction.
    - Standard optimization may suffice, or only a small ambiguity set is needed.

    This explains the empirical finding that simple robust strategies (e.g., $1/N$ equal weighting or minimum variance) often outperform optimized portfolios in practice: the estimation error in real financial data is large enough that the variance reduction from robustness outweighs the bias cost.

---

**Exercise 5.** A risk manager must choose a model for computing VaR. Model A (Gaussian) gives $\text{VaR}_{99\%} = 2.3\%$, Model B (Student-$t$ with 5 df) gives $\text{VaR}_{99\%} = 3.1\%$, and Model C (historical simulation) gives $\text{VaR}_{99\%} = 2.7\%$. A robust approach takes $\text{VaR}^{\text{robust}} = \max_m \text{VaR}_m$. (a) Compute the robust VaR. (b) This "model envelope" approach is a simple form of robust learning. Discuss its advantages (protection against model misspecification) and disadvantages (always picks the most conservative model). (c) Propose a weighted alternative $\text{VaR}^{\text{weighted}} = \sum_m w_m \text{VaR}_m$ where $w_m$ are Bayesian posterior model weights, and explain how this is less conservative while still accounting for model uncertainty.

??? success "Solution to Exercise 5"
    **(a)** The robust VaR under the model envelope approach is:

    $$
    \text{VaR}^{\text{robust}} = \max\{2.3\%, 3.1\%, 2.7\%\} = 3.1\%
    $$

    This is the VaR from Model B (Student-$t$ with 5 degrees of freedom), which produces the most conservative estimate due to its heavier tails.

    **(b)** Advantages of the model envelope approach:

    - **Protection against misspecification**: If any one of the models is correct, the robust VaR provides a valid upper bound. This is a minimax guarantee.
    - **Simplicity**: No need to assign model probabilities or solve optimization problems. Just compute VaR under each model and take the maximum.
    - **Regulatory appeal**: Regulators favor conservative estimates; the envelope approach guarantees conservatism.

    Disadvantages:

    - **Always picks the most conservative model**: Even if strong evidence supports a particular model, the envelope ignores this. The heavy-tailed model dominates regardless of how well the Gaussian fits.
    - **Increasing conservatism with more models**: Adding models can only increase the robust VaR, even if the new models are implausible.
    - **No learning**: The approach does not update model plausibility based on data.

    **(c)** A Bayesian weighted alternative is:

    $$
    \text{VaR}^{\text{weighted}} = \sum_{m=1}^M w_m \text{VaR}_m
    $$

    where $w_m$ are posterior model weights obtained from Bayesian model comparison:

    $$
    w_m = \frac{p(\text{data} \mid \text{Model } m) \cdot \pi_m}{\sum_{j} p(\text{data} \mid \text{Model } j) \cdot \pi_j}
    $$

    Here $p(\text{data} \mid \text{Model } m)$ is the marginal likelihood of model $m$ and $\pi_m$ is the prior model probability. For example, if the data favor Model A (Gaussian) with posterior weight 0.6, Model C with weight 0.3, and Model B with weight 0.1:

    $$
    \text{VaR}^{\text{weighted}} = 0.6 \times 2.3\% + 0.1 \times 3.1\% + 0.3 \times 2.7\% = 1.38\% + 0.31\% + 0.81\% = 2.50\%
    $$

    This is less conservative than the envelope (3.1%) but still accounts for model uncertainty through the weights. The weighted approach is preferable when:

    - The model set is rich enough that at least one model is approximately correct.
    - Sufficient data exists to discriminate among models.
    - A balance between conservatism and accuracy is desired.

    However, BMA can be fragile if none of the models is correct (model misspecification), in which case the posterior concentrates on the least-wrong model rather than providing genuine robustness.

---

**Exercise 6.** Robust learning in non-stationary environments requires algorithms that adapt to distribution shifts. Consider a strategy that retrains a return prediction model every $W$ days using a rolling window. (a) If the underlying distribution changes at rate $\delta$ per period, argue that the optimal window size balances estimation error (decreasing in $W$) against staleness error (increasing in $W$). (b) Derive the heuristic that optimal $W \propto \delta^{-2/3}$. (c) In practice, how would you detect that a regime change has occurred and trigger early retraining? Discuss CUSUM tests and structural break detection as robust monitoring tools.

??? success "Solution to Exercise 6"
    **(a)** Let the distribution shift at rate $\delta$ per period, meaning the total variation distance between the true distributions at times $t$ and $t + k$ is approximately $k\delta$. Using a rolling window of $W$ observations:

    - **Estimation error** (statistical): With $W$ observations, the estimation error of the sample mean is of order $\sigma / \sqrt{W}$, which **decreases** as $W$ increases.
    - **Staleness error** (model drift): The oldest observation in the window comes from a distribution that has drifted by approximately $W\delta$ from the current distribution. The average staleness across the window contributes an error of order $W\delta / 2$, which **increases** with $W$.

    The total error is approximately:

    $$
    \text{Error}(W) \approx \frac{c_1}{\sqrt{W}} + c_2 W \delta
    $$

    The optimal $W$ balances these two terms.

    **(b)** To minimize the total error, take the derivative and set it to zero:

    $$
    \frac{d}{dW}\left(\frac{c_1}{\sqrt{W}} + c_2 W \delta\right) = -\frac{c_1}{2W^{3/2}} + c_2 \delta = 0
    $$

    Solving:

    $$
    W^{3/2} = \frac{c_1}{2 c_2 \delta} \implies W = \left(\frac{c_1}{2 c_2 \delta}\right)^{2/3}
    $$

    Therefore:

    $$
    W^* \propto \delta^{-2/3}
    $$

    This makes intuitive sense: fast-changing environments ($\delta$ large) require short windows; slow-changing environments allow longer windows. The $-2/3$ exponent reflects the three-halves power relationship between window length and the competing error terms.

    **(c)** To detect regime changes and trigger early retraining:

    - **CUSUM (Cumulative Sum) test**: Maintains a running sum $S_t = \max(0, S_{t-1} + (x_t - \mu_0) - k)$ where $\mu_0$ is the in-control mean and $k$ is a slack parameter. An alarm is raised when $S_t > h$ (a threshold). CUSUM is optimal for detecting small persistent shifts in the mean.
    - **Structural break detection** (e.g., Chow test, Bai-Perron): Tests whether regression coefficients have changed at unknown breakpoints. Multiple breakpoint detection algorithms can identify several regime changes.
    - **Bayesian online changepoint detection**: Maintains a posterior distribution over the current "run length" (time since last changepoint). When the posterior probability of a recent changepoint exceeds a threshold, retraining is triggered.

    In practice, a combination is used: CUSUM for fast detection of mean shifts, supplemented by monitoring of higher moments (variance, correlation breakdowns) and model performance metrics (prediction error, P&L attribution residuals). The rolling window is used as a baseline, with early retraining triggered when monitoring statistics indicate a regime change.

---

**Exercise 7.** Compare three approaches to handling model uncertainty in a credit risk portfolio: (a) Bayesian model averaging with posterior weights over a set of models, (b) distributionally robust optimization over an ambiguity set, and (c) worst-case (maximin) selection. For each approach, describe the mathematical formulation, the assumptions required, and the degree of conservatism. Which approach is most appropriate when (i) the model set is well-specified (true model is in the set), (ii) the model set is misspecified, and (iii) the regulator demands a clear worst-case bound? Argue that in practice, a combination of Bayesian averaging with a robust floor provides the best balance.

??? success "Solution to Exercise 7"
    **(a) Bayesian Model Averaging (BMA):**

    Let $\mathcal{M} = \{M_1, \ldots, M_K\}$ be a set of models, each specifying a distribution $\mathbb{P}_{M_k}$ for portfolio losses. The BMA estimate of any quantity of interest $Q$ (e.g., expected loss, VaR) is:

    $$
    \hat{Q}^{\text{BMA}} = \sum_{k=1}^K w_k \, Q_{M_k}, \quad w_k = \frac{p(\text{data} \mid M_k) \pi_k}{\sum_j p(\text{data} \mid M_j) \pi_j}
    $$

    - **Assumptions**: Requires prior model probabilities $\pi_k$ and the ability to compute marginal likelihoods. Assumes the true model is (approximately) in the set.
    - **Conservatism**: Moderate. Weights reflect data evidence; bad models get downweighted. Not inherently conservative -- can be anti-conservative if all models underestimate risk.

    **(b) Distributionally Robust Optimization (DRO):**

    $$
    \min_x \sup_{\mathbb{P} \in \mathcal{P}} \mathbb{E}_\mathbb{P}[\ell(x, \xi)]
    $$

    where $\mathcal{P}$ is an ambiguity set (e.g., Wasserstein ball, moment constraints).

    - **Assumptions**: Requires specification of the ambiguity set $\mathcal{P}$ and its radius. Does not require prior probabilities over models. Assumes the true distribution lies in $\mathcal{P}$.
    - **Conservatism**: Adjustable through the size of $\mathcal{P}$. More conservative than BMA when $\mathcal{P}$ is large, less when small.

    **(c) Worst-Case (Maximin) Selection:**

    $$
    \min_x \max_{k} \mathbb{E}_{\mathbb{P}_{M_k}}[\ell(x, \xi)]
    $$

    - **Assumptions**: Only requires the ability to evaluate loss under each model. No probabilities needed.
    - **Conservatism**: Highest. Always prepares for the worst model. Can be excessively conservative if one model is extreme.

    **Comparison by scenario:**

    - **(i) Well-specified model set** (true model $\in \mathcal{M}$): **BMA is most appropriate**. With sufficient data, the posterior concentrates on the true model, and BMA converges to the correct answer. DRO is unnecessarily conservative. Worst-case is wasteful.
    - **(ii) Misspecified model set** (true model $\notin \mathcal{M}$): **DRO is most appropriate**. BMA concentrates on the least wrong model, which may still be badly wrong. DRO with a sufficiently large ambiguity set can accommodate distributions outside the parametric model set. Worst-case may also be reasonable if the models bracket the truth.
    - **(iii) Regulatory worst-case bound required**: **Worst-case (maximin) is most appropriate**. It provides a clear, defensible upper bound that does not depend on subjective probabilities or ambiguity set calibration.

    **Practical recommendation**: A hybrid approach combining BMA with a robust floor:

    $$
    \hat{Q}^{\text{hybrid}} = \max\!\left(\hat{Q}^{\text{BMA}}, \, Q^{\text{floor}}\right)
    $$

    where $Q^{\text{floor}}$ is a conservative lower bound (e.g., from DRO or from a stress test). This uses BMA's data-driven weighting in normal conditions while ensuring that the estimate never falls below the robust floor. The floor protects against joint model misspecification (where all models in $\mathcal{M}$ underestimate risk), while BMA prevents excessive conservatism in typical conditions.
