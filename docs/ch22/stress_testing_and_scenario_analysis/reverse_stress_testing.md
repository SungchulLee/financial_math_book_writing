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

??? success "Solution to Exercise 1"

    **Step 1: Compute the failure loss threshold $L^*$.**

    The bank has CET1 capital of \$20 billion and RWA of \$250 billion. The current CET1 ratio is:

    $$
    \text{CET1 Ratio}_0 = \frac{20}{250} = 8.0\%
    $$

    The regulatory minimum CET1 ratio is 4.5%. The capital at the minimum ratio is:

    $$
    K_{\min} = 4.5\% \times 250 = \$11.25 \text{ billion}
    $$

    The failure loss threshold (loss that brings CET1 exactly to the minimum) is:

    $$
    L^* = K_0 - K_{\min} = 20 - 11.25 = \$8.75 \text{ billion}
    $$

    **Step 2: Compute the net failure loss accounting for PPNR.**

    Expected PPNR over the stress horizon is \$6 billion. This revenue partially absorbs losses. The gross losses from credit, market, and operational risks must exceed:

    $$
    L^{\text{net}} = L^* + \text{PPNR} = 8.75 + 6 = \$14.75 \text{ billion}
    $$

    In other words, the bank can sustain up to \$14.75 billion in gross losses before breaching the minimum CET1 ratio, because \$6 billion of those losses is offset by earnings.

    **Interpretation:** The reverse stress test must find scenarios that generate at least \$14.75 billion in combined credit, market, and operational losses. Any scenario producing less than this amount does not trigger failure, assuming PPNR materializes as projected. Note that under severe stress, PPNR itself may decline (compressed margins, lower fee income), so the \$6 billion PPNR figure may be optimistic and should be stressed as well.

---

**Exercise 2.** For a linear portfolio with loss function $L(\mathbf{x}) = -\boldsymbol{\delta}^\top (\mathbf{x} - \mathbf{x}_0)$ and Mahalanobis distance as the plausibility measure, the most plausible failure scenario is

$$
\mathbf{x}^* = \mathbf{x}_0 + \frac{L^*}{\boldsymbol{\delta}^\top \boldsymbol{\Sigma} \boldsymbol{\delta}} \boldsymbol{\Sigma} \boldsymbol{\delta}
$$

Suppose $\boldsymbol{\delta} = (5, 3)^\top$ (in billions per unit factor move) and $\boldsymbol{\Sigma} = \begin{pmatrix} 1 & 0.5 \\ 0.5 & 2 \end{pmatrix}$. For a failure threshold of $L^* = 10$ billion, compute $\mathbf{x}^*$ and its Mahalanobis distance. Interpret the direction of the most plausible failure scenario.

