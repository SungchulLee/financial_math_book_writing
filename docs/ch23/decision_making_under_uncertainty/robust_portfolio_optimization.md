# Robust Portfolio Optimization


## Introduction


**Robust portfolio optimization** addresses a fundamental challenge in quantitative finance: optimal portfolios are highly sensitive to estimation errors in expected returns and covariances. Small changes in estimated parameters can lead to dramatically different portfolio weights, often resulting in extreme, undiversified positions that perform poorly out-of-sample.

The robust approach explicitly incorporates **parameter uncertainty** into the optimization problem, seeking portfolios that perform well across a range of plausible parameter values rather than optimizing for a single point estimate.

Key developments include:

1. **Goldfarb-Iyengar (2003)**: SOCP reformulation for ellipsoidal uncertainty
2. **Ben-Tal-Nemirovski**: Conic optimization for robust problems
3. **Black-Litterman (1992)**: Bayesian shrinkage as implicit robustness
4. **Distributionally robust optimization**: Ambiguity over probability distributions

## Classical Mean-Variance Optimization


### 1. Markowitz Framework


**Setup**: $n$ assets with random returns $R = (R_1, \ldots, R_n)^\top$.

**Parameters**:

- $\mu = \mathbb{E}[R]$: Expected returns
- $\Sigma = \text{Cov}(R)$: Covariance matrix

**Mean-Variance Problem**:

$$
\max_w \left\{w^\top \mu - \frac{\lambda}{2} w^\top \Sigma w\right\}
$$

subject to $\mathbf{1}^\top w = 1$ (full investment).

**Solution**: The optimal portfolio is:

$$
w^* = \frac{1}{\lambda} \Sigma^{-1}(\mu - \nu \mathbf{1})
$$

where $\nu$ is the Lagrange multiplier for the budget constraint.

### 2. Estimation Error Problem


**Sensitivity Analysis**: The optimal weights depend on $\Sigma^{-1} \mu$. Estimation errors in $\mu$ are amplified by $\Sigma^{-1}$.

**Empirical Finding** (Michaud, 1989): Mean-variance optimization is an "error maximizer" — it overweights assets with overestimated returns and underweights those with underestimated returns.

**Estimation Error Magnitudes**: With $T$ observations:

$$
\text{SE}(\hat{\mu}_i) \approx \frac{\sigma_i}{\sqrt{T}}, \quad \text{SE}(\hat{\sigma}_{ij}) \approx \frac{\sigma_{ij}}{\sqrt{T}}
$$

For typical parameters ($\sigma \approx 20\%$, $T = 60$ months), the standard error of expected return is $\approx 2.5\%$ annually — larger than reasonable expected return differences.

## Robust Optimization Framework


### 1. Uncertainty Sets


**Definition**: An uncertainty set $\mathcal{U}$ contains all parameter values considered plausible:

$$
(\mu, \Sigma) \in \mathcal{U}
$$

**Robust Problem**:

$$
\max_w \min_{(\mu, \Sigma) \in \mathcal{U}} \left\{w^\top \mu - \frac{\lambda}{2} w^\top \Sigma w\right\}
$$

**Interpretation**: Maximize the worst-case risk-adjusted return over all plausible parameters.

### 2. Types of Uncertainty Sets


**Box Uncertainty** (Mean):

$$
\mathcal{U}_{\text{box}} = \{\mu: |\mu_i - \hat{\mu}_i| \leq \delta_i, \, i = 1, \ldots, n\}
$$

**Ellipsoidal Uncertainty** (Mean):

$$
\mathcal{U}_{\text{ellip}} = \{\mu: (\mu - \hat{\mu})^\top \Omega^{-1} (\mu - \hat{\mu}) \leq \kappa^2\}
$$

where $\Omega$ is the estimation error covariance and $\kappa$ controls the confidence level.

**Factor Model Uncertainty**:

$$
\mu = B f + \epsilon, \quad f \in \mathcal{U}_f
$$

with uncertainty in factor returns $f$.

### 3. Worst-Case Analysis


**Lemma** (Worst-Case Mean): For ellipsoidal uncertainty $\mathcal{U}_{\text{ellip}}$:

$$
\min_{\mu \in \mathcal{U}_{\text{ellip}}} w^\top \mu = w^\top \hat{\mu} - \kappa \sqrt{w^\top \Omega w}
$$

**Proof**: By Cauchy-Schwarz, the minimum is achieved at:

$$
\mu^* = \hat{\mu} - \kappa \frac{\Omega w}{\sqrt{w^\top \Omega w}}
$$

## Goldfarb-Iyengar Formulation


### 1. Joint Uncertainty in Mean and Covariance


**Setup**: Consider separate uncertainty sets:

$$
\mu \in \mathcal{U}_{\mu} = \{\mu: \|\Sigma_{\mu}^{-1/2}(\mu - \hat{\mu})\|_2 \leq \delta_1\}
$$

$$
\Sigma \in \mathcal{U}_{\Sigma} = \{\Sigma: \|\Sigma_{\Sigma}^{-1/2}(\text{vec}(\Sigma) - \text{vec}(\hat{\Sigma}))\|_2 \leq \delta_2\}
$$

### 2. SOCP Reformulation


**Theorem** (Goldfarb-Iyengar, 2003): The robust mean-variance problem:

$$
\max_w \min_{\mu \in \mathcal{U}_{\mu}} w^\top \mu - \frac{\lambda}{2} \max_{\Sigma \in \mathcal{U}_{\Sigma}} w^\top \Sigma w
$$

subject to $\mathbf{1}^\top w = 1$, is equivalent to the SOCP:

$$
\begin{aligned}
\max_{w, t, s} \quad & t - \frac{\lambda}{2} s \\
\text{s.t.} \quad & w^\top \hat{\mu} - \delta_1 \|\Sigma_{\mu}^{1/2} w\|_2 \geq t \\
& w^\top \hat{\Sigma} w + \delta_2 \|\Sigma_{\Sigma}^{1/2} (w \otimes w)\|_2 \leq s \\
& \mathbf{1}^\top w = 1
\end{aligned}
$$

