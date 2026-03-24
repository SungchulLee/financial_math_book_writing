# Correlation Structure

The correlations between components of a multidimensional affine process are encoded in the off-diagonal elements of the instantaneous covariance matrix $a(x) = a_0 + \sum_i \alpha_i x^{(i)}$. Because this covariance is itself an affine function of the state, the instantaneous correlation between components is generally **state-dependent** --- a feature that captures the leverage effect in equity markets and the time-varying comovement of yields across maturities. However, the affine structure also imposes significant constraints: not every desired correlation pattern is achievable while maintaining admissibility. This section develops the correlation structure of affine processes, derives the key limitations, and illustrates the trade-offs with the Heston model and multi-factor interest rate models.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Compute instantaneous correlations from the affine covariance matrix $a(x)$
    2. Identify which correlation specifications are compatible with admissibility constraints
    3. Derive the leverage effect parameter $\rho$ in the Heston model from the affine covariance structure
    4. Explain why affine models have limited ability to generate time-varying correlations
    5. Assess the implications of correlation constraints for model calibration

---

## Motivation

### Why Correlation Matters

In equity derivatives, the correlation between asset returns and volatility --- the **leverage effect** --- drives the implied volatility skew. In fixed income, the correlations between short-rate factors, long-rate factors, and volatility factors determine the shape and dynamics of the yield curve. In credit, the correlation between default intensities of different obligors determines portfolio loss distributions.

Modeling these correlations correctly is essential for accurate pricing and hedging. The affine framework provides a tractable way to incorporate correlations, but the admissibility conditions constrain which correlation structures are achievable. Understanding these constraints is crucial for choosing the right model specification.

---

## Instantaneous Correlation

### Derivation from the Covariance Matrix

For a $d$-dimensional affine diffusion with instantaneous covariance $a(x) = a_0 + \sum_{i=1}^d \alpha_i x^{(i)}$, the instantaneous covariance between the $k$-th and $l$-th components is

$$
\operatorname{Cov}_t\!\bigl[dX_t^{(k)}, dX_t^{(l)}\bigr] = a_{kl}(X_t)\,dt
$$

The **instantaneous correlation** is

$$
\rho_{kl}(X_t) = \frac{a_{kl}(X_t)}{\sqrt{a_{kk}(X_t)\,a_{ll}(X_t)}}
$$

!!! info "Proposition: State-Dependent Correlation in Affine Models"
    If both $a_{kk}(x)$ and $a_{ll}(x)$ depend on the state through different components, the instantaneous correlation $\rho_{kl}(x)$ is a **nonlinear function** of $x$, even though the covariance matrix is affine in $x$.

This nonlinearity arises because correlation is a ratio involving square roots of diagonal entries. An affine covariance does not imply an affine correlation.

### Constant vs. State-Dependent Correlation

**Case 1: Both components Gaussian ($k, l \in J$).** Then $a_{kk}(x) = (a_0)_{kk}$ and $a_{ll}(x) = (a_0)_{ll}$ (constant), and $a_{kl}(x) = (a_0)_{kl}$ (constant). The correlation $\rho_{kl}$ is **constant**.

**Case 2: One CIR, one Gaussian ($k \in I$, $l \in J$).** Then $a_{kk}(x) = (\alpha_k)_{kk} x^{(k)}$, $a_{ll}(x) = (a_0)_{ll}$, and $a_{kl}(x) = (\alpha_k)_{kl} x^{(k)}$. The correlation is

$$
\rho_{kl}(x) = \frac{(\alpha_k)_{kl}\,x^{(k)}}{\sqrt{(\alpha_k)_{kk}\,x^{(k)} \cdot (a_0)_{ll}}} = \frac{(\alpha_k)_{kl}}{\sqrt{(\alpha_k)_{kk} \cdot (a_0)_{ll}}} \cdot \sqrt{x^{(k)}} \cdot \frac{1}{\sqrt{x^{(k)}}}
$$

Wait --- simplifying properly: the $x^{(k)}$ cancels in numerator and denominator, giving a **constant** correlation:

$$
\rho_{kl} = \frac{(\alpha_k)_{kl}}{\sqrt{(\alpha_k)_{kk} \cdot (a_0)_{ll}}}
$$

This is the situation in the Heston model, where the correlation $\rho$ between returns and variance is a fixed parameter.

**Case 3: Two CIR components driven by different state variables ($k, l \in I$, $k \neq l$).** The covariance $a_{kl}(x)$ can depend on $x^{(k)}$ and $x^{(l)}$ through $(\alpha_k)_{kl} x^{(k)} + (\alpha_l)_{kl} x^{(l)}$. If this dependence is nontrivial, the correlation becomes genuinely state-dependent.

---

## The Heston Leverage Effect

### Covariance Structure

In the Heston model with state $X_t = (V_t, \log S_t)^\top$, the covariance matrix is

$$
a(X_t) = \alpha_1\,V_t = \begin{pmatrix} \xi^2 & \rho\xi \\ \rho\xi & 1 \end{pmatrix}V_t
$$

The instantaneous covariance between $d\log S_t$ and $dV_t$ is $\rho\xi\,V_t\,dt$, and the correlation is

