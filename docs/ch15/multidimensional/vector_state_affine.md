# Vector State Affine Processes

Single-factor affine models produce yield curves and volatility surfaces that are too rigid for practical applications: a one-factor model ties level, slope, and curvature of the yield curve to a single state variable, and cannot generate the independent movements observed in data. The extension to **vector-valued** affine processes on $D = \mathbb{R}_+^m \times \mathbb{R}^{d-m}$ introduces multiple interacting factors that can separately drive stochastic volatility, mean-reverting rates, and long-run levels. This section develops the full multidimensional affine framework: the state space structure, affine drift-diffusion-jump specification, the vector Riccati system, and the key examples that motivate the theory.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Write down the SDE system for a $d$-dimensional affine process with state space $\mathbb{R}_+^m \times \mathbb{R}^{d-m}$
    2. Identify the affine drift, diffusion, and jump components in vector form
    3. Derive the $d$-dimensional Riccati ODE system for the characteristic function
    4. Explain the role of the non-negative components $\mathbb{R}_+^m$ in modeling stochastic volatility and non-negative rates
    5. Formulate the Heston model as a two-dimensional affine process

---

## Motivation

### Why Multiple Factors

Empirical studies of interest rate markets consistently identify at least three independent sources of yield curve variation (level, slope, curvature). Equity derivatives markets exhibit stochastic volatility that evolves semi-independently of the underlying price. Credit markets require separate default intensity and recovery rate dynamics. A single-factor affine model cannot capture any of these phenomena adequately.

The multidimensional affine framework addresses this by allowing $d$ state variables to interact through correlated Brownian motions, cross-effects in the drift matrix, and state-dependent diffusion. The affine structure ensures that the resulting Riccati system is a system of $d$ coupled ODEs --- more complex than the scalar case, but still far more tractable than a general $d$-dimensional PDE.

### The State Space Structure

The state space $D = \mathbb{R}_+^m \times \mathbb{R}^{d-m}$ has a natural financial interpretation:

- The first $m$ components live in $\mathbb{R}_+$ and model **non-negative quantities**: variance processes, interest rates, default intensities
- The remaining $d - m$ components live in $\mathbb{R}$ and model **unrestricted quantities**: log-prices, Gaussian interest rate factors, spreads

The non-negative components have square-root (CIR-type) diffusion that vanishes at zero, ensuring the process stays in $\mathbb{R}_+^m$. The Gaussian components have constant diffusion and can take any real value.

---

## The Vector Affine SDE

### General Specification

!!! info "Definition: Vector Affine Process"
    A $d$-dimensional affine process $X_t = (X_t^{(1)}, \ldots, X_t^{(d)})^\top$ on the state space $D = \mathbb{R}_+^m \times \mathbb{R}^{d-m}$ satisfies the SDE

    $$
    dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t + dJ_t
    $$

    where the coefficients are affine in the state:

    **Drift:**

    $$
    \mu(x) = b_0 + B\,x
    $$

    with $b_0 \in \mathbb{R}^d$ and $B \in \mathbb{R}^{d \times d}$.

    **Instantaneous covariance:**

    $$
    a(x) = \sigma(x)\sigma(x)^\top = a_0 + \sum_{i=1}^d \alpha_i\,x^{(i)}
    $$

    with $a_0, \alpha_1, \ldots, \alpha_d \in \mathbb{R}^{d \times d}$ symmetric positive semi-definite.

    **Jump compensator:**

    $$
    m(x, dz) = m_0(dz) + \sum_{i=1}^d x^{(i)}\,m_i(dz)
    $$

    where $m_0, m_1, \ldots, m_d$ are Levy measures on $\mathbb{R}^d \setminus \{0\}$.

### Component-Wise Structure

For the standard partition $X_t = (X_t^+, X_t^G)$ with $X_t^+ \in \mathbb{R}_+^m$ and $X_t^G \in \mathbb{R}^{d-m}$, the SDE system takes the block form:

**CIR-type components** ($i = 1, \ldots, m$):

$$
dX_t^{(i)} = \left(b_0^{(i)} + \sum_{j=1}^d B_{ij}\,X_t^{(j)}\right)dt + \sqrt{\alpha_{ii}\,X_t^{(i)}}\,dW_t^{(i)} + \text{cross-diffusion terms}
$$

where $b_0^{(i)} \geq 0$ and the diagonal diffusion coefficient is proportional to $\sqrt{X_t^{(i)}}$.

**Gaussian components** ($i = m+1, \ldots, d$):

$$
dX_t^{(i)} = \left(b_0^{(i)} + \sum_{j=1}^d B_{ij}\,X_t^{(j)}\right)dt + \sigma_i\,dW_t^{(i)} + \text{cross-diffusion terms}
$$

where $\sigma_i > 0$ is constant.

---

## The Vector Riccati System

### Characteristic Function

The conditional characteristic function of the vector affine process has the exponential-affine form:

$$
\mathbb{E}\!\left[e^{u^\top X_T} \mid X_t = x\right] = \exp\!\bigl(\phi(\tau, u) + \psi(\tau, u)^\top x\bigr)
$$

where $\tau = T - t$, $\phi : \mathbb{R}_+ \times \mathcal{U} \to \mathbb{C}$, and $\psi : \mathbb{R}_+ \times \mathcal{U} \to \mathbb{C}^d$.

### The Riccati ODEs

!!! info "Theorem: Vector Riccati System"
    The functions $\phi$ and $\psi$ satisfy the system

    $$
    \frac{d\psi_i}{d\tau} = R_i(\psi) = (B^\top\psi)_i + \frac{1}{2}\psi^\top\alpha_i\,\psi + \int_{\mathbb{R}^d \setminus \{0\}} \bigl(e^{\psi^\top z} - 1 - \psi^\top h(z)\bigr)\,m_i(dz)
    $$

    for $i = 1, \ldots, d$, and

    $$
    \frac{d\phi}{d\tau} = F(\psi) = b_0^\top\psi + \frac{1}{2}\psi^\top a_0\,\psi + \int_{\mathbb{R}^d \setminus \{0\}} \bigl(e^{\psi^\top z} - 1 - \psi^\top h(z)\bigr)\,m_0(dz)
    $$

    with initial conditions $\psi(0, u) = u$ and $\phi(0, u) = 0$.

The system for $\psi$ is a $d$-dimensional ODE that couples through the matrices $B$, $\alpha_i$, and the jump measures $m_i$. The equation for $\phi$ is scalar and driven by $\psi$: once $\psi(\tau)$ is known, $\phi(\tau)$ is obtained by a single quadrature.

### Structure of the Coupling

The quadratic term $\frac{1}{2}\psi^\top\alpha_i\psi$ in the $\psi_i$ equation produces the **nonlinear coupling** between components. For $A_0(d)$ models (purely Gaussian), all $\alpha_i = 0$ for $i \geq 1$, so the $\psi$ equation is linear in $\psi$ and can be solved by matrix exponentials:

$$
\psi(\tau) = e^{B^\top\tau}\,u
$$

For $A_m(d)$ models with $m > 0$, the quadratic terms make the system genuinely nonlinear, typically requiring numerical solution except in special cases (e.g., diagonal systems where each $\psi_i$ decouples).

---

## Key Examples

### Two-Factor Gaussian Model: $A_0(2)$

State: $X_t = (r_t, \ell_t)^\top \in \mathbb{R}^2$ where $r_t$ is a short-rate factor and $\ell_t$ is a long-rate factor.