### 3. Efficient Computation


**Complexity**: The SOCP can be solved in polynomial time using interior-point methods.

**Software**: CVXPY, MOSEK, Gurobi support SOCP.

```python
import cvxpy as cp
import numpy as np

def robust_portfolio(mu_hat, Sigma_hat, Sigma_mu, delta1, lambda_risk):
    n = len(mu_hat)
    w = cp.Variable(n)
    t = cp.Variable()
    
    # Worst-case expected return
    worst_return = w @ mu_hat - delta1 * cp.norm(Sigma_mu @ w, 2)
    
    # Risk term
    risk = cp.quad_form(w, Sigma_hat)
    
    objective = cp.Maximize(t - 0.5 * lambda_risk * risk)
    constraints = [
        worst_return >= t,
        cp.sum(w) == 1,
        w >= 0  # Long-only constraint
    ]
    
    prob = cp.Problem(objective, constraints)
    prob.solve()
    return w.value
```

## Distributional Robustness


### 1. Ambiguity Sets


**Definition**: Instead of parameter uncertainty, consider uncertainty over the entire distribution:

$$
\max_w \min_{P \in \mathcal{P}} \mathbb{E}_P[u(w^\top R)]
$$

**Common Ambiguity Sets**:

1. **Moment Constraints**:
   
$$
\mathcal{P} = \{P: \mathbb{E}_P[R] \in \mathcal{U}_{\mu}, \, \mathbb{E}_P[RR^\top] \in \mathcal{U}_{\Sigma}\}
$$

2. **Wasserstein Ball**:

$$
\mathcal{P} = \{P: W_p(P, \hat{P}) \leq \epsilon\}
$$

3. **Relative Entropy Ball**:

$$
\mathcal{P} = \{P: D_{\text{KL}}(P \| \hat{P}) \leq \eta\}
$$

### 2. Worst-Case CVaR


**Distributionally Robust CVaR**:

$$
\max_w \min_{P \in \mathcal{P}} \text{CVaR}_{\alpha}^P(w^\top R)
$$

**Theorem** (Zhu-Fukushima, 2009): For Wasserstein ambiguity:

$$
\sup_{P: W_1(P, \hat{P}) \leq \epsilon} \text{CVaR}_{\alpha}^P(X) = \text{CVaR}_{\alpha}^{\hat{P}}(X) + \frac{\epsilon}{\alpha}
$$

**Implication**: Wasserstein robustness adds a penalty proportional to the Lipschitz constant of the loss function.

### 3. Tractable Reformulations


**Moment-Based Ambiguity**: With mean $\mu \in \mathcal{U}_{\mu}$ and covariance $\Sigma \in \mathcal{U}_{\Sigma}$:

$$
\min_{P \in \mathcal{P}} \mathbb{E}_P[-w^\top R] = -w^\top \mu^* + \sqrt{w^\top \Sigma^* w}
$$

where $(\mu^*, \Sigma^*)$ are worst-case parameters (not necessarily from the same distribution).

## Regularization Interpretation


### 1. Shrinkage Estimators


**James-Stein Shrinkage**: Shrink $\hat{\mu}$ toward a target $\mu_0$:

$$
\tilde{\mu} = (1-\alpha) \hat{\mu} + \alpha \mu_0
$$

**Optimal Shrinkage** (Ledoit-Wolf):

$$
\alpha^* = \frac{\sum_{i=1}^n \text{Var}(\hat{\mu}_i)}{|\hat{\mu} - \mu_0|^2 + \sum_{i=1}^n \text{Var}(\hat{\mu}_i)}
$$

### 2. Equivalence to Robust Optimization


**Theorem**: The robust portfolio problem with ellipsoidal uncertainty:

$$
\max_w \left\{w^\top \hat{\mu} - \kappa \sqrt{w^\top \Omega w} - \frac{\lambda}{2} w^\top \Sigma w\right\}
$$

is equivalent to mean-variance optimization with shrinkage:

$$
\max_w \left\{w^\top \tilde{\mu} - \frac{\tilde{\lambda}}{2} w^\top \Sigma w\right\}
$$

for appropriate $\tilde{\mu}$ and $\tilde{\lambda}$.

### 3. Norm Constraints


**L1 Penalty** (Sparse Portfolios):

$$
\max_w \left\{w^\top \mu - \frac{\lambda}{2} w^\top \Sigma w - \gamma \|w\|_1\right\}
$$

**L2 Penalty** (Ridge):

$$
\max_w \left\{w^\top \mu - \frac{\lambda}{2} w^\top \Sigma w - \gamma \|w\|_2^2\right\}
$$

**Equivalence**: L2 penalty is equivalent to shrinkage toward zero; L1 promotes sparsity.

## Black-Litterman Model


### 1. Bayesian Framework


**Prior**: Market equilibrium returns are the prior:

$$
\pi = \lambda \Sigma w_{\text{mkt}}
$$

where $w_{\text{mkt}}$ is the market capitalization weighted portfolio.

**Views**: Investor views are expressed as:

$$
P \mu = q + \epsilon, \quad \epsilon \sim N(0, \Omega)
$$

where $P$ is the pick matrix and $q$ is the view vector.

### 2. Posterior Returns


**Bayesian Update**:

$$
\mathbb{E}[\mu | \text{views}] = [(\tau \Sigma)^{-1} + P^\top \Omega^{-1} P]^{-1} [(\tau \Sigma)^{-1} \pi + P^\top \Omega^{-1} q]
$$

**Posterior Covariance**:

$$
\text{Cov}[\mu | \text{views}] = [(\tau \Sigma)^{-1} + P^\top \Omega^{-1} P]^{-1}
$$

### 3. Robust Interpretation


**Connection**: Black-Litterman shrinks extreme views toward market equilibrium:

- High confidence views ($\Omega$ small): Posterior close to views
- Low confidence ($\Omega$ large): Posterior close to equilibrium

**Implicit Robustness**: The model is robust to specification errors in views through the uncertainty parameter $\Omega$.

