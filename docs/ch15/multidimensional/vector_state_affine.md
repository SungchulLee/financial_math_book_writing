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
