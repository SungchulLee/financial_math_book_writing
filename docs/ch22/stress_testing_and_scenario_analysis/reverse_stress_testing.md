# Reverse Stress Testing

Reverse stress testing is a powerful complement to traditional stress testing. Instead of asking "what happens under this scenario?", reverse stress testing asks **"what scenarios would break the institution?"**

---

## Concept

### Traditional Stress Testing (Forward)

$$
\text{Scenario } \mathcal{S} \xrightarrow{\text{Impact Analysis}} \text{Loss } L^\mathcal{S}
$$

Ask: "Given scenario $\mathcal{S}$, what is the loss?"

### Reverse Stress Testing (Backward)

$$
\text{Failure Threshold } L^* \xrightarrow{\text{Scenario Search}} \text{Scenarios } \{\mathcal{S}: L^\mathcal{S} \ge L^*\}
$$

Ask: "What scenarios would cause losses exceeding threshold $L^*$?"

---

## Motivation

### Why Reverse Stress Testing?

**1. Exposes Hidden Assumptions**
Traditional scenarios reflect past crises or regulatory prescriptions. Reverse stress testing identifies threats not previously imagined.

**2. Identifies Concentration Risks**
The search reveals which factor combinations are most dangerous—often exposing hidden concentrations.

**3. Challenges Business-as-Usual Thinking**
Forces management to confront uncomfortable possibilities.

**4. Regulatory Requirement**
Required under Basel III, UK PRA, and other frameworks.

---

## Methodology

### Step 1: Define Failure Threshold

The failure threshold $L^*$ could be:

- **Capital breach:** Losses that would violate regulatory capital requirements
- **Solvency breach:** Losses exceeding equity capital
- **Liquidity breach:** Cash outflows exceeding liquidity buffer
- **Business viability:** Losses that would trigger regulatory intervention

**Example:** $L^* = $ CET1 capital buffer (losses that would breach minimum capital ratios).

### Step 2: Identify Portfolio Losses Required

Given current portfolio, calculate the loss required to reach failure:

$$
L^{\text{required}} = L^* - \text{Current Buffer}
$$

For a bank with \$10B capital buffer:
- Failure threshold: Capital < 0
- Required loss: \$10B

### Step 3: Construct Scenarios

Find risk factor configurations $\mathbf{x}$ such that:

$$
L(\mathbf{x}) \ge L^{\text{required}}
$$

This is typically a large set—characterize its structure.

### Step 4: Assess Plausibility

For identified scenarios, evaluate:
- Historical precedent
- Economic coherence
- Causal narrative
- Warning indicators

**Key insight:** Probability is secondary to plausibility in reverse stress testing.

---

## Mathematical Formulation

### Optimization Approach

Find the "most plausible" scenario causing failure:

$$
\mathbf{x}^* = \arg\min_{\mathbf{x}} \text{Implausibility}(\mathbf{x}) \quad \text{s.t.} \quad L(\mathbf{x}) \ge L^*
$$

where $\text{Implausibility}(\mathbf{x})$ could be:

**Mahalanobis distance:**

$$
D(\mathbf{x}) = \sqrt{(\mathbf{x} - \boldsymbol{\mu})^\top \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu})}
$$

**Kullback-Leibler divergence:** From historical distribution to scenario.

**Entropic distance:** Related to large deviations theory.

### Lagrangian Formulation

$$
\mathcal{L}(\mathbf{x}, \lambda) = D(\mathbf{x}) - \lambda(L(\mathbf{x}) - L^*)
$$

First-order conditions:

$$
\nabla D(\mathbf{x}) = \lambda \nabla L(\mathbf{x})
$$

The gradient of plausibility aligns with the gradient of loss—the most dangerous direction with given plausibility.

---

## Sensitivity-Based Reverse Stress Testing

For linear portfolios, the loss function is:

$$
L(\mathbf{x}) = -\boldsymbol{\delta}^\top (\mathbf{x} - \mathbf{x}_0)
$$

where $\boldsymbol{\delta}$ is the vector of delta sensitivities.

**Minimum plausibility failure:**

$$
\mathbf{x}^* = \mathbf{x}_0 + \frac{L^*}{\boldsymbol{\delta}^\top \boldsymbol{\Sigma} \boldsymbol{\delta}} \boldsymbol{\Sigma} \boldsymbol{\delta}
$$