## Resampled Efficiency


### 1. Michaud's Approach


**Resampling Procedure**:

1. Generate $B$ bootstrap samples of returns
2. Estimate $(\hat{\mu}^{(b)}, \hat{\Sigma}^{(b)})$ for each sample
3. Compute efficient frontier portfolio $w^{(b)}$ for each
4. Average: $\bar{w} = \frac{1}{B} \sum_{b=1}^B w^{(b)}$

### 2. Properties


**Diversification**: Resampled portfolios are typically more diversified than single-estimate portfolios.

**Stability**: Small changes in data lead to small changes in weights.

**Critique**: Lacks axiomatic foundation; may be suboptimal in certain senses.

### 3. Bayesian Interpretation


**Connection**: Resampling approximates the Bayesian posterior mean portfolio:

$$
\bar{w} \approx \mathbb{E}[w^*(\mu, \Sigma) | \text{data}]
$$

where the expectation is over posterior parameter uncertainty.

## Factor Model Robustness


### 1. Factor Structure


**Model**: Returns follow:

$$
R = \alpha + B f + \epsilon
$$

where $f$ are factor returns, $B$ is the loading matrix, and $\epsilon$ is idiosyncratic risk.

**Covariance Decomposition**:

$$
\Sigma = B \Sigma_f B^\top + D
$$

where $\Sigma_f$ is factor covariance and $D$ is diagonal idiosyncratic covariance.

### 2. Robust Factor Investing


**Uncertainty in Loadings**: Consider:

$$
\mathcal{U}_B = \{B: \|B - \hat{B}\|_F \leq \delta_B\}
$$

**Robust Factor Tilt**:

$$
\max_w \min_{B \in \mathcal{U}_B} w^\top B \mathbb{E}[f] - \frac{\lambda}{2} w^\top (B \Sigma_f B^\top + D) w
$$

### 3. Estimation with Few Factors


**Dimensionality Reduction**: With $k \ll n$ factors:

- $n(n+1)/2$ covariance parameters reduced to $nk + k(k+1)/2 + n$
- More stable estimation
- Implicit regularization

## Dynamic Robust Portfolio


### 1. Multi-Period Setup


**Dynamics**: Wealth evolves as:

$$
W_{t+1} = W_t (1 + r_f + w_t^\top (R_t - r_f \mathbf{1}))
$$

**Robust Objective**:

$$
\max_{w_0, \ldots, w_{T-1}} \min_{P \in \mathcal{P}} \mathbb{E}_P[U(W_T)]
$$

### 2. Rectangularity


**Time Consistency**: For dynamic consistency, require **rectangular** ambiguity sets:

$$
\mathcal{P} = \{P: P_t(\cdot | \mathcal{F}_t) \in \mathcal{P}_t \text{ for all } t\}
$$

**Bellman Equation**:

$$
V_t(w) = \max_{w_t} \min_{P_t \in \mathcal{P}_t} \mathbb{E}_{P_t}[V_{t+1}(W_{t+1}) | \mathcal{F}_t]
$$

### 3. Model Predictive Control


**Rolling Horizon**: At each $t$:

1. Solve robust problem over horizon $[t, t+H]$
2. Implement $w_t^*$
3. Roll forward and repeat

**Advantages**: Adapts to changing market conditions while maintaining robustness.

## Empirical Performance


### 1. Out-of-Sample Tests


**Key Finding**: Robust portfolios typically outperform mean-variance portfolios out-of-sample despite lower in-sample Sharpe ratios.

**DeMiguel-Garlappi-Uppal (2009)**: The equally-weighted ($1/n$) portfolio often outperforms optimized portfolios due to estimation error.

### 2. Turnover Reduction


**Observation**: Robust portfolios exhibit lower turnover:

- Estimation errors that would cause rebalancing are absorbed by uncertainty sets
- Transaction cost savings can be substantial

### 3. Practical Guidelines


**Recommendations**:

1. Use factor models for covariance estimation
2. Shrink expected returns toward equilibrium or zero
3. Impose position limits and sector constraints
4. Re-estimate uncertainty sets periodically

## Summary


### Key Results


1. **SOCP Formulation**: Goldfarb-Iyengar enables efficient computation of robust portfolios

2. **Regularization Equivalence**: Robust optimization is equivalent to shrinkage/regularization

3. **Distributional Robustness**: Extends to ambiguity over entire distributions

4. **Black-Litterman**: Provides implicit robustness through Bayesian updating

### Practical Implications


1. **Parameter Uncertainty**: Explicitly model estimation error in optimization
2. **Diversification**: Robust approaches naturally produce diversified portfolios
3. **Stability**: Reduced sensitivity to small data changes
4. **Performance**: Better out-of-sample performance despite lower in-sample optimality

Robust portfolio optimization provides a principled framework for translating parameter uncertainty into improved investment decisions, bridging statistical estimation theory with portfolio construction.

---

## Exercises

**Exercise 1.** For a two-asset portfolio with estimated returns $\hat{\mu} = (0.08, 0.12)^\top$ and covariance $\hat{\Sigma} = \begin{pmatrix} 0.04 & 0.01 \\ 0.01 & 0.09 \end{pmatrix}$, compute the classical Markowitz portfolio and the robust portfolio under an ellipsoidal uncertainty set $\mathcal{U} = \{\mu : (\mu - \hat{\mu})^\top \hat{\Sigma}^{-1} (\mu - \hat{\mu}) \leq \kappa^2\}$ with $\kappa = 0.5$ and risk aversion $\lambda = 2$. Compare the two portfolios and explain why the robust portfolio is more conservative.

