# Admissibility Conditions

An affine process on the state space $D = \mathbb{R}_+^m \times \mathbb{R}^{d-m}$ must satisfy algebraic constraints on its drift, diffusion, and jump parameters to ensure that the process never leaves $D$. These **admissibility conditions**, formalized by Duffie, Filipovic, and Schachermayer (2003), are the necessary and sufficient constraints that any well-defined affine process must satisfy. Without admissibility, the CIR-type components could become negative, the diffusion matrix could lose positive semi-definiteness, or the process could explode in finite time. This section states the full set of admissibility conditions, explains their geometric interpretation, proves necessity for the key conditions, and verifies admissibility for standard models.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State the Duffie-Filipovic-Schachermayer admissibility conditions for affine processes on $\mathbb{R}_+^m \times \mathbb{R}^{d-m}$
    2. Explain the geometric meaning of each condition in terms of boundary behavior and state space invariance
    3. Verify admissibility for the CIR, Heston, and multi-factor affine models
    4. Distinguish necessary conditions from sufficient conditions and understand their interplay
    5. Identify common parameter specifications that violate admissibility

---

## Motivation

### The State Space Invariance Problem

Consider a two-dimensional affine process $(V_t, r_t)$ where $V_t \geq 0$ represents variance and $r_t \in \mathbb{R}$ represents the short rate. The process lives on $D = \mathbb{R}_+ \times \mathbb{R}$. What prevents $V_t$ from becoming negative?

For the CIR-type component $dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t$, the square-root diffusion vanishes at $V_t = 0$, eliminating the noise that could push $V_t$ below zero. The drift $\kappa\theta > 0$ at $V_t = 0$ pushes the process back into the interior. Together, these conditions --- **vanishing diffusion** and **inward-pointing drift** at the boundary --- form the core of admissibility.

In higher dimensions, the conditions become more intricate because the drift and diffusion of one component can depend on other state variables. The admissibility conditions systematize these constraints for the full $d$-dimensional affine family.

---

## Setup and Notation

### The Parameter Set

An affine process on $D = \mathbb{R}_+^m \times \mathbb{R}^{d-m}$ is characterized by the parameter tuple $(b_0, B, a_0, \alpha_1, \ldots, \alpha_d, m_0, m_1, \ldots, m_d)$ where:

- $(b_0, B)$ define the affine drift $\mu(x) = b_0 + Bx$
- $(a_0, \alpha_1, \ldots, \alpha_d)$ define the affine diffusion $a(x) = a_0 + \sum_{i=1}^d \alpha_i x^{(i)}$
- $(m_0, m_1, \ldots, m_d)$ define the affine jump compensator $m(x, dz) = m_0(dz) + \sum_{i=1}^d x^{(i)} m_i(dz)$

We partition the indices into $I = \{1, \ldots, m\}$ (CIR-type, non-negative) and $J = \{m+1, \ldots, d\}$ (Gaussian, unrestricted).

### Boundary of the State Space

The boundary of $D$ consists of points where at least one CIR-type component is zero:

$$
\partial D = \{x \in D : x^{(i)} = 0 \text{ for some } i \in I\}
$$

The $k$-th face of the boundary is $\partial_k D = \{x \in D : x^{(k)} = 0\}$ for $k \in I$.

---

## The Admissibility Conditions

### Statement of the Main Result

