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

??? success "Solution to Exercise 1"
    **(a)** For the equal-weighted portfolio $x = (0.5, 0.5)^\top$ with $\mu = (0.08, 0.05)^\top$ and $\Sigma = \begin{pmatrix} 0.04 & 0.01 \\ 0.01 & 0.02 \end{pmatrix}$:

    The portfolio loss is $L = -x^\top \xi$, so:

    $$
    \mu_L = -x^\top \mu = -(0.5 \times 0.08 + 0.5 \times 0.05) = -0.065
    $$

    $$
    \sigma_L^2 = x^\top \Sigma x = (0.5, 0.5) \begin{pmatrix} 0.04 & 0.01 \\ 0.01 & 0.02 \end{pmatrix} \begin{pmatrix} 0.5 \\ 0.5 \end{pmatrix} = (0.5)(0.025) + (0.5)(0.015) = 0.02
    $$

    so $\sigma_L = \sqrt{0.02} = 0.1414$.

    The worst-case CVaR at $\alpha = 0.05$:

    $$
    \text{CVaR}_{0.05}^{\text{wc}} = \mu_L + \sigma_L \sqrt{\frac{1 - \alpha}{\alpha}} = -0.065 + 0.1414 \times \sqrt{\frac{0.95}{0.05}}
    $$

    $$
    = -0.065 + 0.1414 \times \sqrt{19} = -0.065 + 0.1414 \times 4.3589 = -0.065 + 0.6163 = 0.5513
    $$

    So the worst-case CVaR is approximately $55.1\%$ (as a loss).

    **(b)** The Gaussian CVaR uses the formula:

    $$
    \text{CVaR}_\alpha^{\text{Gaussian}} = \mu_L + \sigma_L \frac{\phi(\Phi^{-1}(\alpha))}{\alpha}
    $$

    With $\alpha = 0.05$: $\Phi^{-1}(0.05) = -1.6449$, so $\phi(-1.6449) = \phi(1.6449) = 0.1031$ (the standard normal PDF).

    $$
    \text{CVaR}_{0.05}^{\text{Gaussian}} = -0.065 + 0.1414 \times \frac{0.1031}{0.05} = -0.065 + 0.1414 \times 2.0627
    $$

    $$
    = -0.065 + 0.2917 = 0.2267
    $$

    **Comparison**: The worst-case (Chebyshev-type) CVaR is $0.551$, while the Gaussian CVaR is $0.227$. The worst-case CVaR is more conservative by:

    $$
    0.551 - 0.227 = 0.324
    $$

    a difference of about 32.4 percentage points, or roughly $0.551/0.227 \approx 2.43$ times larger. The worst-case CVaR is more conservative because it considers all distributions with the given mean and covariance, including heavy-tailed distributions that concentrate mass in the tail. The Gaussian CVaR assumes a specific (thin-tailed) distributional form. The ratio $\sqrt{(1-\alpha)/\alpha} / (\phi(\Phi^{-1}(\alpha))/\alpha) = 4.359 / 2.063 \approx 2.11$ quantifies this conservatism gap.

---

**Exercise 2.** For linear loss $\ell(x, \xi) = \xi^\top x$ and type-1 Wasserstein ball with $\ell_2$-norm transport cost, the DRO problem reduces to

$$
\min_{x \in \mathcal{X}} \left\{\frac{1}{n}\sum_{i=1}^n \hat{\xi}_i^\top x + \varepsilon \|x\|_2\right\}
$$

(a) Show that this is equivalent to Ridge-penalized optimization. (b) If the transport cost uses the $\ell_\infty$-norm instead, show that the regularization becomes $\varepsilon \|x\|_1$ (LASSO). (c) For a factor model with $k = 20$ factors, $n = 60$ monthly observations, and $\varepsilon = 0.05$, discuss which norm choice ($\ell_1$ vs $\ell_2$) produces sparser and more interpretable portfolio weights.