??? success "Solution to Exercise 2"

    **Given:**

    - $\boldsymbol{\delta} = (5, 3)^\top$ (billions per unit factor move)
    - $\boldsymbol{\Sigma} = \begin{pmatrix} 1 & 0.5 \\ 0.5 & 2 \end{pmatrix}$
    - $L^* = 10$ billion

    **Step 1: Compute $\boldsymbol{\Sigma}\boldsymbol{\delta}$.**

    $$
    \boldsymbol{\Sigma}\boldsymbol{\delta} = \begin{pmatrix} 1 & 0.5 \\ 0.5 & 2 \end{pmatrix}\begin{pmatrix} 5 \\ 3 \end{pmatrix} = \begin{pmatrix} 5 + 1.5 \\ 2.5 + 6 \end{pmatrix} = \begin{pmatrix} 6.5 \\ 8.5 \end{pmatrix}
    $$

    **Step 2: Compute $\boldsymbol{\delta}^\top\boldsymbol{\Sigma}\boldsymbol{\delta}$.**

    $$
    \boldsymbol{\delta}^\top\boldsymbol{\Sigma}\boldsymbol{\delta} = (5, 3)\begin{pmatrix} 6.5 \\ 8.5 \end{pmatrix} = 32.5 + 25.5 = 58
    $$

    **Step 3: Compute $\mathbf{x}^*$ (taking $\mathbf{x}_0 = \mathbf{0}$ for simplicity).**

    $$
    \mathbf{x}^* = \frac{L^*}{\boldsymbol{\delta}^\top\boldsymbol{\Sigma}\boldsymbol{\delta}}\boldsymbol{\Sigma}\boldsymbol{\delta} = \frac{10}{58}\begin{pmatrix} 6.5 \\ 8.5 \end{pmatrix} = \begin{pmatrix} 1.1207 \\ 1.4655 \end{pmatrix}
    $$

    Note: This formula gives the factor *changes* from $\mathbf{x}_0$. Since $L(\mathbf{x}) = -\boldsymbol{\delta}^\top(\mathbf{x} - \mathbf{x}_0)$, loss is positive when factors move opposite to the sensitivity direction. Let us verify: $L(\mathbf{x}^*) = -\boldsymbol{\delta}^\top \mathbf{x}^* = -(5 \times 1.1207 + 3 \times 1.4655) = -(5.6035 + 4.3965) = -10$.

    The loss is $-10$, meaning the portfolio actually *gains* 10 billion. For the failure scenario (loss of 10 billion), we need $\mathbf{x}^*$ in the opposite direction:

    $$
    \mathbf{x}^* = -\frac{L^*}{\boldsymbol{\delta}^\top\boldsymbol{\Sigma}\boldsymbol{\delta}}\boldsymbol{\Sigma}\boldsymbol{\delta} = -\frac{10}{58}\begin{pmatrix} 6.5 \\ 8.5 \end{pmatrix} = \begin{pmatrix} -1.1207 \\ -1.4655 \end{pmatrix}
    $$

    Verification: $L = -\boldsymbol{\delta}^\top\mathbf{x}^* = -(5 \times (-1.1207) + 3 \times (-1.4655)) = 5.6035 + 4.3965 = 10$ billion. Correct.

    **Step 4: Compute the Mahalanobis distance.**

    $$
    D(\mathbf{x}^*) = \frac{L^*}{\sqrt{\boldsymbol{\delta}^\top\boldsymbol{\Sigma}\boldsymbol{\delta}}} = \frac{10}{\sqrt{58}} = \frac{10}{7.6158} \approx 1.313
    $$

    Alternatively, compute directly. First find $\boldsymbol{\Sigma}^{-1}$:

    $$
    \det(\boldsymbol{\Sigma}) = 2 - 0.25 = 1.75, \quad \boldsymbol{\Sigma}^{-1} = \frac{1}{1.75}\begin{pmatrix} 2 & -0.5 \\ -0.5 & 1 \end{pmatrix}
    $$

    $$
    (\mathbf{x}^*)^\top\boldsymbol{\Sigma}^{-1}\mathbf{x}^* = \frac{L^{*2}}{(\boldsymbol{\delta}^\top\boldsymbol{\Sigma}\boldsymbol{\delta})^2} \cdot (\boldsymbol{\Sigma}\boldsymbol{\delta})^\top\boldsymbol{\Sigma}^{-1}(\boldsymbol{\Sigma}\boldsymbol{\delta}) = \frac{L^{*2}}{(\boldsymbol{\delta}^\top\boldsymbol{\Sigma}\boldsymbol{\delta})^2} \cdot \boldsymbol{\delta}^\top\boldsymbol{\Sigma}\boldsymbol{\delta} = \frac{L^{*2}}{\boldsymbol{\delta}^\top\boldsymbol{\Sigma}\boldsymbol{\delta}}
    $$

    So $D = L^*/\sqrt{\boldsymbol{\delta}^\top\boldsymbol{\Sigma}\boldsymbol{\delta}} = 10/\sqrt{58} \approx 1.313$.

    **Interpretation:** The most plausible failure scenario involves both factors declining: factor 1 falls by 1.12 units and factor 2 falls by 1.47 units. The direction is $\boldsymbol{\Sigma}\boldsymbol{\delta}$, which accounts for both the portfolio's sensitivity (factor 1 is more sensitive at \$5B/unit vs. \$3B/unit) and the covariance structure (factor 2 is more volatile with variance 2 vs. 1, and the positive correlation means both factors tend to move together). The covariance weighting pushes the scenario direction toward factor 2 (more volatile) relative to the raw sensitivity direction $\boldsymbol{\delta}$, because moving factor 2 is "cheaper" in Mahalanobis distance per unit of additional loss.

    The Mahalanobis distance of 1.313 indicates that this failure scenario is about 1.3 standard deviations from the mean in the worst-case direction---a relatively plausible event.

