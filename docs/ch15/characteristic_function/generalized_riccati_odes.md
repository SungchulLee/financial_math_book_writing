# Generalized Riccati ODEs

The generalized Riccati ODE system is the computational heart of the affine framework. Every pricing formula, every bond price, and every characteristic function evaluation in an affine model reduces to solving this system. This section derives the Riccati equations from the backward Kolmogorov equation, states the general multidimensional system, and explains the roles of the functions $F$ and $R$ that govern the dynamics.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the generalized Riccati ODEs from the backward Kolmogorov equation
    2. State the full multidimensional Riccati system with initial conditions
    3. Identify $F$ and $R$ from the model parameters
    4. Distinguish the linear $\phi$-equation from the nonlinear $\psi$-equation
    5. Write the Riccati system for specific affine models

---

## Intuition

The exponential-affine ansatz $g(\tau, x) = \exp(\phi(\tau) + \langle \psi(\tau), x \rangle)$ transforms the PDE for the conditional expectation into a system of ODEs. The mechanism is straightforward: differentiating the exponential with respect to $x$ produces powers of $\psi$, and the affine structure of the drift and diffusion ensures that after substitution and cancellation, all terms organize themselves by powers of $x$. Since the equation must hold for all $x$ in the state space, matching the constant terms gives the $\phi$-equation and matching the linear terms gives the $\psi$-equation. The $\psi$-equation is autonomous (it does not involve $\phi$), so it can be solved first. Then $\phi$ is obtained by a single integration---making the $\phi$-equation effectively linear once $\psi$ is known.

---

## Derivation for the Scalar Case

### Setup

Consider a scalar affine diffusion:

$$
dX_t = (\kappa_0 + \kappa_1 X_t)\,dt + \sqrt{\sigma_0 + \sigma_1 X_t}\,dW_t
$$

The conditional expectation $g(\tau, x) = \mathbb{E}[e^{u X_{t+\tau}} \mid X_t = x]$ satisfies the backward Kolmogorov PDE:

$$
\frac{\partial g}{\partial \tau} = (\kappa_0 + \kappa_1 x)\frac{\partial g}{\partial x} + \frac{1}{2}(\sigma_0 + \sigma_1 x)\frac{\partial^2 g}{\partial x^2}
$$

with initial condition $g(0, x) = e^{ux}$.

### The Affine Ansatz

Substitute $g(\tau, x) = \exp(\phi(\tau) + \psi(\tau)x)$ with $\phi(0) = 0$, $\psi(0) = u$:

$$
\frac{\partial g}{\partial \tau} = (\phi' + \psi' x)\,g, \qquad \frac{\partial g}{\partial x} = \psi\,g, \qquad \frac{\partial^2 g}{\partial x^2} = \psi^2\,g
$$

Substituting into the PDE and dividing by $g > 0$:

$$
\phi' + \psi' x = (\kappa_0 + \kappa_1 x)\psi + \frac{1}{2}(\sigma_0 + \sigma_1 x)\psi^2
$$

### Separation by Powers of x

Rearranging the right-hand side:

$$
\phi' + \psi' x = \underbrace{\left(\kappa_0\psi + \frac{1}{2}\sigma_0\psi^2\right)}_{\text{constant in } x} + \underbrace{\left(\kappa_1\psi + \frac{1}{2}\sigma_1\psi^2\right)}_{\text{coefficient of } x} \cdot x
$$

Matching:

**Constant terms:**

$$
\phi'(\tau) = \kappa_0\psi(\tau) + \frac{1}{2}\sigma_0\psi(\tau)^2 =: F(\psi(\tau))
$$

**Linear terms:**

$$
\psi'(\tau) = \kappa_1\psi(\tau) + \frac{1}{2}\sigma_1\psi(\tau)^2 =: R(\psi(\tau))
$$

with initial conditions $\phi(0) = 0$ and $\psi(0) = u$.

!!! note "Why Separation Works"
    The separation into constant and linear terms succeeds because the drift $\kappa_0 + \kappa_1 x$ and the diffusion $\sigma_0 + \sigma_1 x$ are both affine in $x$. If the diffusion were $\sigma(x) = \sigma_0 + \sigma_1 x + \sigma_2 x^2$, the substitution would produce a term $\sigma_2 x^2 \psi^2$ that cannot be absorbed into the $\phi$- or $\psi$-equations, and the ansatz would fail.