??? success "Solution to Exercise 2"
    **(a)** The DRO problem with type-1 Wasserstein ball ($\ell_2$-norm transport cost) and linear loss $\ell(x, \xi) = \xi^\top x$ is:

    $$
    \min_{x \in \mathcal{X}} \sup_{\mathbb{P}: W_1(\mathbb{P}, \hat{\mathbb{P}}_n) \le \varepsilon} \mathbb{E}_\mathbb{P}[\xi^\top x]
    $$

    By the Wasserstein DRO duality theorem with $\ell_2$-norm transport:

    $$
    \sup_{\mathbb{P}: W_1(\mathbb{P}, \hat{\mathbb{P}}_n) \le \varepsilon} \mathbb{E}_\mathbb{P}[\xi^\top x] = \frac{1}{n}\sum_{i=1}^n \hat{\xi}_i^\top x + \varepsilon \|x\|_2
    $$

    This holds because the linear loss $\xi^\top x$ is $\|x\|_2$-Lipschitz in $\xi$ (with respect to the $\ell_2$-norm): $|(\xi_1 - \xi_2)^\top x| \le \|\xi_1 - \xi_2\|_2 \|x\|_2$. The worst-case distribution shifts each data point in the direction that maximizes $\xi^\top x$, which is the direction $x / \|x\|_2$, contributing $\varepsilon \|x\|_2$.

    The resulting optimization:

    $$
    \min_{x \in \mathcal{X}} \left\{\hat{\mu}^\top x + \varepsilon \|x\|_2\right\}
    $$

    where $\hat{\mu} = \frac{1}{n}\sum_i \hat{\xi}_i$. This is precisely **Ridge-penalized** (Tikhonov regularized) optimization with penalty parameter $\varepsilon$.

    **(b)** If the transport cost uses the $\ell_\infty$-norm, the Lipschitz constant of $\xi \mapsto \xi^\top x$ with respect to $\|\cdot\|_\infty$ is $\|x\|_1$ (since $|\xi^\top x| \le \|\xi\|_\infty \|x\|_1$ and the dual norm of $\ell_\infty$ is $\ell_1$). Therefore:

    $$
    \sup_{\mathbb{P}: W_1^{(\infty)}(\mathbb{P}, \hat{\mathbb{P}}_n) \le \varepsilon} \mathbb{E}_\mathbb{P}[\xi^\top x] = \hat{\mu}^\top x + \varepsilon \|x\|_1
    $$

    This is **LASSO** ($\ell_1$-penalized) optimization with penalty parameter $\varepsilon$.

    **(c)** With $k = 20$ factors and $n = 60$ observations:

    - **$\ell_1$ (LASSO) penalty**: Promotes **sparsity** in portfolio weights. Many weights are driven exactly to zero, producing a portfolio that invests in only a few factors. This is desirable when only a subset of factors are truly predictive, and the rest are noise. With $n/k = 3$ (only 3 observations per parameter), sparsity is crucial for avoiding overfitting.
    - **$\ell_2$ (Ridge) penalty**: Shrinks all weights toward zero but retains all factors with small weights. No factor is eliminated entirely. This is appropriate when many factors have small but nonzero effects.

    For interpretability and robustness with $n = 60$ and $k = 20$, the $\ell_1$ penalty is generally preferred because: (i) it automatically selects the most important factors, reducing model complexity; (ii) sparse portfolios are cheaper to implement (fewer positions, lower transaction costs); (iii) with $n/k = 3$, the estimation error per factor is large, and eliminating weak factors reduces total estimation error.

---

**Exercise 3.** The Wasserstein distance between the empirical distribution $\hat{\mathbb{P}}_n$ and the true distribution $\mathbb{P}^*$ satisfies $\mathbb{P}(W_p(\hat{\mathbb{P}}_n, \mathbb{P}^*) > \varepsilon) \le C \exp(-c \, n \varepsilon^{\max(d,2)})$. (a) For $d = 5$ asset returns and $n = 250$ daily observations, find the radius $\varepsilon$ such that $\mathbb{P}^* \in \mathcal{P}_W$ with probability at least 95%. (b) Explain the curse of dimensionality: how does the required $\varepsilon$ scale with $d$ for fixed $n$ and confidence level? (c) Discuss why this concentration result is important for calibrating the ambiguity set radius in practice.