---

**Exercise 3.** Explain why the first-order condition $\nabla D(\mathbf{x}) = \lambda \nabla L(\mathbf{x})$ implies that the most plausible failure scenario lies at a point where the iso-plausibility contour is tangent to the loss contour $L(\mathbf{x}) = L^*$. Draw a sketch in two dimensions illustrating the failure region $\mathcal{F}$, the Mahalanobis distance contours, and the optimal scenario $\mathbf{x}^*$.

??? success "Solution to Exercise 3"

    **Part 1: Interpreting the first-order condition.**

    The optimization problem is:

    $$
    \min_{\mathbf{x}} D(\mathbf{x}) \quad \text{s.t.} \quad L(\mathbf{x}) \ge L^*
    $$

    At the optimum, the constraint is binding ($L(\mathbf{x}^*) = L^*$) and the gradients are proportional:

    $$
    \nabla D(\mathbf{x}^*) = \lambda \nabla L(\mathbf{x}^*)
    $$

    **Geometric interpretation:** The iso-plausibility contours are the level sets $\{D(\mathbf{x}) = c\}$, which are ellipses centered at $\boldsymbol{\mu}$ (with shape determined by $\boldsymbol{\Sigma}$). The loss contour is $\{L(\mathbf{x}) = L^*\}$.

    The gradient $\nabla D(\mathbf{x})$ points in the direction of steepest increase of the Mahalanobis distance (outward from the center of the ellipses, perpendicular to the iso-distance contours). The gradient $\nabla L(\mathbf{x})$ points perpendicular to the loss contour, in the direction of increasing loss.

    The condition $\nabla D = \lambda \nabla L$ means these two gradient vectors are **parallel** at $\mathbf{x}^*$. Geometrically, this means the iso-distance ellipse passing through $\mathbf{x}^*$ is **tangent** to the loss contour $L = L^*$ at that point.

    **Why tangency gives the minimum:** If the two curves were not tangent (i.e., if they crossed), then one could move along the loss contour $L = L^*$ to a point with smaller Mahalanobis distance---meaning a more plausible scenario achieving the same loss. At the tangent point, there is no such improvement: any movement along the loss contour increases the distance from the center.

    **Part 2: Sketch description.**

    In a two-dimensional sketch:

    - **Origin/center:** The mean $\boldsymbol{\mu}$ is at the center.
    - **Ellipses:** Concentric ellipses represent $D(\mathbf{x}) = c$ for increasing values of $c$. These are the iso-plausibility contours (smaller $c$ = more plausible).
    - **Failure region $\mathcal{F}$:** The shaded region where $L(\mathbf{x}) \ge L^*$, bounded by the curve $L(\mathbf{x}) = L^*$. For a linear loss function, this boundary is a straight line (hyperplane).
    - **Optimal scenario $\mathbf{x}^*$:** The point on the boundary $L = L^*$ closest to the center in Mahalanobis distance. This is where the smallest ellipse just touches the failure boundary.
    - **Tangency:** At $\mathbf{x}^*$, the ellipse $D = D(\mathbf{x}^*)$ is tangent to the line $L = L^*$. The normal to both curves at this point is the same direction (up to sign and scaling).

---

**Exercise 4.** A portfolio has three main risk exposures: equity (delta = \$200M per 1%), interest rates (delta = \$150M per 100 bps), and credit spreads (delta = \$100M per 100 bps). The failure threshold requires a loss of \$5 billion. Construct three distinct reverse stress scenarios along the failure boundary $L(\mathbf{x}) = L^*$ that correspond to (a) a pure equity crash, (b) a combined equity and credit event, and (c) a rates-driven scenario. For each, specify the required factor moves and briefly assess plausibility relative to historical episodes.

