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

---

## Exercises

**Exercise 1.** Consider a model $f$ with three features $N = \{1, 2, 3\}$ and characteristic function values $v(\emptyset) = 0$, $v(\{1\}) = 4$, $v(\{2\}) = 2$, $v(\{3\}) = 1$, $v(\{1,2\}) = 8$, $v(\{1,3\}) = 6$, $v(\{2,3\}) = 5$, $v(\{1,2,3\}) = 12$. Compute the exact Shapley value $\phi_i$ for each player using the formula

$$
\phi_i(v) = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|!\,(n - |S| - 1)!}{n!}\,\big[v(S \cup \{i\}) - v(S)\big]
$$

Verify that the efficiency axiom $\phi_1 + \phi_2 + \phi_3 = v(N)$ holds. Then verify symmetry: are any two players symmetric, and do they receive equal Shapley values?

??? success "Solution to Exercise 1"
    **Computing Shapley values for each player.**

    We have $N = \{1, 2, 3\}$, $n = 3$, and the formula:

    $$
    \phi_i(v) = \sum_{S \subseteq N \setminus \{i\}} \frac{|S|!\,(n - |S| - 1)!}{n!}\,\big[v(S \cup \{i\}) - v(S)\big]
    $$

    The weighting coefficients for $n = 3$ are:

    - $|S| = 0$: $\frac{0! \cdot 2!}{3!} = \frac{2}{6} = \frac{1}{3}$
    - $|S| = 1$: $\frac{1! \cdot 1!}{3!} = \frac{1}{6}$
    - $|S| = 2$: $\frac{2! \cdot 0!}{3!} = \frac{2}{6} = \frac{1}{3}$

    **Player 1:** The coalitions $S \subseteq \{2, 3\}$ are $\emptyset, \{2\}, \{3\}, \{2,3\}$.

    $$
    \phi_1 = \frac{1}{3}[v(\{1\}) - v(\emptyset)] + \frac{1}{6}[v(\{1,2\}) - v(\{2\})] + \frac{1}{6}[v(\{1,3\}) - v(\{3\})] + \frac{1}{3}[v(\{1,2,3\}) - v(\{2,3\})]
    $$

    $$
    \phi_1 = \frac{1}{3}(4 - 0) + \frac{1}{6}(8 - 2) + \frac{1}{6}(6 - 1) + \frac{1}{3}(12 - 5)
    $$

    $$
    \phi_1 = \frac{4}{3} + \frac{6}{6} + \frac{5}{6} + \frac{7}{3} = \frac{4}{3} + 1 + \frac{5}{6} + \frac{7}{3}
    $$

    Converting to sixths: $\frac{8}{6} + \frac{6}{6} + \frac{5}{6} + \frac{14}{6} = \frac{33}{6} = \frac{11}{2} = 5.5$

    **Player 2:** The coalitions $S \subseteq \{1, 3\}$ are $\emptyset, \{1\}, \{3\}, \{1,3\}$.

    $$
    \phi_2 = \frac{1}{3}(2 - 0) + \frac{1}{6}(8 - 4) + \frac{1}{6}(5 - 1) + \frac{1}{3}(12 - 6)
    $$

    $$
    \phi_2 = \frac{2}{3} + \frac{4}{6} + \frac{4}{6} + \frac{6}{3} = \frac{4}{6} + \frac{4}{6} + \frac{4}{6} + \frac{12}{6} = \frac{24}{6} = 4
    $$

    **Player 3:** The coalitions $S \subseteq \{1, 2\}$ are $\emptyset, \{1\}, \{2\}, \{1,2\}$.

    $$
    \phi_3 = \frac{1}{3}(1 - 0) + \frac{1}{6}(6 - 4) + \frac{1}{6}(5 - 2) + \frac{1}{3}(12 - 8)
    $$

    $$
    \phi_3 = \frac{1}{3} + \frac{2}{6} + \frac{3}{6} + \frac{4}{3} = \frac{2}{6} + \frac{2}{6} + \frac{3}{6} + \frac{8}{6} = \frac{15}{6} = \frac{5}{2} = 2.5
    $$

    **Verification of efficiency:**

    $$
    \phi_1 + \phi_2 + \phi_3 = 5.5 + 4 + 2.5 = 12 = v(N) \checkmark
    $$

    **Symmetry check.** Two players $i$ and $j$ are symmetric if $v(S \cup \{i\}) = v(S \cup \{j\})$ for all $S \subseteq N \setminus \{i, j\}$. For players 1 and 2, we check coalitions $S \subseteq \{3\}$:

    - $S = \emptyset$: $v(\{1\}) = 4 \neq 2 = v(\{2\})$

    Players 1 and 2 are **not** symmetric, and indeed $\phi_1 = 5.5 \neq 4 = \phi_2$. Similarly, no pair of players is symmetric (one can verify that all pairs have unequal marginal contributions for at least one coalition), consistent with all three Shapley values being distinct.

