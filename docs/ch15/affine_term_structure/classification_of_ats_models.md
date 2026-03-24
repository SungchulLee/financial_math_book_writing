# Classification of Affine Term Structure Models

The affine term structure family contains a vast number of models, distinguished by the dimension of the state vector, the number of factors that drive stochastic volatility, and the correlation structure among factors. Without a systematic taxonomy, practitioners face a bewildering model zoo with no principled way to compare specifications. Dai and Singleton (2000) resolved this by introducing the **$A_m(d)$ classification**, which organizes every $d$-dimensional affine term structure model according to the number $m$ of state variables that enter the conditional variance. This section develops the classification, states the admissibility constraints that define each sub-class, introduces the notions of maximal and essential models, and maps the standard models of fixed-income finance into the taxonomy.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Define the $A_m(d)$ classification and explain its role in organizing affine term structure models
    2. State the admissibility constraints on drift, diffusion, and correlation parameters for each sub-class
    3. Distinguish between maximal and essential models and explain the identification problem
    4. Classify the Vasicek, CIR, and Heston models within the $A_m(d)$ framework
    5. Assess the trade-offs between model flexibility and tractability across sub-classes

---

## Motivation

### The Model Selection Problem

Consider a portfolio manager who needs to price and hedge a book of interest rate derivatives. The affine framework offers closed-form bond prices, but which affine model should be used? A one-factor Vasicek model? A two-factor CIR model? A three-factor model with correlated Gaussian and square-root factors?

Each choice involves different trade-offs: more factors improve the fit to the cross-section of yields, but increase the number of parameters and the risk of overfitting. Stochastic volatility factors capture time-varying yield volatility, but constrain the correlation structure. A systematic classification provides a map of the territory, showing exactly which models are nested within which, what each specification can and cannot capture, and where the boundaries of the affine family lie.

### From Ad Hoc to Systematic

Before Dai and Singleton (2000), affine models were specified on a case-by-case basis. The Vasicek (1977), CIR (1985), and Longstaff-Schwartz (1992) models were analyzed individually without a unifying framework. The $A_m(d)$ taxonomy brought order by showing that all these models are special cases of a single parametric family, distinguished by a single integer $m$.

---

## The Canonical Affine Specification

### State Dynamics

Consider a $d$-dimensional state vector $X_t$ with risk-neutral dynamics

$$
dX_t = (K_0 + K_1 X_t)\,dt + \Sigma(X_t)\,dW_t
$$

where $W_t$ is a $d$-dimensional Brownian motion under $\mathbb{Q}$, $K_0 \in \mathbb{R}^d$, $K_1 \in \mathbb{R}^{d \times d}$, and the instantaneous covariance matrix is

$$
\Sigma(X_t)\Sigma(X_t)^\top = H_0 + \sum_{i=1}^d H_i\,X_t^{(i)}
$$

with $H_0, H_1, \ldots, H_d \in \mathbb{R}^{d \times d}$ symmetric positive semi-definite matrices.

The short rate is affine:

$$
r_t = \rho_0 + \rho_1^\top X_t
$$

### The Role of $m$

!!! info "Definition: The Integer $m$"
    A $d$-dimensional affine term structure model belongs to class $A_m(d)$ if exactly $m$ of the $d$ state variables enter the conditional covariance matrix $\Sigma(X_t)\Sigma(X_t)^\top$ with nonzero coefficients. That is, $H_i \neq 0$ for exactly $m$ values of $i \in \{1, \ldots, d\}$.

The integer $m$ ranges from $0$ to $d$:

- **$A_0(d)$**: All $H_i = 0$ for $i \geq 1$. The covariance matrix $H_0$ is constant. These are **Gaussian** models (e.g., multi-factor Vasicek). The conditional distribution is normal, yields are normally distributed, and interest rates can go negative.
- **$A_d(d)$**: All factors contribute to the diffusion. These are **square-root** models (e.g., multi-factor CIR). The state-dependent volatility ensures non-negativity of the relevant state variables.
- **$A_m(d)$ with $0 < m < d$**: A mixture of $m$ CIR-type factors and $d - m$ Gaussian factors, enabling richer dynamics.

