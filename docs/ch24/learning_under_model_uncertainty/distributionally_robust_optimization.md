# Distributionally Robust Optimization

**Distributionally robust optimization (DRO)** hedges against model uncertainty by optimizing worst-case expected performance over an **ambiguity set** of plausible probability distributions. Rather than committing to a single model $\mathbb{P}$ (which may be misspecified) or preparing for the absolute worst case (which is overly conservative), DRO restricts the adversary to distributions "close" to a reference model, interpolating between stochastic optimization and robust optimization. The framework is particularly natural for finance, where model uncertainty is pervasive and the consequences of misspecification are severe.

---

## The DRO Framework

### General Formulation

**Definition (DRO Problem).** Given a decision variable $x \in \mathcal{X}$, a loss function $\ell(x, \xi)$ depending on an uncertain parameter $\xi$, and an ambiguity set $\mathcal{P}$ of probability distributions on $\xi$, the DRO problem is:

$$
\min_{x \in \mathcal{X}} \sup_{\mathbb{P} \in \mathcal{P}} \mathbb{E}_{\mathbb{P}}[\ell(x, \xi)]
$$

The inner supremum computes the worst-case expected loss over all distributions in $\mathcal{P}$; the outer minimization finds the decision that performs best under this worst case.

### Relation to Other Frameworks

DRO sits between two extremes:

**Stochastic optimization** ($\mathcal{P} = \{\hat{\mathbb{P}}\}$, a singleton):

$$
\min_{x \in \mathcal{X}} \mathbb{E}_{\hat{\mathbb{P}}}[\ell(x, \xi)]
$$

Optimal for $\hat{\mathbb{P}}$ but fragile to misspecification.

**Robust optimization** ($\mathcal{P}$ is all distributions on the support):

$$
\min_{x \in \mathcal{X}} \sup_{\xi \in \Xi} \ell(x, \xi)
$$

Immune to distributional error but often overly conservative.

DRO provides a principled middle ground. The size of $\mathcal{P}$ controls the robustness-performance trade-off.

---

## Ambiguity Set Constructions

### Moment-Based Ambiguity Sets

**Definition.** The moment ambiguity set constrains the first and second moments:

$$
\mathcal{P}_{\text{mom}} = \left\{\mathbb{P} : \mathbb{E}_\mathbb{P}[\xi] = \mu, \; \mathbb{E}_\mathbb{P}[\xi\xi^\top] \preceq \Sigma \right\}
$$

or more generally, with moment inequalities:

$$
\mathcal{P}_{\text{mom}} = \left\{\mathbb{P} : \mathbb{E}_\mathbb{P}[\xi] \in \mathcal{M}_1, \; \text{Cov}_\mathbb{P}(\xi) \preceq \Sigma_{\max} \right\}
$$

**Theorem (Scarf 1958).** For portfolio optimization with loss $\ell(x, \xi) = -x^\top \xi$ and the moment ambiguity set $\{\mathbb{P} : \mathbb{E}[\xi] = \mu, \text{Cov}(\xi) = \Sigma\}$, the DRO problem:

$$
\min_{x} \max_{\mathbb{P} \in \mathcal{P}_{\text{mom}}} \mathbb{E}_\mathbb{P}[-x^\top \xi] + \lambda \, \text{Var}_\mathbb{P}(x^\top \xi)
$$

has a closed-form solution related to the mean-variance portfolio with an additional robustness penalty.

### Wasserstein Ambiguity Sets

**Definition (Wasserstein Distance).** The type-$p$ Wasserstein distance between distributions $\mathbb{P}$ and $\mathbb{Q}$ is:

$$
W_p(\mathbb{P}, \mathbb{Q}) = \left(\inf_{\pi \in \Pi(\mathbb{P}, \mathbb{Q})} \int \|x - y\|^p \, d\pi(x, y)\right)^{1/p}
$$

where $\Pi(\mathbb{P}, \mathbb{Q})$ is the set of all couplings (joint distributions with marginals $\mathbb{P}$ and $\mathbb{Q}$).

**Definition (Wasserstein Ambiguity Set).** Given a reference distribution $\hat{\mathbb{P}}_n$ (typically the empirical distribution from $n$ data points) and radius $\varepsilon > 0$:

$$
\mathcal{P}_W = \left\{\mathbb{P} : W_p(\mathbb{P}, \hat{\mathbb{P}}_n) \leq \varepsilon\right\}
$$

This is a ball of radius $\varepsilon$ around $\hat{\mathbb{P}}_n$ in Wasserstein space.

!!! tip "Why Wasserstein?"
    Unlike moment-based or $f$-divergence ambiguity sets, the Wasserstein ball:

    - Includes distributions with different support than $\hat{\mathbb{P}}_n$ (important for tail risk)
    - Has a natural geometric interpretation (cost of transporting mass)
    - Leads to tractable reformulations for many loss functions
    - Provides finite-sample performance guarantees

---

## Tractable Reformulations

### Wasserstein DRO Duality

**Theorem (Strong Duality -- Blanchet & Murthy 2019).** For the type-1 Wasserstein DRO problem with loss $\ell(x, \xi)$ that is $L$-Lipschitz in $\xi$:

$$
\sup_{\mathbb{P}: W_1(\mathbb{P}, \hat{\mathbb{P}}_n) \leq \varepsilon} \mathbb{E}_\mathbb{P}[\ell(x, \xi)] = \inf_{\lambda \geq 0} \left\{\lambda \varepsilon + \frac{1}{n}\sum_{i=1}^n \sup_{\xi} \left[\ell(x, \xi) - \lambda \|\xi - \hat{\xi}_i\|\right]\right\}
$$

where $\hat{\xi}_1, \ldots, \hat{\xi}_n$ are the data points.

The dual variable $\lambda$ acts as a **Lagrange multiplier** controlling the trade-off between robustness (large $\varepsilon$) and performance (small $\varepsilon$).

### Connection to Regularization

**Theorem (Wasserstein DRO as Regularization).** For linear loss $\ell(x, \xi) = \xi^\top x$ and type-1 Wasserstein ball with $\ell_q$-norm transport cost:

$$
\sup_{\mathbb{P}: W_1(\mathbb{P}, \hat{\mathbb{P}}_n) \leq \varepsilon} \mathbb{E}_\mathbb{P}[\xi^\top x] = \frac{1}{n}\sum_{i=1}^n \hat{\xi}_i^\top x + \varepsilon \|x\|_p
$$

where $1/p + 1/q = 1$.

This reveals that Wasserstein DRO with linear loss is equivalent to **norm regularization**:

- $q = 2$ (Euclidean transport) $\implies$ $\ell_2$ regularization (Ridge)
- $q = \infty$ ($\ell_\infty$ transport) $\implies$ $\ell_1$ regularization (LASSO)

This provides a robustness interpretation of regularization: Ridge regression is the DRO-optimal estimator when the true distribution lies within a Wasserstein ball around the empirical distribution.

---

## DRO for Portfolio Optimization

### Mean-Variance with Distributional Robustness

Consider a portfolio $x \in \mathbb{R}^d$ with $\mathbf{1}^\top x = 1$, $x \geq 0$, and return $R = \xi^\top x$. The distributionally robust mean-variance problem:

$$
\min_{x \in \mathcal{X}} \sup_{\mathbb{P} \in \mathcal{P}} \left\{-\mathbb{E}_\mathbb{P}[R] + \frac{\gamma}{2}\text{Var}_\mathbb{P}(R)\right\}
$$

### Moment-Based DRO Portfolio

With $\mathcal{P} = \{\mathbb{P} : \mathbb{E}[\xi] \in \mathcal{E}_\mu, \; \text{Cov}(\xi) \preceq \Sigma_{\max}\}$:

$$
\min_{x \in \mathcal{X}} \left\{-\min_{\mu \in \mathcal{E}_\mu} \mu^\top x + \frac{\gamma}{2} x^\top \Sigma_{\max} x\right\}
$$

If $\mathcal{E}_\mu = \{\mu : \|\mu - \hat{\mu}\|_2 \leq \delta\}$ (ellipsoidal uncertainty in the mean):

$$
= \min_{x \in \mathcal{X}} \left\{-\hat{\mu}^\top x + \delta\|x\|_2 + \frac{\gamma}{2}x^\top \Sigma_{\max} x\right\}
$$