---

**Exercise 2.** A credit scoring model $f(x)$ produces a probability of default. For a denied applicant with $f(x) = 0.18$ and base value $\phi_0 = \mathbb{E}[f(X)] = 0.06$, the SHAP values are $\phi_{\text{income}} = +0.01$, $\phi_{\text{DTI}} = +0.06$, $\phi_{\text{history}} = +0.03$, $\phi_{\text{inquiries}} = +0.02$. (a) Verify the efficiency property $f(x) = \phi_0 + \sum_i \phi_i$. (b) Rank the features for an adverse action notice as required by ECOA. (c) If the denial threshold is $\theta = 0.10$, identify the minimal set of features whose SHAP contributions, if removed (set to zero), would bring the prediction below the threshold. (d) Discuss why SHAP-based explanations may not satisfy a causal interpretation of "reasons for denial."

??? success "Solution to Exercise 2"
    **(a) Verifying efficiency.**

    $$
    \phi_0 + \phi_{\text{income}} + \phi_{\text{DTI}} + \phi_{\text{history}} + \phi_{\text{inquiries}} = 0.06 + 0.01 + 0.06 + 0.03 + 0.02 = 0.18 = f(x) \checkmark
    $$

    The efficiency property holds: the base value plus all SHAP contributions sum exactly to the model's prediction.

    **(b) Ranking features for adverse action notice.**

    For a denial, we rank features by their positive contribution to the predicted PD (i.e., the features that most increase the default probability above the base rate):

    1. **Debt-to-income ratio** ($\phi_{\text{DTI}} = +0.06$) --- largest contributor
    2. **Credit history length** ($\phi_{\text{history}} = +0.03$)
    3. **Number of recent inquiries** ($\phi_{\text{inquiries}} = +0.02$)
    4. **Income** ($\phi_{\text{income}} = +0.01$) --- smallest contributor

    Under ECOA, the adverse action notice would list these as the primary reasons for denial, in this order. Typically, the top 4 reasons are reported.

    **(c) Minimal set of features to remove for approval.**

    The denial threshold is $\theta = 0.10$. Currently $f(x) = 0.18$. We need to reduce the prediction by at least $0.18 - 0.10 = 0.08$.

    If we "remove" a feature (set its SHAP contribution to zero), the prediction decreases by $\phi_i$. We seek the smallest set $R$ such that $\sum_{i \in R} \phi_i \ge 0.08$.

    - DTI alone: $0.06 < 0.08$ --- insufficient.
    - DTI + history: $0.06 + 0.03 = 0.09 \ge 0.08$ --- sufficient.

    The minimal set is $\{\text{DTI}, \text{history}\}$. Removing the two largest contributors brings the prediction to $0.18 - 0.09 = 0.09 < 0.10$.

    Note: this analysis is approximate. SHAP values are additive decompositions of the *current* prediction, but removing features and recomputing the model may not yield exactly the predicted change, because SHAP values account for interactions that shift when features are removed.

    **(d) Why SHAP-based explanations may not satisfy causal interpretation.**

    SHAP values measure the **associative** contribution of each feature to the prediction, not its **causal** effect. The distinction matters:

    - A high $\phi_{\text{DTI}}$ means that the model associates a high DTI with elevated default risk for this applicant. But DTI may be correlated with other unobserved factors (e.g., medical expenses, divorce) that are the true causal drivers.
    - The adverse action notice says "your high debt-to-income ratio contributed to the denial." The applicant interprets this causally: "if I reduce my DTI, I will be approved." But if the model's learned association is actually driven by a correlated factor, reducing DTI alone may not change the outcome.
    - SHAP values can attribute importance to features that are proxies for protected characteristics (e.g., zip code as a proxy for race), which is associatively correct but causally misleading and potentially discriminatory.

    For a truly causal explanation, one would need a causal model (e.g., a structural equation model or a do-calculus analysis), which SHAP does not provide.