??? success "Solution to Exercise 1"
    **Classical Markowitz portfolio.**

    With $\hat{\mu} = (0.08, 0.12)^\top$, $\hat{\Sigma} = \begin{pmatrix} 0.04 & 0.01 \\ 0.01 & 0.09 \end{pmatrix}$, and $\lambda = 2$.

    First compute $\hat{\Sigma}^{-1}$. The determinant is $0.04 \times 0.09 - 0.01^2 = 0.0035$.

    $$
    \hat{\Sigma}^{-1} = \frac{1}{0.0035}\begin{pmatrix} 0.09 & -0.01 \\ -0.01 & 0.04 \end{pmatrix} = \begin{pmatrix} 25.714 & -2.857 \\ -2.857 & 11.429 \end{pmatrix}
    $$

    The unconstrained Markowitz solution (without budget constraint) is:

    $$
    w_{\text{MV}} = \frac{1}{\lambda}\hat{\Sigma}^{-1}\hat{\mu} = \frac{1}{2}\begin{pmatrix} 25.714 & -2.857 \\ -2.857 & 11.429 \end{pmatrix}\begin{pmatrix} 0.08 \\ 0.12 \end{pmatrix}
    $$

    $$
    = \frac{1}{2}\begin{pmatrix} 25.714 \times 0.08 + (-2.857) \times 0.12 \\ (-2.857) \times 0.08 + 11.429 \times 0.12 \end{pmatrix} = \frac{1}{2}\begin{pmatrix} 1.714 \\ 1.143 \end{pmatrix} = \begin{pmatrix} 0.857 \\ 0.571 \end{pmatrix}
    $$

    Total weight is $0.857 + 0.571 = 1.428$, so the portfolio uses leverage. If we impose a budget constraint $\mathbf{1}^\top w = 1$, we normalize:

    $$
    w_{\text{MV}} = \begin{pmatrix} 0.857/1.428 \\ 0.571/1.428 \end{pmatrix} = \begin{pmatrix} 0.600 \\ 0.400 \end{pmatrix}
    $$

    **Robust portfolio with ellipsoidal uncertainty.**

    The uncertainty set is $\mathcal{U} = \{\mu : (\mu - \hat{\mu})^\top \hat{\Sigma}^{-1}(\mu - \hat{\mu}) \leq \kappa^2\}$ with $\kappa = 0.5$ and $\Omega = \hat{\Sigma}$ (the shape matrix of the ellipsoid equals the covariance).

    The robust problem is:

    $$
    \max_w \left\{w^\top \hat{\mu} - \kappa\sqrt{w^\top \hat{\Sigma}\, w} - \frac{\lambda}{2}w^\top \hat{\Sigma}\, w\right\}
    $$

    **First-order condition.** Taking the derivative and setting it to zero:

    $$
    \hat{\mu} - \kappa \frac{\hat{\Sigma}\,w}{\sqrt{w^\top \hat{\Sigma}\, w}} - \lambda \hat{\Sigma}\, w = 0
    $$

    $$
    w = \frac{1}{\lambda}\hat{\Sigma}^{-1}\hat{\mu} - \frac{\kappa}{\lambda}\frac{w}{\sqrt{w^\top \hat{\Sigma}\, w}}
    $$

    This is a fixed-point equation. Notice that the robust solution has the form $w_{\text{robust}} = \alpha \cdot w_{\text{MV}}$ for some scalar $\alpha \in (0, 1)$ (since the penalty term is proportional to $w$). Substituting $w = \alpha w_{\text{MV}}^{(\text{unconstrained})}$:

    $$
    \alpha w_{\text{MV}} = w_{\text{MV}} - \frac{\kappa}{\lambda} \frac{\alpha w_{\text{MV}}}{\alpha \sqrt{w_{\text{MV}}^\top \hat{\Sigma}\, w_{\text{MV}}}}
    $$

    $$
    \alpha = 1 - \frac{\kappa}{\lambda \sqrt{w_{\text{MV}}^\top \hat{\Sigma}\, w_{\text{MV}}}}
    $$

    Compute $w_{\text{MV}}^\top \hat{\Sigma}\, w_{\text{MV}}$ using the unconstrained $w_{\text{MV}} = (0.857, 0.571)^\top$:

    $$
    \hat{\Sigma}\, w_{\text{MV}} = \begin{pmatrix} 0.04 \times 0.857 + 0.01 \times 0.571 \\ 0.01 \times 0.857 + 0.09 \times 0.571 \end{pmatrix} = \begin{pmatrix} 0.0400 \\ 0.0600 \end{pmatrix}
    $$

    $$
    w_{\text{MV}}^\top \hat{\Sigma}\, w_{\text{MV}} = 0.857 \times 0.0400 + 0.571 \times 0.0600 = 0.03428 + 0.03426 = 0.06854
    $$

    $$
    \sqrt{w_{\text{MV}}^\top \hat{\Sigma}\, w_{\text{MV}}} = 0.2618
    $$

    $$
    \alpha = 1 - \frac{0.5}{2 \times 0.2618} = 1 - \frac{0.5}{0.5236} = 1 - 0.955 = 0.045
    $$

    This gives an extreme shrinkage. Let us recompute more carefully. Note: the robust problem with $\Omega = \hat{\Sigma}$ uses $\sqrt{w^\top \hat{\Sigma} w}$, and the Markowitz unconstrained portfolio has risk $\sqrt{0.06854} = 26.18\%$. With $\kappa = 0.5$, the penalty $\kappa \sqrt{w^\top \hat{\Sigma} w} = 0.5 \times 0.2618 = 0.1309$ is large relative to the expected return $w^\top \hat{\mu} = 0.857 \times 0.08 + 0.571 \times 0.12 = 0.0686 + 0.0685 = 0.1371$, consuming almost all the return. This confirms substantial shrinkage.

    The robust portfolio weights are:

    $$
    w_{\text{robust}} = 0.045 \times \begin{pmatrix} 0.857 \\ 0.571 \end{pmatrix} = \begin{pmatrix} 0.039 \\ 0.026 \end{pmatrix}
    $$

    After normalizing to sum to 1 (if full investment is required):

    $$
    w_{\text{robust}} = \begin{pmatrix} 0.600 \\ 0.400 \end{pmatrix}
    $$

    The relative weights are identical to Markowitz (60/40), but the total risky allocation is only $6.5\%$, with $93.5\%$ in the risk-free asset.

    **Comparison.** The robust portfolio maintains the same relative allocation between assets (since the ellipsoidal penalty preserves the direction of the Markowitz solution) but dramatically reduces total exposure to risky assets. This is the hallmark of robustness: the penalty for estimation uncertainty reduces aggressiveness while preserving the structure of the optimal portfolio. The robust portfolio is more conservative because it explicitly accounts for the possibility that $\hat{\mu}$ overestimates true expected returns.

