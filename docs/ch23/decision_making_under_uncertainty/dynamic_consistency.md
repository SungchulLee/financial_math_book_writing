# Dynamic Consistency


## Introduction


**Dynamic consistency** is a fundamental requirement for coherent multi-period decision-making under uncertainty. A decision-maker is dynamically consistent if their planned future actions remain optimal when the future arrives — that is, they have no incentive to deviate from previously optimal plans.

Under standard expected utility with Bayesian updating, dynamic consistency is automatic. However, when preferences incorporate **ambiguity aversion**, **robust optimization**, or **non-expected utility**, dynamic consistency may fail, leading to time-inconsistent behavior.

Understanding and ensuring dynamic consistency is crucial for:
1. **Dynamic portfolio optimization**: Multi-period investment strategies
2. **Derivatives pricing**: Hedging strategies over time
3. **Risk management**: Coherent risk assessment across horizons
4. **Mechanism design**: Contracts that remain incentive-compatible

## Foundations of Dynamic Consistency


### 1. Sequential Decision Problems


**Setup**: Consider a decision tree with:
- Time periods $t = 0, 1, \ldots, T$
- Information filtration $\{\mathcal{F}_t\}$
- Acts (strategies) $\{a_t\}_{t=0}^T$
- Outcomes determined by actions and states

**Strategy**: A strategy $\sigma = \{a_t(\cdot)\}$ specifies actions contingent on information.

### 2. Planned vs. Actual Behavior


**Ex-Ante Plan**: At $t=0$, the decision-maker forms optimal strategy $\sigma^* = \{a_0^*, a_1^*(\cdot), \ldots\}$.

**Ex-Post Behavior**: At $t=1$, given realized information $\omega \in \mathcal{F}_1$, the decision-maker may re-optimize.

**Dynamic Consistency**: The plan is dynamically consistent if:

$$
a_t^*(\omega) = \arg\max_{a_t} V_t(a_t, \sigma^*_{t+1:T} | \mathcal{F}_t = \omega)
$$

for all $t$ and $\omega$ — the planned action remains optimal at the time of execution.

### 3. Time Consistency vs. Dynamic Consistency


**Time Consistency**: Preferences over consumption streams are time-consistent if:

$$
(c_0, c_1, \ldots) \succeq_0 (c_0', c_1', \ldots) \implies (c_1, c_2, \ldots) \succeq_1 (c_1', c_2', \ldots)
$$

when $c_0 = c_0'$.

**Dynamic Consistency**: Broader concept including consistency of conditional preferences over acts.

**Relationship**: Time consistency is necessary but not sufficient for dynamic consistency under uncertainty.

## Expected Utility and Dynamic Consistency


### 1. Bayesian Updating


**Bayes' Rule**: Given prior $P$ and event $A$:

$$
P(\cdot | A) = \frac{P(\cdot \cap A)}{P(A)}
$$

**Sequential Expected Utility**: Value of strategy $\sigma$ at time $t$:

$$
V_t(\sigma) = \mathbb{E}_P[U(\sigma) | \mathcal{F}_t]
$$

### 2. Tower Property


**Law of Iterated Expectations**:

$$
\mathbb{E}_P[\mathbb{E}_P[U | \mathcal{F}_s] | \mathcal{F}_t] = \mathbb{E}_P[U | \mathcal{F}_t] \quad \text{for } t \leq s
$$

**Implication**: Sequential optimization is equivalent to backward induction:

$$
V_t(\sigma) = \mathbb{E}_P[V_{t+1}(\sigma) | \mathcal{F}_t]
$$

### 3. Bellman Principle


**Dynamic Programming**: Under EU with Bayesian updating:

$$
V_t(x) = \max_{a_t} \left\{u(x, a_t) + \beta \mathbb{E}_P[V_{t+1}(x') | \mathcal{F}_t]\right\}
$$

**Dynamic Consistency**: The Bellman optimal policy is dynamically consistent by construction.

## Dynamic Inconsistency Under Ambiguity


### 1. Max-Min Expected Utility


**MEU Preferences**: 

$$
V(f) = \min_{P \in \mathcal{P}} \mathbb{E}_P[U(f)]
$$

**Problem**: The minimum may be achieved by different measures at different times.

### 2. Example of Inconsistency


**Two-Period Problem**:
- States: $\{\omega_1, \omega_2, \omega_3\}$
- Period 1 information: $\{\{\omega_1\}, \{\omega_2, \omega_3\}\}$
- Priors: $\mathcal{P} = \{P_1, P_2\}$ with different weights

**At $t=0$**: Worst-case measure might be $P_1$.

**At $t=1$**, conditional on $\{\omega_2, \omega_3\}$: Worst-case measure might be $P_2|_{\{\omega_2, \omega_3\}}$.

**Result**: Planned action at $t=0$ may differ from optimal action at $t=1$ — dynamic inconsistency.

### 3. Source of Inconsistency


**Non-Additive Expectations**: MEU uses:

$$
V_0(f) = \min_{P \in \mathcal{P}} \mathbb{E}_P[f]
$$

but this does not satisfy the tower property:

$$
\min_{P \in \mathcal{P}} \mathbb{E}_P[\min_{Q \in \mathcal{P}} \mathbb{E}_Q[f | \mathcal{F}_1]] \neq \min_{P \in \mathcal{P}} \mathbb{E}_P[f]
$$

in general.

## Rectangularity


### 1. Definition


**Definition** (Epstein-Schneider, 2003): A set of priors $\mathcal{P}$ is **rectangular** with respect to filtration $\{\mathcal{F}_t\}$ if it can be decomposed as:

$$
\mathcal{P} = \left\{P: P_t(\cdot | \mathcal{F}_t) \in \mathcal{P}_t(\omega) \text{ for all } t, \omega\right\}
$$

where $\mathcal{P}_t(\omega)$ is a family of conditional probability measures.

**Equivalent Characterization**: For any $P, Q \in \mathcal{P}$ and stopping time $\tau$, the "pasted" measure:

$$
(P \otimes_{\tau} Q)(A) = \mathbb{E}_P[\mathbb{1}_{\tau > T} \mathbb{1}_A] + \mathbb{E}_P[\mathbb{1}_{\tau \leq T} Q(A | \mathcal{F}_{\tau})]
$$

is also in $\mathcal{P}$.

### 2. Intuition


**Product Structure**: Rectangularity means the set of priors has a "product" structure across time:
- Period-by-period uncertainty sets are independent
- No constraints linking uncertainty at different times

**Example** (Rectangular):

$$
\mathcal{P} = \{P: P_t(\cdot | \mathcal{F}_t) \in \mathcal{P}_t \text{ for all } t\}
$$

where each $\mathcal{P}_t$ is specified independently.

**Example** (Non-Rectangular):

$$
\mathcal{P} = \{P: \mathbb{E}_P[\sum_{t=0}^T X_t] \in [a, b]\}
$$

Constraints across periods create non-rectangularity.

### 3. Main Theorem


**Theorem** (Epstein-Schneider, 2003): Max-min expected utility preferences with prior set $\mathcal{P}$ are dynamically consistent if and only if $\mathcal{P}$ is rectangular.

**Proof Sketch**:

*Necessity*: If $\mathcal{P}$ is not rectangular, construct a counterexample showing inconsistency.

*Sufficiency*: Under rectangularity:

$$
\min_{P \in \mathcal{P}} \mathbb{E}_P[U] = \min_{P_0 \in \mathcal{P}_0} \mathbb{E}_{P_0}\left[\min_{P_1 \in \mathcal{P}_1} \mathbb{E}_{P_1}[\cdots]\right]
$$

The tower property holds for the "min" operation, enabling backward induction.

## Recursive Preferences Under Ambiguity


### 1. Recursive Max-Min


**Formulation**: With rectangular priors, value function satisfies:

$$
V_t = \min_{P_t \in \mathcal{P}_t} \mathbb{E}_{P_t}[u(c_t) + \beta V_{t+1} | \mathcal{F}_t]
$$

**Properties**:
- Dynamically consistent by construction
- Nests EU as special case ($\mathcal{P}_t$ singleton)
- Tractable for computation

### 2. Epstein-Zin with Ambiguity


**Standard Epstein-Zin**:

$$
V_t = \left[(1-\beta) c_t^{1-1/\psi} + \beta \mu_t(V_{t+1})^{1-1/\psi}\right]^{1/(1-1/\psi)}
$$

where $\mu_t(V) = (\mathbb{E}_t[V^{1-\gamma}])^{1/(1-\gamma)}$.

**With Ambiguity**: Replace $\mu_t$ with robust certainty equivalent:

$$
\mu_t^R(V) = \min_{P_t \in \mathcal{P}_t} (\mathbb{E}_{P_t}[V^{1-\gamma}])^{1/(1-\gamma)}
$$

**Dynamic Consistency**: Preserved under rectangularity.

### 3. Smooth Ambiguity (Recursive)


**KMM Recursive**:

$$
V_t = u(c_t) + \beta \phi^{-1}\left(\mathbb{E}_{\mu_t}\left[\phi\left(\mathbb{E}_{P_t}[V_{t+1}]\right)\right]\right)
$$

where $\mu_t$ is a second-order probability over models.

**Dynamic Consistency**: Automatic with proper recursive structure.

## Variational Preferences


### 1. Static Formulation


**Definition** (Maccheroni-Marinacci-Rustichini, 2006):

$$
V(f) = \min_{P} \left\{\mathbb{E}_P[U(f)] + c(P)\right\}
$$

where $c: \mathcal{M}_1 \to [0, \infty]$ is a convex, lower semicontinuous cost function.

### 2. Dynamic Extension


**Conditional Cost Function**: For dynamic consistency, require cost function to factor:

$$
c(P) = \sum_{t=0}^{T-1} \mathbb{E}_P[c_t(P_{t+1}(\cdot | \mathcal{F}_t))]
$$

**Recursive Formulation**:

$$
V_t = \min_{P_t} \left\{\mathbb{E}_{P_t}[u(c_t, a_t) + \beta V_{t+1} | \mathcal{F}_t] + c_t(P_t)\right\}
$$

### 3. Multiplier Preferences (Hansen-Sargent)


**Static**: $c(P) = \theta D_{\text{KL}}(P \| P_0)$

**Dynamic**:

$$
V_t = \min_{P_t} \left\{\mathbb{E}_{P_t}[u_t + \beta V_{t+1} | \mathcal{F}_t] + \theta D_{\text{KL}}(P_t \| P_{0,t})\right\}
$$

**Solution**: Exponential tilting preserves dynamic consistency.

## Alternative Approaches to Inconsistency


### 1. Sophisticated Agents


**Definition**: A sophisticated agent anticipates future preference changes and optimizes accordingly.

**Backward Induction**: Solve for period-$T$ optimal action, then period-$(T-1)$ optimal given anticipated period-$T$ behavior, etc.

**Equilibrium**: Subgame-perfect equilibrium within the decision-maker.

### 2. Naive Agents


**Definition**: A naive agent ignores potential preference changes and assumes future selves will follow current optimal plan.

**Behavior**: Re-optimizes at each period, potentially cycling or exhibiting erratic behavior.

### 3. Pre-Commitment


**Definition**: Agent commits at $t=0$ to a complete strategy, enforced by external mechanism.

**Limitation**: Requires credible commitment technology.

**Examples**: 
- Pension contributions with withdrawal penalties
- Derivative contracts with fixed terms

### 4. Self-Control Preferences


**Gul-Pesendorfer**: Model temptation and self-control explicitly:

$$
V(B) = \max_{x \in B} \{u(x) + v(x)\} - \max_{y \in B} v(y)
$$

where $v$ represents temptation.

**Dynamic Consistency**: Maintained through recursive structure.

## Financial Applications


### 1. Dynamic Portfolio Choice


**Problem**: Invest over $T$ periods with ambiguity about return distribution.

**Inconsistent MEU**: Without rectangularity, $t=0$ plan may be abandoned at $t=1$.

**Rectangular Solution**: 

$$
V_t(W_t) = \max_{w_t} \min_{P_t \in \mathcal{P}_t} \mathbb{E}_{P_t}[V_{t+1}(W_{t+1}) | \mathcal{F}_t]
$$

with $W_{t+1} = W_t(1 + r_f + w_t^\top (R_t - r_f \mathbf{1}))$.

### 2. Robust Control in Finance


**Hansen-Sargent Setup**: Continuous-time wealth dynamics under model uncertainty.

**HJB Equation**:

$$
\rho V = \max_{c, w} \min_h \{u(c) + \mathcal{L}^{w,h} V - \frac{\theta}{2} h^2\}
$$

**Dynamic Consistency**: Preserved by quadratic penalty structure.

### 3. Dynamic Hedging


**Problem**: Hedge derivative over multiple periods with model uncertainty.

**Pathwise Hedging**: With rectangularity:

$$
\Pi_t = V_t - \Delta_t S_t
$$

is a supermartingale under all $P \in \mathcal{P}$.

**Rebalancing**: Consistent rebalancing strategy exists.

### 4. Risk Management Over Time


**Consistent Risk Measures**: For multi-period risk assessment, require:

$$
\rho_0(X) = \rho_0(\rho_1(X | \mathcal{F}_1))
$$

**Time Consistency of CVaR**: Standard CVaR is NOT time-consistent.

**Conditional Risk Measures**: Use recursive formulation:

$$
\rho_t(X) = \rho_t^{\text{1-period}}(\rho_{t+1}(X))
$$

## Behavioral Implications


### 1. Preference for Flexibility


**Observation**: Under ambiguity, agents may prefer to delay decisions.

**Mechanism**: Later periods reveal information that may resolve ambiguity.

**Implication**: Excess option value under ambiguity.

### 2. Aversion to Information


**Paradox**: Under certain non-EU preferences, agents may avoid costless information.

**Example**: With MEU, information that reveals which prior is worst-case may reduce welfare.

**Resolution**: Rectangular priors avoid this pathology.

### 3. Updating and Learning


**Bayesian Updating Under MEU**: For each $P \in \mathcal{P}$:

$$
P(\cdot | A) = \frac{P(\cdot \cap A)}{P(A)}
$$

**Challenge**: Updated set $\mathcal{P}_A = \{P(\cdot | A): P \in \mathcal{P}\}$ may not preserve rectangularity.

**Resolution**: Impose rectangularity on the dynamic structure, not just the initial set.

## Summary


### Key Results


1. **Dynamic Consistency Failure**: MEU and other non-EU preferences can be dynamically inconsistent

2. **Rectangularity Characterization**: Epstein-Schneider theorem: MEU is dynamically consistent iff priors are rectangular

3. **Recursive Formulation**: Proper recursive structure ensures consistency for variational and smooth ambiguity preferences

4. **Alternative Approaches**: Sophisticated agents, pre-commitment, and self-control models address inconsistency

### Practical Implications


1. **Model Design**: When building ambiguity models, ensure rectangularity or use recursive formulations

2. **Computational Tractability**: Dynamic consistency enables backward induction algorithms

3. **Interpretation**: Dynamically inconsistent preferences may reflect genuine psychological phenomena

4. **Risk Management**: Time-consistent risk measures require careful recursive construction

Dynamic consistency is essential for coherent multi-period decision-making and must be explicitly addressed when extending standard expected utility to incorporate ambiguity or robustness concerns.