The most plausible failure scenario moves factors in the direction $\boldsymbol{\Sigma} \boldsymbol{\delta}$—the covariance-weighted sensitivity direction.

---

## Multiple Failure Scenarios

There are typically **many** scenarios causing failure. Characterize the failure set:

### Failure Region

$$
\mathcal{F} = \{\mathbf{x} : L(\mathbf{x}) \ge L^*\}
$$

### Boundary Scenarios

The boundary $\partial \mathcal{F}$ represents **minimal failure scenarios**—the smallest moves that just trigger failure.

### Diverse Scenarios

Generate multiple scenarios along the boundary:
- Different economic narratives
- Different factor combinations
- Different time horizons

This provides a richer picture of vulnerabilities.

---

## Example: Bank Reverse Stress Test

### Portfolio
- \$100B loan book (corporate, consumer, mortgage)
- \$20B trading book (rates, credit, equity)
- \$15B CET1 capital

### Failure Threshold
CET1 ratio < 4.5% (regulatory minimum)
- Required capital: \$4.5B (assuming 4.5% of \$100B RWA)
- Failure loss: \$15B − \$4.5B = **\$10.5B**

### Reverse Stress Analysis

**Scenario 1: Credit Losses**
- Corporate defaults: 8% default rate, 60% LGD
- Consumer defaults: 12% default rate, 80% LGD
- Mortgage losses: 5% default rate, 50% LGD
- Combined credit loss: \$10B+

**Scenario 2: Market + Credit**
- Equity trading loss: \$2B
- Rates trading loss: \$1.5B
- Credit spread widening: \$3B
- Loan impairments: \$5B

**Scenario 3: Liquidity Crisis**
- Funding costs spike
- Fire sale losses on assets
- Operational strain

### Plausibility Assessment

| Scenario | Historical Analog | Plausibility |
|----------|------------------|--------------|
| Pure credit | 2008-2009 | Moderate |
| Market + credit | 2008 (more severe) | Lower |
| Liquidity | 2008, regional crises | Moderate |

---

## Governance

### Board and Senior Management

- Results presented to board at least annually
- Discussion of implications and mitigants
- Challenge of assumptions and scope

### Documentation Requirements

For each failure scenario:
- Economic narrative
- Factor specifications
- Impact calculations
- Plausibility assessment
- Management actions
- Monitoring indicators

### Action Planning

For identified vulnerabilities:
- Early warning indicators
- Contingency actions
- Recovery options
- Communication plans

---

## Integration with Risk Framework

### Link to Risk Appetite

- Failure scenarios should be outside risk appetite
- If plausible scenarios breach appetite, action required

### Link to Capital Planning

- Capital buffers should absorb plausible scenarios
- Stress capital buffer calibration

### Link to Recovery Planning

- Failure scenarios inform recovery plan triggers
- Identify recovery actions for each scenario type

---

## Challenges

### Subjectivity
Scenario construction involves judgment—different analysts may find different scenarios.

### Computational Complexity
For nonlinear portfolios, finding failure scenarios requires optimization over high-dimensional spaces.

### Plausibility Assessment
No objective measure of scenario plausibility exists.

### Management Resistance
Results can be uncomfortable; may face pushback.

### Completeness
Cannot guarantee all failure scenarios are identified.

---

## Algorithmic Approaches

### Gradient-Based Search
Use automatic differentiation to compute $\nabla L(\mathbf{x})$ and search along steepest ascent.

### Evolutionary Algorithms
Genetic algorithms can explore diverse failure scenarios.

### Importance Sampling
Tilt sampling distribution toward high-loss regions.

### Machine Learning
Train surrogate models for $L(\mathbf{x})$ to enable fast scenario evaluation.

---

## Key Takeaways

- Reverse stress testing starts from failure and works backward to scenarios
- It complements forward stress testing by revealing unknown vulnerabilities
- The mathematical problem is finding minimum-plausibility scenarios that exceed loss thresholds
- Multiple failure scenarios should be identified, not just one
- Results feed into capital planning, recovery planning, and risk appetite
- Governance requires board engagement and clear documentation

---

## Further Reading

