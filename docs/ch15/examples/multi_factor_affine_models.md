# Multi-Factor Affine Models

Single-factor models cannot simultaneously match the level, slope, and curvature of the yield curve, nor can they reproduce the joint dynamics of interest rates, credit spreads, and volatility. Multi-factor affine models address these limitations by combining multiple state variables---some CIR-type (non-negative, driving stochastic volatility) and some Gaussian (unconstrained)---into a single affine framework. This section develops the $A_m(d)$ classification, constructs multi-factor models from building blocks, and examines how correlation between factors is introduced.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State the $A_m(d)$ classification of affine term structure models
    2. Construct multi-factor affine models by combining CIR and Gaussian components
    3. Explain how off-diagonal elements in the drift matrix create correlation between factors
    4. Write the Riccati system for a two-factor model and identify when it decouples

---

## Intuition

The yield curve has at least three independent degrees of freedom---level, slope, and curvature---that evolve stochastically. A single CIR or Vasicek factor can only generate parallel shifts in the yield curve. Two factors can capture level and slope. Three or more factors are needed for curvature and richer dynamics. The key design question is: how many of the $d$ factors should be CIR-type (non-negative, driving state-dependent volatility) and how many should be Gaussian? This choice determines the model's ability to produce stochastic volatility, non-negative rates, and fat tails, and is captured by the integer $m$ in the Dai-Singleton $A_m(d)$ classification.

---

## The Dai-Singleton Classification

### The Aₘ(d) Family

Recall (see [affine definition](../definition_and_setup/definition_of_affine_process.md)) the canonical state space $D = \mathbb{R}^m_+ \times \mathbb{R}^{d-m}$.

**Definition ($A_m(d)$ Models).** An affine term structure model with $d$ state variables, of which $m$ are CIR-type (non-negative), belongs to the $A_m(d)$ family, where $0 \leq m \leq d$.

### Classification Table

| Class | CIR | Gaussian | Key Features |
|-------|-----|----------|-------------|
| $A_0(d)$ | 0 | $d$ | Purely Gaussian. Vasicek-type. Negative rates possible. Constant volatility. |
| $A_1(d)$ | 1 | $d-1$ | One stochastic volatility factor. Most popular for equities. |
| $A_d(d)$ | $d$ | 0 | All CIR. Non-negative rates. Square-root volatility for all factors. |
| $A_m(d)$ | $m$ | $d-m$ | General case. Mixed dynamics. |

### Common Specifications

| Model | Classification | State Variables |
|-------|---------------|-----------------|
| Vasicek | $A_0(1)$ | $r_t$ |
| CIR | $A_1(1)$ | $r_t \geq 0$ |
| Two-factor Vasicek | $A_0(2)$ | $(r_t, s_t)$ |
| CIR + Vasicek | $A_1(2)$ | $(V_t \geq 0, r_t)$ |
| Two-factor CIR | $A_2(2)$ | $(r_t^{(1)} \geq 0, r_t^{(2)} \geq 0)$ |
| Heston | $A_1(2)$ | $(V_t \geq 0, \log S_t)$ |
| Three-factor | $A_1(3)$ or $A_2(3)$ | Level, slope, curvature |

---

## Building Multi-Factor Models

### Independent Factors

The simplest construction combines independent factors. Consider a two-factor CIR model where the short rate is the sum of two independent CIR processes:

$$
r_t = X_t^{(1)} + X_t^{(2)}
$$

$$
dX_t^{(i)} = \kappa_i(\theta_i - X_t^{(i)})\,dt + \xi_i\sqrt{X_t^{(i)}}\,dW_t^{(i)}, \quad i = 1, 2
$$

The state vector is $\mathbf{X}_t = (X_t^{(1)}, X_t^{(2)}) \in \mathbb{R}^2_+$ with affine parameters:

$$
b_0 = (\kappa_1\theta_1, \kappa_2\theta_2)^\top, \quad b_1 = \text{diag}(-\kappa_1, 0), \quad b_2 = \text{diag}(0, -\kappa_2)
$$