---

**Exercise 3.** For KernelSHAP with $n = 4$ features, compute the SHAP kernel weight $\pi(z)$ for coalitions of size $|z| = 1$, $|z| = 2$, and $|z| = 3$. Recall

$$
\pi(z) = \frac{n - 1}{\binom{n}{|z|}\,|z|\,(n - |z|)}
$$

Show that $\pi(z) \to \infty$ as $|z| \to 0$ or $|z| \to n$ (i.e., the kernel diverges for the empty and full coalitions). Explain intuitively why very small and very large coalitions receive the highest weight in the regression. How does the sampling approximation handle this divergence in practice?

??? success "Solution to Exercise 3"
    **Computing the SHAP kernel weights for $n = 4$.**

    The SHAP kernel is:

    $$
    \pi(z) = \frac{n - 1}{\binom{n}{|z|}\,|z|\,(n - |z|)} = \frac{3}{\binom{4}{|z|}\,|z|\,(4 - |z|)}
    $$

    **For $|z| = 1$:**

    $$
    \pi = \frac{3}{\binom{4}{1} \cdot 1 \cdot 3} = \frac{3}{4 \cdot 1 \cdot 3} = \frac{3}{12} = \frac{1}{4}
    $$

    **For $|z| = 2$:**

    $$
    \pi = \frac{3}{\binom{4}{2} \cdot 2 \cdot 2} = \frac{3}{6 \cdot 2 \cdot 2} = \frac{3}{24} = \frac{1}{8}
    $$

    **For $|z| = 3$:**

    $$
    \pi = \frac{3}{\binom{4}{3} \cdot 3 \cdot 1} = \frac{3}{4 \cdot 3 \cdot 1} = \frac{3}{12} = \frac{1}{4}
    $$

    **Divergence at $|z| \to 0$ and $|z| \to n$.**

    For $|z| = 0$: $\pi = \frac{3}{\binom{4}{0} \cdot 0 \cdot 4}$. The denominator contains the factor $|z| = 0$, so $\pi \to \infty$.

    For $|z| = 4 = n$: $\pi = \frac{3}{\binom{4}{4} \cdot 4 \cdot 0}$. The denominator contains the factor $(n - |z|) = 0$, so $\pi \to \infty$.

    In general, $\pi(z) \propto \frac{1}{|z|(n-|z|)}$, which diverges as $|z| \to 0$ or $|z| \to n$.

    **Intuitive explanation.** Very small coalitions ($|z| \approx 0$) and very large coalitions ($|z| \approx n$) are the most informative for determining individual Shapley values because:

    - With $|z| = 1$ (only one feature present), the characteristic function $v_x(\{i\})$ directly reveals the "standalone" value of feature $i$.
    - With $|z| = n - 1$ (only one feature absent), $v_x(N \setminus \{i\})$ reveals the value of the grand coalition minus feature $i$, giving the marginal contribution of $i$ to the full model.

    Coalitions of intermediate size ($|z| \approx n/2$) are less informative because many different features are present, making it harder to isolate individual contributions.

    **Handling divergence in practice.** In the sampling approximation, the empty ($|z| = 0$) and full ($|z| = n$) coalitions are handled separately:

    - $v_x(\emptyset) = \phi_0 = \mathbb{E}[f(X)]$ and $v_x(N) = f(x)$ are computed exactly (they are just the base value and the prediction).
    - These two extreme points are included as exact constraints in the weighted regression, not sampled with infinite weight.
    - The remaining coalitions ($1 \le |z| \le n-1$) are sampled with finite weights, and the regression is solved with these samples.

    This ensures numerical stability while respecting the theoretical requirement that the empty and full coalitions carry the most information.