---

**Exercise 2.** Show that robust mean-variance optimization with a norm-bounded uncertainty set $\|\mu - \hat{\mu}\| \leq \delta$ is equivalent to a standard mean-variance problem with an adjusted risk aversion. Specifically, derive that the robust portfolio is $w^* = \frac{1}{\lambda}\Sigma^{-1}\hat{\mu} - \frac{\delta}{\lambda}\frac{\Sigma^{-1}\Sigma^{-1}\hat{\mu}}{\|\Sigma^{-1}\hat{\mu}\|}$ (under appropriate norm) and interpret the correction term as a shrinkage toward zero.

??? success "Solution to Exercise 2"
    **Setup.** The robust problem is:

    $$
    \max_w \left\{w^\top \hat{\mu} - \frac{\lambda}{2}w^\top \Sigma w\right\} \quad \text{subject to} \quad \|\mu - \hat{\mu}\| \leq \delta
    $$

    which is equivalent to:

    $$
    \max_w \min_{\|\mu - \hat{\mu}\| \leq \delta} \left\{w^\top \mu - \frac{\lambda}{2}w^\top \Sigma w\right\}
    $$

    **Worst-case analysis.** For a given $w$, the inner minimization over $\mu$:

    $$
    \min_{\|\mu - \hat{\mu}\| \leq \delta} w^\top \mu = w^\top \hat{\mu} - \delta \|w\|
    $$

    (by Cauchy-Schwarz, the minimum is achieved at $\mu^* = \hat{\mu} - \delta w / \|w\|$).

    For the $\ell_2$ norm, this uses $\|w\|_2$. The robust problem becomes:

    $$
    \max_w \left\{w^\top \hat{\mu} - \delta \|w\|_2 - \frac{\lambda}{2}w^\top \Sigma w\right\}
    $$

    **First-order condition.** Differentiating with respect to $w$:

    $$
    \hat{\mu} - \delta \frac{w}{\|w\|_2} - \lambda \Sigma w = 0
    $$

    $$
    w = \frac{1}{\lambda}\Sigma^{-1}\left(\hat{\mu} - \delta \frac{w}{\|w\|_2}\right)
    $$

    **Solving for the correction.** Let $w_{\text{MV}} = \frac{1}{\lambda}\Sigma^{-1}\hat{\mu}$ be the Markowitz solution. Then:

    $$
    w = w_{\text{MV}} - \frac{\delta}{\lambda}\frac{\Sigma^{-1}w}{\|w\|_2}
    $$

    Assuming $w$ is proportional to $w_{\text{MV}}$ (which holds when the correction is a scalar multiple), write $w = \alpha w_{\text{MV}}$:

    $$
    \alpha w_{\text{MV}} = w_{\text{MV}} - \frac{\delta}{\lambda}\frac{\Sigma^{-1}(\alpha w_{\text{MV}})}{\|\alpha w_{\text{MV}}\|_2}
    $$

    More generally, the exact solution is:

    $$
    w^* = \frac{1}{\lambda}\Sigma^{-1}\hat{\mu} - \frac{\delta}{\lambda}\frac{\Sigma^{-1}w^*}{\|w^*\|_2}
    $$

    When $\Sigma = \sigma^2 I$ (diagonal with equal variances), $\Sigma^{-1} = \sigma^{-2} I$ and:

    $$
    w^* = \frac{1}{\lambda \sigma^2}\hat{\mu} - \frac{\delta}{\lambda \sigma^2}\frac{w^*}{\|w^*\|_2}
    $$

    Since $w^*$ is proportional to $\hat{\mu}$, we get $w^*/\|w^*\| = \hat{\mu}/\|\hat{\mu}\|$, and:

    $$
    w^* = \frac{1}{\lambda \sigma^2}\hat{\mu} - \frac{\delta}{\lambda \sigma^2}\frac{\hat{\mu}}{\|\hat{\mu}\|} = \frac{1}{\lambda \sigma^2}\left(\hat{\mu} - \delta \frac{\hat{\mu}}{\|\hat{\mu}\|}\right)
    $$

    This is the Markowitz portfolio with a shrunk expected return:

    $$
    \tilde{\mu} = \hat{\mu} - \delta \frac{\hat{\mu}}{\|\hat{\mu}\|} = \hat{\mu}\left(1 - \frac{\delta}{\|\hat{\mu}\|}\right)
    $$

    For general $\Sigma$, the correction term $\frac{\delta}{\lambda}\frac{\Sigma^{-1}w^*}{\|w^*\|_2}$ acts as a shrinkage toward zero. Assets with large positions (high $|w_i^*|$) are shrunk more, and the direction of shrinkage is governed by $\Sigma^{-1}$, which amplifies the correction for correlated assets. This is equivalent to an increase in effective risk aversion from $\lambda$ to $\lambda + \delta / \sqrt{w^\top \Sigma w}$, demonstrating that robustness and conservatism are two faces of the same coin.

---

**Exercise 3.** The Goldfarb-Iyengar SOCP formulation recasts the robust portfolio problem as a second-order cone program. For the uncertainty set $\mathcal{U} = \{\mu : \|\mu - \hat{\mu}\|_2 \leq \delta\}$, write the robust problem $\max_w \{w^\top \hat{\mu} - \delta \|w\| - \frac{\lambda}{2}w^\top \hat{\Sigma} w\}$ and formulate it as an SOCP. Explain why this is computationally efficient.