---

## The General Multidimensional System

### Statement

For a $d$-dimensional affine process on $D = \mathbb{R}^m_+ \times \mathbb{R}^{d-m}$ with drift $b(x) = b_0 + \sum_{j=1}^d b_j x_j$, diffusion $a(x) = a_0 + \sum_{j=1}^d a_j x_j$, and jump compensator $m(x, dz) = m_0(dz) + \sum_{j=1}^d x_j\,m_j(dz)$, the functions $\phi$ and $\psi$ satisfy:

$$
\frac{\partial \phi}{\partial \tau}(\tau, u) = F(\psi(\tau, u)), \qquad \phi(0, u) = 0
$$

$$
\frac{\partial \psi_j}{\partial \tau}(\tau, u) = R_j(\psi(\tau, u)), \qquad \psi_j(0, u) = u_j, \quad j = 1, \ldots, d
$$

where the functions $F : \mathbb{C}^d \to \mathbb{C}$ and $R : \mathbb{C}^d \to \mathbb{C}^d$ are defined by:

$$
F(w) = \langle b_0, w \rangle + \frac{1}{2}\langle w, a_0 w \rangle + \int_{D \setminus \{0\}} \left(e^{\langle w, z \rangle} - 1\right) m_0(dz)
$$

$$
R_j(w) = \langle b_j, w \rangle + \frac{1}{2}\langle w, a_j w \rangle + \int_{D \setminus \{0\}} \left(e^{\langle w, z \rangle} - 1\right) m_j(dz)
$$

for $j = 1, \ldots, d$.

### Structure of $F$ and $R$

Each function $F$ and $R_j$ has three terms corresponding to the three sources of randomness:

| Term | $F$ (state-independent) | $R_j$ (state-dependent) |
|------|------------------------|------------------------|
| Drift | $\langle b_0, w \rangle$ | $\langle b_j, w \rangle$ |
| Diffusion | $\frac{1}{2}\langle w, a_0 w \rangle$ | $\frac{1}{2}\langle w, a_j w \rangle$ |
| Jumps | $\int(e^{\langle w, z \rangle} - 1)m_0(dz)$ | $\int(e^{\langle w, z \rangle} - 1)m_j(dz)$ |

The drift term is linear in $w$. The diffusion term is quadratic in $w$---this is what makes $R_j$ a *Riccati* equation (quadratic ODE). The jump term is generally nonlinear but well-defined on the admissible domain.

### The Hierarchical Structure

A crucial observation is that the $\psi$-system is **autonomous**: the equations $\psi' = R(\psi)$ form a closed system that does not involve $\phi$. Once $\psi(\tau, u)$ is determined, the $\phi$-equation $\phi' = F(\psi(\tau, u))$ is a simple quadrature:

$$
\phi(\tau, u) = \int_0^\tau F(\psi(s, u))\,ds
$$

This hierarchical structure is computationally advantageous: the hard work is solving the $\psi$-system, which is a $d$-dimensional Riccati equation, and the $\phi$-equation is then a one-dimensional integration.

---

## Classification of the Riccati Equation

The character of the $\psi_j$-equation depends on whether the $j$-th component has state-dependent diffusion or jumps.

### Case 1: Gaussian Component ($a_j = 0$, $m_j = 0$)

When neither the diffusion nor the jump intensity depends on $x_j$, the $R_j$ function is linear in $w$:

$$
R_j(w) = \langle b_j, w \rangle
$$

The ODE $\psi_j' = \langle b_j, \psi \rangle$ is linear and can be solved by matrix exponentials in the multidimensional case.

### Case 2: CIR-Type Component ($a_j \neq 0$, $m_j = 0$)

When the diffusion depends on $x_j$ but there are no state-dependent jumps:

$$
R_j(w) = \langle b_j, w \rangle + \frac{1}{2}\langle w, a_j w \rangle
$$

The quadratic term makes this a genuine **Riccati equation**. For the scalar CIR process ($d = 1$), this becomes $\psi' = \kappa_1 \psi + \frac{1}{2}\sigma_1 \psi^2$, which has a well-known closed-form solution.

### Case 3: Jump-Diffusion Component ($m_j \neq 0$)