??? success "Solution to Exercise 4"

    The portfolio has linear sensitivities:

    - Equity: $\Delta_E = \$200$M per 1% (or \$200M per unit in the appropriate scaling)
    - Interest rates: $\Delta_R = \$150$M per 100 bps
    - Credit spreads: $\Delta_C = \$100$M per 100 bps

    The loss function is:

    $$
    L = \Delta_E \cdot |\Delta x_E| + \Delta_R \cdot |\Delta x_R| + \Delta_C \cdot |\Delta x_C|
    $$

    where the signs depend on the direction of the moves. The failure threshold is $L^* = \$5$ billion.

    **Scenario (a): Pure equity crash.**

    Set $\Delta x_R = 0$ and $\Delta x_C = 0$. Then:

    $$
    L = \Delta_E \cdot |\Delta x_E| = 200 \text{M} \times |\Delta x_E|
    $$

    For $L = 5000$M:

    $$
    |\Delta x_E| = \frac{5000}{200} = 25\%
    $$

    **Required move:** Equities decline 25%.

    **Plausibility:** A 25% equity decline is severe but has historical precedent. The S&P 500 fell approximately 20% in the Q4 2018 correction, 34% in March 2020 (COVID), and over 50% during 2008--2009. A 25% decline is within the range of historical crises and is considered plausible.

    **Scenario (b): Combined equity and credit event.**

    Assume equities decline and credit spreads widen simultaneously (typical crisis pattern). Set $\Delta x_R = 0$.

    $$
    L = 200 \cdot |\Delta x_E| + 100 \cdot |\Delta x_C| = 5000 \text{ M}
    $$

    One plausible combination: equities $-15\%$, credit spreads $+200$ bps.

    $$
    L = 200 \times 15 + 100 \times 2 = 3000 + 200 = 3200 \text{ M}
    $$

    Not enough. Try equities $-15\%$, credit $+350$ bps:

    $$
    L = 200 \times 15 + 100 \times 3.5 = 3000 + 350 = 3350 \text{ M}
    $$

    Still short. Try equities $-20\%$, credit $+500$ bps:

    $$
    L = 200 \times 20 + 100 \times 5 = 4000 + 500 = 4500 \text{ M}
    $$

    Close. Try equities $-20\%$, credit $+500$ bps, and add a small rates component: rates $+100$ bps:

    $$
    L = 200 \times 20 + 150 \times 1 + 100 \times 5 = 4000 + 150 + 500 = 4650 \text{ M}
    $$

    Adjust to exactly \$5B: equities $-18\%$, credit $+700$ bps:

    $$
    L = 200 \times 18 + 100 \times 7 = 3600 + 700 = 4300 \text{ M}
    $$

    More precisely, equities $-20\%$, credit $+1000$ bps:

    $$
    L = 200 \times 20 + 100 \times 10 = 4000 + 1000 = 5000 \text{ M}
    $$

    **Required moves:** Equities $-20\%$ and credit spreads $+1000$ bps.

    **Plausibility:** A 20% equity decline with 1000 bps credit spread widening is reminiscent of the 2008 GFC, where the S&P 500 fell over 40% and HY credit spreads widened by over 1500 bps. A combination of $-20\%$ equity with $+1000$ bps is severe but within historical bounds. This combined scenario is more plausible than a pure 25% equity crash, as equity and credit losses typically co-occur.

    **Scenario (c): Rates-driven scenario.**

    Interest rates move sharply, while equities and credit are less affected. For rates alone:

    $$
    L = 150 \cdot |\Delta x_R| = 5000 \implies |\Delta x_R| = 33.3 \text{ (i.e., 3333 bps)}
    $$

    A 3333 bps rate move is implausible. A more realistic rates-dominated scenario combines a large rate move with moderate equity and credit impacts. For example, rates $+500$ bps, equities $-10\%$, credit $+400$ bps:

    $$
    L = 200 \times 10 + 150 \times 5 + 100 \times 4 = 2000 + 750 + 400 = 3150 \text{ M}
    $$

    Increasing: rates $+1000$ bps, equities $-10\%$, credit $+500$ bps:

    $$
    L = 2000 + 1500 + 500 = 4000 \text{ M}
    $$

    Adjust: rates $+1300$ bps, equities $-5\%$, credit $+200$ bps:

    $$
    L = 1000 + 1950 + 200 = 3150 \text{ M}
    $$

    Try: rates $+1500$ bps, equities $-10\%$, credit $+350$ bps:

    $$
    L = 2000 + 2250 + 350 = 4600 \text{ M}
    $$

    Try: rates $+1500$ bps, equities $-10\%$, credit $+400$ bps:

    $$
    L = 2000 + 2250 + 400 = 4650 \text{ M}
    $$

    Close enough. A precise combination: rates $+2000$ bps, equities $-5\%$, credit $+0$ bps:

    $$
    L = 1000 + 3000 + 0 = 4000 \text{ M}
    $$

    Final: rates $+2000$ bps, equities $-5\%$, credit $+500$ bps:

    $$
    L = 1000 + 3000 + 500 = 4500 \text{ M}
    $$

    To reach exactly \$5B: rates $+2000$ bps, equities $-5\%$, credit $+1000$ bps:

    $$
    L = 1000 + 3000 + 1000 = 5000 \text{ M}
    $$

    **Required moves:** Rates $+2000$ bps, equities $-5\%$, credit $+1000$ bps.

    **Plausibility:** A 2000 bps rate rise is extreme and unprecedented in modern markets as a sudden move (though rates rose approximately 500 bps in 2022--2023). This scenario is the least plausible of the three and would correspond to a catastrophic inflation/central bank credibility scenario. It highlights that the portfolio is relatively less vulnerable to rates than to equities or credit in isolation.