The term $\delta\|x\|_2$ penalizes portfolios that are sensitive to mean estimation error, naturally shrinking toward equal-weighted or minimum-variance portfolios.

### Wasserstein DRO Portfolio

**Theorem (Wasserstein Robust Portfolio -- Esfahani & Kuhn 2018).** For the type-2 Wasserstein DRO problem with quadratic loss:

$$
\sup_{\mathbb{P}: W_2(\mathbb{P}, \hat{\mathbb{P}}_n) \leq \varepsilon} \mathbb{E}_\mathbb{P}[-x^\top \xi + \frac{\gamma}{2}(x^\top \xi)^2]
$$

the worst-case distribution shifts mass outward from the empirical distribution, inflating the variance. The resulting optimization is a semidefinite program (SDP) or a tractable convex problem.

---

## DRO for Risk Management

### Worst-Case CVaR

The distributionally robust CVaR:

$$
\sup_{\mathbb{P} \in \mathcal{P}} \text{CVaR}_\alpha^{\mathbb{P}}(L) = \sup_{\mathbb{P} \in \mathcal{P}} \inf_{t \in \mathbb{R}} \left\{t + \frac{1}{\alpha}\mathbb{E}_\mathbb{P}[(L - t)^+]\right\}
$$

For moment-based ambiguity sets, this reduces to a second-order cone program (SOCP).

**Proposition.** With mean-variance ambiguity set $\mathcal{P} = \{\mathbb{P} : \mathbb{E}[L] = \mu, \text{Var}(L) \leq \sigma^2\}$:

$$
\sup_{\mathbb{P} \in \mathcal{P}} \text{CVaR}_\alpha(L) = \mu + \sigma\sqrt{\frac{1-\alpha}{\alpha}}
$$

This is a Chebyshev-type bound: the worst-case CVaR depends only on the first two moments, providing a conservative but model-free risk estimate.

### Stress Testing Interpretation

DRO provides a principled approach to stress testing. The worst-case distribution $\mathbb{P}^*$ achieving the supremum represents the **most adverse scenario** consistent with the ambiguity set. Examining $\mathbb{P}^*$ reveals:

- Which tails are most dangerous
- How correlations shift under stress
- Which risk factors drive worst-case losses

This is more informative than ad-hoc scenario construction.

---

## Finite-Sample Guarantees

### Concentration of the Wasserstein Distance

**Theorem (Fournier & Guillin 2015).** Let $\hat{\mathbb{P}}_n$ be the empirical distribution from $n$ i.i.d. samples from $\mathbb{P}^*$. Then for $p \geq 1$ and dimension $d$:

$$
\mathbb{P}\!\left(W_p(\hat{\mathbb{P}}_n, \mathbb{P}^*) > \varepsilon\right) \leq C \exp(-c \, n \varepsilon^{\max(d, 2)})
$$

for constants $C, c$ depending on $d$ and the moments of $\mathbb{P}^*$.

### Out-of-Sample Performance Guarantee

**Corollary.** If the radius $\varepsilon_n$ is chosen such that $\mathbb{P}^* \in \mathcal{P}_W(\hat{\mathbb{P}}_n, \varepsilon_n)$ with probability at least $1 - \beta$, then the DRO solution $x^*_n$ satisfies:

$$
\mathbb{E}_{\mathbb{P}^*}[\ell(x_n^*, \xi)] \leq \sup_{\mathbb{P} \in \mathcal{P}_W} \mathbb{E}_\mathbb{P}[\ell(x_n^*, \xi)]
$$

with probability at least $1 - \beta$. The DRO objective provides an **upper confidence bound** on the true out-of-sample performance.

This is a key advantage over standard empirical risk minimization, which provides no finite-sample guarantees on out-of-sample performance.

---

## Example: Robust Factor Portfolio

Consider constructing a portfolio using $k$ factor signals $f_1, \ldots, f_k$ to predict returns $r_{t+1}$. The predictive model:

$$
\hat{r}_{t+1} = \beta^\top f_t
$$

has estimated coefficients $\hat{\beta}$ from historical data. The standard mean-variance portfolio:

$$
x^{\text{MV}} = \frac{1}{\gamma}\hat{\Sigma}^{-1}\hat{\mu}
$$