??? success "Solution to Exercise 3"
    **(a)** The concentration inequality states:

    $$
    \mathbb{P}(W_p(\hat{\mathbb{P}}_n, \mathbb{P}^*) > \varepsilon) \le C \exp(-c \, n \varepsilon^{\max(d, 2)})
    $$

    For $d = 5$ and $p \ge 1$, we have $\max(d, 2) = 5$. Setting the right side equal to $0.05$ (for 95% confidence):

    $$
    C \exp(-c \, n \varepsilon^5) = 0.05
    $$

    $$
    c \, n \varepsilon^5 = \ln(C/0.05) = \ln(20C)
    $$

    Taking $C$ and $c$ as order-1 constants (say $C = 1, c = 1$ for illustration):

    $$
    250 \cdot \varepsilon^5 = \ln 20 \approx 3.0
    $$

    $$
    \varepsilon^5 = 0.012 \implies \varepsilon = (0.012)^{1/5} = 0.012^{0.2} \approx 0.416
    $$

    This is a substantial radius, reflecting the difficulty of estimating a 5-dimensional distribution from only 250 observations.

    **(b)** The **curse of dimensionality** is evident from the exponent $\max(d, 2)$:

    $$
    \varepsilon \propto \left(\frac{\ln(C/\beta)}{cn}\right)^{1/\max(d,2)}
    $$

    For fixed $n$ and confidence $1-\beta$:

    - $d = 2$: $\varepsilon \propto n^{-1/2}$ (standard parametric rate)
    - $d = 5$: $\varepsilon \propto n^{-1/5}$ (much slower)
    - $d = 10$: $\varepsilon \propto n^{-1/10}$ (even slower)
    - $d = 50$: $\varepsilon \propto n^{-1/50}$ (essentially no convergence with practical sample sizes)

    For example, to achieve $\varepsilon = 0.1$ with $d = 50$, one would need $n \propto 0.1^{-50}$, an astronomically large sample. This is the fundamental limitation of non-parametric distributional estimation in high dimensions.

    **(c)** This concentration result is important for calibrating $\varepsilon$ because:

    - It provides a **principled** way to set the ambiguity radius: choose $\varepsilon$ so that the true distribution is contained in the Wasserstein ball with a desired confidence level.
    - The out-of-sample guarantee then follows automatically: with probability at least $1-\beta$, the DRO solution performs at least as well out-of-sample as the DRO objective value predicts.
    - In practice, the constants $C$ and $c$ are often unknown, so the theoretical $\varepsilon$ serves as a guide. Cross-validation or bootstrap methods can be used to fine-tune $\varepsilon$ empirically.
    - The curse of dimensionality suggests that in high-dimensional settings ($d \gg 10$), purely non-parametric Wasserstein balls become too large to be useful, and one should instead use structured ambiguity sets (e.g., factor model-based, moment-based) that exploit domain knowledge to reduce effective dimensionality.

---

**Exercise 4.** Compare the DRO robust factor portfolio $x^{\text{DRO}} = \arg\min_{x \in \mathcal{X}} \{-\hat{\mu}^\top x + \varepsilon\|x\|_2 + \frac{\gamma}{2} x^\top \hat{\Sigma} x\}$ with the standard mean-variance portfolio $x^{\text{MV}} = \frac{1}{\gamma}\hat{\Sigma}^{-1}\hat{\mu}$. (a) Derive the first-order optimality condition for $x^{\text{DRO}}$ and show how the robustness parameter $\varepsilon$ shrinks the portfolio weights. (b) Show that as $\varepsilon \to \infty$, $x^{\text{DRO}}$ converges to the minimum-variance portfolio. (c) Using simulated data with $d = 10$ assets, true Sharpe ratio 0.5, and $n = 120$ observations, argue why $x^{\text{DRO}}$ typically outperforms $x^{\text{MV}}$ out-of-sample due to estimation error in $\hat{\mu}$.

