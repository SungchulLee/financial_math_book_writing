# Multiplier Preferences


## Introduction


**Multiplier preferences**, introduced by Hansen and Sargent (2001) as part of their program on robust macroeconomics, provide a tractable and theoretically elegant approach to decision-making under model uncertainty. The key idea is to evaluate actions not under a single reference probability measure $P_0$ but under a worst-case measure $P^*$ that maximizes expected cost, subject to an **entropy penalty** for deviating from $P_0$.

Where max-min expected utility uses a **hard constraint** (the set of priors $\mathcal{P}$), multiplier preferences impose a **soft penalty** proportional to the Kullback-Leibler divergence between the alternative and reference models. This single parameter $\theta > 0$ controls the degree of robustness:

- **Large $\theta$**: Weak robustness concern, close to standard expected utility under $P_0$
- **Small $\theta$**: Strong robustness concern, approaching worst-case analysis

The framework connects to exponential utility, risk-sensitive control, and entropic risk measures, providing a unified perspective on model uncertainty across decision theory, control theory, and financial mathematics.

## Mathematical Framework


### 1. Definition of Multiplier Preferences


**Setup**: Let $(\Omega, \mathcal{F}, P_0)$ be a probability space where $P_0$ is the **reference model** (the decision-maker's best estimate of the true data-generating process). Let $u: X \to \mathbb{R}$ be a utility function and $f: \Omega \to X$ an act.

**Definition** (Multiplier Preferences): The multiplier preference functional evaluates an act $f$ by:

$$
V(f) = \min_{P \ll P_0} \left\{ \mathbb{E}_P[u(f)] + \theta \, D_{\text{KL}}(P \| P_0) \right\}
$$

where $\theta > 0$ is the **robustness parameter** and $D_{\text{KL}}(P \| P_0)$ is the relative entropy:

$$
D_{\text{KL}}(P \| P_0) = \mathbb{E}_P\left[\log \frac{dP}{dP_0}\right] = \int_{\Omega} \log\left(\frac{dP}{dP_0}\right) \, dP
$$

**Interpretation**: The decision-maker:

1. Considers alternative models $P$ that could replace the reference $P_0$
2. Evaluates expected utility $\mathbb{E}_P[u(f)]$ under each alternative
3. Penalizes deviations from $P_0$ by $\theta \, D_{\text{KL}}(P \| P_0)$
4. Selects the model yielding the worst penalized expected utility

### 2. Closed-Form Solution via Exponential Tilting


**Theorem** (Worst-Case Measure): The minimizing measure $P^*$ in the multiplier preference problem satisfies:

$$
\frac{dP^*}{dP_0} = \frac{e^{-u(f)/\theta}}{\mathbb{E}_{P_0}[e^{-u(f)/\theta}]}
$$

and the value of the multiplier preference functional is:

$$
V(f) = -\theta \log \mathbb{E}_{P_0}\left[e^{-u(f)/\theta}\right]
$$

**Proof**: Define the Lagrangian $\mathcal{L}(P, \lambda)$ over all $P \ll P_0$. Write $\frac{dP}{dP_0} = M$ (the Radon-Nikodym derivative). The objective becomes:

$$
\mathcal{L}(M) = \mathbb{E}_{P_0}[M \cdot u(f)] + \theta \, \mathbb{E}_{P_0}[M \log M]
$$

subject to $\mathbb{E}_{P_0}[M] = 1$ and $M \geq 0$. Using the variational formula for the cumulant generating function:

$$
\log \mathbb{E}_{P_0}[e^X] = \sup_{P \ll P_0} \left\{ \mathbb{E}_P[X] - D_{\text{KL}}(P \| P_0) \right\}
$$

with $X = -u(f)/\theta$, we obtain:

$$
\sup_{P \ll P_0}\left\{ -\frac{1}{\theta}\mathbb{E}_P[u(f)] - D_{\text{KL}}(P \| P_0) \right\} = \log \mathbb{E}_{P_0}\left[e^{-u(f)/\theta}\right]
$$

Multiplying by $-\theta$ yields:

$$
\min_{P \ll P_0}\left\{ \mathbb{E}_P[u(f)] + \theta \, D_{\text{KL}}(P \| P_0) \right\} = -\theta \log \mathbb{E}_{P_0}\left[e^{-u(f)/\theta}\right]
$$

The supremum is achieved by the exponentially tilted measure $P^*$. $\square$

### 3. Connection to Exponential Utility


**Observation**: With identity utility $u(x) = x$, the multiplier preference value is:

$$
V(f) = -\theta \log \mathbb{E}_{P_0}\left[e^{-f/\theta}\right]
$$

This is precisely the **certainty equivalent** under exponential utility with risk aversion coefficient $\gamma = 1/\theta$:

$$
u_{\text{exp}}(x) = -e^{-x/\theta} \implies CE(f) = -\theta \log \mathbb{E}_{P_0}[e^{-f/\theta}]
$$

**Implication**: Multiplier preferences with robustness parameter $\theta$ are **observationally equivalent** to exponential utility with risk aversion $1/\theta$ when the reference model is correct. This creates an identification problem: observed conservative behavior could reflect either risk aversion or robustness concern.

### 4. Limiting Cases


**Large $\theta$ (Low Robustness)**: As $\theta \to \infty$, the entropy penalty becomes infinitely costly, so $P^* \to P_0$:

$$
V(f) \to \mathbb{E}_{P_0}[u(f)]
$$

recovering standard expected utility under the reference model.

**Small $\theta$ (High Robustness)**: As $\theta \to 0^+$, the penalty vanishes and the decision-maker faces the unconstrained worst case:

$$
V(f) \to \inf_{\omega \in \text{supp}(P_0)} u(f(\omega))
$$

reducing to pure max-min over outcomes.

**Intermediate $\theta$**: Provides a smooth interpolation between full trust in $P_0$ and pure worst-case analysis.

## Constraint vs Multiplier Formulations


### 1. Entropy-Constrained Problem


**Dual Formulation**: The multiplier problem is the Lagrangian dual of the entropy-constrained problem:

$$
V_{\eta}(f) = \min_{P: D_{\text{KL}}(P \| P_0) \leq \eta} \mathbb{E}_P[u(f)]
$$

**Lagrangian**: Introducing multiplier $\theta$ for the entropy constraint:

$$
\mathcal{L}(P, \theta) = \mathbb{E}_P[u(f)] + \theta \left( D_{\text{KL}}(P \| P_0) - \eta \right)
$$

At the optimum, complementary slackness gives $D_{\text{KL}}(P^* \| P_0) = \eta$.

### 2. Relationship Between Parameters


**Theorem**: The entropy budget $\eta$ and the multiplier $\theta$ are related by:

$$
\eta(\theta) = D_{\text{KL}}(P^*(\theta) \| P_0)
$$

where $P^*(\theta)$ is the worst-case measure at robustness level $\theta$. The function $\eta(\theta)$ is:

- Monotonically decreasing in $\theta$
- Continuous
- $\eta(\theta) \to 0$ as $\theta \to \infty$ (trust reference model)
- $\eta(\theta) \to \infty$ as $\theta \to 0^+$ (maximum distortion)

**Implication**: Each entropy budget $\eta$ corresponds to exactly one multiplier $\theta$, so the two formulations produce equivalent decisions.

### 3. Relationship to Variational Preferences


**Maccheroni-Marinacci-Rustichini (2006)** showed that multiplier preferences are a special case of **variational preferences**:

$$
V(f) = \min_{P \in \mathcal{M}_1(\Omega)} \left\{ \mathbb{E}_P[u(f)] + c(P) \right\}
$$

with the specific cost function $c(P) = \theta \, D_{\text{KL}}(P \| P_0)$.

**Other Special Cases**:

| Cost Function $c(P)$ | Preference Model |
|---|---|
| $\theta \, D_{\text{KL}}(P \| P_0)$ | Multiplier preferences |
| $0$ if $P \in \mathcal{P}$, $\infty$ otherwise | Max-min expected utility |
| $\theta \, D_\phi(P \| P_0)$ | $\phi$-divergence robustness |

## Detection Error Probability


### 1. Calibrating the Robustness Parameter


A central challenge is choosing $\theta$. Hansen and Sargent propose calibration via the **detection error probability** (DEP), which measures the statistical difficulty of distinguishing the worst-case model $P^*$ from the reference model $P_0$.

**Setup**: Consider a likelihood ratio test with $n$ observations from either $P_0$ or $P^*$:

$$
\Lambda_n = \prod_{i=1}^n \frac{dP^*}{dP_0}(\xi_i)
$$

**Type I Error**: $\alpha = P_0(\Lambda_n > c)$ (rejecting $P_0$ when true)

**Type II Error**: $\beta = P^*(\Lambda_n \leq c)$ (failing to reject $P_0$ when $P^*$ is true)

**Detection Error Probability**: For the symmetric test with equal priors:

$$
\text{DEP} = \frac{1}{2}(\alpha + \beta)
$$

### 2. Connection to Entropy


**Theorem** (Stein's Lemma): As $n \to \infty$, for fixed Type I error $\alpha$:

$$
\beta_n \approx e^{-n \, D_{\text{KL}}(P_0 \| P^*)}
$$

**Consequence**: The KL divergence determines the rate at which evidence against the wrong model accumulates. Small $D_{\text{KL}}(P^* \| P_0)$ means $P^*$ is hard to distinguish from $P_0$, implying a legitimate robustness concern.

### 3. Calibration Procedure


**Algorithm**:

1. Fix a sample size $n$ and target detection error $\overline{\text{DEP}}$ (e.g., 10%)
2. For a candidate $\theta$, compute the worst-case measure $P^*(\theta)$
3. Simulate the likelihood ratio test and compute $\text{DEP}(\theta)$
4. Find $\theta^*$ such that $\text{DEP}(\theta^*) = \overline{\text{DEP}}$

**Typical Finding**: Detection error of approximately 10% yields reasonable robustness that is neither too conservative nor too trusting.

**Gaussian Example**: For $P_0 = N(\mu_0, \sigma^2)$ and worst-case $P^* = N(\mu^*, \sigma^2)$:

$$
D_{\text{KL}}(P^* \| P_0) = \frac{(\mu^* - \mu_0)^2}{2\sigma^2}
$$

Setting $\text{DEP} = 0.10$ with $n = 100$ observations gives $D_{\text{KL}} \approx 0.013$, which via the relationship $\eta = D_{\text{KL}}(P^* \| P_0)$ pins down $\theta$.

## Hansen-Sargent Robust Control


### 1. Discrete-Time Framework


**State Dynamics**: Under reference model $P_0$:

$$
x_{t+1} = A x_t + B u_t + C w_t
$$

where $w_t \sim N(0, I)$ under $P_0$, $u_t$ is the control, and $x_t$ is the state.

**Standard LQG Objective**: Minimize:

$$
J = \mathbb{E}_{P_0}\left[\sum_{t=0}^{\infty} \beta^t \left( x_t^\top Q x_t + u_t^\top R u_t \right)\right]
$$

**Robust Formulation**: The controller minimizes against a worst-case model perturbation:

$$
\min_{u} \max_{v} \mathbb{E}_{P_0}\left[\sum_{t=0}^{\infty} \beta^t \left( x_t^\top Q x_t + u_t^\top R u_t - \theta \|v_t\|^2 \right)\right]
$$

subject to $x_{t+1} = A x_t + B u_t + C(w_t + v_t)$, where $v_t$ is the adversarial model distortion.

**Interpretation**: The term $-\theta \|v_t\|^2$ penalizes the adversary's distortion of the noise process. The quadratic penalty on $v_t$ arises from the entropy penalty on the distorted measure.

### 2. Robust Riccati Equation


**Theorem**: The value function takes the form $V(x) = x^\top P x + d$, where $P$ satisfies the **robust algebraic Riccati equation**:

$$
P = Q + \beta A^\top P A - \beta A^\top P B (R + \beta B^\top P B)^{-1} B^\top P A + \beta A^\top P C (\theta I - \beta C^\top P C)^{-1} C^\top P A
$$

**Well-Posedness Condition**: The equation has a solution if and only if:

$$
\theta > \beta \lambda_{\max}(C^\top P C)
$$

This is the **breakdown point**: below this threshold, the adversary can create unbounded distortions and the problem is ill-posed.

**Optimal Control**:

$$
u_t^* = -F x_t, \quad F = (R + \beta B^\top P B)^{-1} \beta B^\top P A
$$

**Worst-Case Distortion**:

$$
v_t^* = (\theta I - \beta C^\top P C)^{-1} \beta C^\top P (A - BF) x_t
$$

### 3. Comparison with Standard LQG


**Key Differences**:

| Feature | Standard LQG | Robust Control |
|---|---|---|
| Riccati equation | Standard ARE | Augmented ARE with $\theta$ term |
| Certainty equivalence | Yes | Yes (separation still holds) |
| Optimal control gain | $F = (R + \beta B^\top P B)^{-1} \beta B^\top PA$ | Same formula, different $P$ |
| Effective dynamics | $A - BF$ | $A - BF + C v^*$ |
| Volatility | $\sigma^2 = C C^\top$ | Effective $\tilde{\sigma}^2 > \sigma^2$ |

**Result**: The robust controller uses the same certainty-equivalence structure as LQG, but the Riccati solution $P$ is larger, reflecting the additional cost of robustness. This leads to more conservative control actions.

## Continuous-Time Extension


### 1. Robust HJB Equation


**Asset Dynamics** under reference model:

$$
dX_t = b(X_t, u_t) \, dt + \sigma(X_t) \, dW_t
$$

**Robust Value Function**: $V(t, x)$ satisfies the robust Hamilton-Jacobi-Bellman equation:

$$
V_t + \sup_u \inf_h \left\{ \mathcal{L}^{u,h} V + \ell(x, u) + \frac{\theta}{2} |h|^2 \right\} = 0
$$

where $\mathcal{L}^{u,h} V = (b + \sigma h) \cdot \nabla V + \frac{1}{2} \text{tr}(\sigma \sigma^\top \nabla^2 V)$ and $h$ is the drift distortion.

**Optimal Distortion**: First-order condition in $h$ gives:

$$
h^*(t, x) = -\frac{\sigma(x)^\top \nabla V(t, x)}{\theta}
$$

### 2. Reduced HJB Equation


Substituting $h^*$ back:

$$
V_t + \sup_u \left\{ b(x, u) \cdot \nabla V + \frac{1}{2} \text{tr}(\sigma \sigma^\top \nabla^2 V) + \ell(x, u) - \frac{|\sigma^\top \nabla V|^2}{2\theta} \right\} = 0
$$

**Observation**: The robustness correction adds a **quadratic gradient term** $-\frac{|\sigma^\top \nabla V|^2}{2\theta}$ to the standard HJB. This is a semilinear PDE that can be solved numerically.

### 3. Entropy Rate in Continuous Time


**Continuous-Time Entropy**: Under drift distortion $h_t$, the entropy rate is:

$$
\frac{d}{dt} D_{\text{KL}}(P^h_t \| P^0_t) = \frac{1}{2} \mathbb{E}^h[|h_t|^2]
$$

**Total Entropy Budget**:

$$
D_{\text{KL}}(P^h \| P^0) = \frac{1}{2} \mathbb{E}^h\left[\int_0^T |h_t|^2 \, dt\right]
$$

This connects the continuous-time penalty to the cumulative squared distortion of the drift.

## Financial Applications


### 1. Equity Premium and Robust Asset Pricing


**Representative Agent**: With log consumption growth $\Delta c \sim N(\mu_c, \sigma_c^2)$ under $P_0$ and CRRA utility $u(c) = c^{1-\gamma}/(1-\gamma)$:

**Standard Euler Equation**:

$$
\mathbb{E}[R_e] - R_f = \gamma \sigma_c^2
$$

**With Multiplier Preferences**: The effective risk aversion increases:

$$
\mathbb{E}[R_e] - R_f = \left(\gamma + \frac{\sigma_c^2}{\theta}\right) \sigma_c^2
$$

**Calibration**: With $\gamma = 2$, $\sigma_c = 0.02$, and detection error $\approx 10\%$:

$$
\theta \approx 0.001 \implies \text{Robustness premium} \approx 4\%
$$

This resolves the equity premium puzzle: reasonable robustness concern ($\theta$ calibrated via detection error) generates the additional 4% premium needed to match historical data without extreme risk aversion.

### 2. Robust Portfolio Choice


**Problem**: Investor with wealth $W_t$ in a market with risky asset return $R \sim N(\mu, \sigma^2)$ under $P_0$:

$$
\max_\pi \min_{P: D_{\text{KL}}(P \| P_0) \leq \eta} \mathbb{E}_P\left[-e^{-\gamma W_T}\right]
$$

where $\pi$ is the fraction invested in the risky asset.

**Solution** (Gaussian Returns):

$$
\pi^* = \frac{\mu - r}{\gamma \sigma^2 + \sigma^2/\theta} = \frac{\mu - r}{(\gamma + 1/\theta) \sigma^2}
$$

**Effect**: The robustness correction $1/\theta$ effectively increases risk aversion from $\gamma$ to $\gamma + 1/\theta$, shrinking the risky asset position. The investor holds a more conservative portfolio not because of greater risk aversion but because of doubt about the reference model.

### 3. Robust Monetary Policy


**Taylor Rule**: Central bank sets interest rate $i_t$:

$$
i_t = r^* + \phi_\pi (\pi_t - \pi^*) + \phi_y y_t
$$

**Robust Design**: Under model uncertainty about the Phillips curve and IS curve parameters, the Hansen-Sargent framework yields robust policy coefficients $\phi_\pi^R > \phi_\pi$ and $\phi_y^R > \phi_y$.

**Result**: Robust monetary policy is **more aggressive** than its certainty-equivalent counterpart. The controller acts more forcefully because the worst-case model implies greater persistence and larger policy multipliers.

## Comparison with Alternative Approaches


### 1. Multiplier vs Max-Min Preferences


| Aspect | Max-Min (Gilboa-Schmeidler) | Multiplier (Hansen-Sargent) |
|---|---|---|
| Constraint | Hard: $P \in \mathcal{P}$ | Soft: KL penalty |
| Solution | Corner of $\mathcal{P}$ | Interior: smooth tilting |
| Calibration | Specify set $\mathcal{P}$ | Single parameter $\theta$ or DEP |
| Smoothness | Kinks at boundaries | Smooth everywhere |
| Tractability | LP for finite $\mathcal{P}$ | Closed-form for Gaussians |
| Dynamic consistency | Requires rectangularity | Automatic (recursive structure) |

### 2. Multiplier vs Smooth Ambiguity


**Klibanoff-Marinacci-Mukerji (2005)**: $V(f) = \int_{\mathcal{P}} \phi(\mathbb{E}_P[u(f)]) \, d\mu(P)$

**Connection**: When $\phi(x) = -e^{-x/\theta}$ and $\mu$ is a point mass at $P_0$:

$$
V(f) = -e^{-\mathbb{E}_{P_0}[u(f)]/\theta}
$$

which, after monotone transformation, recovers multiplier preferences. The smooth ambiguity model is strictly more general, allowing for non-degenerate second-order beliefs.

### 3. Relationship to Risk-Sensitive Control


**Risk-Sensitive Criterion**: For parameter $\beta > 0$:

$$
J_\beta = -\frac{1}{\beta} \log \mathbb{E}_{P_0}\left[\exp\left(-\beta \sum_{t=0}^T r(x_t, u_t)\right)\right]
$$

**Equivalence**: Risk-sensitive control with parameter $\beta$ is equivalent to multiplier preferences with $\theta = 1/\beta$ and stage reward $r$.

**Advantage of the Robustness Interpretation**: While risk-sensitive control is formulated purely as a preference specification, multiplier preferences provide a structural interpretation: the agent is uncertain about the model and hedges against misspecification. This interpretation guides calibration (via detection error) and comparative statics.

## Axiomatic Foundations


### 1. Strzalecki's Axiomatization


**Theorem** (Strzalecki, 2011): Multiplier preferences are characterized by the axioms of variational preferences (Maccheroni-Marinacci-Rustichini) plus:

**Axiom** (Constant Absolute Ambiguity Aversion): For all acts $f, g$ and constants $c$:

$$
f \succeq g \iff f + c \succeq g + c
$$

This is analogous to constant absolute risk aversion (CARA) in expected utility theory.

**Representation**: Under these axioms, there exist a unique $\theta > 0$ and a unique reference measure $P_0$ such that:

$$
V(f) = \min_{P \ll P_0} \left\{ \mathbb{E}_P[u(f)] + \theta \, D_{\text{KL}}(P \| P_0) \right\}
$$

### 2. Dynamic Consistency


**Theorem**: Multiplier preferences with a fixed $\theta$ and reference measure $P_0$ are **dynamically consistent**: if the agent prefers plan $A$ over plan $B$ at time $t = 0$, then at any intermediate time $t$, the agent still prefers to continue with plan $A$.

**Proof**: The recursive structure of the BSDE representation ensures that the conditional multiplier preference $V_t(f) = -\theta \log \mathbb{E}_{P_0}[e^{-u(f)/\theta} | \mathcal{F}_t]$ satisfies the tower property:

$$
V_s(V_t(f)) = V_s(f) \quad \text{for } s \leq t
$$

This follows from the tower property of conditional expectations applied to exponential transformations. $\square$

## Summary and Key Takeaways


1. **Core Mechanism**: Multiplier preferences evaluate acts by minimizing expected utility plus an entropy penalty, creating a smooth trade-off between model fit and robustness

2. **Exponential Tilting**: The worst-case measure has an explicit exponentially tilted form, yielding the closed-form value $V(f) = -\theta \log \mathbb{E}_{P_0}[e^{-u(f)/\theta}]$

3. **Detection Error Calibration**: The robustness parameter $\theta$ can be calibrated by requiring that the worst-case model is statistically difficult to distinguish from the reference model (e.g., 10% detection error)

4. **Robust Control**: In linear-quadratic settings, multiplier preferences yield a modified Riccati equation with the same certainty-equivalence structure as standard LQG but with more conservative gains

5. **Financial Implications**: Multiplier preferences generate additional risk premia (resolving the equity premium puzzle), reduce portfolio leverage, and justify more aggressive monetary policy

6. **Observational Equivalence**: With exponential utility, multiplier preferences are indistinguishable from standard expected utility with higher risk aversion --- the interpretation (robustness vs risk aversion) determines calibration and comparative statics

7. **Dynamic Consistency**: Unlike max-min preferences, multiplier preferences are automatically dynamically consistent without requiring rectangularity conditions

---

## Exercises

**Exercise 1.** For a gamble $f$ with two outcomes: $f(\omega_1) = 10$ with $P_0(\omega_1) = 0.6$ and $f(\omega_2) = -5$ with $P_0(\omega_2) = 0.4$, compute the multiplier preference value $V(f) = -\theta \log \mathbb{E}_{P_0}[e^{-u(f)/\theta}]$ for $u(x) = x$ (linear utility) and $\theta \in \{1, 5, 50\}$. Verify that as $\theta \to \infty$, $V(f) \to \mathbb{E}_{P_0}[f]$, and as $\theta \to 0$, $V(f) \to \min_\omega f(\omega)$.

---

**Exercise 2.** Derive the worst-case measure for the multiplier preference. Starting from $V(f) = \min_{P \ll P_0}\{\mathbb{E}_P[u(f)] + \theta D_{\text{KL}}(P \| P_0)\}$, use calculus of variations to show that the minimizing $P^*$ satisfies $dP^*/dP_0 \propto e^{-u(f)/\theta}$. Compute $P^*$ for the gamble in Exercise 1 with $\theta = 5$, and verify that $P^*$ shifts probability toward the worse outcome.

---

**Exercise 3.** In the Hansen-Sargent robust control framework with linear dynamics $x_{t+1} = Ax_t + Bu_t + Cw_t$ and quadratic cost, the robust optimal control is $u_t^* = -(R + B^\top P_\theta B)^{-1}B^\top P_\theta A x_t$ where $P_\theta$ satisfies a modified Riccati equation involving $\theta$. For $A = 0.95$, $B = 1$, $C = 0.3$, $Q = 1$, $R = 0.1$, compare the optimal control gains for $\theta = \infty$ (standard LQG), $\theta = 10$, and $\theta = 2$.

---

**Exercise 4.** Show that multiplier preferences with exponential utility $u(x) = -e^{-\alpha x}$ are observationally equivalent to standard expected utility with adjusted risk aversion $\alpha' = \alpha + 1/\theta$. What implication does this have for empirically distinguishing robustness concerns from pure risk aversion? Discuss how comparative statics (e.g., response to information quality changes) can break this equivalence.

---

**Exercise 5.** Prove that multiplier preferences are dynamically consistent without requiring rectangularity. Specifically, show that for the recursive formulation $V_t = -\theta \log \mathbb{E}_{P_0}[e^{-V_{t+1}/\theta} | \mathcal{F}_t]$, the tower property holds: $V_0 = -\theta \log \mathbb{E}_{P_0}[e^{-(-\theta \log \mathbb{E}_{P_0}[e^{-V_2/\theta}|\mathcal{F}_1])/\theta}] = -\theta \log \mathbb{E}_{P_0}[e^{-V_2/\theta}]$.

---

**Exercise 6.** Apply multiplier preferences to the equity premium puzzle. In a consumption-based asset pricing model with $\log C_{t+1} - \log C_t \sim N(\mu_c, \sigma_c^2)$, the equity premium under multiplier preferences is $\mathbb{E}[R_e - R_f] = (\alpha + 1/\theta)\sigma_c^2 + \sigma_c^2/\theta$. For $\mu_c = 0.02$, $\sigma_c = 0.035$, $\alpha = 2$, show that $\theta = 5$ generates an equity premium consistent with the historical average of approximately 6%, while standard expected utility with $\alpha = 2$ generates a premium of only about 0.25%.