---

## Admissibility Constraints

### Why Constraints Are Needed

The affine specification imposes constraints beyond what a generic SDE requires. The instantaneous covariance matrix $H_0 + \sum_i H_i X_t^{(i)}$ must be positive semi-definite for **all** values of $X_t$ in the state space $D = \mathbb{R}_+^m \times \mathbb{R}^{d-m}$. Additionally, the drift must ensure that the first $m$ components remain non-negative. These requirements translate into algebraic constraints on the parameter matrices.

### Constraints for the Canonical Form

!!! info "Theorem: Dai-Singleton Admissibility Conditions"
    In the canonical $A_m(d)$ specification with state space $D = \mathbb{R}_+^m \times \mathbb{R}^{d-m}$, the following conditions are necessary and sufficient for the process to be well-defined:

    **Diffusion constraints:**

    1. $H_i$ is zero except possibly in the $(i,i)$ diagonal entry for $i = 1, \ldots, m$
    2. $H_0$ restricted to the last $d-m$ rows and columns is positive definite
    3. $H_0$ restricted to the first $m$ rows and columns is zero

    **Drift constraints (boundary non-attainment):**

    4. $(K_0)_i \geq 0$ for $i = 1, \ldots, m$ (drift pushes CIR-type components away from zero)
    5. $(K_1)_{ij} \geq 0$ for $i = 1, \ldots, m$ and $j \neq i$, $j \leq m$ (cross-effects among CIR components are non-negative)

    **Correlation constraints:**

    6. Off-diagonal terms coupling CIR and Gaussian components are constrained to maintain positive semi-definiteness of the total covariance

In the simplest form, the canonical $A_m(d)$ model partitions the state as $X_t = (X_t^+, X_t^G)$ where $X_t^+ \in \mathbb{R}_+^m$ collects the CIR-type components and $X_t^G \in \mathbb{R}^{d-m}$ collects the Gaussian components. The diffusion of each CIR component $X_t^{(i)}$ is proportional to $\sqrt{X_t^{(i)}}$, while the Gaussian components have constant diffusion.

---

## Maximal and Essential Models

### The Identification Problem

The parametrization of a $d$-dimensional affine model involves the matrices $K_0$, $K_1$, $H_0$, $H_1, \ldots, H_d$, $\rho_0$, $\rho_1$. Not all of these parameters are separately identified from bond price data, because an invertible linear transformation $\tilde{X}_t = C X_t + c$ preserves the affine structure while reshuffling the parameters.

!!! info "Definition: Maximal Model"
    The **maximal** $A_m(d)$ model is the specification that includes all parameters consistent with the admissibility constraints, without imposing any normalization beyond what is needed for the state space to be $\mathbb{R}_+^m \times \mathbb{R}^{d-m}$.

!!! info "Definition: Essential Model"
    An **essential** $A_m(d)$ model is obtained from the maximal model by imposing identification constraints that eliminate the freedom of affine state transformations. The essential model has the minimal number of free parameters consistent with a given $A_m(d)$ sub-class.

### Counting Parameters

For a $d$-dimensional affine model, the affine state transformation $X \mapsto CX + c$ has $d^2 + d$ free parameters ($d^2$ for the invertible matrix $C$ and $d$ for the translation $c$). The essential model therefore has $d^2 + d$ fewer parameters than the maximal model.

!!! example "Parameter Count for $A_1(3)$"
    The maximal $A_1(3)$ model has:

    - $K_0$: 3 parameters
    - $K_1$: 9 parameters
    - $H_0$: 6 parameters (symmetric $3 \times 3$ restricted by admissibility)
    - $H_1$: 1 parameter (only the $(1,1)$ entry)
    - $\rho_0, \rho_1$: 4 parameters

    Total: 23 parameters in the maximal model. After removing $3^2 + 3 = 12$ parameters through normalization, the essential $A_1(3)$ model has 11 free parameters.

