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

??? success "Solution to Exercise 1"
    **(a)** Three factors, all with constant diffusion coefficients, means no state variable enters the conditional covariance. Hence $m = 0$ and $d = 3$: the model belongs to $A_0(3)$. This is a three-factor Gaussian (Vasicek-type) model.

    **(b)** Two factors, both with diffusion proportional to $\sqrt{X_t^{(i)}}$, means both state variables enter the covariance with nonzero coefficients. Hence $m = 2$ and $d = 2$: the model belongs to $A_2(2)$. This is a two-factor square-root (CIR-type) model, such as the Longstaff-Schwartz (1992) specification.

    **(c)** Three factors with one CIR-type component and two Gaussian components means exactly one state variable enters the covariance. Hence $m = 1$ and $d = 3$: the model belongs to $A_1(3)$. This is the most widely used specification in empirical term structure work, as it allows one stochastic volatility factor alongside two level/slope factors.

---

**Exercise 2.** For the maximal $A_2(3)$ model, count the total number of parameters in the matrices $K_0$, $K_1$, $H_0$, $H_1$, $H_2$, $\rho_0$, $\rho_1$ (accounting for symmetry of the $H$ matrices and the admissibility constraints). Then compute the number of free parameters in the essential model after removing the $d^2 + d = 12$ normalization degrees of freedom.

??? success "Solution to Exercise 2"
    **Maximal $A_2(3)$ parameter count.** The state space is $\mathbb{R}_+^2 \times \mathbb{R}$.

    - $K_0 \in \mathbb{R}^3$: 3 parameters
    - $K_1 \in \mathbb{R}^{3 \times 3}$: 9 parameters
    - $H_0 \in \mathbb{R}^{3 \times 3}$ symmetric: by admissibility, the first $2 \times 2$ block is zero, and the $(3,3)$ entry is positive. Additionally, the off-diagonal entries coupling CIR and Gaussian components are constrained. The Gaussian block is $1 \times 1$, giving 1 free entry, and cross-terms between CIR and Gaussian components contribute at most 2 entries. Total for $H_0$: at most 3 parameters.
    - $H_1 \in \mathbb{R}^{3 \times 3}$ symmetric: only the $(1,1)$ entry is nonzero (by canonical form). Total: 1 parameter.
    - $H_2 \in \mathbb{R}^{3 \times 3}$ symmetric: only the $(2,2)$ entry is nonzero. Total: 1 parameter.
    - $\rho_0 \in \mathbb{R}$: 1 parameter
    - $\rho_1 \in \mathbb{R}^3$: 3 parameters

    Total in the maximal model: $3 + 9 + 3 + 1 + 1 + 1 + 3 = 21$ parameters.

    The normalization group has $d^2 + d = 9 + 3 = 12$ degrees of freedom.

    Essential model: $21 - 12 = 9$ free parameters.

---

**Exercise 3.** State the admissibility conditions on $K_0$ and $K_1$ for the canonical $A_1(2)$ model with state space $\mathbb{R}_+ \times \mathbb{R}$. In particular, explain why $(K_0)_1 \geq 0$ is required but there is no sign restriction on $(K_0)_2$.

??? success "Solution to Exercise 3"
    In the canonical $A_1(2)$ model, the state space is $D = \mathbb{R}_+ \times \mathbb{R}$, where $X_t^{(1)} \geq 0$ (CIR-type) and $X_t^{(2)} \in \mathbb{R}$ (Gaussian).

    **Admissibility conditions on $K_0$:**

    - $(K_0)_1 \geq 0$: This ensures the drift of the first component pushes it away from the boundary at zero. Since $dX_t^{(1)} = ((K_0)_1 + (K_1)_{11}X_t^{(1)} + (K_1)_{12}X_t^{(2)})\,dt + \ldots$, the constant term $(K_0)_1$ must be non-negative so that when $X_t^{(1)}$ approaches zero, the drift remains non-negative (assuming $(K_1)_{12} X_t^{(2)}$ is controlled). This is the Feller-type boundary non-attainment condition.
    - $(K_0)_2$ has **no sign restriction**: The second component lives on $\mathbb{R}$, so its drift can push it in either direction. There is no boundary to protect.

    **Admissibility conditions on $K_1$:**

    - $(K_1)_{11}$ is typically negative (mean reversion of the CIR component), but the admissibility requirement is only that the overall drift keeps $X_t^{(1)} \geq 0$.
    - $(K_1)_{12}$: The cross-effect of $X_t^{(2)}$ on the drift of $X_t^{(1)}$ must be constrained. Since $X_t^{(2)}$ can be negative, a large positive $(K_1)_{12}$ could make the drift of $X_t^{(1)}$ negative. In the canonical form, $(K_1)_{12} = 0$ or is constrained to prevent the first component from reaching zero with positive probability.
    - $(K_1)_{21}$ and $(K_1)_{22}$ are unrestricted (they govern the Gaussian component).