---

**Exercise 5.** Discuss the relationship between reverse stress testing and recovery planning. If a reverse stress test identifies a scenario in which the bank's CET1 ratio falls to 3.0% (below the 4.5% minimum), describe at least four specific recovery actions the bank could take to restore capital adequacy. For each action, estimate the capital benefit and the time required, and discuss potential constraints or side effects.

??? success "Solution to Exercise 5"

    **Relationship between reverse stress testing and recovery planning:**

    Reverse stress testing identifies scenarios that would cause the bank to breach minimum capital requirements or threaten viability. Recovery planning specifies the actions the bank would take to restore capital adequacy if such scenarios materialized. The two are linked: reverse stress test results define the *conditions* under which recovery actions would be needed, and recovery plans define the *responses*.

    **Four specific recovery actions:**

    **1. Equity issuance (rights issue or private placement).**

    - *Capital benefit:* \$3--5 billion, depending on market conditions and existing authorization.
    - *Time required:* 2--6 months for a public rights issue (regulatory approval, prospectus, marketing); potentially 2--4 weeks for a pre-arranged backstop facility or private placement to a sovereign wealth fund.
    - *Constraints:* Share price will be depressed during stress, making issuance dilutive and potentially difficult. Market appetite for bank equity during a crisis may be limited. Existing shareholders may face massive dilution.

    **2. Asset disposal (sale of non-core businesses or loan portfolios).**

    - *Capital benefit:* \$2--8 billion, depending on the assets sold and the discount to book value. For example, selling a foreign subsidiary or a wealth management division.
    - *Time required:* 3--12 months for a strategic sale. Distressed asset sales can be completed faster but at larger discounts.
    - *Constraints:* During a systemic crisis, there are few buyers, and assets sell at deep discounts ("fire sale" problem). Selling revenue-generating assets reduces future earnings capacity. Regulatory approval may be required for disposal of regulated entities.

    **3. Dividend suspension and share buyback cancellation.**

    - *Capital benefit:* \$1--3 billion per year (depends on existing payout policy). If the bank pays \$2 billion in annual dividends and has a \$1 billion buyback program, suspending both preserves \$3 billion.
    - *Time required:* Immediate (board decision). Can be implemented within days.
    - *Constraints:* Sends a negative signal to the market, potentially triggering a loss of confidence. May cause a decline in share price. Pension funds and income investors may sell shares. Once dividends are cut, restoring them is difficult and requires demonstrating sustained recovery.

    **4. Risk reduction (deleveraging the portfolio).**

    - *Capital benefit:* Reducing RWA by \$50 billion at a 10% CET1 ratio frees \$5 billion in capital requirement, but the actual capital benefit depends on the spread between the current ratio and the requirement. More directly, reducing risky assets releases capital held against them.
    - *Time required:* Weeks to months, depending on liquidity of the assets.
    - *Constraints:* Selling assets into a stressed market incurs losses (the cure can worsen the disease). Reducing lending damages client relationships and economic activity. Regulatory pressure may actually discourage deleveraging during a crisis to avoid procyclical effects.

    **Additional considerations:**

    - Recovery plans should include quantitative triggers (e.g., CET1 ratio falls below 6%) that initiate specific actions.
    - Actions should be ordered by speed of implementation and certainty of capital benefit: dividend cut first (immediate, certain), then risk reduction, then asset sales, then equity issuance.
    - The bank should maintain "recovery capacity"---the total capital that could be generated from all recovery actions---in excess of the reverse stress test loss.