---

**Exercise 4.** TreeSHAP has complexity $O(T \cdot L \cdot D^2)$ per instance for an ensemble of $T$ trees, each with $L$ leaves and maximum depth $D$. (a) For a gradient-boosted model with $T = 500$ trees, $D = 8$, and $L = 200$ leaves per tree, compute the cost per instance and compare it to the exact exponential computation $O(2^n)$ for $n = 50$ features. (b) Explain why the polynomial-time algorithm is possible for trees but not for arbitrary models. (c) Discuss the difference between observational and interventional TreeSHAP when features are correlated: if income and education are positively correlated, how might the two variants differ in attributing importance to education?

??? success "Solution to Exercise 4"
    **(a) Cost comparison.**

    **TreeSHAP cost:** $O(T \cdot L \cdot D^2) = O(500 \cdot 200 \cdot 8^2) = O(500 \cdot 200 \cdot 64) = O(6{,}400{,}000)$ operations per instance. This is approximately $6.4 \times 10^6$ elementary operations.

    **Exact Shapley computation:** $O(2^n) = O(2^{50}) \approx 1.13 \times 10^{15}$ evaluations of the characteristic function. Each evaluation requires a full model forward pass.

    The ratio is:

    $$
    \frac{2^{50}}{6.4 \times 10^6} \approx \frac{1.13 \times 10^{15}}{6.4 \times 10^6} \approx 1.76 \times 10^8
    $$

    TreeSHAP is approximately **176 million times faster** than exact computation. The exact computation is utterly infeasible ($2^{50} \approx 10^{15}$ evaluations), while TreeSHAP can process thousands of instances per second.

    **(b) Why polynomial time is possible for trees.**

    Tree-based models have a special structure that enables efficient computation:

    - **Recursive decomposition:** A decision tree partitions the input space into disjoint regions (leaves). For any coalition $S$, the characteristic function $v_x(S)$ can be computed by propagating through the tree: at each node, if the splitting feature is in $S$, follow the branch determined by $x$; if not, average over both branches weighted by the training data distribution.
    - **Shared subproblems:** The tree structure means that many coalitions share the same path down to a certain depth, enabling dynamic programming to reuse computations.
    - **Finite depth:** The tree has depth $D$, so only $D$ features are actually used in any root-to-leaf path. The Shapley value computation only needs to consider subsets of these $D$ features (at most $2^D$ subsets), not all $2^n$ subsets of input features.

    For arbitrary models (e.g., neural networks), no such structure exists. The characteristic function $v_x(S)$ requires marginalizing over absent features, which generally requires a separate model evaluation for each coalition. Without structural shortcuts, the exponential enumeration cannot be avoided.

    **(c) Observational vs interventional TreeSHAP with correlated features.**

    Consider income and education, which are positively correlated.

    **Observational TreeSHAP:** When marginalizing over absent features, it respects the observed data distribution, including correlations. If education is absent from coalition $S$, the algorithm conditions on the observed relationship: high income implies high education. This means education receives less credit because its effect is partially captured through the income-education correlation.

    **Interventional TreeSHAP:** When marginalizing over absent features, it breaks correlations by sampling each absent feature independently from its marginal distribution. This answers the counterfactual question: "what would happen if we *intervened* to set education to a random value, regardless of income?"

    **Example:** Suppose the model predicts lower default risk for high education. An applicant has high income and high education.

    - Observational: Education's SHAP value may be small because, conditional on high income, high education is expected (the correlation absorbs education's contribution into income).
    - Interventional: Education's SHAP value will be larger because the method asks what happens if education were randomly assigned, breaking the correlation with income. The full effect of education on the prediction is attributed to education.

    The interventional variant is preferred when the goal is to understand which features the model *uses* (a causal question), rather than which features are *associated* with the prediction (a correlational question).

