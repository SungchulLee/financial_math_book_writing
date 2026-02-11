# Portfolio Construction and Simulation



Having established rigorous estimations of expected returns and covariances from historical data, we now address the core problem of portfolio optimization: allocating capital across a finite universe of risky assets to construct investment portfolios that meet predefined risk-return objectives. This section presents a mathematically grounded and computationally intensive approach to portfolio construction via stochastic simulation, situating the procedure within the framework of mean-variance analysis. Beyond merely computing optimal portfolios, we investigate the geometric properties of the feasible set, articulate the implications of various allocation constraints, and explore the visualization of risk-return landscapes as an empirical lens into the theory of efficient investment.



## 1. Mathematical Formulation of Portfolios



Let $n$ denote the number of investable assets, each characterized by an expected return $\mu_i$ and a variance $\sigma_i^2$. An investor selects a portfolio defined by the weight vector:

$$
\mathbf{w} = (w_1, w_2, \dots, w_n)^T
$$

with the constraint:

$$
\sum_{i=1}^n w_i = 1
$$

This constraint ensures full investment of capital. Additional constraints—arising from institutional mandates, regulatory limits, or investor preferences—can be included, such as:

- **No short positions:** $w_i \geq 0$ for all $i$.
- **Upper and lower bounds:** $w_i \in [a_i, b_i]$.
- **Sectoral or thematic caps:** group-wise limits for portfolio exposure.
- **Cardinality constraints:** upper bounds on the number of non-zero positions.

Given the expected return vector $\boldsymbol{\mu} \in \mathbb{R}^n$ and covariance matrix $\boldsymbol{\Sigma} \in \mathbb{R}^{n \times n}$, the portfolio’s expected return and variance are computed as:

- **Expected Return:**
  $$
  \mu_P = \mathbf{w}^T \boldsymbol{\mu}
  $$

- **Portfolio Variance:**
  $$
  \sigma_P^2 = \mathbf{w}^T \boldsymbol{\Sigma} \mathbf{w}
  $$

These quantities define the feasible region in the mean-variance space, serving as the basis for identifying efficient portfolios under specific investor criteria.

## 2. Python Demo



## 3. Simulation-Based Exploration of the Feasible Set



While closed-form solutions to the mean-variance optimization problem are available under idealized conditions (e.g., unconstrained or linearly constrained problems), real-world allocation problems often involve nonlinear and combinatorial constraints. To navigate these complexities, we adopt a Monte Carlo simulation approach to empirically sample the set of admissible portfolios.



#### **A. Stochastic Simulation Framework**



1. **Random Weight Generation:**
   - Draw $M$ candidate portfolios by sampling weights from a multivariate distribution.
   - Normalize each weight vector to satisfy the budget constraint.
   - Apply additional constraints via projection or rejection methods.

2. **Computation of Performance Metrics:**
   - For each portfolio $\mathbf{w}^{(m)}$:
     - Compute $\mu^{(m)} = \mathbf{w}^{(m)T} \boldsymbol{\mu}$
     - Compute $\sigma^{(m)} = \sqrt{\mathbf{w}^{(m)T} \boldsymbol{\Sigma} \mathbf{w}^{(m)}}$
     - Compute Sharpe Ratio: $S^{(m)} = (\mu^{(m)} - r_f)/\sigma^{(m)}$

3. **Data Storage and Structure:**
   - Store results in structured arrays or dataframes for filtering and ranking.


## 4. Extraction of Benchmark Portfolios




From the simulated cloud, we identify two anchor points of the efficient frontier:

- **Global Minimum Variance Portfolio (GMVP):**
  $$
  \mathbf{w}_{\text{GMVP}} = \arg\min_{\mathbf{w}} \ \mathbf{w}^T \boldsymbol{\Sigma} \mathbf{w}
  $$

- **Tangency Portfolio (Max Sharpe Ratio):**
  $$
  \mathbf{w}_{\text{MSR}} = \arg\max_{\mathbf{w}} \ \frac{\mathbf{w}^T \boldsymbol{\mu} - r_f}{\sqrt{\mathbf{w}^T \boldsymbol{\Sigma} \mathbf{w}}}
  $$