$$
a_0 = 0, \quad a_1 = \text{diag}(\xi_1^2, 0), \quad a_2 = \text{diag}(0, \xi_2^2)
$$

$$
\rho_0 = 0, \quad \rho_1 = (1, 1)^\top
$$

Since the factors are independent, the Riccati system decouples into two independent scalar Riccati equations:

$$
B_i'(\tau) = -\kappa_i B_i(\tau) + \frac{\xi_i^2}{2}B_i(\tau)^2 - 1, \quad B_i(0) = 0, \quad i = 1, 2
$$

$$
A'(\tau) = \kappa_1\theta_1 B_1(\tau) + \kappa_2\theta_2 B_2(\tau), \quad A(0) = 0
$$

Each $B_i$ has the standard CIR solution with its own discriminant $\gamma_i = \sqrt{\kappa_i^2 + 2\xi_i^2}$.

### Correlated Factors via Drift Coupling

Correlation between factors is introduced through off-diagonal elements in the drift matrix. Consider:

$$
d\mathbf{X}_t = (b_0 + B\,\mathbf{X}_t)\,dt + \text{diag}(\xi_1\sqrt{X_t^{(1)}}, \xi_2\sqrt{X_t^{(2)}})\,d\mathbf{W}_t
$$

where $B$ is a $2 \times 2$ matrix with off-diagonal elements:

$$
B = \begin{pmatrix} -\kappa_1 & \beta_{12} \\ \beta_{21} & -\kappa_2 \end{pmatrix}
$$

The off-diagonal terms $\beta_{12}$ and $\beta_{21}$ couple the drift of each factor to the level of the other, creating mean-reversion toward a target that depends on both factors. This coupling does not affect the diffusion matrix (which remains diagonal), but it couples the Riccati system: the $B_1$-equation now depends on $B_2$ and vice versa.

!!! warning "Admissibility Constraints on Coupling"
    Not all choices of $\beta_{12}$ and $\beta_{21}$ are admissible. For the process to remain in $\mathbb{R}^2_+$, the drift must point inward at the boundary. When $X_t^{(1)} = 0$, the drift in the first component is $\kappa_1\theta_1 + \beta_{12} X_t^{(2)}$, which must be non-negative for all $X_t^{(2)} \geq 0$. This requires $\beta_{12} \geq 0$ and $\kappa_1\theta_1 \geq 0$. Similarly, $\beta_{21} \geq 0$. These sign constraints limit the types of correlation that can be achieved through drift coupling alone.

---

## Correlation via Common Factors

### Correlated Brownian Motions

An alternative to drift coupling is using correlated driving Brownian motions. If $\text{Corr}(dW_t^{(1)}, dW_t^{(2)}) = \rho\,dt$, the diffusion matrix becomes:

$$
a(\mathbf{X}_t) = \begin{pmatrix} \xi_1^2 X_t^{(1)} & \rho\xi_1\xi_2\sqrt{X_t^{(1)} X_t^{(2)}} \\ \rho\xi_1\xi_2\sqrt{X_t^{(1)} X_t^{(2)}} & \xi_2^2 X_t^{(2)} \end{pmatrix}
$$

However, this diffusion matrix is **not affine** in $\mathbf{X}_t$ because of the $\sqrt{X_t^{(1)} X_t^{(2)}}$ cross-term. Direct Brownian correlation between two CIR processes breaks the affine structure.

### The Resolution: Latent Factor Approach

To achieve correlation while preserving the affine structure, introduce a common latent CIR factor $Z_t$:

$$
X_t^{(1)} = Y_t^{(1)} + Z_t, \qquad X_t^{(2)} = Y_t^{(2)} + Z_t
$$

where $Y_t^{(1)}, Y_t^{(2)}, Z_t$ are independent CIR processes. The common factor $Z_t$ induces positive correlation between $X_t^{(1)}$ and $X_t^{(2)}$:

$$
\text{Corr}(X_t^{(1)}, X_t^{(2)}) = \frac{\text{Var}(Z_t)}{\sqrt{\text{Var}(X_t^{(1)})\,\text{Var}(X_t^{(2)})}} > 0
$$

