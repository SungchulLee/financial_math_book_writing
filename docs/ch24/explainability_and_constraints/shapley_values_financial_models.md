# Shapley Values for Financial Models

When a credit model denies a loan or a risk system flags a portfolio for excessive exposure, regulators and clients demand an answer to a deceptively simple question: *which input features drove this decision?* For complex models---gradient-boosted trees, neural networks, ensemble methods---the answer is not obvious. **Shapley values**, rooted in cooperative game theory, provide a principled, axiomatically justified method for attributing a model's output to its input features. This section develops the theory from its game-theoretic foundations, presents the SHAP framework and its efficient algorithms, and examines applications to pricing, risk, and regulatory interpretability in finance.

---

!!! abstract "Learning Objectives"
    After completing this section, you should understand:

    - The cooperative game theory foundation and the four Shapley axioms
    - The exact Shapley value formula and its computational complexity
    - SHAP (SHapley Additive exPlanations) as a unified framework for feature attribution
    - KernelSHAP and TreeSHAP as practical estimation algorithms
    - Financial applications including credit scoring, risk attribution, and regulatory compliance

---

## Cooperative Game Theory Foundation

### Coalitional Games

A **coalitional game** (or cooperative game) consists of:

- A set of players $N = \{1, 2, \ldots, n\}$
- A **characteristic function** $v : 2^N \to \mathbb{R}$ with $v(\emptyset) = 0$

The value $v(S)$ represents the total payoff that coalition $S \subseteq N$ can achieve by cooperating.

In the model explanation context:

- **Players** = input features $\{x_1, \ldots, x_n\}$
- **Characteristic function** = the model prediction using only the features in coalition $S$

### The Fair Allocation Problem

The central question is: how should the total value $v(N)$ be fairly divided among the players? Shapley (1953) showed that there is a **unique** allocation satisfying four natural fairness axioms.

---

## The Shapley Value

### Definition

The **Shapley value** of player $i$ is:

$$
\phi_i(v) = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|!\,(n - |S| - 1)!}{n!}\,\big[v(S \cup \{i\}) - v(S)\big]
$$

The term $v(S \cup \{i\}) - v(S)$ is the **marginal contribution** of player $i$ to coalition $S$. The Shapley value averages this marginal contribution over all possible orderings in which players join the coalition.

### Equivalent Permutation Form

Equivalently, if $\sigma$ is a uniformly random permutation of $N$ and $S_i^\sigma$ denotes the set of players preceding $i$ in $\sigma$:

$$
\phi_i(v) = \mathbb{E}_\sigma\!\big[v(S_i^\sigma \cup \{i\}) - v(S_i^\sigma)\big]
$$

This form is more intuitive: imagine the players arriving in a random order, and each player receives their marginal contribution upon arrival.

### Shapley Axioms

**Theorem (Shapley, 1953).** There exists a unique allocation $\phi : \mathcal{G}_N \to \mathbb{R}^n$ satisfying:

1. **Efficiency:** $\sum_{i=1}^n \phi_i(v) = v(N) - v(\emptyset)$
2. **Symmetry:** If $v(S \cup \{i\}) = v(S \cup \{j\})$ for all $S$, then $\phi_i = \phi_j$
3. **Null player (Dummy):** If $v(S \cup \{i\}) = v(S)$ for all $S$, then $\phi_i = 0$
4. **Linearity (Additivity):** $\phi_i(v + w) = \phi_i(v) + \phi_i(w)$

$\square$

!!! note "Why Shapley Values Are Unique"
    The uniqueness theorem is powerful: any method that satisfies these four fairness axioms *must* be the Shapley value. No other allocation scheme can simultaneously be efficient, symmetric, and linear while ignoring irrelevant players. This gives Shapley values a privileged axiomatic status among all feature attribution methods.

---

## SHAP: SHapley Additive exPlanations

### From Games to Model Explanations

Lundberg and Lee (2017) introduced **SHAP** by connecting Shapley values to model explanation. Given a model $f$ and an instance $x$, define the characteristic function:

$$
v_x(S) = \mathbb{E}\!\big[f(X) \mid X_S = x_S\big]
$$

where $X_S = x_S$ means the features in $S$ are fixed to their values in $x$, and the remaining features are integrated out according to their conditional distribution.

The SHAP value of feature $i$ for prediction $f(x)$ is:

$$
\phi_i(f, x) = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|!\,(n - |S| - 1)!}{n!}\,\big[v_x(S \cup \{i\}) - v_x(S)\big]
$$

By the efficiency axiom:

$$
f(x) = \phi_0 + \sum_{i=1}^n \phi_i(f, x)
$$

where $\phi_0 = \mathbb{E}[f(X)]$ is the base value. This provides an **exact additive decomposition** of every prediction.

### Computational Complexity

The exact Shapley value requires evaluating $v_x(S)$ for all $2^n$ subsets of features. This is **exponential** in the number of features, making exact computation intractable for models with many inputs.

Two practical algorithms address this: **KernelSHAP** (model-agnostic) and **TreeSHAP** (tree-specific).

---

## KernelSHAP

### Weighted Least Squares Formulation

KernelSHAP approximates SHAP values by solving a weighted linear regression. Define binary coalition vectors $z \in \{0,1\}^n$ where $z_i = 1$ means feature $i$ is in the coalition. The SHAP values are the solution to:

$$
\min_{\phi_0, \phi_1, \ldots, \phi_n} \sum_{z \in \{0,1\}^n} \pi(z)\,\Big[v_x(z) - \phi_0 - \sum_{i=1}^n z_i\,\phi_i\Big]^2
$$

where the **SHAP kernel** is:

$$
\pi(z) = \frac{n - 1}{\binom{n}{|z|}\,|z|\,(n - |z|)}
$$

with $|z| = \sum_i z_i$. This kernel assigns higher weight to coalitions of very small and very large size, where marginal contributions are most informative.

### Sampling Approximation

In practice, KernelSHAP samples coalitions $z^{(1)}, \ldots, z^{(M)}$ according to $\pi$ and solves the weighted regression on the sample. The approximation converges as $M \to \infty$.

**Complexity:** $O(M \cdot n \cdot T_f)$ where $T_f$ is the cost of one model evaluation.

!!! warning "Conditional vs Marginal Expectations"
    A subtle but important distinction: the theoretical $v_x(S) = \mathbb{E}[f(X) \mid X_S = x_S]$ uses **conditional** expectations, but in practice KernelSHAP often uses **marginal** expectations (replacing absent features with random samples from the marginal distribution). This can distort attributions when features are correlated, because the marginal approach evaluates the model at implausible feature combinations.

---

## TreeSHAP

### Exact Polynomial-Time Algorithm

For tree-based models (decision trees, random forests, gradient-boosted trees), Lundberg et al. (2020) developed **TreeSHAP**, which computes exact SHAP values in polynomial time.

**Key insight:** For a single decision tree with $L$ leaves, the characteristic function $v_x(S)$ can be computed by propagating the data through the tree while marginalizing over absent features using the training data distribution at each split node.

**Complexity:** $O(L \cdot D^2)$ per instance, where $L$ is the number of leaves and $D$ is the maximum tree depth. For an ensemble of $T$ trees:

$$
\text{Total complexity} = O(T \cdot L \cdot D^2)
$$

This is dramatically faster than the exponential exact computation and enables SHAP analysis of large-scale production models.

### Interventional vs Observational TreeSHAP

TreeSHAP can use either:

- **Observational** (path-dependent): conditions on correlated features jointly
- **Interventional**: breaks correlations by independently marginalizing absent features

The interventional variant is preferred for causal interpretations.

---

## Financial Applications

### Credit Scoring and Adverse Action Notices

Under regulations such as the US Equal Credit Opportunity Act (ECOA), lenders must provide **specific reasons** for credit denials. SHAP values naturally provide this:

Given a credit model $f(x)$ with threshold $\theta$:

$$
f(x) = \phi_0 + \sum_{i=1}^n \phi_i(f, x) < \theta \implies \text{denial}
$$

The features with the largest negative $\phi_i$ are the primary reasons for denial. This satisfies the regulatory requirement for specific, actionable explanations.

### Risk Factor Attribution

For a portfolio risk model $\text{VaR}(x_1, \ldots, x_n)$ where $x_i$ represents exposure to risk factor $i$, SHAP values decompose the total risk:

$$
\text{VaR}(x) = \phi_0 + \sum_{i=1}^n \phi_i
$$

Unlike marginal risk contributions (which assume linearity), SHAP values correctly attribute risk even for nonlinear models, capturing interaction effects.

### Option Pricing Attribution

For a pricing model $V(S, K, T, \sigma, r)$, SHAP values can decompose the price into contributions from each input:

$$
V = \phi_0 + \phi_S + \phi_K + \phi_T + \phi_\sigma + \phi_r
$$

This is particularly useful for exotic derivatives where intuition about sensitivity is limited.

??? example "SHAP for Credit Risk"
    Consider a gradient-boosted tree model for probability of default with features: income, debt-to-income ratio, credit history length, and number of recent inquiries.

    For a specific applicant with $f(x) = 0.15$ (predicted PD) and base value $\phi_0 = 0.05$:

    | Feature | Value | SHAP Value |
    |---------|-------|------------|
    | Income | \$45,000 | +0.02 |
    | Debt-to-income | 0.55 | +0.05 |
    | Credit history | 3 years | +0.02 |
    | Recent inquiries | 4 | +0.01 |

    The largest contributor to elevated default risk is the high debt-to-income ratio ($\phi = +0.05$), followed by short credit history and low income. This decomposition satisfies adverse action notice requirements.

---

## SHAP Interaction Values

### Pairwise Interactions

The **SHAP interaction value** between features $i$ and $j$ is defined as:

$$
\Phi_{ij}(f, x) = \sum_{S \subseteq N \setminus \{i,j\}} \frac{|S|!\,(n - |S| - 2)!}{2(n-1)!}\,\Delta_{ij}(S)
$$

where:

$$
\Delta_{ij}(S) = v_x(S \cup \{i,j\}) - v_x(S \cup \{i\}) - v_x(S \cup \{j\}) + v_x(S)
$$

The main effect and interaction effects satisfy:

$$
\phi_i = \Phi_{ii} + \sum_{j \neq i} \Phi_{ij}
$$

In finance, interactions capture phenomena like: "high leverage combined with short credit history is much riskier than either alone."

---

## Regulatory Interpretability Requirements

### SR 11-7 and Model Explainability

The Federal Reserve's SR 11-7 guidance on model risk management requires that models be **understood** by their users. For machine learning models, SHAP provides:

1. **Local explanations:** Why this specific decision was made
2. **Global feature importance:** Average $|\phi_i|$ across instances
3. **Consistency checks:** Do attributions align with domain knowledge?

### EU AI Act and High-Risk Systems

Financial models classified as high-risk under the EU AI Act must provide:

- Meaningful explanations of automated decisions
- The ability to challenge and correct outcomes
- Documentation of model logic

SHAP values serve as a compliance mechanism, though they explain *what* drives predictions, not *why* in a causal sense.

!!! warning "Limitations of SHAP in Finance"
    - **Not causal:** SHAP values measure association, not causation. A feature may have high SHAP value due to correlation with the true causal driver.
    - **Conditional distribution assumptions:** Results depend on how absent features are handled (marginal vs conditional).
    - **Stability:** SHAP values for individual predictions can be sensitive to small input perturbations, especially in regions with sparse training data.
    - **Gaming risk:** If explanations are disclosed, applicants may learn to manipulate inputs that have high SHAP values without actually reducing risk.

---

## Key Takeaways

- Shapley values are the unique allocation satisfying efficiency, symmetry, null player, and linearity axioms
- SHAP connects Shapley values to machine learning by defining a cooperative game over input features
- KernelSHAP provides a model-agnostic approximation via weighted regression; TreeSHAP gives exact values for tree models in polynomial time
- In finance, SHAP values enable compliant adverse action notices, risk factor attribution, and model validation
- SHAP interaction values capture nonlinear feature interactions important in credit and risk modeling
- Limitations include the non-causal nature of attributions and sensitivity to the treatment of correlated features

---

## Further Reading

- Shapley, L. (1953), "A Value for N-Person Games," in *Contributions to the Theory of Games II*, Princeton University Press
- Lundberg, S. & Lee, S. (2017), "A Unified Approach to Interpreting Model Predictions," *NeurIPS*
- Lundberg, S. et al. (2020), "From Local Explanations to Global Understanding with Explainable AI for Trees," *Nature Machine Intelligence*, 2, 56--67
- Molnar, C. (2022), *Interpretable Machine Learning*, 2nd ed.
- Joseph, A. (2019), "Shapley Regressions: A Framework for Statistical Inference on Machine Learning Models," Bank of England Staff Working Paper No. 784
- Sudjianto, A. & Zhang, A. (2021), "Designing Inherently Interpretable Machine Learning Models," *SSRN*