These are located computationally via:

```python
max_sharpe_idx = np.argmax(sharpe_ratios)
min_var_idx = np.argmin(risks)
```

The GMVP serves as the left-most point of the efficient frontier and is often interpreted as the lowest-risk fully invested portfolio. The tangency portfolio achieves the highest possible Sharpe Ratio and serves as the optimal portfolio in the Capital Market Line model.

## 5. GMVP



The **Global Minimum Variance Portfolio (GMVP)** represents the unique portfolio on the **mean-variance efficient frontier** that minimizes total portfolio variance, regardless of expected returns. It is the cornerstone of modern portfolio theory and serves as the foundation for constructing more complex mean-variance optimal portfolios.

#### Problem Statement





Let $\Sigma \in \mathbb{R}^{n \times n}$ denote the **positive definite covariance matrix** of asset returns, and let $\mathbf{x} \in \mathbb{R}^n$ be the vector of portfolio weights. The global minimum variance problem is defined as the following constrained quadratic program:

$$
\begin{aligned}
\min_{\mathbf{x} \in \mathbb{R}^n} \quad & \mathbf{x}^T \Sigma \mathbf{x} \\
\text{subject to} \quad & \mathbf{1}^T \mathbf{x} = 1
\end{aligned}
$$

The objective function $\mathbf{x}^T \Sigma \mathbf{x}$ represents the **portfolio variance**, while the constraint $\mathbf{1}^T \mathbf{x} = 1$ ensures the portfolio is fully invested.



#### Lagrangian and First-Order Conditions



To solve this constrained optimization problem, we use the method of Lagrange multipliers. Define the Lagrangian:

$$
L(\mathbf{x}, \lambda) = \mathbf{x}^T \Sigma \mathbf{x} - \lambda (\mathbf{1}^T \mathbf{x} - 1)
$$

Taking gradients with respect to $\mathbf{x}$ and $\lambda$, and setting them to zero:

$$
\frac{\partial L}{\partial \mathbf{x}} = 2\Sigma \mathbf{x} - \lambda \mathbf{1} = 0 \quad \Rightarrow \quad \Sigma \mathbf{x} = \frac{\lambda}{2} \mathbf{1}
$$

$$
\frac{\partial L}{\partial \lambda} = \mathbf{1}^T \mathbf{x} - 1 = 0
$$

Solving the first condition yields:

$$
\mathbf{x} = \frac{\lambda}{2} \Sigma^{-1} \mathbf{1}
$$

Plug this into the constraint:

$$
\mathbf{1}^T \mathbf{x} = \frac{\lambda}{2} \mathbf{1}^T \Sigma^{-1} \mathbf{1} = 1 \quad \Rightarrow \quad \lambda = \frac{2}{\mathbf{1}^T \Sigma^{-1} \mathbf{1}}
$$

Hence, the optimal weights of the **GMVP** are given by the normalized expression:

$$
\mathbf{x}_{GMVP} = \frac{\Sigma^{-1} \mathbf{1}}{\mathbf{1}^T \Sigma^{-1} \mathbf{1}}
$$

This is a closed-form solution for the weights of the global minimum variance portfolio.



#### Economic Interpretation



- **$\Sigma^{-1} \mathbf{1}$** can be interpreted as the direction in which variance increases most slowly. We are allocating more weight to assets that help reduce overall portfolio variance.
- The normalization factor $\mathbf{1}^T \Sigma^{-1} \mathbf{1}$ ensures that the weights sum to one, keeping the portfolio fully invested.
- This portfolio **does not incorporate expected returns** — it is purely risk-based. This makes it especially useful when expected returns are difficult to estimate robustly.





#### Properties



- **Uniqueness**: The solution is unique as long as $\Sigma$ is positive definite.
- **No Expected Return Target**: Unlike the tangency (or Markowitz efficient) portfolio, the GMVP does not consider investor preferences or required returns.
- **Minimum Risk**: It represents the leftmost point on the mean-variance frontier (i.e., the portfolio with minimum variance).
- **Linearity**: Any efficient portfolio can be written as a linear combination of the GMVP and any other mean-variance efficient portfolio.