This latent factor construction is affine in the augmented state $(Y_t^{(1)}, Y_t^{(2)}, Z_t) \in \mathbb{R}^3_+$, and the Riccati system for the three independent factors decouples into three scalar equations.

---

## The Coupled Riccati System

### General Two-Factor System

For a coupled $A_2(2)$ model with drift matrix $B$:

$$
\mathbf{B}'(\tau) = B^\top \mathbf{B}(\tau) + \frac{1}{2}\begin{pmatrix} \xi_1^2 B_1(\tau)^2 \\ \xi_2^2 B_2(\tau)^2 \end{pmatrix} - \rho_1, \qquad \mathbf{B}(0) = 0
$$

$$
A'(\tau) = \langle b_0, \mathbf{B}(\tau) \rangle, \qquad A(0) = 0
$$

When $B$ is diagonal, the system decouples. When $B$ has off-diagonal elements, the system is coupled and typically requires numerical solution.

### Numerical Solution Strategy

For coupled systems:

1. Apply RK4 to the $\mathbf{B}$-system as a $d$-dimensional ODE
2. Use the solution $\mathbf{B}(\tau)$ to integrate $A(\tau)$ by quadrature
3. Total cost per frequency point: $O(N_\tau \cdot d^2)$

For $d = 3$ and $N_\tau = 1000$ (maturity $T = 10$ years with step $h = 0.01$), this takes microseconds on modern hardware.

??? example "Two-Factor CIR Model"
    Parameters: $\kappa_1 = 0.5$, $\theta_1 = 0.03$, $\xi_1 = 0.1$, $\kappa_2 = 0.2$, $\theta_2 = 0.02$, $\xi_2 = 0.08$, independent factors. Short rate $r_t = X_t^{(1)} + X_t^{(2)}$.

    Each factor has its own discriminant:

    $$
    \gamma_1 = \sqrt{0.25 + 0.02} = \sqrt{0.27} \approx 0.520
    $$

    $$
    \gamma_2 = \sqrt{0.04 + 0.0128} = \sqrt{0.0528} \approx 0.230
    $$

    The bond price is $P(t, T) = e^{A(\tau) + B_1(\tau)X_t^{(1)} + B_2(\tau)X_t^{(2)}}$ where each $B_i$ has the standard CIR formula. The two-factor model generates richer yield curve shapes (including humped curves) that a single CIR factor cannot produce. $\square$

---

## Yield Curve Flexibility

### Shapes Generated by Multi-Factor Models

| $d$ | Possible Yield Curve Shapes |
|-----|----------------------------|
| 1 | Monotone (upward or downward) |
| 2 | Monotone, humped, inverse humped |
| 3 | Monotone, humped, S-shaped, double-humped |
| $\geq 4$ | Arbitrary shapes (in practice) |

The level factor controls the overall height, the slope factor controls the difference between short and long rates, and the curvature factor controls the hump. This corresponds to the first three principal components of yield curve movements, which explain approximately 99% of the variance in practice.

---

## Summary

Multi-factor affine models in the $A_m(d)$ classification combine $m$ CIR-type and $d-m$ Gaussian factors to capture the rich dynamics of yield curves, credit spreads, and volatility surfaces. Independent factors decouple the Riccati system into scalar equations with explicit solutions. Correlated factors, introduced through drift coupling or common latent factors, produce coupled Riccati systems that typically require numerical solution. The latent factor approach preserves the affine structure while generating arbitrary positive correlations between CIR components. With $d \geq 3$ factors, multi-factor affine models can match essentially any yield curve shape and its dynamics.

---

## Further Reading

- Dai, Q. & Singleton, K. J. (2000). "Specification Analysis of Affine Term Structure Models." *Journal of Finance*, 55(5), 1943-1978.
- Duffie, D. & Kan, R. (1996). "A Yield-Factor Model of Interest Rates." *Mathematical Finance*, 6(4), 379-406.
- Piazzesi, M. (2010). "Affine Term Structure Models." *Handbook of Financial Econometrics*, Volume 1, 691-766.
- Filipovic, D. *Term-Structure Models: A Graduate Course*. Springer, 2009, Chapter 11.

---