??? success "Solution to Exercise 4"
    **(a)** The DRO problem (ignoring simplex constraints for clarity) is:

    $$
    \min_x \left\{-\hat{\mu}^\top x + \varepsilon\|x\|_2 + \frac{\gamma}{2}x^\top \hat{\Sigma} x\right\}
    $$

    The first-order condition (using the subdifferential of $\|x\|_2$ at $x \ne 0$) is:

    $$
    -\hat{\mu} + \varepsilon \frac{x}{\|x\|_2} + \gamma \hat{\Sigma} x = 0
    $$

    Rearranging:

    $$
    \gamma \hat{\Sigma} x = \hat{\mu} - \varepsilon \frac{x}{\|x\|_2}
    $$

    $$
    x = \frac{1}{\gamma}\hat{\Sigma}^{-1}\left(\hat{\mu} - \varepsilon \frac{x}{\|x\|_2}\right)
    $$

    Compared to the standard mean-variance solution $x^{\text{MV}} = \frac{1}{\gamma}\hat{\Sigma}^{-1}\hat{\mu}$, the robust solution **shrinks** the effective mean from $\hat{\mu}$ to $\hat{\mu} - \varepsilon \frac{x}{\|x\|_2}$. The shrinkage direction is $x / \|x\|_2$, meaning the mean is reduced most in the direction of the portfolio itself. This penalizes precisely the component of $\hat{\mu}$ that the portfolio exploits, reducing sensitivity to estimation error in the mean.

    **(b)** As $\varepsilon \to \infty$, the penalty $\varepsilon \|x\|_2$ dominates the linear term $-\hat{\mu}^\top x$. For any $x \ne 0$:

    $$
    -\hat{\mu}^\top x + \varepsilon \|x\|_2 + \frac{\gamma}{2}x^\top \hat{\Sigma} x \approx \varepsilon \|x\|_2 + \frac{\gamma}{2}x^\top \hat{\Sigma} x
    $$

    The optimal portfolio minimizes $\frac{\gamma}{2}x^\top \hat{\Sigma} x$ subject to any remaining constraints (e.g., $\mathbf{1}^\top x = 1$), because $\varepsilon \|x\|_2$ is minimized at the same point as the variance (or, more precisely, the portfolio that minimizes variance subject to the constraint also has small $\|x\|_2$). In the limit, the mean return $\hat{\mu}$ plays no role:

    $$
    x^{\text{DRO}} \xrightarrow{\varepsilon \to \infty} x^{\text{MinVar}} = \arg\min_{x: \mathbf{1}^\top x = 1} x^\top \hat{\Sigma} x = \frac{\hat{\Sigma}^{-1}\mathbf{1}}{\mathbf{1}^\top \hat{\Sigma}^{-1}\mathbf{1}}
    $$

    This is the **minimum-variance portfolio**, which ignores expected returns entirely and focuses solely on risk reduction.

    **(c)** With $d = 10$ assets, true Sharpe ratio 0.5, and $n = 120$ observations:

    - The sample mean $\hat{\mu}$ has estimation error of order $\sigma / \sqrt{n} \approx 0.2 / \sqrt{120} \approx 0.018$ per asset per month. With 10 assets, the total estimation error $\|\hat{\mu} - \mu\| \approx 0.018\sqrt{10} \approx 0.058$.
    - The mean-variance portfolio $x^{\text{MV}} = \frac{1}{\gamma}\hat{\Sigma}^{-1}\hat{\mu}$ **amplifies** estimation error because $\hat{\Sigma}^{-1}$ can have large eigenvalues (condition number issues), especially with $n = 120$ and $d = 10$.
    - The true Sharpe ratio of 0.5 means expected excess returns are modest, so estimation error in $\hat{\mu}$ is large relative to the signal.
    - Out-of-sample, $x^{\text{MV}}$ typically has a realized Sharpe ratio far below 0.5 (often near zero or negative) because it overweights assets with overestimated means.
    - $x^{\text{DRO}}$ with appropriate $\varepsilon$ discounts the unreliable mean estimates, producing a portfolio closer to minimum-variance that retains some (shrunk) exposure to expected returns. The out-of-sample Sharpe ratio is typically much higher because the variance reduction from shrinkage more than compensates for the loss of expected return signal.

---

**Exercise 5.** The strong duality result for type-1 Wasserstein DRO states

$$
\sup_{\mathbb{P}: W_1(\mathbb{P}, \hat{\mathbb{P}}_n) \le \varepsilon} \mathbb{E}_\mathbb{P}[\ell(x, \xi)] = \inf_{\lambda \ge 0} \left\{\lambda \varepsilon + \frac{1}{n}\sum_{i=1}^n \sup_\xi [\ell(x, \xi) - \lambda \|\xi - \hat{\xi}_i\|]\right\}
$$