$$
\begin{pmatrix} dr_t \\ d\ell_t \end{pmatrix} = \begin{pmatrix} \kappa_r(\theta_r - r_t) + \beta\,\ell_t \\ \kappa_\ell(\theta_\ell - \ell_t) \end{pmatrix}dt + \begin{pmatrix} \sigma_r & 0 \\ 0 & \sigma_\ell \end{pmatrix}\begin{pmatrix} dW_t^{(1)} \\ dW_t^{(2)} \end{pmatrix}
$$

Affine parameters: $b_0 = (\kappa_r\theta_r, \kappa_\ell\theta_\ell)^\top$, $B = \begin{pmatrix} -\kappa_r & \beta \\ 0 & -\kappa_\ell \end{pmatrix}$, $a_0 = \operatorname{diag}(\sigma_r^2, \sigma_\ell^2)$, $\alpha_1 = \alpha_2 = 0$.

The Riccati system is linear: $\psi'(\tau) = B^\top\psi(\tau)$, which gives $\psi(\tau) = e^{B^\top\tau}\,u$. Both components can go negative, making this suitable for nominal rates in a low-rate environment but problematic as a model for variance.

### Heston Model: $A_1(2)$

State: $X_t = (V_t, \log S_t)^\top$ with $V_t \in \mathbb{R}_+$ (variance) and $\log S_t \in \mathbb{R}$ (log-price).

$$
dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^{(1)}
$$

$$
d\log S_t = \left(r - \tfrac{1}{2}V_t\right)dt + \sqrt{V_t}\left(\rho\,dW_t^{(1)} + \sqrt{1-\rho^2}\,dW_t^{(2)}\right)
$$

Affine parameters:

- $b_0 = (\kappa\theta, r)^\top$, $B = \begin{pmatrix} -\kappa & 0 \\ -1/2 & 0 \end{pmatrix}$
- $a_0 = 0$, $\alpha_1 = \begin{pmatrix} \xi^2 & \rho\xi \\ \rho\xi & 1 \end{pmatrix}$, $\alpha_2 = 0$

The variance $V_t$ drives the diffusion of both itself and the log-price, placing the Heston model in $A_1(2)$: one CIR-type factor ($V_t$) among two total.

!!! example "Heston Riccati System"
    Writing $\psi = (\psi_1, \psi_2)^\top$, the Riccati equations become:

    $$
    \psi_1' = -\kappa\psi_1 - \tfrac{1}{2}\psi_2 + \tfrac{1}{2}(\xi^2\psi_1^2 + 2\rho\xi\psi_1\psi_2 + \psi_2^2)
    $$

    $$
    \psi_2' = 0
    $$

    The second equation gives $\psi_2(\tau) = u_2$ (constant), reducing the system to a scalar Riccati equation for $\psi_1$ with coefficients depending on $u_2$. This is why the Heston characteristic function has a semi-closed form.

### Three-Factor Interest Rate Model: $A_1(3)$

State: $X_t = (V_t, r_t, \ell_t)^\top$ with $V_t \in \mathbb{R}_+$ (volatility), $r_t \in \mathbb{R}$ (short rate), $\ell_t \in \mathbb{R}$ (long rate).

This specification allows stochastic volatility of yields (through $V_t$) together with independent level and slope factors ($r_t$ and $\ell_t$). The Riccati system is three-dimensional with one nonlinear component (from $V_t$) and two linear components, typically requiring numerical integration.

---

## Bond Pricing in the Vector Case

For the affine short rate $r_t = \rho_0 + \rho_1^\top X_t$, the zero-coupon bond price is

$$
P(t,T) = \exp\!\bigl(A(\tau) + B(\tau)^\top X_t\bigr)
$$

where $A$ and $B$ satisfy the **extended Riccati system**:

$$
\frac{dB_i}{d\tau} = R_i(B) - (\rho_1)_i, \qquad \frac{dA}{d\tau} = F(B) - \rho_0
$$