## Exercises

**Exercise 1.** For the $A_0(3)$ model (three Gaussian factors), write the most general drift structure $b(x) = b_0 + Bx$ with a full $3 \times 3$ matrix $B$. How many free parameters does this model have (counting drift, diffusion, and short rate parameters)?

??? success "Solution to Exercise 1"
    For the $A_0(3)$ model, all three factors $X_1, X_2, X_3 \in \mathbb{R}$ are Gaussian. The drift structure is:

    $$
    b(\mathbf{X}) = b_0 + B\mathbf{X} = \begin{pmatrix} b_{0,1} \\ b_{0,2} \\ b_{0,3} \end{pmatrix} + \begin{pmatrix} B_{11} & B_{12} & B_{13} \\ B_{21} & B_{22} & B_{23} \\ B_{31} & B_{32} & B_{33} \end{pmatrix} \begin{pmatrix} X_1 \\ X_2 \\ X_3 \end{pmatrix}
    $$

    **Drift parameters**: $b_0$ has 3 free parameters and $B$ is a full $3 \times 3$ matrix with 9 free parameters, giving 12 drift parameters.

    **Diffusion parameters**: Since $m = 0$ (no CIR components), the diffusion is constant: $a(\mathbf{X}) = a_0$. The matrix $a_0$ is a $3 \times 3$ symmetric positive semi-definite matrix with $3(3+1)/2 = 6$ free parameters.

    **Short rate parameters**: $r(\mathbf{X}) = \rho_0 + \rho_1^\top \mathbf{X}$ gives 1 scalar $\rho_0$ and 3 components of $\rho_1$, for 4 parameters.

    **Total**: $12 + 6 + 4 = 22$ free parameters. However, without loss of generality, one can normalize the model by rotating the state vector (since the factors are latent). The rotation group $O(3)$ has 3 degrees of freedom, and one can also rescale and shift each factor (3 scales, 3 shifts). This removes up to 9 parameters, leaving approximately 13 identifiable parameters in a canonical form. The exact count depends on the normalization convention chosen.

---

**Exercise 2.** Consider the $A_1(2)$ model with one CIR factor $X_1 \geq 0$ and one Gaussian factor $X_2 \in \mathbb{R}$. If the short rate is $r_t = X_t^{(1)} + X_t^{(2)}$, write down the bond pricing Riccati system for $B_1(\tau)$ and $B_2(\tau)$. Under what condition on the drift matrix $B$ do these two equations decouple?

??? success "Solution to Exercise 2"
    For the $A_1(2)$ model with $r_t = X_t^{(1)} + X_t^{(2)}$, the short rate coefficients are $\rho_0 = 0$ and $\rho_1 = (1, 1)^\top$. The drift matrix is:

    $$
    B = \begin{pmatrix} -\kappa_1 & \beta_{12} \\ \beta_{21} & -\kappa_2 \end{pmatrix}
    $$

    The diffusion matrices are $\alpha_1 = \text{diag}(\xi_1^2, 0)$ (CIR component) and $\alpha_0 = \text{diag}(0, \sigma_2^2)$ (Gaussian constant diffusion).

    The Riccati system for $\mathbf{B}(\tau) = (B_1(\tau), B_2(\tau))^\top$ is:

    $$
    B_1'(\tau) = -\kappa_1 B_1 + \beta_{21} B_2 + \frac{1}{2}\xi_1^2 B_1^2 - 1
    $$

    $$
    B_2'(\tau) = \beta_{12} B_1 - \kappa_2 B_2 + \frac{1}{2}\sigma_2^2 B_2^2 - 1
    $$

    with $B_1(0) = B_2(0) = 0$.

    These equations decouple when $\beta_{12} = 0$ and $\beta_{21} = 0$, i.e., when the drift matrix $B$ is diagonal. In that case, the $B_1$-equation depends only on $B_1$ (a scalar Riccati) and the $B_2$-equation depends only on $B_2$ (also a scalar Riccati), each solvable independently with the standard CIR or Vasicek closed-form solutions.

---