(a) Interpret the dual variable $\lambda$ as the sensitivity of the worst-case loss to the ambiguity radius $\varepsilon$. (b) For the loss $\ell(x, \xi) = (-x^\top \xi)^+$ (portfolio shortfall), show that the inner supremum is finite only when $\lambda$ is large enough relative to $\|x\|$. (c) Explain why this duality converts an infinite-dimensional optimization (over distributions) into a finite-dimensional convex program.

??? success "Solution to Exercise 5"
    **(a)** The dual variable $\lambda$ can be interpreted as follows. Consider the Lagrangian formulation where $\varepsilon$ is the primal constraint:

    $$
    \sup_{\mathbb{P}: W_1(\mathbb{P}, \hat{\mathbb{P}}_n) \le \varepsilon} \mathbb{E}_\mathbb{P}[\ell(x, \xi)]
    $$

    The dual variable $\lambda$ satisfies:

    $$
    \lambda^* = \frac{\partial}{\partial \varepsilon}\left[\sup_{\mathbb{P}: W_1 \le \varepsilon} \mathbb{E}_\mathbb{P}[\ell]\right]
    $$

    by the envelope theorem. So $\lambda^*$ is the **marginal increase** in worst-case expected loss per unit increase in the ambiguity radius $\varepsilon$. A large $\lambda^*$ means the problem is highly sensitive to distributional uncertainty: expanding the ambiguity set significantly increases the worst-case loss. A small $\lambda^*$ means the worst-case loss is relatively insensitive to the size of the ambiguity set, indicating that the portfolio is already robust.

    **(b)** For the shortfall loss $\ell(x, \xi) = (-x^\top \xi)^+ = \max(0, -x^\top \xi)$, the inner supremum in the dual is:

    $$
    \sup_\xi \left[(-x^\top \xi)^+ - \lambda \|\xi - \hat{\xi}_i\|\right]
    $$

    As $\xi \to \infty$ in the direction $-x/\|x\|_2$, the loss $(-x^\top \xi)^+$ grows linearly with rate $\|x\|_2$, while the penalty $\lambda \|\xi - \hat{\xi}_i\|$ also grows linearly with rate $\lambda$. The supremum is **finite** only if the penalty growth rate exceeds the loss growth rate:

    $$
    \lambda \ge \|x\|_2
    $$

    If $\lambda < \|x\|_2$, the adversary can move mass to $\xi \to -\infty$ (in the direction of $x$) faster than the transport penalty grows, making the worst-case loss infinite. This threshold $\lambda \ge \|x\|_2$ is the binding constraint in the dual, and at optimality $\lambda^* = \|x\|_2$ if the Wasserstein constraint is active.

    **(c)** The duality converts the problem as follows:

    - **Primal (infinite-dimensional)**: The decision variable is a probability distribution $\mathbb{P}$, which is an element of an infinite-dimensional function space. Optimizing over all distributions in a Wasserstein ball is intractable in general.
    - **Dual (finite-dimensional)**: The decision variable is $\lambda \ge 0$ (a scalar) plus $n$ inner optimization problems (one per data point). Each inner problem $\sup_\xi[\ell(x, \xi) - \lambda\|\xi - \hat{\xi}_i\|]$ is a finite-dimensional optimization over $\xi \in \mathbb{R}^d$.
    - For many common loss functions (linear, quadratic, piecewise linear), the inner supremum has a closed-form solution or is a tractable convex program.
    - The overall dual is therefore a finite-dimensional convex optimization problem that can be solved efficiently using standard solvers.

    This is the key computational advantage of the Wasserstein DRO framework: strong duality (guaranteed by the Blanchet-Murthy theorem under mild conditions) allows replacing an intractable infinite-dimensional problem with a tractable finite-dimensional one.

---