---

**Exercise 6.** A risk analyst uses importance sampling to search for failure scenarios. The sampling distribution is tilted as $f^{\text{tilted}}(\mathbf{x}) \propto f(\mathbf{x}) \cdot \exp(\theta \cdot L(\mathbf{x}))$ where $\theta > 0$ is the tilt parameter. Explain how increasing $\theta$ concentrates samples in the failure region. What is the tradeoff in choosing $\theta$? How does the analyst recover unbiased probability estimates from the tilted samples (i.e., what is the importance weight)?

??? success "Solution to Exercise 6"

    **Part 1: How increasing $\theta$ concentrates samples.**

    The tilted sampling distribution is:

    $$
    f^{\text{tilted}}(\mathbf{x}) \propto f(\mathbf{x}) \cdot \exp(\theta \cdot L(\mathbf{x}))
    $$

    The exponential tilting factor $\exp(\theta \cdot L(\mathbf{x}))$ assigns exponentially higher weight to scenarios with larger losses. As $\theta$ increases:

    - Scenarios with $L(\mathbf{x}) \gg 0$ receive exponentially more weight: $\exp(\theta L)$ grows rapidly.
    - Scenarios with small or negative $L(\mathbf{x})$ are suppressed.

    The effective sampling distribution shifts its mass toward the high-loss region. In the limit $\theta \to \infty$, virtually all samples concentrate on the scenario maximizing $L(\mathbf{x})$.

    **Part 2: Tradeoff in choosing $\theta$.**

    - **$\theta$ too small:** Samples are close to the original distribution $f$. Few samples fall in the failure region $L(\mathbf{x}) \ge L^*$, so the variance of the probability estimate $\hat{P}(\mathcal{F})$ is large. The algorithm fails to find failure scenarios efficiently.

    - **$\theta$ too large:** Samples cluster tightly around the maximum-loss scenario. The exploration of the failure region is poor---many different failure scenarios may exist, but the algorithm only finds one. Moreover, the importance weights (see below) become highly variable, with a few samples receiving extremely large weights, leading to high variance in probability estimates.

    - **Optimal $\theta$:** Balances exploration (sufficient diversity of failure scenarios) against focus (enough samples in the failure region to estimate probabilities accurately). In practice, $\theta$ is chosen so that a target fraction (e.g., 10--50%) of samples fall in the failure region.

    **Part 3: Importance weights for unbiased estimation.**

    Samples $\mathbf{x}_1, \ldots, \mathbf{x}_N$ are drawn from $f^{\text{tilted}}$. To recover unbiased estimates under the original distribution $f$, each sample receives an importance weight:

    $$
    w_i = \frac{f(\mathbf{x}_i)}{f^{\text{tilted}}(\mathbf{x}_i)} = \frac{f(\mathbf{x}_i)}{c \cdot f(\mathbf{x}_i) \cdot \exp(\theta L(\mathbf{x}_i))} = \frac{1}{c \cdot \exp(\theta L(\mathbf{x}_i))} \propto \exp(-\theta L(\mathbf{x}_i))
    $$

    where $c$ is the normalizing constant of $f^{\text{tilted}}$.

    The probability of failure under the original distribution is estimated as:

    $$
    \hat{P}(\mathcal{F}) = \frac{\sum_{i=1}^N w_i \cdot \mathbf{1}\{L(\mathbf{x}_i) \ge L^*\}}{\sum_{i=1}^N w_i}
    $$

    This is a self-normalized importance sampling estimator. Samples in the failure region with large $L(\mathbf{x}_i)$ receive small weights $\exp(-\theta L(\mathbf{x}_i))$ (because they were oversampled), while samples outside the failure region receive large weights (because they were undersampled). The weighting corrects for the sampling bias introduced by the tilt, producing an unbiased estimate of the true failure probability.

---