---

**Exercise 5.** The SHAP interaction value between features $i$ and $j$ is based on

$$
\Delta_{ij}(S) = v_x(S \cup \{i,j\}) - v_x(S \cup \{i\}) - v_x(S \cup \{j\}) + v_x(S)
$$

Using the characteristic function from Exercise 1, compute $\Delta_{12}(S)$ for all $S \subseteq \{3\}$ (i.e., $S = \emptyset$ and $S = \{3\}$). Then compute the SHAP interaction value $\Phi_{12}$. Interpret the sign: does the interaction between players 1 and 2 exhibit complementarity ($\Delta_{12} > 0$) or substitutability ($\Delta_{12} < 0$)? Relate this to a financial example where two risk factors interact nonlinearly.

??? success "Solution to Exercise 5"
    **Computing $\Delta_{12}(S)$ for $S \subseteq \{3\}$.**

    Recall: $\Delta_{ij}(S) = v(S \cup \{i,j\}) - v(S \cup \{i\}) - v(S \cup \{j\}) + v(S)$.

    **For $S = \emptyset$:**

    $$
    \Delta_{12}(\emptyset) = v(\{1,2\}) - v(\{1\}) - v(\{2\}) + v(\emptyset) = 8 - 4 - 2 + 0 = 2
    $$

    **For $S = \{3\}$:**

    $$
    \Delta_{12}(\{3\}) = v(\{1,2,3\}) - v(\{1,3\}) - v(\{2,3\}) + v(\{3\}) = 12 - 6 - 5 + 1 = 2
    $$

    **Computing the SHAP interaction value $\Phi_{12}$.**

    The formula is:

    $$
    \Phi_{ij} = \sum_{S \subseteq N \setminus \{i,j\}} \frac{|S|!\,(n - |S| - 2)!}{2(n-1)!}\,\Delta_{ij}(S)
    $$

    For $n = 3$, $N \setminus \{1,2\} = \{3\}$, so $S \in \{\emptyset, \{3\}\}$.

    **For $S = \emptyset$ ($|S| = 0$):**

    $$
    \text{weight} = \frac{0! \cdot (3 - 0 - 2)!}{2 \cdot 2!} = \frac{1 \cdot 1}{2 \cdot 2} = \frac{1}{4}
    $$

    **For $S = \{3\}$ ($|S| = 1$):**

    $$
    \text{weight} = \frac{1! \cdot (3 - 1 - 2)!}{2 \cdot 2!} = \frac{1 \cdot 0!}{2 \cdot 2} = \frac{1}{4}
    $$

    Therefore:

    $$
    \Phi_{12} = \frac{1}{4} \cdot 2 + \frac{1}{4} \cdot 2 = \frac{1}{2} + \frac{1}{2} = 1
    $$

    **Interpretation.**

    Since $\Delta_{12}(S) = 2 > 0$ for both coalitions, the interaction between players 1 and 2 exhibits **complementarity**: the combined value of having both players exceeds the sum of their individual contributions. Adding player 2 to a coalition that already contains player 1 is worth more than adding player 2 to a coalition without player 1 (and vice versa).

    **Financial example.** Consider two risk factors: leverage ratio (player 1) and interest rate sensitivity (player 2). Individually, each contributes moderately to portfolio risk. But together, they interact nonlinearly: a highly leveraged portfolio with high rate sensitivity is far riskier than the sum of the two individual risks, because rising rates simultaneously increase funding costs and reduce asset values. This complementarity ($\Delta_{12} > 0$) means the interaction effect amplifies the total risk beyond what a linear risk model would predict.