$$
\rho_{12} = \frac{\rho\xi\,V_t}{\sqrt{\xi^2 V_t \cdot V_t}} = \frac{\rho\xi}{\xi} = \rho
$$

The correlation parameter $\rho$ in the Heston model is therefore the **instantaneous correlation** between the return $d\log S_t$ and the variance change $dV_t$.

!!! example "Financial Interpretation of Leverage"
    Empirically, $\rho < 0$ for equity markets (typically $\rho \in [-0.9, -0.5]$): when stock prices fall, volatility tends to rise. This negative correlation generates the **implied volatility skew** --- out-of-the-money puts are more expensive than out-of-the-money calls.

    Setting $\rho = 0$ recovers a model where returns and volatility are independent, producing a symmetric implied volatility smile rather than a skew.

### Admissibility Constraint on Correlation

The matrix $\alpha_1$ must be positive semi-definite, requiring

$$
\det(\alpha_1) = \xi^2 \cdot 1 - (\rho\xi)^2 = \xi^2(1 - \rho^2) \geq 0
$$

This gives $|\rho| \leq 1$, which is the natural constraint on a correlation parameter. The admissibility condition automatically enforces this.

---

## Correlation Constraints in Multi-Factor Models

### The $A_m(d)$ Constraints

For a general $A_m(d)$ model, the correlation structure is constrained by the positive semi-definiteness of $a(x)$ for all $x \in D$. This imposes restrictions beyond the simple $|\rho| \leq 1$ condition.

!!! info "Proposition: Correlation Constraints in $A_2(3)$"
    For a three-factor model with two CIR components ($V_1, V_2 \in \mathbb{R}_+$) and one Gaussian component ($r \in \mathbb{R}$), the covariance matrix is

    $$
    a(x) = a_0 + \alpha_1 V_1 + \alpha_2 V_2
    $$

    The conditions for $a(x) \succeq 0$ for all $V_1, V_2 \geq 0$ require:

    1. $a_0 \succeq 0$
    2. $\alpha_1 \succeq 0$ and $\alpha_2 \succeq 0$
    3. No cancellation: $a_0 + \alpha_1 V_1 + \alpha_2 V_2 \succeq 0$ must hold even at the boundary where $V_1 = 0$ or $V_2 = 0$

    These constraints are more restrictive than requiring $a(x) \succeq 0$ at a single point.

### Off-Diagonal Constraints

Between two CIR components $X^{(k)}$ and $X^{(l)}$ with $k, l \in I$, the admissibility condition (A4) from the [admissibility section](admissibility_conditions.md) requires $(\alpha_i)_{kk} = 0$ for $i \neq k$. This means the variance of the $k$-th component is driven only by $x^{(k)}$ itself. However, the **covariance** between $k$ and $l$ can depend on both $x^{(k)}$ and $x^{(l)}$:

$$
a_{kl}(x) = (a_0)_{kl} + (\alpha_k)_{kl}\,x^{(k)} + (\alpha_l)_{kl}\,x^{(l)}
$$

The positive semi-definiteness requirement constrains $(\alpha_k)_{kl}$ and $(\alpha_l)_{kl}$ jointly with the diagonal terms.

---

## Limitations of the Affine Correlation Structure

### What Affine Models Cannot Do

!!! warning "Fixed Correlation Topology"
    In the standard affine framework, the instantaneous correlation between Gaussian components is constant (determined by $a_0$), and the correlation between a CIR component and any other component is at most a simple function of the CIR state variables. This means:

    1. **Stochastic correlation** between returns and volatility (beyond the fixed $\rho$) is not available in the basic Heston model
    2. **Regime-dependent correlations** (e.g., correlations increasing during crises) require additional state variables
    3. **Arbitrary time-varying correlations** cannot be achieved without breaking the affine structure

### Workarounds

Several extensions address these limitations while preserving partial tractability:

- **Multi-factor stochastic volatility**: Using multiple CIR factors with different correlations to returns creates an effective time-varying correlation through the mix of active factors
- **Wishart affine processes**: Extending the state space to include matrix-valued processes (Bru, 1991; Gourieroux and Sufana, 2003) allows the entire covariance matrix to be stochastic and affine
- **Regime-switching affine models**: Different parameter sets (including correlations) in different regimes, with affine structure within each regime

---

## Example: Two-Factor Interest Rate Model

Consider an $A_1(2)$ model with state $(V_t, r_t)$ where $V_t \geq 0$ is a volatility factor and $r_t \in \mathbb{R}$ is the short rate:

$$
dV_t = \kappa_V(\theta_V - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^{(1)}
$$

$$
dr_t = \kappa_r(\theta_r - r_t)\,dt + \sigma_r\,dW_t^{(2)} + \eta\sqrt{V_t}\,dW_t^{(1)}
$$

The covariance matrix is

$$
a(V_t) = \begin{pmatrix} 0 \\ 0 \end{pmatrix} + \begin{pmatrix} \xi^2 & \eta\xi \\ \eta\xi & \sigma_r^2/V_t \cdot V_t + \eta^2 \end{pmatrix}V_t
$$

Wait --- let us be more careful. Actually with constant $\sigma_r$:

$$
a(x) = \begin{pmatrix} 0 & 0 \\ 0 & \sigma_r^2 \end{pmatrix} + \begin{pmatrix} \xi^2 & \eta\xi \\ \eta\xi & \eta^2 \end{pmatrix}V_t
$$

Here $a_0 = \operatorname{diag}(0, \sigma_r^2)$ and $\alpha_1 = \begin{pmatrix} \xi^2 & \eta\xi \\ \eta\xi & \eta^2 \end{pmatrix}$.

The instantaneous correlation between $dV_t$ and $dr_t$ is

$$
\rho_{Vr}(V_t) = \frac{\eta\xi\,V_t}{\sqrt{\xi^2 V_t \cdot (\sigma_r^2 + \eta^2 V_t)}} = \frac{\eta\xi\sqrt{V_t}}{\xi\sqrt{\sigma_r^2 + \eta^2 V_t}} = \frac{\eta\sqrt{V_t}}{\sqrt{\sigma_r^2 + \eta^2 V_t}}
$$

This correlation is **state-dependent**: it increases with $V_t$ (approaching $\eta/|\eta| = \operatorname{sign}(\eta)$ as $V_t \to \infty$) and vanishes as $V_t \to 0$ (because the volatility factor contributes no noise at the boundary). This is a genuine stochastic correlation effect within the affine framework, arising because the Gaussian component has both a constant diffusion ($\sigma_r$) and a state-dependent diffusion ($\eta\sqrt{V_t}$).

---

## Summary

The correlation structure of multidimensional affine processes is encoded in the off-diagonal elements of the affine covariance matrix $a(x) = a_0 + \sum_i \alpha_i x^{(i)}$. For two Gaussian components, the correlation is constant; for a CIR-Gaussian pair with diffusion driven only by the CIR component, the correlation simplifies to a constant parameter (as in Heston's $\rho$). State-dependent correlations arise when both constant and state-dependent diffusion terms contribute to the same component. The admissibility conditions --- particularly positive semi-definiteness of $a(x)$ for all $x \in D$ --- constrain the achievable correlation patterns and impose restrictions on model parameters. The affine framework cannot generate arbitrary time-varying correlations, motivating extensions such as Wishart processes and multi-factor specifications that increase the effective dimensionality of the correlation structure.

---

## Further Reading

- Heston, S. (1993). "A Closed-Form Solution for Options with Stochastic Volatility." *Review of Financial Studies*, 6(2), 327--343.
- Dai, Q. and Singleton, K. (2000). "Specification Analysis of Affine Term Structure Models." *Journal of Finance*, 55(5), 1943--1978.
- Gourieroux, C. and Sufana, R. (2003). "Wishart Quadratic Term Structure Models." Working Paper, CREST.
- Filipovic, D. (2009). *Term-Structure Models: A Graduate Course*. Springer.

---

## Exercises

**Exercise 1.** For the Heston model with covariance matrix $a(V) = V \begin{pmatrix} 1 & \rho\xi \\ \rho\xi & \xi^2 \end{pmatrix}$, compute the instantaneous correlation $\operatorname{Corr}(d\log S_t, dV_t) = \rho\xi\sqrt{V}/(\sqrt{V}\cdot\xi\sqrt{V}) = \rho$. Verify that the correlation is state-independent and equals $\rho$.

---

**Exercise 2.** For a two-factor CIR model on $\mathbb{R}_+^2$ with independent components (no off-diagonal terms in $\alpha_1$ or $\alpha_2$), show that the instantaneous correlation between $X_t^{(1)}$ and $X_t^{(2)}$ is zero. Can a two-factor CIR model ever produce nonzero instantaneous correlation while maintaining admissibility?

---

**Exercise 3.** Consider a three-factor model on $\mathbb{R}_+ \times \mathbb{R}^2$ where the CIR component $V_t$ drives the diffusion of both Gaussian factors. Write the diffusion matrix $a(x) = a_0 + \alpha_1 V$ and compute the instantaneous correlation between the two Gaussian factors as a function of $V_t$. Is this correlation time-varying?

---

**Exercise 4.** Explain the leverage effect in the context of the Heston model: why does $\rho < 0$ imply that stock price declines are associated with volatility increases? Derive the covariance $\operatorname{Cov}(d\log S_t, dV_t) = \rho\xi V_t\,dt$ and interpret the state-dependence on $V_t$.

---

**Exercise 5.** For the Dai-Singleton $A_1(3)$ model with one CIR factor and two Gaussian factors, what is the maximum number of free correlation parameters? Compare this to the three independent correlations in a general $3 \times 3$ correlation matrix, and explain why affine models have restricted correlation flexibility.

---

**Exercise 6.** In calibrating the Heston model to equity options, the correlation parameter $\rho$ primarily controls the skew of the implied volatility smile. Describe qualitatively how the implied volatility smile changes as $\rho$ varies from $-0.9$ to $0$. Why can't the affine structure generate a purely symmetric smile with $\rho = 0$ and still match observed market skews?