**Exercise 7.** Consider a bank with exposures to both market risk and credit risk. Argue that the failure region $\mathcal{F} = \{\mathbf{x} : L(\mathbf{x}) \ge L^*\}$ may be non-convex when the portfolio contains options or other nonlinear instruments. Provide a specific example of a portfolio where two distinct scenarios $\mathbf{x}_1, \mathbf{x}_2 \in \mathcal{F}$ exist but their midpoint $(\mathbf{x}_1 + \mathbf{x}_2)/2 \notin \mathcal{F}$. What challenges does non-convexity pose for algorithmic scenario search?

??? success "Solution to Exercise 7"

    **Part 1: Why $\mathcal{F}$ may be non-convex with nonlinear instruments.**

    The failure region is $\mathcal{F} = \{\mathbf{x} : L(\mathbf{x}) \ge L^*\}$. For a linear portfolio, $L(\mathbf{x})$ is linear (or affine) in $\mathbf{x}$, and the super-level set of a linear function is a half-space, which is convex.

    However, when the portfolio contains options or other instruments with nonlinear payoffs, $L(\mathbf{x})$ is a nonlinear (and generally non-concave) function of $\mathbf{x}$. The super-level set of a non-concave function can be non-convex.

    **Part 2: Specific example.**

    Consider a portfolio consisting of a **long straddle** on an equity index $S$. A straddle comprises a long call and a long put, both at strike $K$, with current $S_0 = K$.

    The portfolio profit at expiry is:

    $$
    \Pi(\Delta S) = |S_0 + \Delta S - K| - \text{Premium} = |\Delta S| - C_0
    $$

    where $C_0$ is the total premium paid. The loss function (from the perspective of the counterparty who is *short* the straddle) is:

    $$
    L(\Delta S) = |\Delta S| - C_0
    $$

    This loss is large when $|\Delta S|$ is large (either direction). Suppose $C_0 = 5$ and $L^* = 10$, so we need $|\Delta S| \ge 15$.

    Now introduce a second risk factor, $\Delta r$ (interest rates), with negligible portfolio impact for simplicity. Define:

    - $\mathbf{x}_1 = (\Delta S, \Delta r) = (-20, 0)$: equity crash. Loss: $|{-20}| - 5 = 15 \ge 10$. So $\mathbf{x}_1 \in \mathcal{F}$.
    - $\mathbf{x}_2 = (\Delta S, \Delta r) = (+20, 0)$: equity rally. Loss: $|{+20}| - 5 = 15 \ge 10$. So $\mathbf{x}_2 \in \mathcal{F}$.
    - Midpoint: $(\mathbf{x}_1 + \mathbf{x}_2)/2 = (0, 0)$. Loss: $|0| - 5 = -5 < 10$. So the midpoint $\notin \mathcal{F}$.

    This demonstrates non-convexity: two failure scenarios on opposite sides of the current market level average to a benign scenario where the straddle expires at-the-money with minimal payoff to the holder (and hence minimal loss to the short straddle writer).

    **Part 3: Challenges of non-convexity for algorithmic search.**

    1. **Gradient-based methods may find only local optima.** The failure region may have multiple disconnected components (as in the straddle example, where both large positive and large negative equity moves cause failure). Gradient descent starting from one side will never discover the failure scenario on the other side.

    2. **Convex optimization tools are inapplicable.** Many efficient algorithms (quadratic programming, interior point methods) require convexity. Non-convex feasibility problems are NP-hard in general.

    3. **Interpolation between known failure scenarios is unreliable.** If two failure scenarios are found, one cannot assume the path between them also causes failure. This makes it difficult to characterize the complete failure boundary.

    4. **Completeness is not guaranteed.** With a non-convex failure region, there is no systematic way to ensure all components have been found. Multiple random restarts, evolutionary algorithms, or global optimization heuristics are needed, but none guarantee completeness.

    5. **Importance sampling efficiency degrades.** Tilting toward one component of the failure region may miss others entirely, and designing a single tilting distribution that covers all components is difficult.

    To address these challenges, practitioners use **multiple starting points** for gradient searches, **evolutionary algorithms** (which maintain a diverse population of candidate scenarios), and **scenario decomposition** (analyzing different instrument types separately to identify distinct failure mechanisms).