with $A(0) = 0$ and $B(0) = \mathbf{0}$. The additional terms $-\rho_1$ and $-\rho_0$ account for the discounting by the short rate. The [exponential-affine bond price formula](../affine_term_structure/exponential_affine_bond_price.md) page treats this in detail for the scalar case; the vector extension is a direct generalization.

---

## Summary

The vector affine process on $D = \mathbb{R}_+^m \times \mathbb{R}^{d-m}$ extends the scalar theory to multiple interacting factors with affine drift $\mu(x) = b_0 + Bx$, affine diffusion $a(x) = a_0 + \sum_i \alpha_i x^{(i)}$, and affine jump compensator $m(x,dz) = m_0(dz) + \sum_i x^{(i)} m_i(dz)$. The conditional characteristic function remains exponential-affine, governed by a $d$-dimensional Riccati system that couples through the matrices $B$ and $\alpha_i$. For Gaussian models ($m = 0$), the Riccati system is linear; for models with CIR-type components ($m > 0$), the quadratic terms introduce nonlinear coupling. The Heston model illustrates the $A_1(2)$ case where a single variance factor drives the diffusion of the entire system, producing a semi-closed-form characteristic function through a scalar Riccati equation.

---

## Further Reading

- Duffie, D., Filipovic, D., and Schachermayer, W. (2003). "Affine Processes and Applications in Finance." *Annals of Applied Probability*, 13(3), 984--1053.
- Duffie, D., Pan, J., and Singleton, K. (2000). "Transform Analysis and Asset Pricing for Affine Jump-Diffusions." *Econometrica*, 68(6), 1343--1376.
- Filipovic, D. (2009). *Term-Structure Models: A Graduate Course*. Springer.

---

## Exercises

**Exercise 1.** For a $d = 3$ dimensional affine process on $D = \mathbb{R}_+^2 \times \mathbb{R}$ with state vector $X_t = (V_t^{(1)}, V_t^{(2)}, r_t)^T$, write down the most general affine drift $b(x) = b_0 + Bx$ specifying the dimensions of $b_0 \in \mathbb{R}^3$ and $B \in \mathbb{R}^{3 \times 3}$. Which entries of $b_0$ must be non-negative for admissibility?

??? success "Solution to Exercise 1"
    The state vector is $X_t = (V_t^{(1)}, V_t^{(2)}, r_t)^\top \in D = \mathbb{R}_+^2 \times \mathbb{R}$, so $m = 2$ and $d = 3$.

    The most general affine drift is $\mu(x) = b_0 + Bx$ where $b_0 \in \mathbb{R}^3$ and $B \in \mathbb{R}^{3 \times 3}$:

    $$
    b_0 = \begin{pmatrix} b_0^{(1)} \\ b_0^{(2)} \\ b_0^{(3)} \end{pmatrix}, \qquad B = \begin{pmatrix} B_{11} & B_{12} & B_{13} \\ B_{21} & B_{22} & B_{23} \\ B_{31} & B_{32} & B_{33} \end{pmatrix}
    $$

    The affine drift for each component is therefore:

    $$
    \mu_i(x) = b_0^{(i)} + B_{i1} V^{(1)} + B_{i2} V^{(2)} + B_{i3} r
    $$

    For admissibility, the constant drift entries of the CIR-type components must be non-negative by condition (B1):

    $$
    b_0^{(1)} \geq 0, \qquad b_0^{(2)} \geq 0
    $$

    The third entry $b_0^{(3)}$ is unrestricted because $r_t \in \mathbb{R}$ is the Gaussian component. Additionally, by condition (B2), the cross-effects among CIR components must be non-negative: $B_{12} \geq 0$ and $B_{21} \geq 0$.

---

**Exercise 2.** For the Heston model as a two-dimensional affine process with $X_t = (\log S_t, V_t) \in \mathbb{R} \times \mathbb{R}_+$, write out the drift vector $b(x) = b_0 + Bx$ and diffusion matrix $a(x) = a_0 + \alpha_1 x_1 + \alpha_2 x_2$ explicitly, accounting for the correlation $\rho$ between the two Brownian motions.