#### Generalizations



1. **With Expected Returns**: When a target return $\mu^*$ is specified, the problem becomes a mean-variance optimization subject to an additional constraint $\mu^T \mathbf{x} = \mu^*$.
2. **With No Short Selling**: This introduces inequality constraints $\mathbf{x} \geq 0$, requiring quadratic programming techniques.
3. **With Transaction Costs or Cardinality Constraints**: The problem becomes non-convex and may require heuristic or mixed-integer optimization methods.





#### Practical Considerations



- **Estimation Risk**: The GMVP relies heavily on accurate estimation of the covariance matrix. Shrinkage estimators (e.g., Ledoit–Wolf) are often used in practice to improve robustness.
- **Stability**: The GMVP tends to be more stable than portfolios that rely on return estimates, but can still result in extreme weights if the covariance matrix is ill-conditioned.
- **Diversification**: Despite its objective, the GMVP can be **concentrated** in a few assets if correlations are high, hence regularization or constraints are often imposed.



## 6. Tangency Portfolio (Maximum Sharpe Ratio Portfolio)



In classical portfolio theory, the **Tangency Portfolio** is the unique portfolio on the **efficient frontier** that achieves the **maximum Sharpe ratio** when combined with a risk-free asset. It is so named because it lies at the **point of tangency** between the Capital Market Line (CML) and the efficient frontier of risky assets.

This portfolio plays a central role in the **two-fund separation theorem**, the **Capital Asset Pricing Model (CAPM)**, and the broader theory of mean-variance optimization under Merton's (1973) intertemporal setting.



#### Mathematical Formulation



Let:
- $\mu \in \mathbb{R}^n$: vector of expected returns,
- $\Sigma \in \mathbb{R}^{n \times n}$: positive definite covariance matrix of returns,
- $r \in \mathbb{R}$: risk-free rate,
- $\mathbf{1} \in \mathbb{R}^n$: vector of ones.

The **Sharpe ratio** of a portfolio $\mathbf{x}$ is defined as:
$$
\text{Sharpe}(\mathbf{x}) = \frac{\mu^T \mathbf{x} - r}{\sqrt{\mathbf{x}^T \Sigma \mathbf{x}}}
$$

Our goal is to find the portfolio $\mathbf{x}^*$ that maximizes this ratio.




#### Optimization Problem



The original Sharpe ratio maximization problem is non-convex due to the fractional objective and the budget constraint:

$$
\begin{aligned}
\max_{\mathbf{x}} \quad & \frac{\mu^T \mathbf{x} - r}{\sqrt{\mathbf{x}^T \Sigma \mathbf{x}}} \\\\
\text{subject to} \quad & \mathbf{1}^T \mathbf{x} = 1
\end{aligned}
$$

This is difficult to solve directly due to the ratio of quadratic and linear forms. Instead, we take advantage of the **scale-invariance** property of the Sharpe ratio.




#### Step 1: Remove Budget Constraint via Homogeneity



Since $\text{Sharpe}(\alpha \mathbf{x}) = \text{Sharpe}(\mathbf{x})$ for any scalar $\alpha > 0$, we can rescale the optimization without changing the solution.

This leads to the reformulation:

$$
\begin{aligned}
\max_{\mathbf{x}} \quad & (\mu - r\mathbf{1})^T \mathbf{x} \\\\
\text{subject to} \quad & \mathbf{x}^T \Sigma \mathbf{x} = 1
\end{aligned}
$$

This is a **convex quadratic constraint** with a linear objective — amenable to Lagrangian methods.





#### Step 2: Lagrangian and First-Order Conditions



Let $\tilde{\mu} = \mu - r\mathbf{1}$. The Lagrangian is:
$$
\mathcal{L}(\mathbf{x}, \lambda) = \tilde{\mu}^T \mathbf{x} - \lambda (\mathbf{x}^T \Sigma \mathbf{x} - 1)
$$