---

## Classification of Standard Models

### One-Factor Models: $A_0(1)$ and $A_1(1)$

| Model | Class | Dynamics | Rates |
|---|---|---|---|
| Vasicek (1977) | $A_0(1)$ | $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$ | Can be negative |
| CIR (1985) | $A_1(1)$ | $dr_t = \kappa(\theta - r_t)\,dt + \xi\sqrt{r_t}\,dW_t$ | Non-negative |

The Vasicek model is the unique (up to reparametrization) one-factor Gaussian model: constant diffusion, Ornstein-Uhlenbeck dynamics. The CIR model is the unique one-factor square-root model.

### Two-Factor Models

!!! example "The $A_m(2)$ Family"
    For $d = 2$, there are three sub-classes:

    - **$A_0(2)$**: Two Gaussian factors (two-factor Vasicek). Both state variables can be negative. Six essential parameters.
    - **$A_1(2)$**: One CIR factor and one Gaussian factor. The Heston stochastic volatility model, when written as a term structure model, belongs here: the variance $V_t$ is the CIR factor and the log-price $\log S_t$ is the Gaussian factor.
    - **$A_2(2)$**: Two CIR factors (two-factor CIR). Both state variables are non-negative. Longstaff and Schwartz (1992) proposed a model of this type.

### Three-Factor Models and Beyond

The general $A_m(d)$ family grows rapidly with $d$. For $d = 3$, there are four sub-classes: $A_0(3)$, $A_1(3)$, $A_2(3)$, and $A_3(3)$. The $A_1(3)$ class is particularly popular in empirical work because it allows one stochastic volatility factor (capturing time-varying yield volatility) alongside two Gaussian factors (capturing level and slope).

---

## Trade-offs Across Sub-Classes

### Gaussian Models: $A_0(d)$

**Advantages:**

- The Riccati equations are **linear** and can be solved in closed form
- All conditional distributions are Gaussian, so likelihood functions are available analytically
- Yields are normally distributed, enabling simple econometric analysis

**Disadvantages:**

- Interest rates can go negative (problematic for nominal rates in normal environments)
- Yield volatilities are constant, contradicting the empirical evidence of time-varying volatility
- Cannot generate the volatility smile observed in interest rate options

### Square-Root Models: $A_d(d)$

**Advantages:**

- Non-negative interest rates guaranteed
- State-dependent volatility captures time-varying yield volatility
- Richer dynamics for option pricing

**Disadvantages:**

- The Riccati equations are **nonlinear** (though still solvable in closed form for CIR)
- Correlation structure is heavily constrained by admissibility
- Likelihood evaluation requires non-central chi-squared distributions

### Mixed Models: $A_m(d)$ with $0 < m < d$

**Advantages:**

- Combine the flexibility of Gaussian factors with the non-negativity and stochastic volatility of CIR factors
- Richer correlation structure than pure $A_d(d)$ models
- Can match a wider range of yield curve and volatility surface shapes

**Disadvantages:**

- More parameters to estimate
- Admissibility constraints reduce the effective parameter space
- Numerical Riccati solutions may be needed for multi-factor cases

---

## The Invariance Principle

!!! info "Proposition: Affine Invariance Under Linear Transformation"
    If $X_t$ is an affine process in the $A_m(d)$ class, then $\tilde{X}_t = CX_t + c$ for any invertible $C \in \mathbb{R}^{d \times d}$ and $c \in \mathbb{R}^d$ is also affine, with transformed parameters

    $$
    \tilde{K}_0 = CK_0 + K_1 C^{-1}c, \quad \tilde{K}_1 = CK_1C^{-1}, \quad \tilde{H}_0 = CH_0C^\top
    $$

    and similarly for the other parameters. The transformation preserves the bond price $P(t,T)$ but changes the state representation.

This invariance is why identification constraints are necessary: infinitely many different parametrizations of $(K_0, K_1, H_0, \ldots)$ generate the same bond prices and yields. The essential model fixes a canonical representative from each equivalence class.