---

**Exercise 6.** A portfolio risk model computes $\text{VaR}(x) = 15.2\%$ for a portfolio with exposures to four asset classes. SHAP decomposes this as $\phi_0 = 5.0\%$, $\phi_{\text{equity}} = 4.8\%$, $\phi_{\text{credit}} = 3.1\%$, $\phi_{\text{rates}} = 1.5\%$, $\phi_{\text{FX}} = 0.8\%$. (a) Verify efficiency. (b) Compare these SHAP-based risk attributions with the Euler allocation (marginal contributions scaled to sum to total): under what conditions would Euler allocation and SHAP attribution agree? (c) The portfolio manager wants to reduce VaR to below 12%. Using the SHAP decomposition, suggest a reallocation strategy. (d) Discuss why SHAP attributions might be misleading if VaR is not subadditive (i.e., when diversification benefits are negative).

??? success "Solution to Exercise 6"
    **(a) Verifying efficiency.**

    $$
    \phi_0 + \phi_{\text{equity}} + \phi_{\text{credit}} + \phi_{\text{rates}} + \phi_{\text{FX}} = 5.0 + 4.8 + 3.1 + 1.5 + 0.8 = 15.2\% = \text{VaR}(x) \checkmark
    $$

    **(b) Comparison with Euler allocation.**

    The **Euler allocation** (or marginal contribution allocation) assigns to each asset class its marginal contribution scaled to sum to the total:

    $$
    \text{RC}_i^{\text{Euler}} = x_i \frac{\partial \text{VaR}}{\partial x_i}, \quad \sum_i \text{RC}_i^{\text{Euler}} = \text{VaR}
    $$

    This is valid when VaR is a **homogeneous function of degree 1** in the exposures $x_i$ (Euler's theorem). This holds when the portfolio return is a linear function of exposures and the risk measure is applied to this linear combination.

    **When Euler and SHAP agree:**

    - If the risk model is **linear** in exposures: $\text{VaR}(x) = \sum_i a_i x_i$ for some coefficients $a_i$, then both Euler allocation and Shapley values reduce to $\phi_i = a_i x_i$, and they agree exactly.
    - More generally, if the model is linear (no interaction effects between features), SHAP values equal the linear coefficients, which coincide with marginal contributions.

    **When they disagree:**

    - If the risk model is **nonlinear** (e.g., a neural network or a model with significant interaction effects), Euler allocation may not be well-defined (VaR may not be homogeneous of degree 1), or it may produce different attributions than SHAP because Euler captures only marginal effects while SHAP averages over all coalition orderings, accounting for interactions.
    - If the risk measure is not positively homogeneous (e.g., Expected Shortfall in some formulations), Euler's theorem does not apply.

    **(c) Reallocation strategy to reduce VaR below 12%.**

    Current VaR: 15.2%. Target: < 12%. Required reduction: > 3.2%.

    The SHAP decomposition suggests focusing on the largest contributors:

    - **Equity** ($\phi = 4.8\%$): Reducing equity exposure would have the largest impact. A proportional reduction of equity exposure by approximately $3.2/4.8 \approx 67\%$ would (approximately) reduce the equity contribution to $\sim 1.6\%$, bringing total VaR to $\sim 12.0\%$.
    - Alternatively, a combined reduction: reduce equity exposure by 50% ($-2.4\%$ contribution) and credit exposure by 30% ($-0.93\%$), for a combined reduction of $\sim 3.3\%$.

    **Caveat:** These are linear approximations. SHAP values decompose the *current* risk, but the risk function is nonlinear. Rebalancing the portfolio changes the correlations and interaction effects, so the actual VaR after reallocation must be recomputed.

    **(d) Potential for misleading attributions when VaR is not subadditive.**

    VaR is known to violate subadditivity in certain cases:

    $$
    \text{VaR}(X + Y) > \text{VaR}(X) + \text{VaR}(Y)
    $$

    When diversification benefits are negative (concentrated tail risks), the SHAP decomposition may be misleading because:

    - The efficiency axiom forces $\sum_i \phi_i = \text{VaR}(N) - \phi_0$, but individual $\phi_i$ values may not accurately reflect the *incremental* risk of each asset class.
    - A portfolio manager might reduce exposure to the highest-SHAP asset class, only to find that VaR increases because the removed asset was providing tail diversification that was not captured in the SHAP attribution.
    - SHAP values can be negative (indicating diversification benefit) for some asset classes, but the lack of subadditivity means that removing a "diversifying" asset class (negative SHAP) does not guarantee VaR increases by the expected amount.

    For risk management applications, SHAP should be supplemented with stress testing and scenario analysis to capture tail dependencies that additive decompositions may miss.

---

**Exercise 7.** A bank deploys a neural network credit model and uses KernelSHAP with $M = 500$ samples for adverse action explanations. (a) Discuss the statistical uncertainty in the SHAP estimates: how would you construct confidence intervals for individual $\phi_i$ values? (b) If two features have SHAP values $\phi_1 = -0.03 \pm 0.02$ and $\phi_2 = -0.025 \pm 0.02$, can you reliably rank them for the adverse action notice? (c) KernelSHAP uses marginal expectations rather than conditional expectations. For a model with correlated features (e.g., income and zip code), explain how this can lead to attributions based on implausible feature combinations and propose a correction. (d) Discuss the gaming risk: if a bank discloses that "number of recent credit inquiries" has the highest SHAP value for denial, how might applicants respond, and does this actually reduce the bank's credit risk?

??? success "Solution to Exercise 7"
    **(a) Confidence intervals for KernelSHAP estimates.**

    KernelSHAP solves a weighted least squares regression on $M = 500$ sampled coalitions. The SHAP values $\hat{\phi}_i$ are regression coefficients, and their uncertainty can be quantified using standard regression theory:

    $$
    \hat{\phi} = (Z^\top W Z)^{-1} Z^\top W y
    $$

    where $Z$ is the $M \times (n+1)$ design matrix of coalition vectors, $W = \text{diag}(\pi(z^{(1)}), \ldots, \pi(z^{(M)}))$ is the weight matrix, and $y$ is the vector of characteristic function evaluations.

    The covariance of $\hat{\phi}$ is:

    $$
    \text{Cov}(\hat{\phi}) = \hat{\sigma}^2 (Z^\top W Z)^{-1}
    $$

    where $\hat{\sigma}^2$ is the estimated residual variance. Approximate 95% confidence intervals are:

    $$
    \hat{\phi}_i \pm 1.96 \sqrt{\text{Var}(\hat{\phi}_i)}
    $$

    Alternatively, a **bootstrap** approach: resample the $M$ coalitions with replacement, recompute $\hat{\phi}$ for each bootstrap sample, and use the empirical quantiles as confidence intervals. This is more robust to non-normality.

    Increasing $M$ reduces the confidence interval width proportionally to $1/\sqrt{M}$.

    **(b) Reliability of feature ranking.**

    With $\phi_1 = -0.03 \pm 0.02$ and $\phi_2 = -0.025 \pm 0.02$, the difference is:

    $$
    \phi_1 - \phi_2 = -0.005
    $$

    The standard error of the difference (assuming independence) is:

    $$
    \text{SE}(\phi_1 - \phi_2) = \sqrt{0.02^2 + 0.02^2} = 0.02\sqrt{2} \approx 0.0283
    $$

    The signal-to-noise ratio is $|{-0.005}|/0.0283 \approx 0.18$, far below the threshold for statistical significance. The 95% confidence interval for the difference is approximately $-0.005 \pm 0.055$, which comfortably includes zero.

    **Conclusion:** No, the ranking is **not reliable**. The two features have SHAP values that are statistically indistinguishable. Reporting feature 1 as more important than feature 2 in an adverse action notice would not be justified by the data. In practice, when features have overlapping confidence intervals, the institution should either: (i) increase $M$ to reduce uncertainty, (ii) report both features as equally contributing, or (iii) use a more conservative ranking that acknowledges estimation uncertainty.

    **(c) Marginal vs conditional expectations with correlated features.**

    KernelSHAP typically uses **marginal expectations**: when feature $j$ is absent from coalition $S$, it is replaced by random draws from the marginal distribution $P(X_j)$, independent of the features in $S$.

    **Problem with correlated features.** If income and zip code are correlated (wealthy zip codes have higher incomes), the marginal approach creates implausible combinations. For example, it might evaluate the model with:

    - Income = \$200,000 (from the instance) and zip code = low-income neighborhood (from the marginal distribution)

    This combination is rare or nonexistent in the real data. The model's prediction at this implausible point may be unreliable (the model was never trained on such inputs), and the resulting SHAP values may be distorted.

    Specifically, income may receive disproportionate attribution because it "explains" variance that is actually shared with zip code: when zip code is marginalized independently, income appears uniquely important, but in reality their effects are confounded.

    **Proposed corrections:**

    1. **Conditional SHAP:** Replace the marginal distribution with the conditional: $v_x(S) = \mathbb{E}[f(X) \mid X_S = x_S]$, using the true conditional distribution of absent features given present features. This avoids implausible combinations but is harder to estimate (requires modeling feature dependencies).

    2. **Coalitional SHAP with data-driven conditional sampling:** When marginalizing absent features, sample from the empirical conditional distribution (e.g., using nearest neighbors in the feature space or a fitted conditional density model).

    3. **Interventional TreeSHAP (for tree models):** Uses the tree structure to compute conditional expectations more accurately, though it still involves approximations for correlated features.

    **(d) Gaming risk from disclosure of SHAP explanations.**

    If the bank discloses that "number of recent credit inquiries" has the highest SHAP value for denial, applicants may respond by:

    - **Avoiding credit inquiries:** Refraining from applying for new credit in the months before a loan application. This is easy to manipulate because inquiries are under the applicant's direct control.
    - **Timing applications strategically:** Spacing out credit applications to keep the inquiry count low.

    **Does this reduce the bank's credit risk?** The answer is nuanced:

    - If high inquiries are a **causal** risk factor (more inquiries reflect genuine credit-seeking behavior due to financial distress), then gaming does not reduce actual risk---the underlying financial distress persists even if the inquiry count is artificially low. The bank's model becomes less informative.
    - If high inquiries are merely a **correlate** of risk (associated with risk but not causing it), then gaming is even more problematic: the applicant manipulates an input that was never causally linked to default, and the model's predictive power degrades without any actual risk reduction.
    - Over time, widespread gaming would reduce the predictive power of the inquiry feature, forcing the bank to reweight its model or find alternative signals.

    **Mitigation strategies:**

    - Use features that are harder to manipulate (e.g., payment history, time since last delinquency) as primary risk factors.
    - Monitor for gaming patterns (sudden drops in inquiry counts that are inconsistent with overall credit behavior).
    - Provide explanations at a level of abstraction that is informative but not easily actionable for gaming (e.g., "credit utilization patterns" rather than the specific feature name and threshold).
    - Recognize that some degree of gaming is inevitable and build robustness into the model by diversifying the feature set.