is notoriously sensitive to estimation error in $\hat{\mu}$ (the mean return estimates).

The DRO portfolio with Wasserstein ball of radius $\varepsilon$:

$$
x^{\text{DRO}} = \arg\min_{x \in \mathcal{X}} \left\{-\hat{\mu}^\top x + \varepsilon\|x\|_2 + \frac{\gamma}{2}x^\top \hat{\Sigma} x\right\}
$$

The robustness penalty $\varepsilon\|x\|_2$ acts as an $\ell_2$ shrinkage on portfolio weights, reducing sensitivity to mean estimation error. Empirically, $x^{\text{DRO}}$ interpolates between the standard mean-variance portfolio ($\varepsilon = 0$) and the minimum-variance portfolio ($\varepsilon \to \infty$), with optimal $\varepsilon$ selected by cross-validation or the finite-sample guarantee.

---

## Key Takeaways

1. **DRO optimizes worst-case expected performance** over an ambiguity set of distributions, providing a principled framework for decision-making under model uncertainty.

2. **Wasserstein ambiguity sets** lead to tractable reformulations and have a natural connection to **regularization**: Wasserstein DRO with linear loss is equivalent to norm-penalized estimation.

3. **Moment-based ambiguity sets** yield SOCP and SDP reformulations, applicable to portfolio optimization and risk management.

4. **Finite-sample guarantees** ensure that the DRO solution performs well out-of-sample with high probability, unlike standard empirical optimization.

5. In finance, DRO naturally addresses **estimation error in mean returns**, producing portfolios that are more robust and often outperform classical mean-variance optimization out-of-sample.

---

## Further Reading

- Esfahani & Kuhn (2018), "Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric"
- Blanchet & Murthy (2019), "Quantifying Distributional Model Risk via Optimal Transport"
- Delage & Ye (2010), "Distributionally Robust Optimization Under Moment Uncertainty"
- Fournier & Guillin (2015), "On the Rate of Convergence in Wasserstein Distance"
- Pflug & Wozabal (2007), "Ambiguity in Portfolio Selection"

---

## Exercises

**Exercise 1.** Consider a portfolio with two assets and return vector $\xi \sim \mathbb{P}$. The moment-based ambiguity set is $\mathcal{P} = \{\mathbb{P} : \mathbb{E}[\xi] = \mu, \; \text{Cov}(\xi) = \Sigma\}$ with $\mu = (0.08, 0.05)^\top$ and $\Sigma = \begin{pmatrix} 0.04 & 0.01 \\ 0.01 & 0.02 \end{pmatrix}$. The worst-case CVaR under this ambiguity set is $\text{CVaR}_\alpha^{\text{wc}} = \mu_L + \sigma_L \sqrt{(1-\alpha)/\alpha}$ where $\mu_L = -x^\top \mu$ and $\sigma_L^2 = x^\top \Sigma x$ for portfolio loss $L = -x^\top \xi$. (a) For the equal-weighted portfolio $x = (0.5, 0.5)^\top$ and $\alpha = 0.05$, compute the worst-case CVaR. (b) Compare this with the Gaussian CVaR using $\text{CVaR}_\alpha = \mu_L + \sigma_L \frac{\phi(\Phi^{-1}(\alpha))}{\alpha}$. Which is more conservative, and by how much?

---

**Exercise 2.** For linear loss $\ell(x, \xi) = \xi^\top x$ and type-1 Wasserstein ball with $\ell_2$-norm transport cost, the DRO problem reduces to

$$
\min_{x \in \mathcal{X}} \left\{\frac{1}{n}\sum_{i=1}^n \hat{\xi}_i^\top x + \varepsilon \|x\|_2\right\}
$$

(a) Show that this is equivalent to Ridge-penalized optimization. (b) If the transport cost uses the $\ell_\infty$-norm instead, show that the regularization becomes $\varepsilon \|x\|_1$ (LASSO). (c) For a factor model with $k = 20$ factors, $n = 60$ monthly observations, and $\varepsilon = 0.05$, discuss which norm choice ($\ell_1$ vs $\ell_2$) produces sparser and more interpretable portfolio weights.

---