---

## Summary

The Dai-Singleton $A_m(d)$ classification organizes the entire family of $d$-dimensional affine term structure models by the number $m$ of state variables entering the conditional covariance. At one extreme, $A_0(d)$ models are purely Gaussian with constant volatility and analytically tractable linear Riccati equations; at the other, $A_d(d)$ models have fully state-dependent volatility ensuring non-negative rates but imposing strict admissibility constraints. Intermediate $A_m(d)$ models balance flexibility against tractability. The distinction between maximal and essential models addresses the identification problem arising from the invariance of bond prices under affine state transformations. Standard models --- Vasicek as $A_0(1)$, CIR as $A_1(1)$, and the Heston-type specification as $A_1(2)$ --- are special cases within this unified framework.

---

## Further Reading

- Dai, Q. and Singleton, K. (2000). "Specification Analysis of Affine Term Structure Models." *Journal of Finance*, 55(5), 1943--1978.
- Duffie, D. and Kan, R. (1996). "A Yield-Factor Model of Interest Rates." *Mathematical Finance*, 6(4), 379--406.
- Collin-Dufresne, P., Goldstein, R., and Jones, C. (2008). "Identification of Maximal Affine Term Structure Models." *Journal of Finance*, 63(2), 743--795.
- Filipovic, D. (2009). *Term-Structure Models: A Graduate Course*. Springer.

---

## Exercises

**Exercise 1.** Classify each of the following models in the $A_m(d)$ framework:
(a) A three-factor model where all three state variables have constant diffusion coefficients.
(b) A two-factor model where both state variables have diffusion proportional to $\sqrt{X_t^{(i)}}$.
(c) A three-factor model with one CIR-type component and two Gaussian components.

---

**Exercise 2.** For the maximal $A_2(3)$ model, count the total number of parameters in the matrices $K_0$, $K_1$, $H_0$, $H_1$, $H_2$, $\rho_0$, $\rho_1$ (accounting for symmetry of the $H$ matrices and the admissibility constraints). Then compute the number of free parameters in the essential model after removing the $d^2 + d = 12$ normalization degrees of freedom.

---

**Exercise 3.** State the admissibility conditions on $K_0$ and $K_1$ for the canonical $A_1(2)$ model with state space $\mathbb{R}_+ \times \mathbb{R}$. In particular, explain why $(K_0)_1 \geq 0$ is required but there is no sign restriction on $(K_0)_2$.

---

**Exercise 4.** Consider an $A_0(2)$ model (two-factor Vasicek). The covariance matrix $\Sigma \Sigma^\top = H_0$ is constant. Show that the Riccati ODE for $B(\tau) \in \mathbb{R}^2$ is linear, and solve it explicitly when $K_1 = \operatorname{diag}(-\kappa_1, -\kappa_2)$ with $\kappa_1 \neq \kappa_2$.

---

**Exercise 5.** Explain why the Heston stochastic volatility model, when formulated as a term structure model on the state $(r_t, v_t)$, belongs to the class $A_1(2)$ and not $A_2(2)$. Which of the two state variables enters the conditional covariance with a nonzero coefficient?

---

**Exercise 6.** Let $X_t$ be an $A_1(1)$ process (CIR) and define $\tilde{X}_t = cX_t + d$ for constants $c > 0$ and $d \in \mathbb{R}$. Show that $\tilde{X}_t$ is still an affine process by computing its drift and diffusion. Is $\tilde{X}_t$ still in the $A_1(1)$ class? What constraints on $c$ and $d$ preserve the state space $\mathbb{R}_+$?

---

**Exercise 7.** A practitioner argues that an $A_3(3)$ model is always preferable to an $A_1(3)$ model because it has more stochastic volatility factors. Critique this argument by discussing:
(a) the admissibility constraints on the correlation structure in $A_3(3)$,
(b) the econometric challenges of estimating a larger parameter space, and
(c) scenarios where the $A_1(3)$ model might actually provide a better fit.