Set the gradient to zero:
$$
\frac{\partial \mathcal{L}}{\partial \mathbf{x}} = \tilde{\mu} - 2\lambda \Sigma \mathbf{x} = 0
\Rightarrow
\Sigma \mathbf{x} = \frac{1}{2\lambda} \tilde{\mu}
\Rightarrow
\mathbf{x} \propto \Sigma^{-1} (\mu - r\mathbf{1})
$$





#### Step 3: Normalize Weights to Sum to One



We obtain the final tangency portfolio (normalized to be fully invested):
$$
\boxed{
\mathbf{w}_{\text{tan}} = \frac{\Sigma^{-1} (\mu - r\mathbf{1})}{\mathbf{1}^T \Sigma^{-1} (\mu - r\mathbf{1})}
}
$$

#### Q. What happens if no short sale?

There **is a closed-form formula** for the **tangency portfolio** (maximum Sharpe ratio portfolio), assuming **unconstrained optimization** (i.e., **short-selling is allowed**).

**Tangency Portfolio (Closed-Form, Unconstrained)**

Let:
- $\mu$ = expected returns vector
- $\Sigma$ = covariance matrix of returns
- $r_f$ = risk-free rate
- $\mathbf{1}$ = vector of ones

Then the **tangency portfolio weights** (denoted $\mathbf{w}^*$) are:

$$
\mathbf{w}^* = \frac{\Sigma^{-1} (\mu - r_f \mathbf{1})}{\mathbf{1}^\top \Sigma^{-1} (\mu - r_f \mathbf{1})}
$$

**Interpretation:**

- $\Sigma^{-1} (\mu - r_f \mathbf{1})$: direction of optimal risk-adjusted return (the tangency vector)
- The denominator ensures weights sum to 1 (normalization)

**When to use this:**

- Only valid **without short-selling restrictions**
- If I need `no_short=True` (long-only), then you must use **numerical optimization** like I am currently doing



#### Economic Interpretation




- The tangency portfolio allocates more capital to assets with **higher excess returns** $(\mu_i - r)$ and **lower marginal risk** (as measured by their contribution to portfolio variance).
- This portfolio is **mean-variance optimal** for **all investors** who have quadratic utility or normally distributed returns and access to a risk-free asset.
- Under the assumptions of CAPM, this is the **market portfolio**, and all investors should hold some combination of it and the risk-free asset.



#### Advanced Remarks



- If you assume $r = 0$, the tangency portfolio becomes equivalent to the **maximum Sharpe ratio portfolio without a risk-free asset**.
- If $\Sigma$ is ill-conditioned (e.g. due to multicollinearity), regularization techniques (like shrinkage or factor models) can improve stability.
- This approach underpins the **CAPM equilibrium**: if all investors behave this way, market prices will adjust so that the market portfolio becomes the tangency portfolio.



## 7. Envelope Portfolio with Target Return $r$


The **Envelope Portfolio** (also called the **mean-variance efficient portfolio** for a given expected return $r$) is the solution to the problem of minimizing variance subject to an expected return constraint. It lies on the **efficient frontier**, which is the upper boundary of the set of all attainable portfolios in the mean–variance space.

This problem generalizes both:
- The **GMVP**, which is the solution when $r$ is not constrained.
- The **Tangency Portfolio**, when $r$ is implicitly defined by the Sharpe ratio maximization.

#### Optimization Problem



Given:
- Covariance matrix: $\Sigma \in \mathbb{R}^{n \times n}$ (symmetric positive definite)
- Expected returns: $\mu \in \mathbb{R}^n$
- Target return: $r \in \mathbb{R}$

We aim to:

$$
\begin{aligned}
\min_{\mathbf{x}} \quad & \mathbf{x}^T \Sigma \mathbf{x} \\\\
\text{subject to} \quad & \mu^T \mathbf{x} = r \\\\
                        & \mathbf{1}^T \mathbf{x} = 1
\end{aligned}
$$

This is a **convex quadratic program** with two linear equality constraints.





#### Lagrangian Formulation



Define Lagrangian multipliers $\lambda_1$ and $\lambda_2$ for the return and budget constraints respectively:

$$
\mathcal{L}(\mathbf{x}, \lambda_1, \lambda_2) = \mathbf{x}^T \Sigma \mathbf{x} - \lambda_1(\mu^T \mathbf{x} - r) - \lambda_2(\mathbf{1}^T \mathbf{x} - 1)
$$

Taking derivatives:



#### First-order condition w.r.t. $\mathbf{x}$:



$$
\frac{\partial \mathcal{L}}{\partial \mathbf{x}} = 2\Sigma \mathbf{x} - \lambda_1 \mu - \lambda_2 \mathbf{1} = 0
\quad \Rightarrow \quad
\Sigma \mathbf{x} = \frac{1}{2} (\lambda_1 \mu + \lambda_2 \mathbf{1})
$$



#### Constraints:



$$
\mu^T \mathbf{x} = r, \qquad \mathbf{1}^T \mathbf{x} = 1
$$





#### Matrix Form Solution



We solve the following **linear system** to obtain the optimal weights $\mathbf{x}$ and multipliers $\lambda_1$, $\lambda_2$:

$$
\begin{bmatrix}
2\Sigma & -\mu & -\mathbf{1} \\\\
\mu^T & 0 & 0 \\\\
\mathbf{1}^T & 0 & 0
\end{bmatrix}
\begin{bmatrix}
\mathbf{x} \\\\
\lambda_1 \\\\
\lambda_2
\end{bmatrix}
=
\begin{bmatrix}
\mathbf{0} \\\\
r \\\\
1
\end{bmatrix}
$$

This system is well-posed as long as $\Sigma$ is invertible and $\mu$ is not collinear with $\mathbf{1}$.

#### Interpretation



- The solution defines a **parametric curve** — the efficient frontier — as $r$ varies.
- Any point on the efficient frontier (above the GMVP) can be recovered using this formulation.
- When $r = \mu^T \mathbf{w}_{\text{tan}}$, this portfolio equals the tangency portfolio.
- When $r$ equals the expected return of the GMVP, the solution reduces to the GMVP.

#### Applications





- Construction of custom portfolios matching investor return expectations.
- Mapping the entire efficient frontier by sweeping across different $r$.
- A foundation for **constrained** or **robust** optimization (e.g. incorporating inequality constraints or regularization).



## 8. Two-Fund Theorem (Merton)



The **Two-Fund Theorem** is a foundational result in modern portfolio theory. It states that **any efficient portfolio** (on the envelope or efficient frontier) can be constructed as a **convex combination of two other efficient portfolios**. This means that all portfolios on the efficient frontier lie in the span of just two “funds” — hence the name.

This insight has profound implications: it implies that investors with different risk-return preferences need not construct entirely different portfolios — they can mix the same two base funds to achieve their desired outcome.

#### Mathematical Formulation



Let:

- $\mathbf{w}_{e_1}$ and $\mathbf{w}_{e_2}(r)$ be two portfolios lying on the envelope (efficient frontier), where $r$ denotes the target return.
- $t \in [0, 1]$ be a mixing parameter.

Then any efficient portfolio $\mathbf{w}_{\text{frontier}}$ with expected return between the returns of $\mathbf{w}_{e_1}$ and $\mathbf{w}_{e_2}$ can be written as:

$$
\boxed{
\mathbf{w}_{\text{frontier}} = t \cdot \mathbf{w}_{e_1} + (1 - t) \cdot \mathbf{w}_{e_2}(r)
}
$$

This representation shows that **linear combinations** of efficient portfolios remain efficient — provided they lie on the same frontier.

#### Geometric Intuition



- The set of portfolios $\mathbf{x}$ that satisfy $\mu^T \mathbf{x} = r$ and $\mathbf{1}^T \mathbf{x} = 1$ form a **hyperplane** in $\mathbb{R}^n$.
- The optimization $\min \mathbf{x}^T \Sigma \mathbf{x}$ with these constraints finds the point on this hyperplane with **minimum variance**.
- The entire frontier is a **parabola** in mean–variance space, but it's a **line** in the space of portfolio weights.