---

**Exercise 4.** Consider an $A_0(2)$ model (two-factor Vasicek). The covariance matrix $\Sigma \Sigma^\top = H_0$ is constant. Show that the Riccati ODE for $B(\tau) \in \mathbb{R}^2$ is linear, and solve it explicitly when $K_1 = \operatorname{diag}(-\kappa_1, -\kappa_2)$ with $\kappa_1 \neq \kappa_2$.

??? success "Solution to Exercise 4"
    In the $A_0(2)$ model, $H_1 = H_2 = 0$, so the covariance is the constant matrix $H_0 = \Sigma\Sigma^\top$. The Riccati ODE for $B(\tau) = (B_1(\tau), B_2(\tau))^\top$ is

    $$
    \frac{dB}{d\tau} = -\rho_1 + K_1^\top B(\tau), \quad B(0) = \mathbf{0}
    $$

    since the quadratic terms $B^\top H_i B$ vanish for $i \geq 1$. This is a **linear** ODE system.

    With $K_1 = \operatorname{diag}(-\kappa_1, -\kappa_2)$ and $\rho_1 = (\rho_{1,1}, \rho_{1,2})^\top$:

    $$
    B_1'(\tau) = -\rho_{1,1} - \kappa_1 B_1(\tau), \quad B_1(0) = 0
    $$

    $$
    B_2'(\tau) = -\rho_{1,2} - \kappa_2 B_2(\tau), \quad B_2(0) = 0
    $$

    These are two decoupled first-order linear ODEs. Solving each:

    $$
    B_1(\tau) = -\frac{\rho_{1,1}}{\kappa_1}(1 - e^{-\kappa_1\tau})
    $$

    $$
    B_2(\tau) = -\frac{\rho_{1,2}}{\kappa_2}(1 - e^{-\kappa_2\tau})
    $$

    When $\kappa_1 \neq \kappa_2$, the two components decay at different rates, producing different maturity profiles for the factor loadings. The decoupling occurs because $K_1$ is diagonal and there are no quadratic terms.

---

**Exercise 5.** Explain why the Heston stochastic volatility model, when formulated as a term structure model on the state $(r_t, v_t)$, belongs to the class $A_1(2)$ and not $A_2(2)$. Which of the two state variables enters the conditional covariance with a nonzero coefficient?

??? success "Solution to Exercise 5"
    The Heston stochastic volatility model, formulated as a term structure model, has state $(r_t, v_t)$ where $v_t$ is the variance process. The dynamics are:

    $$
    dr_t = \mu_r(r_t, v_t)\,dt + \sqrt{v_t}\,dW_t^{(1)}
    $$

    $$
    dv_t = \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}
    $$

    The instantaneous covariance matrix is

    $$
    \Sigma(X_t)\Sigma(X_t)^\top = \begin{pmatrix} v_t & \rho\xi v_t \\ \rho\xi v_t & \xi^2 v_t \end{pmatrix} = v_t \begin{pmatrix} 1 & \rho\xi \\ \rho\xi & \xi^2 \end{pmatrix}
    $$

    This means $H_0 = 0$ (no constant covariance term) and $H_1 = 0$ (the first state variable $r_t$ does not enter the covariance). Only $H_2 \neq 0$ (the second state variable $v_t$ enters the covariance). Hence exactly $m = 1$ state variable drives the conditional variance, so the model belongs to $A_1(2)$.

    It is **not** $A_2(2)$ because $r_t$ does not appear in the diffusion matrix. The variance $v_t$ is the sole state variable that enters the conditional covariance with a nonzero coefficient.

---

**Exercise 6.** Let $X_t$ be an $A_1(1)$ process (CIR) and define $\tilde{X}_t = cX_t + d$ for constants $c > 0$ and $d \in \mathbb{R}$. Show that $\tilde{X}_t$ is still an affine process by computing its drift and diffusion. Is $\tilde{X}_t$ still in the $A_1(1)$ class? What constraints on $c$ and $d$ preserve the state space $\mathbb{R}_+$?