- Basel Committee on Banking Supervision, "Principles for Sound Stress Testing Practices"
- PRA, "Stress Testing and Scenario Analysis"
- Glasserman, P. & Xu, X. (2014), "Robust Risk Measurement and Model Risk"
- Breuer, T., Jandačka, M., Rheinberger, K., & Summer, M. (2009), "How to Find Plausible, Severe, and Useful Stress Scenarios"
- McNeil, A. & Smith, A. (2012), "Multivariate Stress Scenarios and Solvency"

---

## Exercises

**Exercise 1.** A bank has CET1 capital of \$20 billion, RWA of \$250 billion, and a regulatory minimum CET1 ratio of 4.5%. Compute the failure loss threshold $L^*$ (the amount of loss that would bring the CET1 ratio exactly to the minimum). If expected PPNR over the stress horizon is \$6 billion, what is the net failure loss from credit, market, and operational risks?

---

**Exercise 2.** For a linear portfolio with loss function $L(\mathbf{x}) = -\boldsymbol{\delta}^\top (\mathbf{x} - \mathbf{x}_0)$ and Mahalanobis distance as the plausibility measure, the most plausible failure scenario is

$$
\mathbf{x}^* = \mathbf{x}_0 + \frac{L^*}{\boldsymbol{\delta}^\top \boldsymbol{\Sigma} \boldsymbol{\delta}} \boldsymbol{\Sigma} \boldsymbol{\delta}
$$

Suppose $\boldsymbol{\delta} = (5, 3)^\top$ (in billions per unit factor move) and $\boldsymbol{\Sigma} = \begin{pmatrix} 1 & 0.5 \\ 0.5 & 2 \end{pmatrix}$. For a failure threshold of $L^* = 10$ billion, compute $\mathbf{x}^*$ and its Mahalanobis distance. Interpret the direction of the most plausible failure scenario.

---

**Exercise 3.** Explain why the first-order condition $\nabla D(\mathbf{x}) = \lambda \nabla L(\mathbf{x})$ implies that the most plausible failure scenario lies at a point where the iso-plausibility contour is tangent to the loss contour $L(\mathbf{x}) = L^*$. Draw a sketch in two dimensions illustrating the failure region $\mathcal{F}$, the Mahalanobis distance contours, and the optimal scenario $\mathbf{x}^*$.

---

**Exercise 4.** A portfolio has three main risk exposures: equity (delta = \$200M per 1%), interest rates (delta = \$150M per 100 bps), and credit spreads (delta = \$100M per 100 bps). The failure threshold requires a loss of \$5 billion. Construct three distinct reverse stress scenarios along the failure boundary $L(\mathbf{x}) = L^*$ that correspond to (a) a pure equity crash, (b) a combined equity and credit event, and (c) a rates-driven scenario. For each, specify the required factor moves and briefly assess plausibility relative to historical episodes.

---

**Exercise 5.** Discuss the relationship between reverse stress testing and recovery planning. If a reverse stress test identifies a scenario in which the bank's CET1 ratio falls to 3.0% (below the 4.5% minimum), describe at least four specific recovery actions the bank could take to restore capital adequacy. For each action, estimate the capital benefit and the time required, and discuss potential constraints or side effects.

---

**Exercise 6.** A risk analyst uses importance sampling to search for failure scenarios. The sampling distribution is tilted as $f^{\text{tilted}}(\mathbf{x}) \propto f(\mathbf{x}) \cdot \exp(\theta \cdot L(\mathbf{x}))$ where $\theta > 0$ is the tilt parameter. Explain how increasing $\theta$ concentrates samples in the failure region. What is the tradeoff in choosing $\theta$? How does the analyst recover unbiased probability estimates from the tilted samples (i.e., what is the importance weight)?

---

**Exercise 7.** Consider a bank with exposures to both market risk and credit risk. Argue that the failure region $\mathcal{F} = \{\mathbf{x} : L(\mathbf{x}) \ge L^*\}$ may be non-convex when the portfolio contains options or other nonlinear instruments. Provide a specific example of a portfolio where two distinct scenarios $\mathbf{x}_1, \mathbf{x}_2 \in \mathcal{F}$ exist but their midpoint $(\mathbf{x}_1 + \mathbf{x}_2)/2 \notin \mathcal{F}$. What challenges does non-convexity pose for algorithmic scenario search?