!!! info "Theorem: Duffie-Filipovic-Schachermayer Admissibility"
    An affine process on $D = \mathbb{R}_+^m \times \mathbb{R}^{d-m}$ with parameters $(b_0, B, a_0, \alpha_1, \ldots, \alpha_d, m_0, m_1, \ldots, m_d)$ is well-defined if and only if the following conditions hold:

    **A. Diffusion conditions:**

    (A1) $a_0$ is symmetric positive semi-definite

    (A2) For each $i \in I$: $\alpha_i$ is symmetric positive semi-definite

    (A3) For each $j \in J$: $\alpha_j = 0$ (Gaussian components do not contribute to state-dependent diffusion)

    (A4) For each $i \in I$ and $k \in I$ with $k \neq i$: $(\alpha_i)_{kk} = 0$ (the diffusion of a CIR component depends only on its own level, not on other CIR components)

    (A5) For each $i \in I$: $(a_0)_{ii} = 0$ (the constant part of the diffusion vanishes for CIR components)

    **B. Drift conditions:**

    (B1) For each $i \in I$: $(b_0)_i \geq 0$ (the constant drift of CIR components is non-negative)

    (B2) For each $i \in I$ and $k \in I$ with $k \neq i$: $B_{ik} \geq 0$ (cross-effects among CIR components are non-negative)

    **C. Jump conditions:**

    (C1) $m_0$ is supported on $D$ (state-independent jumps land in the state space)

    (C2) For each $i \in I$: $m_i$ is supported on $\{z \in \mathbb{R}^d : z^{(k)} \geq 0 \text{ for all } k \in I \setminus \{i\}\}$ (state-dependent jumps from the $i$-th component do not cause other CIR components to become negative)

    (C3) For each $i \in I$: $m_i(\{z : z^{(i)} < -1\}) = 0$ (jumps from the $i$-th component cannot make $x^{(i)}$ negative when $x^{(i)} > 0$ is small)

    **D. Integrability conditions:**

    (D1) $\int_{|z| > 1} |z|\,m_0(dz) < \infty$ and $\int_{|z| > 1} |z|\,m_i(dz) < \infty$ for all $i$ (finite first moment for large jumps)

### Interpretation of Each Condition

**Conditions (A4)-(A5): Boundary diffusion vanishes.** On the face $\partial_k D = \{x^{(k)} = 0\}$, the diffusion of the $k$-th component is

$$
a_{kk}(x)\big|_{x^{(k)}=0} = (a_0)_{kk} + \sum_{i \neq k} (\alpha_i)_{kk}\,x^{(i)} = 0
$$

by conditions (A4) and (A5). This ensures that when $X_t^{(k)}$ hits zero, the noise vanishes, preventing the process from being pushed below zero by the diffusion.

**Condition (B1): Inward-pointing drift.** At $x^{(k)} = 0$, the drift of the $k$-th component is

$$
\mu_k(x)\big|_{x^{(k)}=0} = (b_0)_k + \sum_{j \neq k} B_{kj}\,x^{(j)} \geq (b_0)_k \geq 0
$$

The non-negativity of $(b_0)_k$ ensures the drift pushes $X_t^{(k)}$ away from the boundary. Together with vanishing diffusion, this is the multidimensional analog of the Feller condition.

**Condition (B2): Non-negative cross-effects.** When $X_t^{(k)} = 0$, the drift of $X_t^{(k)}$ depends on the other CIR components through $B_{kj} X_t^{(j)}$. For $j \in I$, we need $B_{kj} \geq 0$ so that higher values of other non-negative components strengthen the inward drift, not weaken it.

---

## Proof of Necessity

### Diffusion Must Vanish at the Boundary

!!! info "Proposition: Necessity of Vanishing Boundary Diffusion"
    If $X_t$ is an affine process on $D = \mathbb{R}_+^m \times \mathbb{R}^{d-m}$, then $(a_0)_{ii} = 0$ for all $i \in I$ and $(\alpha_j)_{ii} = 0$ for all $j \neq i$ with $j \in I$.

**Proof.** Suppose $(a_0)_{ii} > 0$ for some $i \in I$. Then at $x^{(i)} = 0$, the instantaneous variance of $X_t^{(i)}$ is

$$
a_{ii}(x)\big|_{x^{(i)}=0} = (a_0)_{ii} + \sum_{j \neq i} (\alpha_j)_{ii}\,x^{(j)} \geq (a_0)_{ii} > 0
$$

The continuous martingale part of $X_t^{(i)}$ has nonzero variance at the boundary, so by the support theorem for diffusions, $X_t^{(i)}$ will visit negative values with positive probability in any neighborhood of $x^{(i)} = 0$. This contradicts $X_t^{(i)} \geq 0$. $\square$