??? success "Solution to Exercise 6"
    Apply Ito's lemma to $\tilde{X}_t = cX_t + d$ where $X_t$ follows the CIR dynamics $dX_t = \kappa(\theta - X_t)\,dt + \xi\sqrt{X_t}\,dW_t$:

    $$
    d\tilde{X}_t = c\,dX_t = c\kappa(\theta - X_t)\,dt + c\xi\sqrt{X_t}\,dW_t
    $$

    Substituting $X_t = (\tilde{X}_t - d)/c$:

    $$
    d\tilde{X}_t = c\kappa\!\left(\theta - \frac{\tilde{X}_t - d}{c}\right)dt + c\xi\sqrt{\frac{\tilde{X}_t - d}{c}}\,dW_t
    $$

    $$
    = \kappa(c\theta + d - \tilde{X}_t)\,dt + \xi\sqrt{c(\tilde{X}_t - d)}\,dW_t
    $$

    **Is $\tilde{X}_t$ affine?** The drift is $\tilde{K}_0 + \tilde{K}_1 \tilde{X}_t$ with $\tilde{K}_0 = \kappa(c\theta + d)$ and $\tilde{K}_1 = -\kappa$, which is affine. The diffusion squared is $\xi^2 c(\tilde{X}_t - d) = -\xi^2 cd + \xi^2 c\,\tilde{X}_t$. This is affine in $\tilde{X}_t$, so $\tilde{X}_t$ is indeed an affine process.

    **Is it still $A_1(1)$?** The covariance $\tilde{H}_0 + \tilde{H}_1 \tilde{X}_t$ has $\tilde{H}_0 = -\xi^2 cd$ and $\tilde{H}_1 = \xi^2 c$. Since $c > 0$, we have $\tilde{H}_1 > 0$, so the state variable enters the diffusion: the model remains in the $A_1(1)$ class.

    **State space constraints.** For $\tilde{X}_t$ to live on $\mathbb{R}_+$, we need $\tilde{X}_t = cX_t + d \geq 0$ whenever $X_t \geq 0$. Since $c > 0$, this requires $d \geq 0$. Additionally, the constant covariance $\tilde{H}_0 = -\xi^2 cd$ must satisfy $\tilde{H}_0 \leq 0$ (so that total variance is non-negative at $\tilde{X}_t = 0$). With $c > 0$, this requires $d \geq 0$, consistent with the previous constraint. If $d > 0$, the state space shifts to $[d, \infty)$ rather than $[0, \infty)$, so to preserve $D = \mathbb{R}_+$, one needs $d = 0$. The constraint is therefore $c > 0$ and $d = 0$ (scaling only, no translation).

---

**Exercise 7.** A practitioner argues that an $A_3(3)$ model is always preferable to an $A_1(3)$ model because it has more stochastic volatility factors. Critique this argument by discussing:
(a) the admissibility constraints on the correlation structure in $A_3(3)$,
(b) the econometric challenges of estimating a larger parameter space, and
(c) scenarios where the $A_1(3)$ model might actually provide a better fit.

??? success "Solution to Exercise 7"
    **(a) Admissibility constraints on $A_3(3)$.** In the $A_3(3)$ class, all three state variables are CIR-type, living on $\mathbb{R}_+^3$. The covariance matrix $\sum_{i=1}^3 H_i X_t^{(i)}$ must be positive semi-definite for all $(X_t^{(1)}, X_t^{(2)}, X_t^{(3)}) \in \mathbb{R}_+^3$. This imposes severe restrictions on the off-diagonal entries of $H_i$: the cross-correlations between factors are tightly constrained, often forced to zero in the canonical form. By contrast, $A_1(3)$ has two Gaussian factors with a constant covariance block $H_0$ that can have arbitrary (positive definite) off-diagonal terms, allowing much richer correlation structure among the Gaussian components.

    **(b) Econometric challenges.** Even though $A_3(3)$ has more stochastic volatility, it does not necessarily have more free parameters after admissibility constraints are imposed. However, the likelihood function involves non-central chi-squared distributions for all three factors (rather than normal distributions for two of them in $A_1(3)$), making maximum likelihood estimation significantly more expensive. Furthermore, the larger number of nonlinear Riccati equations increases the computational cost of bond pricing and calibration. Overfitting is also a concern: more volatility factors can fit noise in the training sample without improving out-of-sample prediction.

    **(c) Scenarios where $A_1(3)$ provides a better fit.** The $A_1(3)$ model is preferable when:

    - **Yield data is approximately normally distributed**: If the empirical distribution of yield changes is close to Gaussian, the two Gaussian factors in $A_1(3)$ provide a natural match, while the three square-root factors in $A_3(3)$ impose asymmetry that may not be present in the data.
    - **The correlation structure matters**: The unrestricted correlation among the Gaussian factors in $A_1(3)$ can better capture the joint dynamics of level, slope, and curvature, which are empirically correlated. The $A_3(3)$ model's admissibility constraints may force correlations that are inconsistent with the data.
    - **Negative rates are observed**: $A_3(3)$ forces all state variables to be non-negative, making it impossible to fit environments with negative short rates (as observed in Europe and Japan). The Gaussian factors in $A_1(3)$ can accommodate negative rates naturally.