??? success "Solution to Exercise 2"
    In the Heston model, the state is $X_t = (\log S_t, V_t)^\top \in \mathbb{R} \times \mathbb{R}_+$, which corresponds to $m = 1$ (with $V_t$ as the single CIR-type component indexed second) rewritten in the $A_1(2)$ classification.

    **Drift vector:**

    $$
    b_0 = \begin{pmatrix} r \\ \kappa\theta \end{pmatrix}, \qquad B = \begin{pmatrix} 0 & -\tfrac{1}{2} \\ 0 & -\kappa \end{pmatrix}
    $$

    so the drift is

    $$
    \mu(x) = \begin{pmatrix} r - \tfrac{1}{2}x_2 \\ \kappa\theta - \kappa x_2 \end{pmatrix}
    $$

    **Diffusion matrix.** With $x_1 = \log S$ and $x_2 = V$, the log-price is the Gaussian component and the variance is the CIR-type component. The instantaneous covariance is:

    $$
    a(x) = a_0 + \alpha_1 x_1 + \alpha_2 x_2
    $$

    Since the Gaussian component contributes no state-dependent diffusion (condition A3), $\alpha_1 = 0$. The constant diffusion also vanishes for the CIR component: $(a_0)_{22} = 0$. For the full structure:

    $$
    a_0 = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}, \qquad \alpha_1 = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}, \qquad \alpha_2 = \begin{pmatrix} 1 & \rho\xi \\ \rho\xi & \xi^2 \end{pmatrix}
    $$

    The full covariance is $a(x) = \alpha_2 V_t$, encoding the correlation $\rho$ between $d\log S_t$ and $dV_t$ through the off-diagonal entry $\rho\xi$.

---

**Exercise 3.** The vector Riccati system for a $d$-dimensional model has the form $\psi_j'(\tau) = R_j(\psi(\tau))$ for $j = 1, \ldots, d$. Explain why this system is generally coupled (the equation for $\psi_j$ depends on all components of $\psi$) and identify under what structural conditions on the diffusion matrices $\alpha_i$ the system decouples into independent scalar equations.

??? success "Solution to Exercise 3"
    The Riccati equation for the $j$-th component is

    $$
    \psi_j'(\tau) = (B^\top \psi)_j + \tfrac{1}{2}\psi^\top \alpha_j \psi + \text{jump terms}
    $$

    **Why the system is coupled.** The linear term $(B^\top \psi)_j = \sum_k B_{kj}\psi_k$ involves all components of $\psi$ whenever the drift matrix $B$ has nonzero off-diagonal entries. The quadratic term $\tfrac{1}{2}\psi^\top \alpha_j \psi = \tfrac{1}{2}\sum_{k,l}(\alpha_j)_{kl}\psi_k\psi_l$ involves all pairs $(\psi_k, \psi_l)$ for which $(\alpha_j)_{kl} \neq 0$. Therefore, the equation for $\psi_j$ depends on all components of $\psi$ through both the drift coupling (via $B$) and the diffusion coupling (via $\alpha_j$).

    **Conditions for decoupling.** The system decouples into independent scalar equations if:

    1. The drift matrix $B$ is diagonal (i.e., $B_{kj} = 0$ for $k \neq j$), so the linear term reduces to $B_{jj}\psi_j$
    2. Each diffusion matrix $\alpha_j$ is diagonal (i.e., $(\alpha_j)_{kl} = 0$ for $k \neq l$), so the quadratic term reduces to $\tfrac{1}{2}(\alpha_j)_{jj}\psi_j^2$
    3. The jump measures $m_j$ depend only on the $j$-th component of $z$

    Under these conditions, each $\psi_j$ satisfies an independent scalar Riccati equation that depends only on $\psi_j$ itself. Financially, this corresponds to a model with no cross-effects in the drift, no correlated diffusion between components, and independent jump structures.