### Drift Must Point Inward

!!! info "Proposition: Necessity of Inward Drift"
    If $X_t$ is an affine process on $D$ with $X_t^{(i)} \geq 0$ for all $t \geq 0$, then $(b_0)_i \geq 0$ for all $i \in I$.

**Proof.** Set $x^{(j)} = 0$ for all $j \in I$ and consider the drift of $X_t^{(i)}$ at this point:

$$
\mu_i(x) = (b_0)_i + \sum_{j \in J} B_{ij} x^{(j)}
$$

By choosing $x^{(j)} = 0$ for all $j \in J$ as well (which is in $D$), we get $\mu_i(x) = (b_0)_i$. If $(b_0)_i < 0$, the drift pushes $X_t^{(i)}$ below zero. Since the diffusion vanishes at this point (by the previous proposition), the process would enter $(-\infty, 0)$ in finite time, contradicting $X_t^{(i)} \geq 0$. $\square$

---

## Verification for Standard Models

### CIR Model

The CIR process $dX_t = \kappa(\theta - X_t)\,dt + \xi\sqrt{X_t}\,dW_t$ on $D = \mathbb{R}_+$ has:

- $b_0 = \kappa\theta$, $B = -\kappa$, $a_0 = 0$, $\alpha_1 = \xi^2$

Checking admissibility:

- (A1): $a_0 = 0 \geq 0$ -- satisfied
- (A2): $\alpha_1 = \xi^2 > 0$ -- satisfied
- (A5): $(a_0)_{11} = 0$ -- satisfied
- (B1): $(b_0)_1 = \kappa\theta \geq 0$ iff $\kappa\theta \geq 0$ -- satisfied when $\kappa > 0$ and $\theta > 0$

!!! tip "Feller Condition vs. Admissibility"
    Admissibility requires only $\kappa\theta \geq 0$, which prevents the drift from pushing the process below zero. The stronger **Feller condition** $2\kappa\theta \geq \xi^2$ ensures the boundary $X_t = 0$ is **never reached**, providing strict positivity. Both conditions allow a well-defined process, but the Feller condition additionally guarantees the transition density exists and is smooth.

### Heston Model

The Heston model on $D = \mathbb{R}_+ \times \mathbb{R}$ with state $(V_t, \log S_t)$:

- $b_0 = (\kappa\theta, r)^\top$, $B = \begin{pmatrix} -\kappa & 0 \\ -1/2 & 0 \end{pmatrix}$
- $a_0 = 0$, $\alpha_1 = \begin{pmatrix} \xi^2 & \rho\xi \\ \rho\xi & 1 \end{pmatrix}$, $\alpha_2 = 0$

Checking:

- (A2): $\alpha_1$ is positive semi-definite iff $\xi^2 \cdot 1 - (\rho\xi)^2 = \xi^2(1 - \rho^2) \geq 0$, which holds for $|\rho| \leq 1$ -- satisfied
- (A3): $\alpha_2 = 0$ -- satisfied (log-price is the Gaussian component)
- (A5): $(a_0)_{11} = 0$ -- satisfied
- (B1): $(b_0)_1 = \kappa\theta \geq 0$ -- satisfied
- (B2): Not applicable (only one CIR component)

!!! example "What Could Go Wrong"
    If the Heston model were specified with $\alpha_1 = \begin{pmatrix} \xi^2 & \rho\xi \\ \rho\xi & 1 \end{pmatrix}$ and $|\rho| > 1$, then $\alpha_1$ would not be positive semi-definite, violating (A2). The covariance matrix $a(x) = \alpha_1 V_t$ would have a negative eigenvalue, making the SDE ill-posed.

---

## The Role of Jump Conditions

### Jump Support Constraints

Conditions (C1)-(C3) ensure that jumps do not eject the process from the state space. For an affine jump-diffusion with state-independent jumps (e.g., the Merton model), condition (C1) requires that jump sizes $z$ satisfy $x + z \in D$ for all $x \in D$.