**Exercise 3.** Explain why the $A_0(d)$ models (purely Gaussian) can produce negative interest rates while the $A_d(d)$ models (purely CIR) guarantee non-negative rates. What is the trade-off in terms of the volatility structure?

??? success "Solution to Exercise 3"
    **$A_0(d)$ models (purely Gaussian)**: All factors follow Ornstein-Uhlenbeck processes with constant diffusion. The transition densities are Gaussian, so each $X_t^{(i)}$ can take any value in $\mathbb{R}$. Since the short rate $r_t = \rho_0 + \rho_1^\top \mathbf{X}_t$ is a linear combination of Gaussian variables, it is itself Gaussian and can become negative with positive probability. The probability of negative rates depends on the parameters but is never zero.

    **$A_d(d)$ models (purely CIR)**: All factors are CIR-type with state space $\mathbb{R}^d_+$. Under the Feller condition ($2\kappa_i\theta_i \geq \xi_i^2$ for each factor), each $X_t^{(i)} > 0$ almost surely. If the short rate is $r_t = \rho_0 + \sum_i \rho_{1,i} X_t^{(i)}$ with $\rho_0 \geq 0$ and $\rho_{1,i} \geq 0$, then $r_t \geq 0$ at all times.

    **The trade-off**: Gaussian models ($A_0(d)$) have constant volatility, meaning the conditional variance of each factor does not depend on the current level. This is analytically convenient but fails to capture the empirical observation that interest rate volatility increases with the rate level. CIR models ($A_d(d)$) have level-dependent volatility ($\sigma \propto \sqrt{X}$), which matches empirical observations better but at the cost of non-Gaussian transition densities (non-central chi-squared) and more complex Riccati equations.

---

**Exercise 4.** For a two-factor CIR model ($A_2(2)$) with independent factors and short rate $r_t = X_t^{(1)} + X_t^{(2)}$, show that the bond price factors as $P(t,T) = P_1(t,T) \cdot P_2(t,T)$ where each $P_i$ is the bond price from a single-factor CIR model. Under what conditions does this factorization break down?

??? success "Solution to Exercise 4"
    With independent factors ($B$ diagonal, $\beta_{12} = \beta_{21} = 0$) and $r_t = X_t^{(1)} + X_t^{(2)}$, the bond price is:

    $$
    P(t, T) = \mathbb{E}\!\left[\exp\!\left(-\int_t^T (X_s^{(1)} + X_s^{(2)})\,ds\right) \bigg| \mathcal{F}_t\right]
    $$

    Since $X^{(1)}$ and $X^{(2)}$ are independent:

    $$
    = \mathbb{E}\!\left[\exp\!\left(-\int_t^T X_s^{(1)}\,ds\right)\bigg| X_t^{(1)}\right] \cdot \mathbb{E}\!\left[\exp\!\left(-\int_t^T X_s^{(2)}\,ds\right)\bigg| X_t^{(2)}\right]
    $$

    $$
    = P_1(t, T) \cdot P_2(t, T)
    $$

    where $P_i(t, T) = e^{A_i(\tau) + B_i(\tau) X_t^{(i)}}$ is the single-factor CIR bond price for factor $i$. The total bond price is:

    $$
    P(t, T) = \exp\!\left(A_1(\tau) + A_2(\tau) + B_1(\tau) X_t^{(1)} + B_2(\tau) X_t^{(2)}\right)
    $$

    This factorization breaks down when:

    1. **The drift matrix $B$ has off-diagonal elements** ($\beta_{12} \neq 0$ or $\beta_{21} \neq 0$), creating drift coupling between factors
    2. **The driving Brownian motions are correlated**, introducing cross-terms in the diffusion matrix
    3. **The short rate has cross-product terms** (e.g., $r_t = X_t^{(1)} X_t^{(2)}$, though this would also break the affine structure)

    In any of these cases, the joint expectation cannot be factored into a product of marginal expectations.

---

**Exercise 5.** The Dai-Singleton classification restricts the matrix $\Lambda$ in the market price of risk to ensure affine closure. For the $A_1(2)$ model, state the restriction and explain its origin: why can the Gaussian component have an unrestricted market price of risk while the CIR component cannot?