Therefore, **two efficient portfolios are sufficient** to span all others on the frontier.

#### Economic Interpretation



- The Two-Fund Theorem justifies **mutual fund separation**: all investors, regardless of preferences, can combine the same two funds.
- When a risk-free asset is available, the theorem becomes the **One-Fund Theorem**: every investor mixes the **tangency portfolio** with the **risk-free asset**.
- The choice of $\mathbf{w}_{e_1}$ and $\mathbf{w}_{e_2}$ is arbitrary as long as both lie on the frontier and produce different returns.

#### Practical Implications



1. **Portfolio Simplification**:
   - Reduces the dimensionality of portfolio construction.
   - Only two building blocks are needed for the entire efficient frontier.

2. **Computational Efficiency**:
   - Once two envelope portfolios are computed (e.g., GMVP and tangency portfolio), others can be interpolated linearly.

## 9. One-Fund Theorem (Capital Market Line)



The **One-Fund Theorem** is a special case of the **Two-Fund Theorem** that emerges in the presence of a **risk-free asset**. This result forms the backbone of the **Capital Market Line (CML)** and **Sharpe’s CAPM formulation**. It states:

> When investors have access to a risk-free asset with return $r_f$, the only risky portfolio they need is the **tangency portfolio** (or Sharpe portfolio). All efficient portfolios can be formed by combining this single fund with the risk-free asset.





#### Statement



If:
- $r_f$ is the risk-free interest rate,
- $\mathbf{x}_{\text{sharpe}}$ is the tangency (Sharpe) portfolio,

Then **any efficient portfolio** $\mathbf{w}_{\text{efficient}}$ satisfies:

$$
\boxed{
\mathbf{w}_{\text{efficient}} = \alpha \cdot \mathbf{x}_{\text{sharpe}} + (1 - \alpha) \cdot \mathbf{e}_f
}
$$

where:
- $\mathbf{e}_f$ is a zero-variance investment (e.g., 100% in the risk-free asset),
- $\alpha \in \mathbb{R}$ reflects the investor's risk tolerance
(can be $>1$ or $<0$ to allow for leverage or lending).


#### Capital Market Line (CML)






The set of all efficient portfolios under this theorem forms a straight line in mean–variance space:

$$
\mu_{\text{portfolio}} = r_f + \frac{\mu_{\text{sharpe}} - r_f}{\sigma_{\text{sharpe}}} \cdot \sigma_{\text{portfolio}}
$$

This is the **Capital Market Line**, and:
- Its **slope** is the maximum Sharpe ratio.
- It **dominates** all other feasible portfolios not on the line.
- All rational investors (under mean-variance utility) will choose a point on this line.

#### Intuition



- The **risk-free asset** allows investors to **shift** their portfolio along the line that connects $(0, r_f)$ to the Sharpe portfolio in mean–standard deviation space.
- Because of **linear separability**, only the **tangency portfolio** needs to be computed; no other risky portfolios are required.
- **All investors**, regardless of preferences, should invest along the **same Capital Market Line**, only differing in how much risk they take (i.e., their $\alpha$).

#### Economic Significance



- This theorem justifies the widespread use of **index funds** as a proxy for the market portfolio.
- It also underpins the **CAPM equilibrium** where the market portfolio becomes the tangency portfolio under homogenous expectations.



#### Visual Summary



**Efficient frontier with no risk-free asset**:
- Curved (parabolic) efficient frontier.
- Investors choose from portfolios like GMVP, tangency, or envelope portfolios.

**With risk-free asset**:
- The CML becomes the new efficient frontier.
- All efficient portfolios lie on the line between the risk-free rate and the tangency portfolio.



## Summary



In summary, this section has formalized the construction of portfolios under uncertainty using Monte Carlo simulation as a flexible and computationally tractable alternative to closed-form optimization. Through empirical sampling, we approximate the feasible risk-return set, identify optimal allocations under diverse constraints, and gain actionable insight into the geometric structure of the investment opportunity set. This simulation framework complements analytical optimization by incorporating practical complexities and revealing the probabilistic texture of portfolio selection under realistic conditions.