For state-dependent jump intensity $\lambda(x) = \lambda_0 + \lambda_1^\top x$ with $\lambda_1^{(i)} > 0$ for $i \in I$, the jump intensity increases with the CIR-type state variables. This is natural in credit models where higher default intensity leads to more frequent jumps.

Condition (C3) prevents catastrophic jumps: if $X_t^{(i)}$ is close to zero, a jump of size $z^{(i)} < -X_t^{(i)}$ would make $X_t^{(i)}$ negative. The condition ensures that the jump distribution does not allow $z^{(i)} < -1$, which combined with $X_t^{(i)} \geq 0$ provides the needed protection.

---

## Summary

The Duffie-Filipovic-Schachermayer admissibility conditions are the algebraic constraints on the parameters $(b_0, B, a_0, \alpha_i, m_0, m_i)$ that guarantee a well-defined affine process on $D = \mathbb{R}_+^m \times \mathbb{R}^{d-m}$. The central requirements are: diffusion must vanish on the boundary of $\mathbb{R}_+^m$ (conditions A4, A5), drift must point inward at the boundary (conditions B1, B2), and jumps must not eject the process from the state space (conditions C1-C3). These conditions are both necessary and sufficient. For the CIR model, admissibility reduces to $\kappa\theta \geq 0$; for the Heston model, it additionally requires $|\rho| \leq 1$ for positive semi-definiteness of the diffusion matrix. The admissibility conditions constrain the parameter space of affine models, with important implications for calibration and estimation: not all parameter combinations that minimize a fitting criterion correspond to a well-defined stochastic process.

---

## Further Reading

- Duffie, D., Filipovic, D., and Schachermayer, W. (2003). "Affine Processes and Applications in Finance." *Annals of Applied Probability*, 13(3), 984--1053.
- Filipovic, D. (2009). *Term-Structure Models: A Graduate Course*. Springer, Chapter 10.
- Keller-Ressel, M. (2011). "Moment Explosions and Long-Term Behavior of Affine Stochastic Volatility Models." *Mathematical Finance*, 21(1), 73--98.

---

## Exercises

**Exercise 1.** For the Heston model on $D = \mathbb{R}_+ \times \mathbb{R}$ (variance $V_t$ and log-price $X_t$), verify all four admissibility conditions (A1)--(A4). Pay particular attention to condition (A2): identify which entries of the diffusion matrices $a_0$ and $\alpha_1$ must be zero for the variance component.

---

**Exercise 2.** Construct a two-dimensional affine process on $D = \mathbb{R}_+^2$ (two CIR components) that violates condition (A1) for the second component. Explain what goes wrong: why does the process leave the state space?

---

**Exercise 3.** Consider a proposed model on $\mathbb{R}_+$ with drift $b(x) = -\alpha$ (constant, $\alpha > 0$) and diffusion $a(x) = \xi^2 x$. Check condition (A1): is $b_0 = -\alpha \geq 0$ satisfied? What happens to the process when it reaches $x = 0$?

---

**Exercise 4.** The admissibility condition (A3) requires that jumps preserve the state space: $m_i$ is supported on $D - e_i$. For a one-dimensional CIR-type process on $\mathbb{R}_+$, what does this imply about the support of the jump size distribution? Can jumps be negative?

---

**Exercise 5.** For a three-factor model on $D = \mathbb{R}_+^2 \times \mathbb{R}$ with a correlated diffusion between the first CIR component and the Gaussian component, write down the diffusion matrix $a(x) = a_0 + \alpha_1 x_1 + \alpha_2 x_2$ and identify which cross-terms are permitted by condition (A2). Can the two CIR components have correlated Brownian motions?

---

**Exercise 6.** Prove that condition (A1) is necessary for state space invariance. That is, if $(b_0)_i < 0$ for some CIR-type component $i$, construct a scenario (starting state near the boundary $x_i = 0$) where the drift pushes $x_i$ negative, violating $x_i \geq 0$.