**Exercise 3.** The Wasserstein distance between the empirical distribution $\hat{\mathbb{P}}_n$ and the true distribution $\mathbb{P}^*$ satisfies $\mathbb{P}(W_p(\hat{\mathbb{P}}_n, \mathbb{P}^*) > \varepsilon) \le C \exp(-c \, n \varepsilon^{\max(d,2)})$. (a) For $d = 5$ asset returns and $n = 250$ daily observations, find the radius $\varepsilon$ such that $\mathbb{P}^* \in \mathcal{P}_W$ with probability at least 95%. (b) Explain the curse of dimensionality: how does the required $\varepsilon$ scale with $d$ for fixed $n$ and confidence level? (c) Discuss why this concentration result is important for calibrating the ambiguity set radius in practice.

---

**Exercise 4.** Compare the DRO robust factor portfolio $x^{\text{DRO}} = \arg\min_{x \in \mathcal{X}} \{-\hat{\mu}^\top x + \varepsilon\|x\|_2 + \frac{\gamma}{2} x^\top \hat{\Sigma} x\}$ with the standard mean-variance portfolio $x^{\text{MV}} = \frac{1}{\gamma}\hat{\Sigma}^{-1}\hat{\mu}$. (a) Derive the first-order optimality condition for $x^{\text{DRO}}$ and show how the robustness parameter $\varepsilon$ shrinks the portfolio weights. (b) Show that as $\varepsilon \to \infty$, $x^{\text{DRO}}$ converges to the minimum-variance portfolio. (c) Using simulated data with $d = 10$ assets, true Sharpe ratio 0.5, and $n = 120$ observations, argue why $x^{\text{DRO}}$ typically outperforms $x^{\text{MV}}$ out-of-sample due to estimation error in $\hat{\mu}$.

---

**Exercise 5.** The strong duality result for type-1 Wasserstein DRO states

$$
\sup_{\mathbb{P}: W_1(\mathbb{P}, \hat{\mathbb{P}}_n) \le \varepsilon} \mathbb{E}_\mathbb{P}[\ell(x, \xi)] = \inf_{\lambda \ge 0} \left\{\lambda \varepsilon + \frac{1}{n}\sum_{i=1}^n \sup_\xi [\ell(x, \xi) - \lambda \|\xi - \hat{\xi}_i\|]\right\}
$$

(a) Interpret the dual variable $\lambda$ as the sensitivity of the worst-case loss to the ambiguity radius $\varepsilon$. (b) For the loss $\ell(x, \xi) = (-x^\top \xi)^+$ (portfolio shortfall), show that the inner supremum is finite only when $\lambda$ is large enough relative to $\|x\|$. (c) Explain why this duality converts an infinite-dimensional optimization (over distributions) into a finite-dimensional convex program.

---

**Exercise 6.** A risk manager uses DRO to stress test a portfolio. The worst-case distribution $\mathbb{P}^*$ achieving $\sup_{\mathbb{P} \in \mathcal{P}} \text{CVaR}_\alpha^\mathbb{P}(L)$ represents the most adverse scenario consistent with the ambiguity set. (a) For a moment-based ambiguity set, describe the structure of $\mathbb{P}^*$ (hint: it is a discrete distribution supported on at most $d+1$ points by Richter's theorem). (b) Compare this principled worst-case approach with ad-hoc stress scenarios. (c) A portfolio has 3 risk factors. The worst-case distribution places mass on 4 points. Explain how examining these points reveals which tail events and correlation structures drive the worst-case risk.

---

**Exercise 7.** A quantitative fund uses cross-validation to select the Wasserstein radius $\varepsilon$. The data consists of 120 monthly returns for 50 assets. (a) Describe a time-series cross-validation procedure (rolling window) for selecting $\varepsilon$, being careful to avoid look-ahead bias. (b) Plot the expected out-of-sample Sharpe ratio as a function of $\varepsilon$: at $\varepsilon = 0$ (standard mean-variance) performance is poor due to estimation error; at $\varepsilon$ too large, performance is poor due to excessive conservatism. Explain this U-shaped curve. (c) Discuss whether the optimal $\varepsilon$ is stable over time or should be adapted to market conditions (e.g., larger $\varepsilon$ during high-volatility regimes).