---

**Exercise 4.** For a two-factor model with one CIR and one Gaussian component, and no cross-diffusion, verify that the Riccati system decouples: $\psi_1$ satisfies a linear ODE and $\psi_2$ satisfies a scalar Riccati equation. Solve both explicitly.

??? success "Solution to Exercise 4"
    Consider a two-factor model on $D = \mathbb{R}_+ \times \mathbb{R}$ with state $X_t = (V_t, Y_t)^\top$, where $V_t$ is CIR-type and $Y_t$ is Gaussian, and no cross-diffusion. The SDE system is:

    $$
    dV_t = (b_0^{(1)} + B_{11}V_t)\,dt + \sqrt{\alpha_{11}V_t}\,dW_t^{(1)}
    $$

    $$
    dY_t = (b_0^{(2)} + B_{22}Y_t)\,dt + \sigma_2\,dW_t^{(2)}
    $$

    The diffusion matrices are $a_0 = \operatorname{diag}(0, \sigma_2^2)$, $\alpha_1 = \operatorname{diag}(\alpha_{11}, 0)$, and $\alpha_2 = 0$. With no cross-diffusion, $B$ is diagonal: $B = \operatorname{diag}(B_{11}, B_{22})$.

    The Riccati system with $\psi = (\psi_1, \psi_2)^\top$ and initial condition $\psi(0) = (u_1, u_2)^\top$:

    **For $\psi_2$ (Gaussian component):** Since $\alpha_2 = 0$ (Gaussian components contribute no state-dependent diffusion) and $B$ is diagonal:

    $$
    \psi_2'(\tau) = B_{22}\psi_2 + \tfrac{1}{2}\cdot 0 = B_{22}\psi_2
    $$

    This is a linear ODE with solution

    $$
    \psi_2(\tau) = u_2\,e^{B_{22}\tau}
    $$

    **For $\psi_1$ (CIR component):** Since $B$ is diagonal and $\alpha_1 = \operatorname{diag}(\alpha_{11}, 0)$:

    $$
    \psi_1'(\tau) = B_{11}\psi_1 + \tfrac{1}{2}\alpha_{11}\psi_1^2
    $$

    This is a scalar Riccati equation. With $\psi_1(0) = u_1$, it can be solved by substitution $\psi_1 = -\frac{2}{\alpha_{11}}\frac{g'}{g}$, yielding the standard result. Setting $\gamma = \sqrt{B_{11}^2 - 2\alpha_{11}\cdot 0} = |B_{11}|$ (no additional constant here since it is a pure Riccati), the solution is:

    $$
    \psi_1(\tau) = \frac{u_1 B_{11}}{B_{11} + \tfrac{1}{2}\alpha_{11} u_1(1 - e^{B_{11}\tau})} \cdot e^{B_{11}\tau}
    $$

    which can be verified by direct substitution. The two equations are fully decoupled: $\psi_2$ is solved independently, and $\psi_1$ does not depend on $\psi_2$.

---

**Exercise 5.** Consider extending the Heston model to three factors by adding a second variance process: $dV_t^{(2)} = \kappa_2(\theta_2 - V_t^{(2)})\,dt + \xi_2\sqrt{V_t^{(2)}}\,dW_t^{(3)}$, with the total variance being $V_t^{(1)} + V_t^{(2)}$. Write the state space, identify $m$ and $d$, and describe how the Riccati system changes compared to the standard Heston model.

??? success "Solution to Exercise 5"
    The extended Heston model has state $X_t = (V_t^{(1)}, V_t^{(2)}, \log S_t)^\top$ with $V_t^{(1)}, V_t^{(2)} \in \mathbb{R}_+$ and $\log S_t \in \mathbb{R}$. Thus $d = 3$ and $m = 2$, placing it in the $A_2(3)$ class.

    The state space is $D = \mathbb{R}_+^2 \times \mathbb{R}$.

    The SDE system is:

    $$
    dV_t^{(1)} = \kappa_1(\theta_1 - V_t^{(1)})\,dt + \xi_1\sqrt{V_t^{(1)}}\,dW_t^{(1)}
    $$

    $$
    dV_t^{(2)} = \kappa_2(\theta_2 - V_t^{(2)})\,dt + \xi_2\sqrt{V_t^{(2)}}\,dW_t^{(3)}
    $$

    $$
    d\log S_t = \bigl(r - \tfrac{1}{2}(V_t^{(1)} + V_t^{(2)})\bigr)\,dt + \sqrt{V_t^{(1)}}\bigl(\rho_1\,dW_t^{(1)} + \sqrt{1-\rho_1^2}\,dW_t^{(2)}\bigr) + \sqrt{V_t^{(2)}}\bigl(\rho_2\,dW_t^{(3)} + \sqrt{1-\rho_2^2}\,dW_t^{(4)}\bigr)
    $$

    **Changes to the Riccati system compared to standard Heston:**

    - The Riccati system is now three-dimensional: $\psi = (\psi_1, \psi_2, \psi_3)^\top$
    - If $W^{(1)}, W^{(3)}$ are independent (the two variance processes are uncorrelated), the Riccati equations for $\psi_1$ and $\psi_2$ each couple only with $\psi_3$ (the log-price component), not with each other
    - $\psi_3'(\tau) = 0$, so $\psi_3(\tau) = u_3$ (constant), just as in the standard Heston model
    - The equations for $\psi_1$ and $\psi_2$ each reduce to a scalar Riccati equation driven by $u_3$, with the same structure as the standard Heston but with different parameters $(\kappa_1, \xi_1, \rho_1)$ and $(\kappa_2, \xi_2, \rho_2)$ respectively
    - The scalar function $\phi(\tau)$ accumulates contributions from both variance factors

    The key difference is that two independent scalar Riccati equations replace the single one in standard Heston, allowing more flexible term structures of implied volatility while retaining semi-closed-form solutions.

---

**Exercise 6.** For a $d$-dimensional affine process, the computational cost of solving the Riccati system numerically is $O(d^2)$ per time step per frequency point. Compare this to the cost of solving the backward Kolmogorov PDE on a grid with $N$ points per dimension, which is $O(N^d)$. For $d = 3$ and $N = 100$, compute both costs and explain why the Riccati approach is vastly superior for multi-factor models.

??? success "Solution to Exercise 6"
    **Riccati approach:** For $d = 3$, the cost per time step per frequency point is

    $$
    O(d^2) = O(9)
    $$

    If we use $M$ time steps and $K$ frequency points for Fourier inversion, the total cost is $O(9MK)$, which is linear in $M$ and $K$.

    **PDE approach:** For $d = 3$ and $N = 100$ grid points per dimension, the total number of grid points is

    $$
    N^d = 100^3 = 10^6
    $$

    Each time step requires updating all grid points (with implicit or explicit finite difference methods), so the cost per time step is $O(N^d) = O(10^6)$.

    **Comparison:** The ratio of costs per time step is approximately

    $$
    \frac{N^d}{d^2} = \frac{10^6}{9} \approx 1.1 \times 10^5
    $$

    The Riccati approach is roughly $10^5$ times cheaper per time step. Moreover, the PDE approach suffers from the **curse of dimensionality**: increasing $d$ from 3 to 4 with $N = 100$ raises the grid cost to $10^8$, while the Riccati cost increases only to $O(16)$. For $d = 5$, the PDE grid has $10^{10}$ points (computationally infeasible), while the Riccati cost is merely $O(25)$.

    This explains why the Riccati/transform approach is the method of choice for multi-factor affine models: it replaces an exponentially expensive PDE solve with a polynomial-cost ODE system, making models with $d = 5$ or more factors practically solvable.