**Exercise 6.** A risk manager uses DRO to stress test a portfolio. The worst-case distribution $\mathbb{P}^*$ achieving $\sup_{\mathbb{P} \in \mathcal{P}} \text{CVaR}_\alpha^\mathbb{P}(L)$ represents the most adverse scenario consistent with the ambiguity set. (a) For a moment-based ambiguity set, describe the structure of $\mathbb{P}^*$ (hint: it is a discrete distribution supported on at most $d+1$ points by Richter's theorem). (b) Compare this principled worst-case approach with ad-hoc stress scenarios. (c) A portfolio has 3 risk factors. The worst-case distribution places mass on 4 points. Explain how examining these points reveals which tail events and correlation structures drive the worst-case risk.

??? success "Solution to Exercise 6"
    **(a)** For a moment-based ambiguity set with constraints on the first two moments, the worst-case distribution $\mathbb{P}^*$ has a specific structure due to classical results in moment problems.

    **Richter's theorem** (also known as the moment problem extremal theorem) states that for an optimization over distributions with $k$ moment constraints in $\mathbb{R}^d$, the extremal distribution is supported on at most $k + 1$ points. For a mean-variance ambiguity set with $d$-dimensional mean ($d$ constraints) and a scalar variance constraint (1 constraint), the worst-case distribution is supported on at most $d + 1$ points.

    Intuitively, this is because the moment constraints define a convex set of distributions, and the extremal point (maximizing a linear functional like CVaR) lies on a face of this set. The extreme points of the set of distributions with given moments are discrete distributions with minimal support.

    For the problem $\sup_{\mathbb{P}: \mathbb{E}[L] = \mu, \text{Var}(L) \le \sigma^2} \text{CVaR}_\alpha(L)$, the worst-case distribution is a **two-point distribution** (since there are 2 moment constraints: mean and variance in 1 dimension):

    $$
    L = \begin{cases} a & \text{with probability } p \\ b & \text{with probability } 1-p \end{cases}
    $$

    where $a, b, p$ are chosen to match the mean and variance constraints while maximizing CVaR.

    **(b)** Comparison with ad-hoc stress scenarios:

    - **DRO worst case**: Mathematically guaranteed to be the most adverse distribution consistent with known information (moments). It is the tightest possible upper bound given the constraints. No scenario is missed that could produce worse outcomes within the ambiguity set.
    - **Ad-hoc scenarios**: Selected based on historical events (e.g., "2008-like crash") or expert judgment. They may miss novel risk configurations. There is no guarantee that the selected scenarios are the worst case -- the actual worst case may involve correlations or tail events that the stress tester did not imagine.
    - **DRO is systematic**: It automates the search for worst-case scenarios, removing subjectivity. The worst-case distribution is a byproduct of the optimization, not an input.
    - **DRO can be overly conservative**: The worst-case distribution may be unrealistic (e.g., a two-point distribution is not a plausible model for financial returns). But it provides a rigorous upper bound.

    **(c)** With $d = 3$ risk factors and a mean-variance ambiguity set, the worst-case distribution is supported on at most $d + 1 = 4$ points. Let these be $\xi^{(1)}, \xi^{(2)}, \xi^{(3)}, \xi^{(4)} \in \mathbb{R}^3$ with weights $p_1, p_2, p_3, p_4$.

    Examining these 4 points reveals:

    - **Tail events**: One or two points typically represent extreme loss scenarios (large negative returns). Their location shows which combination of risk factor movements is most dangerous.
    - **Correlation structure**: The relative positions of the support points reveal the implied correlation under stress. If the extreme point has all three factors moving in the same direction, it indicates that the worst case involves correlation breakdown (all assets falling simultaneously).
    - **Concentration of risk**: The probability weights $p_i$ show how likely each scenario needs to be for the worst case. If most weight is on a single extreme point, the risk is concentrated; if spread across points, the risk comes from multiple scenarios.

    For example, if the 4 points are $(-0.3, -0.2, -0.1)$, $(0.1, 0.05, 0.03)$, $(0.02, -0.15, 0.05)$, and $(0.05, 0.1, -0.2)$ with weights $0.04, 0.90, 0.03, 0.03$, the first point is the dominant tail risk (simultaneous decline across all factors), while the other extreme points represent idiosyncratic risks to individual factors.

---

**Exercise 7.** A quantitative fund uses cross-validation to select the Wasserstein radius $\varepsilon$. The data consists of 120 monthly returns for 50 assets. (a) Describe a time-series cross-validation procedure (rolling window) for selecting $\varepsilon$, being careful to avoid look-ahead bias. (b) Plot the expected out-of-sample Sharpe ratio as a function of $\varepsilon$: at $\varepsilon = 0$ (standard mean-variance) performance is poor due to estimation error; at $\varepsilon$ too large, performance is poor due to excessive conservatism. Explain this U-shaped curve. (c) Discuss whether the optimal $\varepsilon$ is stable over time or should be adapted to market conditions (e.g., larger $\varepsilon$ during high-volatility regimes).

??? success "Solution to Exercise 7"
    **(a)** A time-series cross-validation procedure for selecting $\varepsilon$:

    1. **Define a grid** of candidate values: $\varepsilon \in \{0, 0.01, 0.02, \ldots, 0.50\}$.
    2. **Rolling window**: For each month $t$ from $t_0$ to $T$:
        - **Training set**: Use the most recent $W$ months of data (e.g., months $t - W$ to $t - 1$) to estimate $\hat{\mu}$ and $\hat{\Sigma}$ and solve the DRO portfolio for each $\varepsilon$.
        - **Test set**: Evaluate the out-of-sample return of each portfolio on month $t$.
    3. **Aggregate performance**: For each $\varepsilon$, compute the out-of-sample Sharpe ratio $\text{SR}(\varepsilon) = \frac{\bar{r}(\varepsilon)}{\hat{\sigma}(\varepsilon)}$ using the sequence of out-of-sample returns.
    4. **Select**: $\varepsilon^* = \arg\max_\varepsilon \text{SR}(\varepsilon)$.

    **Avoiding look-ahead bias**: The training set always uses only past data (months before $t$). No future returns are used in constructing the portfolio. The expanding or rolling window moves forward in time, never backward.

    With $T = 120$ months and training window $W = 60$, there are 60 out-of-sample months for evaluation.

    **(b)** The expected out-of-sample Sharpe ratio as a function of $\varepsilon$ has an **inverted U-shape** (or equivalently, the negative Sharpe ratio has a U-shape):

    - **$\varepsilon = 0$** (standard mean-variance): The portfolio $x^{\text{MV}} = \frac{1}{\gamma}\hat{\Sigma}^{-1}\hat{\mu}$ is highly sensitive to estimation error in $\hat{\mu}$. With $n = 60$ observations and $d = 50$ assets (underdetermined: $n > d$ but barely), $\hat{\Sigma}$ is nearly singular and $\hat{\mu}$ is noisy. The portfolio takes extreme, unstable positions. In-sample Sharpe ratio is high (overfitting), but out-of-sample Sharpe ratio is poor (possibly negative).
    - **$\varepsilon$ moderate** (optimal region): The robustness penalty shrinks extreme positions, reducing sensitivity to mean estimation error. The portfolio balances return-seeking (using $\hat{\mu}$) with risk control (the shrinkage). Out-of-sample Sharpe ratio is maximized.
    - **$\varepsilon$ very large**: The portfolio converges to the minimum-variance portfolio, ignoring return forecasts entirely. While stable, it sacrifices all return information. If the return estimates contain any signal (even noisy), the Sharpe ratio declines because that signal is discarded.

    The optimal $\varepsilon^*$ balances these two effects, analogous to the optimal regularization parameter in penalized regression.

    **(c)** The optimal $\varepsilon$ is generally **not stable** over time and should be adapted to market conditions:

    - **High-volatility regimes** (crises): Estimation error is larger because return distributions shift rapidly and correlations break down. A **larger $\varepsilon$** is appropriate to increase robustness. Empirically, minimum-variance strategies outperform in crises, consistent with large $\varepsilon$.
    - **Low-volatility regimes** (calm markets): Return distributions are more stable, estimates are more reliable, and alpha signals are more consistent. A **smaller $\varepsilon$** allows the portfolio to exploit return forecasts more aggressively.
    - **Regime-dependent calibration**: One approach is to set $\varepsilon_t = f(\text{VIX}_t)$ or $\varepsilon_t = g(\hat{\sigma}_t)$, increasing $\varepsilon$ when market volatility is high. Another is to use a time-varying rolling cross-validation with a short lookback for $\varepsilon$ selection.
    - **Stability concern**: Frequent changes in $\varepsilon$ cause portfolio turnover, which incurs transaction costs. A practical approach is to update $\varepsilon$ only quarterly or when the VIX crosses predefined thresholds, reducing unnecessary trading.

    The fundamental insight is that the optimal degree of robustness depends on the signal-to-noise ratio in the data, which varies over time. Larger $\varepsilon$ is needed precisely when the data is least informative.