When state-dependent jumps are present, $R_j$ includes the nonlinear integral term:

$$
R_j(w) = \langle b_j, w \rangle + \frac{1}{2}\langle w, a_j w \rangle + \int_{D \setminus \{0\}} (e^{\langle w, z \rangle} - 1)\,m_j(dz)
$$

For exponentially distributed jumps ($m_j(dz) = \lambda \eta e^{-\eta z}\,dz$), the integral evaluates to $\lambda(\eta/(\eta - w) - 1)$, producing a rational function of $w$.

---

## Initial Conditions and Admissibility

### Initial Conditions

The initial conditions are determined by the definition of the log-affine property:

$$
\phi(0, u) = 0, \qquad \psi(0, u) = u
$$

At $\tau = 0$: $\exp(\phi(0, u) + \langle \psi(0, u), x \rangle) = \exp(\langle u, x \rangle) = e^{\langle u, x \rangle}$, matching $\mathbb{E}[e^{\langle u, X_t \rangle} \mid X_t = x]$.

### Admissibility of the Initial Value

Not every $u \in \mathbb{C}^d$ produces a well-defined solution. The admissible set is:

$$
\mathcal{U} = \{u \in \mathbb{C}^d : \text{the Riccati system has a solution on } [0, \infty) \text{ and } \mathbb{E}[|e^{\langle u, X_t \rangle}|] < \infty\}
$$

For the characteristic function, $u = iv$ with $v \in \mathbb{R}^d$ is always admissible (the expectation is bounded by 1). For the moment generating function with real $u$, admissibility depends on the model: CIR-type components may exhibit finite-time explosion for large $u$.

---

## The Duffie-Pan-Singleton Formulation

In the notation of Duffie, Pan, and Singleton (2000), the affine state vector $\mathbf{X}_t$ has dynamics under $\mathbb{Q}$:

$$
d\mathbf{X}_t = (a_0 + a_1 \mathbf{X}_t)\,dt + \bar{\sigma}(\mathbf{X}_t)\,d\mathbf{W}_t
$$

with short rate $r(\mathbf{X}_t) = r_0 + r_1^\top \mathbf{X}_t$. The discounted characteristic function $\varphi(\mathbf{X}_t, t, T, \mathbf{u}) = \mathbb{E}^\mathbb{Q}[e^{-\int_t^T r_s\,ds + i\mathbf{u}^\top \mathbf{X}_T} \mid \mathcal{F}_t]$ satisfies $\varphi = e^{A(\tau, \mathbf{u}) + \mathbf{B}(\tau, \mathbf{u})^\top \mathbf{X}_t}$ where:

$$
\frac{dA}{d\tau} = -r_0 + \mathbf{B}^\top a_0 + \frac{1}{2}\mathbf{B}^\top c_0 \mathbf{B}
$$

$$
\frac{d\mathbf{B}}{d\tau} = -r_1 + a_1^\top \mathbf{B} + \frac{1}{2}c_1^\top \mathbf{B} \odot \mathbf{B}
$$

with $A(0) = 0$ and $\mathbf{B}(0) = i\mathbf{u}$. Here $c_0$ and $c_1$ encode the diffusion structure: $\bar{\sigma}\bar{\sigma}^\top = c_0 + c_1^\top \mathbf{X}_t$.