??? success "Solution to Exercise 3"
    **The robust problem.** With uncertainty set $\mathcal{U} = \{\mu : \|\mu - \hat{\mu}\|_2 \leq \delta\}$:

    $$
    \max_w \left\{w^\top \hat{\mu} - \delta \|w\|_2 - \frac{\lambda}{2}w^\top \hat{\Sigma} w\right\}
    $$

    **SOCP reformulation.** Introduce auxiliary variables $t$ and $s$:

    $$
    \begin{aligned}
    \max_{w, t, s} \quad & t - \frac{\lambda}{2}s \\
    \text{s.t.} \quad & w^\top \hat{\mu} - \delta \|w\|_2 \geq t \\
    & w^\top \hat{\Sigma} w \leq s \\
    & \mathbf{1}^\top w = 1, \quad w \geq 0
    \end{aligned}
    $$

    The first constraint is equivalent to:

    $$
    w^\top \hat{\mu} - t \geq \delta \|w\|_2
    $$

    which is a **second-order cone constraint** (SOC): $\|w\|_2 \leq (w^\top \hat{\mu} - t)/\delta$, or in standard form:

    $$
    \left\|\begin{pmatrix} w \end{pmatrix}\right\|_2 \leq \frac{w^\top \hat{\mu} - t}{\delta}
    $$

    The second constraint $w^\top \hat{\Sigma} w \leq s$ can also be written as a SOC constraint. Factor $\hat{\Sigma} = L L^\top$ (Cholesky decomposition), then:

    $$
    \|L^\top w\|_2^2 \leq s \iff \|L^\top w\|_2 \leq \sqrt{s}
    $$

    which is a rotated second-order cone constraint: $(s, 1, L^\top w)$ belongs to a rotated SOC.

    **Why SOCP is computationally efficient.** Second-order cone programs are a subclass of convex optimization problems that can be solved by interior-point methods in polynomial time. Specifically:

    1. **Complexity:** $O(n^{3.5} \log(1/\epsilon))$ for $n$ variables to $\epsilon$-accuracy
    2. **Practical solvers:** MOSEK, Gurobi, CPLEX, and CVXPY all have highly optimized SOCP solvers
    3. **Scaling:** For portfolios with hundreds of assets, SOCP solves in seconds
    4. **No local minima:** Convexity guarantees the global optimum is found
    5. **Duality:** Strong duality holds, providing certificates of optimality and sensitivity analysis

    Compared to general nonlinear programming (which would be needed for arbitrary uncertainty set shapes), the SOCP structure enables reliable, fast computation. This is a key practical advantage of ellipsoidal uncertainty sets.

---

**Exercise 4.** Demonstrate the equivalence between robust optimization and regularization. Show that $\max_w \min_{\mu \in \mathcal{U}} w^\top \mu - \frac{\lambda}{2}w^\top \Sigma w$ is equivalent to $\max_w w^\top \hat{\mu} - \frac{\lambda}{2}w^\top \Sigma w - \delta \|w\|$ where the penalty $\delta \|w\|$ acts as a regularizer. What type of regularization (L1, L2, elastic net) arises from different shapes of the uncertainty set?

??? success "Solution to Exercise 4"
    **Equivalence between robust optimization and regularization.**

    **Step 1 — From robust to penalized.** The robust problem is:

    $$
    \max_w \min_{\mu \in \mathcal{U}} \left\{w^\top \mu - \frac{\lambda}{2}w^\top \Sigma w\right\}
    $$

    By the worst-case lemma, for any uncertainty set defined by a norm:

    $$
    \min_{\mu: \|\mu - \hat{\mu}\| \leq \delta} w^\top \mu = w^\top \hat{\mu} - \delta \|w\|_*
    $$

    where $\|\cdot\|_*$ is the **dual norm** of the norm defining the uncertainty set. Therefore:

    $$
    \max_w \left\{w^\top \hat{\mu} - \delta \|w\|_* - \frac{\lambda}{2}w^\top \Sigma w\right\}
    $$

    The penalty $\delta \|w\|_*$ acts as a regularizer.

    **Step 2 — Different uncertainty set shapes yield different regularizations.**

    | Uncertainty set norm | Dual norm on $w$ | Regularization type |
    |---------------------|-----------------|-------------------|
    | $\ell_2$: $\|\mu - \hat{\mu}\|_2 \leq \delta$ | $\|w\|_2$ | **L2 (Ridge)** regularization |
    | $\ell_\infty$: $\|\mu_i - \hat{\mu}_i\| \leq \delta_i$ | $\|w\|_1$ | **L1 (Lasso)** regularization |
    | $\ell_1$: $\sum_i |\mu_i - \hat{\mu}_i| \leq \delta$ | $\|w\|_\infty$ | **$L_\infty$** penalty (position limit) |
    | Ellipsoidal: $(\mu - \hat{\mu})^\top \Omega^{-1}(\mu - \hat{\mu}) \leq \delta^2$ | $\sqrt{w^\top \Omega w}$ | **Mahalanobis** (weighted L2) |

    **Step 3 — Detailed analysis for each case.**

    **L2 (Ridge) from $\ell_2$ uncertainty:** The penalized problem $\max_w \{w^\top \hat{\mu} - \delta \|w\|_2 - \frac{\lambda}{2}w^\top \Sigma w\}$ is equivalent to:

    $$
    \max_w \left\{w^\top \hat{\mu} - \frac{\lambda}{2}w^\top (\Sigma + \gamma I) w\right\}
    $$

    for appropriate $\gamma = \gamma(\delta)$. This adds a multiple of the identity to the covariance, shrinking eigenvalues toward a common value. Solution: $w = \frac{1}{\lambda}(\Sigma + \gamma I)^{-1}\hat{\mu}$.

    **L1 (Lasso) from box uncertainty:** When each component of $\mu$ has independent uncertainty $|\mu_i - \hat{\mu}_i| \leq \delta_i$, the worst case gives $\min_\mu w^\top \mu = w^\top \hat{\mu} - \sum_i \delta_i |w_i|$. The penalty $\sum_i \delta_i |w_i|$ promotes **sparsity** --- assets with high estimation uncertainty ($\delta_i$ large) are driven to zero weight. This produces portfolios that concentrate on a few well-understood assets.

    **Elastic net from mixed uncertainty:** An uncertainty set combining $\ell_1$ and $\ell_2$ constraints produces a penalty $\alpha \|w\|_1 + (1-\alpha)\|w\|_2$, which is exactly the elastic net regularizer. This provides a compromise between sparsity (L1) and shrinkage (L2).

    **Key insight:** The choice of uncertainty set shape is equivalent to choosing a regularization strategy. Practitioners can select the uncertainty set geometry to match their desired portfolio properties (diversification, sparsity, position limits) rather than thinking directly about regularization.