??? success "Solution to Exercise 5"
    In the $A_1(2)$ model, the market price of risk $\Lambda_t$ must preserve the affine structure when changing from the physical measure $\mathbb{P}$ to the risk-neutral measure $\mathbb{Q}$. Dai and Singleton (2000) show that $\Lambda_t$ must be of the form:

    $$
    \Lambda_t = \sqrt{S_t}\,\lambda
    $$

    where $S_t = \text{diag}(\alpha_0 + \alpha_1 X_t^{(1)})$ is the instantaneous covariance matrix and $\lambda$ is a vector of constants.

    For the **Gaussian component** ($X_t^{(2)}$): The diffusion is constant ($\sigma_2$), so the market price of risk $\lambda_2$ can be any constant. Under $\mathbb{Q}$, the drift shifts from $\kappa_2^{\mathbb{P}}(\theta_2^{\mathbb{P}} - X_t^{(2)})$ to $\kappa_2^{\mathbb{Q}}(\theta_2^{\mathbb{Q}} - X_t^{(2)})$, where $\kappa_2^{\mathbb{Q}}$ and $\theta_2^{\mathbb{Q}}$ are free parameters. The affine structure is preserved for any constant shift.

    For the **CIR component** ($X_t^{(1)} \geq 0$): The diffusion is $\xi_1\sqrt{X_t^{(1)}}$, so the market price of risk enters as $\lambda_1 \sqrt{X_t^{(1)}}$. Under Girsanov, the drift changes by $-\sigma(X_t) \Lambda_t \propto X_t^{(1)}$. This shifts the mean-reversion speed: $\kappa_1^{\mathbb{Q}} = \kappa_1^{\mathbb{P}} + \lambda_1 \xi_1$. The new drift $\kappa_1^{\mathbb{Q}}(\theta_1^{\mathbb{Q}} - X_t^{(1)})$ is still affine. However, $\lambda_1$ must be such that $\kappa_1^{\mathbb{Q}} > 0$ and $\theta_1^{\mathbb{Q}} > 0$ (admissibility). A more general (non-constant) $\lambda_1$ would introduce non-affine terms in the drift, destroying the tractability. This is why the CIR component's market price of risk is restricted to the "extended affine" form, where only level-proportional risk prices preserve the affine closure.

---

**Exercise 6.** A three-factor model with $d = 3$ and $m = 1$ (one CIR factor) can capture level, slope, and curvature of the yield curve. Describe qualitatively which factor controls which aspect of the yield curve, and explain why at least three factors are needed for a realistic model.

??? success "Solution to Exercise 6"
    Principal component analysis of yield curve movements reveals three dominant factors explaining approximately 99% of the total variance:

    **Factor 1 --- Level** (explains ~85% of variance): A CIR or Gaussian factor with slow mean reversion ($\kappa_1$ small). This factor shifts the entire yield curve up or down in parallel. When this factor increases, all yields rise by approximately the same amount. In a three-factor model, this is typically the dominant factor, often modeled as a CIR process to ensure non-negativity.

    **Factor 2 --- Slope** (explains ~10% of variance): A Gaussian factor with moderate mean reversion ($\kappa_2$ medium). This factor tilts the yield curve: when it increases, short rates rise more than long rates (or long rates fall relative to short rates), steepening or flattening the curve. The loading $B_2(\tau)$ has opposite signs at short and long maturities.

    **Factor 3 --- Curvature** (explains ~4% of variance): A Gaussian factor with fast mean reversion ($\kappa_3$ large). This factor creates or removes a hump in the yield curve. Its loading $B_3(\tau)$ is largest at intermediate maturities and small at both short and long maturities, producing a butterfly-shaped effect.

    **Why three factors are necessary**: A single factor can only produce monotone yield curves (upward or downward sloping). Two factors can generate monotone and humped curves, but cannot independently control the short end, the long end, and the intermediate maturities. Three factors are the minimum needed to reproduce the level-slope-curvature dynamics observed empirically, including humped, S-shaped, and double-humped yield curves. In practice, the first three principal components are stable across markets and time periods, making the three-factor specification a robust choice.