??? example "Riccati System for a Two-Factor Model"
    Consider $X_t = (r_t, V_t) \in \mathbb{R} \times \mathbb{R}_+$ with:

    $$
    dr_t = \kappa_r(\theta_r - r_t)\,dt + \sigma_r\,dW_t^{(1)}
    $$

    $$
    dV_t = \kappa_V(\theta_V - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^{(2)}
    $$

    The parameters are $b_0 = (\kappa_r\theta_r, \kappa_V\theta_V)^\top$, $b_1 = \text{diag}(-\kappa_r, 0)$, $b_2 = \text{diag}(0, -\kappa_V)$, $a_0 = \text{diag}(\sigma_r^2, 0)$, $a_1 = 0$, $a_2 = \text{diag}(0, \xi^2)$.

    The $\psi$-system is:

    $$
    \psi_1'(\tau) = -\kappa_r \psi_1(\tau), \qquad \psi_1(0) = u_1
    $$

    $$
    \psi_2'(\tau) = -\kappa_V \psi_2(\tau) + \frac{\xi^2}{2}\psi_2(\tau)^2, \qquad \psi_2(0) = u_2
    $$

    The first equation is linear (Gaussian component), the second is Riccati (CIR component). They decouple completely because there is no correlation between the two factors in the diffusion matrix. $\square$

---

## Summary

The generalized Riccati ODE system $\phi' = F(\psi)$, $\psi' = R(\psi)$ arises from substituting the exponential-affine ansatz into the backward Kolmogorov equation and separating by powers of the state variable $x$. The $\psi$-equation is autonomous and potentially nonlinear (quadratic for diffusion-driven components, rational for jump-diffusion components), while the $\phi$-equation is a simple integration once $\psi$ is known. The functions $F$ and $R$ are determined by the drift, diffusion, and jump parameters of the affine process. For Gaussian components, the system is linear; for CIR-type components, it is a genuine Riccati equation; and for jump-diffusion components, additional nonlinear terms arise from the Levy measure.

---

## Further Reading

- Duffie, D., Pan, J., & Singleton, K. (2000). "Transform Analysis and Asset Pricing for Affine Jump-Diffusions." *Econometrica*, 68(6), 1343-1376.
- Filipovic, D. *Term-Structure Models: A Graduate Course*. Springer, 2009, Chapter 10.
- Duffie, D., Filipovic, D., & Schachermayer, W. (2003). "Affine Processes and Applications in Finance." *Annals of Applied Probability*, 13(3), 984-1053.

---

## Exercises

**Exercise 1.** For a scalar affine diffusion with $\kappa_0 = 0.05$, $\kappa_1 = -0.5$, $\sigma_0 = 0$, and $\sigma_1 = 0.04$, write down the functions $F(w)$ and $R(w)$ explicitly. Classify the $\psi$-equation: is it linear, Riccati, or of jump-diffusion type? What financial model does this specification correspond to?

---

**Exercise 2.** Starting from the PDE for $g(\tau, x) = \mathbb{E}[e^{uX_{t+\tau}} \mid X_t = x]$ with a diffusion of the form $\sigma(x) = \sigma_0 + \sigma_1 x + \sigma_2 x^2$, attempt the exponential-affine ansatz and show that matching powers of $x$ produces three equations (for $x^0$, $x^1$, and $x^2$) but only two unknowns ($\phi'$ and $\psi'$), leading to an overdetermined system. What does this prove about the necessity of the affine structure?

---

**Exercise 3.** For the two-factor model in the worked example (Vasicek $r_t$ and CIR $V_t$, independent), solve the decoupled Riccati system explicitly. That is, write $\psi_1(\tau)$ in closed form (linear ODE) and $\psi_2(\tau)$ in closed form (scalar Riccati), then integrate $\phi(\tau) = \int_0^\tau F(\psi(s))\,ds$.

---

**Exercise 4.** Explain the hierarchical structure of the Riccati system: why is it that $\psi' = R(\psi)$ does not depend on $\phi$, but $\phi' = F(\psi)$ does depend on $\psi$? Relate this to the separation of the backward Kolmogorov PDE by powers of $x$.

---

**Exercise 5.** Consider a one-dimensional affine jump-diffusion on $\mathbb{R}_+$ with drift $\kappa_1 = -\kappa$, diffusion $\sigma_1 = \xi^2$, and exponentially distributed jumps with Levy measure $m_1(dz) = \lambda\eta e^{-\eta z}\,dz$. Show that

$$
R(w) = -\kappa w + \frac{\xi^2}{2}w^2 + \lambda\left(\frac{\eta}{\eta - w} - 1\right)
$$

and identify the domain of $w$ for which $R(w)$ is well-defined. What happens at $w = \eta$?

---

**Exercise 6.** In the Duffie-Pan-Singleton formulation, the discounted characteristic function satisfies $\frac{dB}{d\tau} = -r_1 + a_1^T B + \frac{1}{2}c_1^T B \odot B$. For a one-factor CIR model with $r_1 = 1$, $a_1 = -\kappa$, $c_1 = \xi^2$, write this as a scalar Riccati equation for $B(\tau)$ and verify that the initial condition $B(0) = iv$ is correct for the characteristic function and $B(0) = 0$ is correct for bond pricing.