---

**Exercise 5.** In distributionally robust portfolio optimization, the uncertainty is over the entire return distribution, not just the mean. For a Wasserstein ball of radius $\varepsilon$ around the empirical distribution, formulate the problem $\min_w \sup_{P \in \mathcal{P}_W(\varepsilon)} \text{CVaR}_{0.95}^P(-w^\top R)$. Explain why this provides protection against both parameter estimation error and model misspecification.

??? success "Solution to Exercise 5"
    **Distributionally robust CVaR formulation.**

    **Setup.** The Wasserstein ball of radius $\varepsilon$ around the empirical distribution $\hat{P}_n$ is:

    $$
    \mathcal{P}_W(\varepsilon) = \{P : W_1(P, \hat{P}_n) \leq \varepsilon\}
    $$

    where $W_1$ is the type-1 Wasserstein (earth mover's) distance. The problem is:

    $$
    \min_w \sup_{P \in \mathcal{P}_W(\varepsilon)} \text{CVaR}_{0.95}^P(-w^\top R)
    $$

    This minimizes the worst-case CVaR of portfolio losses over all distributions within Wasserstein distance $\varepsilon$ of the empirical distribution.

    **Tractable reformulation.** By the Zhu-Fukushima (2009) result for Wasserstein distributional robustness:

    $$
    \sup_{P: W_1(P, \hat{P}_n) \leq \varepsilon} \text{CVaR}_{\alpha}^P(L) = \text{CVaR}_{\alpha}^{\hat{P}_n}(L) + \frac{\varepsilon \cdot \text{Lip}(L)}{\alpha}
    $$

    where $\text{Lip}(L)$ is the Lipschitz constant of the loss function $L(R) = -w^\top R$. Since $\text{Lip}(-w^\top R) = \|w\|_*$ (the dual norm of the return space norm), the problem becomes:

    $$
    \min_w \left\{\text{CVaR}_{0.05}^{\hat{P}_n}(-w^\top R) + \frac{\varepsilon \|w\|_*}{0.05}\right\}
    $$

    For the $\ell_2$ norm: $\|w\|_* = \|w\|_2$, giving:

    $$
    \min_w \left\{\text{CVaR}_{0.05}^{\hat{P}_n}(-w^\top R) + 20\varepsilon \|w\|_2\right\}
    $$

    The empirical CVaR can be computed using the Rockafellar-Uryasev linear programming formulation:

    $$
    \text{CVaR}_{0.05}^{\hat{P}_n}(-w^\top R) = \min_\eta \left\{\eta + \frac{1}{0.05 \cdot n}\sum_{i=1}^n \max(-w^\top R_i - \eta, 0)\right\}
    $$

    Combining, the full problem is a second-order cone program.

    **Why this provides dual protection.**

    1. **Parameter estimation error:** The empirical distribution $\hat{P}_n$ is based on finite data, so the true distribution $P^*$ is unknown. The Wasserstein ball contains $P^*$ with high probability when $\varepsilon = O(n^{-1/d})$ (where $d$ is the dimension). The worst-case CVaR therefore provides a valid upper bound on the true CVaR.

    2. **Model misspecification:** Unlike parametric approaches (which assume, say, Gaussian returns), the Wasserstein formulation makes no distributional assumptions. The ball $\mathcal{P}_W(\varepsilon)$ contains distributions with fat tails, skewness, and other features absent from the empirical distribution but possibly present in reality. The worst-case optimization hedges against these possibilities.

    3. **Regularization effect:** The penalty $\varepsilon \|w\|_* / \alpha$ regularizes the portfolio, preventing concentration in positions that would be vulnerable to distributional shift. The regularization strength scales inversely with $\alpha$ (more regularization for more extreme risk measures) and proportionally with $\varepsilon$ (more regularization for larger uncertainty).

    The result is a portfolio that is robust to both the sampling noise inherent in historical data and to structural model misspecification --- a stronger guarantee than either parametric robust optimization or standard CVaR optimization alone.

---

**Exercise 6.** The Black-Litterman model can be viewed as an implicit form of robust optimization. Starting from equilibrium returns $\Pi = \lambda \Sigma w_{\text{mkt}}$, show that incorporating views $Q\mu = q + \epsilon$ with $\epsilon \sim N(0, \Omega)$ is equivalent to solving a regularized optimization problem where the regularizer penalizes deviation from equilibrium. Compute the Black-Litterman portfolio for $\tau = 0.05$, and compare it with the robust portfolio from Exercise 1.

??? success "Solution to Exercise 6"
    **Part 1: Black-Litterman as regularized optimization.**

    **Setup.** Equilibrium returns: $\Pi = \lambda \Sigma w_{\text{mkt}}$. Views: $Q\mu = q + \epsilon$, $\epsilon \sim N(0, \Omega)$. Prior: $\mu \sim N(\Pi, \tau \Sigma)$.

    The Black-Litterman posterior mean is:

    $$
    \hat{\mu}_{\text{BL}} = \left[(\tau\Sigma)^{-1} + Q^\top \Omega^{-1} Q\right]^{-1}\left[(\tau\Sigma)^{-1}\Pi + Q^\top \Omega^{-1}q\right]
    $$

    **Regularization interpretation.** The posterior mean $\hat{\mu}_{\text{BL}}$ minimizes the following quadratic objective:

    $$
    \hat{\mu}_{\text{BL}} = \arg\min_\mu \left\{\frac{1}{2}(\mu - \Pi)^\top (\tau\Sigma)^{-1}(\mu - \Pi) + \frac{1}{2}(Q\mu - q)^\top \Omega^{-1}(Q\mu - q)\right\}
    $$

    The first term, $\frac{1}{2}(\mu - \Pi)^\top (\tau\Sigma)^{-1}(\mu - \Pi)$, is a **regularizer** penalizing deviation from the equilibrium returns $\Pi$. It is a Mahalanobis-distance regularizer with shape matrix $(\tau\Sigma)^{-1}$. The second term is the data-fitting (view-matching) term.

    **Connection to portfolio optimization.** When we plug $\hat{\mu}_{\text{BL}}$ into the portfolio problem $w^* = \frac{1}{\lambda}(\Sigma + \hat{\Sigma}_{\text{BL}})^{-1}\hat{\mu}_{\text{BL}}$, the portfolio can be written as:

    $$
    w_{\text{BL}}^* = w_{\text{mkt}} + \text{tilt toward views}
    $$

    The "tilt toward views" is penalized by the regularizer: larger deviations from equilibrium (larger $\|\mu - \Pi\|_{(\tau\Sigma)^{-1}}$) incur a larger penalty, preventing extreme tilts. This is precisely the mechanism of regularized optimization, where the regularizer prevents overfitting to noisy signals (views).

    **Part 2: Computing the BL portfolio for $\tau = 0.05$.**

    Using the data from Exercise 1: $\hat{\mu} = (0.08, 0.12)^\top$, $\Sigma = \begin{pmatrix} 0.04 & 0.01 \\ 0.01 & 0.09 \end{pmatrix}$, $\lambda = 2$.

    **Step 1 — Market weights.** Assume $w_{\text{mkt}} = (0.6, 0.4)^\top$ (given or inferred).

    **Step 2 — Equilibrium returns:**

    $$
    \Pi = \lambda \Sigma w_{\text{mkt}} = 2 \begin{pmatrix} 0.04 & 0.01 \\ 0.01 & 0.09 \end{pmatrix}\begin{pmatrix} 0.6 \\ 0.4 \end{pmatrix} = 2\begin{pmatrix} 0.028 \\ 0.042 \end{pmatrix} = \begin{pmatrix} 0.056 \\ 0.084 \end{pmatrix}
    $$

    **Step 3 — Views.** Suppose the investor has no explicit active views (i.e., $Q$ is empty). Then:

    $$
    \hat{\mu}_{\text{BL}} = \Pi = (0.056, 0.084)^\top
    $$

    and the BL portfolio is simply $w_{\text{BL}} = w_{\text{mkt}} = (0.6, 0.4)^\top$.

    Now suppose the investor has a single view: "Asset 2 will return 12%" (absolute view). Then $Q = (0, 1)$, $q = 0.12$, and $\Omega = (\omega^2)$ for some view uncertainty. Using $\omega^2 = \tau Q \Sigma Q^\top = 0.05 \times 0.09 = 0.0045$ (Idzorek proportional method):

    $$
    \tau \Sigma = 0.05 \begin{pmatrix} 0.04 & 0.01 \\ 0.01 & 0.09 \end{pmatrix} = \begin{pmatrix} 0.002 & 0.0005 \\ 0.0005 & 0.0045 \end{pmatrix}
    $$

    Using the alternative form:

    $$
    \hat{\mu}_{\text{BL}} = \Pi + \tau \Sigma Q^\top (Q \tau \Sigma Q^\top + \Omega)^{-1}(q - Q\Pi)
    $$

    $$
    Q\Pi = 0.084, \quad q - Q\Pi = 0.12 - 0.084 = 0.036
    $$

    $$
    Q \tau \Sigma Q^\top = 0.0045, \quad \Omega = 0.0045
    $$

    $$
    (Q\tau\Sigma Q^\top + \Omega)^{-1} = (0.009)^{-1} = 111.11
    $$

    $$
    \tau \Sigma Q^\top = \begin{pmatrix} 0.0005 \\ 0.0045 \end{pmatrix}
    $$

    $$
    \hat{\mu}_{\text{BL}} = \begin{pmatrix} 0.056 \\ 0.084 \end{pmatrix} + \begin{pmatrix} 0.0005 \\ 0.0045 \end{pmatrix} \times 111.11 \times 0.036 = \begin{pmatrix} 0.056 \\ 0.084 \end{pmatrix} + \begin{pmatrix} 0.002 \\ 0.018 \end{pmatrix} = \begin{pmatrix} 0.058 \\ 0.102 \end{pmatrix}
    $$

    The BL portfolio (ignoring posterior covariance for simplicity):

    $$
    w_{\text{BL}} = \frac{1}{2}\Sigma^{-1}\hat{\mu}_{\text{BL}} = \frac{1}{2}\begin{pmatrix} 25.714 & -2.857 \\ -2.857 & 11.429 \end{pmatrix}\begin{pmatrix} 0.058 \\ 0.102 \end{pmatrix}
    $$

    $$
    = \frac{1}{2}\begin{pmatrix} 1.200 \\ 1.000 \end{pmatrix} = \begin{pmatrix} 0.600 \\ 0.500 \end{pmatrix}
    $$

    Normalizing to sum to 1: $w_{\text{BL}} = (0.545, 0.455)^\top$.

    **Part 3: Comparison.**

    | | Asset 1 | Asset 2 |
    |---|---------|---------|
    | Markowitz (Exercise 1) | 60.0% | 40.0% |
    | BL (with view on Asset 2) | 54.5% | 45.5% |
    | Robust (Exercise 1, $\kappa = 0.5$) | 60.0% | 40.0% (scaled down) |

    The Black-Litterman portfolio shifts weight toward Asset 2 (reflecting the bullish view) while staying close to equilibrium weights. The robust portfolio maintains the Markowitz proportions but scales down total risky exposure. Both approaches avoid the extreme positions that pure plug-in optimization might produce, but through different mechanisms: BL uses Bayesian shrinkage toward equilibrium, while robust optimization uses worst-case penalization. The BL approach is more natural when the investor has explicit views; the robust approach is more natural when the investor wants protection against estimation error without specifying particular beliefs.
