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

??? success "Solution to Exercise 1"
    The Heston model on $D = \mathbb{R}_+ \times \mathbb{R}$ has state $(V_t, X_t)$ where $V_t \geq 0$ is the variance (CIR-type, index $i = 1$) and $X_t = \log S_t \in \mathbb{R}$ is the log-price (Gaussian, index $j = 2$). The affine parameters are:

    $$
    a_0 = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}, \qquad \alpha_1 = \begin{pmatrix} \xi^2 & \rho\xi \\ \rho\xi & 1 \end{pmatrix}, \qquad \alpha_2 = 0
    $$

    **Checking (A1):** $a_0 = 0$ is trivially symmetric positive semi-definite. Satisfied.

    **Checking (A2):** For $i = 1$ (the CIR component), $\alpha_1$ must be symmetric positive semi-definite. It is symmetric by inspection. Its eigenvalues are non-negative iff

    $$
    \det(\alpha_1) = \xi^2 \cdot 1 - (\rho\xi)^2 = \xi^2(1 - \rho^2) \geq 0
    $$

    which holds for $|\rho| \leq 1$. Satisfied.

    **Checking (A3):** For $j = 2$ (the Gaussian component), $\alpha_2 = 0$. Satisfied.

    **Checking (A4):** For the CIR component $i = 1$ and any other CIR component $k \in I$ with $k \neq 1$: there are no other CIR components (only one CIR factor), so (A4) is vacuously satisfied. Additionally, $(a_0)_{11} = 0$ satisfies (A5), ensuring the diffusion of the variance component vanishes at the boundary $V_t = 0$.

---

**Exercise 2.** Construct a two-dimensional affine process on $D = \mathbb{R}_+^2$ (two CIR components) that violates condition (A1) for the second component. Explain what goes wrong: why does the process leave the state space?

??? success "Solution to Exercise 2"
    Consider a two-dimensional affine process on $D = \mathbb{R}_+^2$ with state $(X_t^{(1)}, X_t^{(2)})$. Suppose we attempt a specification where the diffusion matrix for the second component has a nonzero constant part, violating condition (A5) for $i = 2$:

    $$
    a_0 = \begin{pmatrix} 0 & 0 \\ 0 & \epsilon \end{pmatrix}, \qquad \alpha_1 = \begin{pmatrix} \xi_1^2 & 0 \\ 0 & 0 \end{pmatrix}, \qquad \alpha_2 = \begin{pmatrix} 0 & 0 \\ 0 & \xi_2^2 \end{pmatrix}
    $$

    with $\epsilon > 0$. This violates $(a_0)_{22} = \epsilon > 0$ (condition A5 requires $(a_0)_{22} = 0$ for the CIR component $i = 2$).

    **What goes wrong:** At the boundary $X_t^{(2)} = 0$, the instantaneous variance of the second component is

    $$
    a_{22}(x)\big|_{x^{(2)}=0} = (a_0)_{22} + (\alpha_2)_{22} \cdot 0 = \epsilon > 0
    $$

    The diffusion does not vanish at the boundary. The second component behaves locally like $dX_t^{(2)} \approx \mu_2\,dt + \sqrt{\epsilon}\,dW_t$ near zero. By the support theorem for diffusions, the Brownian motion pushes $X_t^{(2)}$ below zero with positive probability in any short time interval. The process leaves $D = \mathbb{R}_+^2$.

---

**Exercise 3.** Consider a proposed model on $\mathbb{R}_+$ with drift $b(x) = -\alpha$ (constant, $\alpha > 0$) and diffusion $a(x) = \xi^2 x$. Check condition (A1): is $b_0 = -\alpha \geq 0$ satisfied? What happens to the process when it reaches $x = 0$?

??? success "Solution to Exercise 3"
    The proposed model on $\mathbb{R}_+$ has $b_0 = -\alpha$ (with $\alpha > 0$) and diffusion $a(x) = \xi^2 x$. The drift is $\mu(x) = -\alpha + 0 \cdot x = -\alpha$, so $b_0 = -\alpha < 0$.

    **Checking condition (B1):** We need $(b_0)_1 \geq 0$, but $(b_0)_1 = -\alpha < 0$. This is violated.

    **What happens at $x = 0$:** The diffusion vanishes ($a(0) = 0$), so the process evolves deterministically near zero. At $x = 0$, the drift is $\mu(0) = -\alpha < 0$, which pushes the process into negative territory. Starting from any $x_0 > 0$, the process will eventually reach a neighborhood of zero, and once there, the negative drift drives $X_t$ below zero. The process cannot remain in $\mathbb{R}_+$, confirming that $b_0 \geq 0$ is necessary for admissibility.

---

**Exercise 4.** The admissibility condition (A3) requires that jumps preserve the state space: $m_i$ is supported on $D - e_i$. For a one-dimensional CIR-type process on $\mathbb{R}_+$, what does this imply about the support of the jump size distribution? Can jumps be negative?

??? success "Solution to Exercise 4"
    The exercise references condition (A3) as a jump condition, but the notation differs from the theorem statement. For a one-dimensional CIR-type process on $\mathbb{R}_+$, the jump compensator is $m(x, dz) = m_0(dz) + x\,m_1(dz)$.

    **Condition (C1):** $m_0$ must be supported on $D = \mathbb{R}_+ = [0, \infty)$. This means the state-independent jump size distribution can only produce non-negative jumps: $z \geq 0$ under $m_0$. Otherwise, starting at $x = 0$, a negative jump would send the process below zero.

    **Condition (C3):** $m_1(\{z : z < -1\}) = 0$. The state-dependent jumps (with intensity proportional to $x$) cannot have size below $-1$. This means jumps can be negative, but bounded below by $-1$.

    **Can jumps be negative?** Under $m_0$: no, all jumps must be non-negative. Under $m_1$: yes, but only in the range $z \in [-1, 0)$. When $x > 0$, a jump of size $z \in [-1, 0)$ moves the state to $x + z$. Since $x \geq 0$ and $z \geq -1$, we need additional conditions to ensure $x + z \geq 0$. For small $x$, the condition $z \geq -1$ alone is not sufficient; finer integrability conditions on $m_1$ near $z = 0$ ensure that the jump activity near zero is compatible with state space invariance.

---

**Exercise 5.** For a three-factor model on $D = \mathbb{R}_+^2 \times \mathbb{R}$ with a correlated diffusion between the first CIR component and the Gaussian component, write down the diffusion matrix $a(x) = a_0 + \alpha_1 x_1 + \alpha_2 x_2$ and identify which cross-terms are permitted by condition (A2). Can the two CIR components have correlated Brownian motions?

??? success "Solution to Exercise 5"
    The state space is $D = \mathbb{R}_+^2 \times \mathbb{R}$ with state $(V_1, V_2, Y)^\top$ where $V_1, V_2 \geq 0$ are CIR components (indices $I = \{1, 2\}$) and $Y \in \mathbb{R}$ is Gaussian (index $J = \{3\}$).

    The diffusion matrix is $a(x) = a_0 + \alpha_1 x_1 + \alpha_2 x_2$ (since $\alpha_3 = 0$ by condition A3). The admissibility conditions constrain:

    **For $a_0$:** $(a_0)_{11} = (a_0)_{22} = 0$ (condition A5), and $(a_0)_{33} \geq 0$ (the constant Gaussian diffusion). The off-diagonal entries $(a_0)_{12} = (a_0)_{21}$ must be zero as well (since the diagonal entries are zero, positive semi-definiteness forces the off-diagonals involving CIR rows to vanish). So

    $$
    a_0 = \begin{pmatrix} 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & \sigma^2 \end{pmatrix}
    $$

    **For $\alpha_1$:** Must be symmetric positive semi-definite. By condition (A4), $(\alpha_1)_{22} = 0$ (the diffusion of the second CIR component cannot depend on $x_1$). So

    $$
    \alpha_1 = \begin{pmatrix} \xi_1^2 & 0 & \eta_1\xi_1 \\ 0 & 0 & 0 \\ \eta_1\xi_1 & 0 & \eta_1^2 \end{pmatrix}
    $$

    which has rank at most 1 (the cross-term between the first CIR component and the Gaussian component is $\eta_1\xi_1$, encoding their correlation driven by $V_1$).

    **For $\alpha_2$:** Similarly, $(\alpha_2)_{11} = 0$ (condition A4), giving

    $$
    \alpha_2 = \begin{pmatrix} 0 & 0 & 0 \\ 0 & \xi_2^2 & \eta_2\xi_2 \\ 0 & \eta_2\xi_2 & \eta_2^2 \end{pmatrix}
    $$

    **Can the two CIR components have correlated Brownian motions?** The covariance between $V_1$ and $V_2$ is $a_{12}(x) = (a_0)_{12} + (\alpha_1)_{12}x_1 + (\alpha_2)_{12}x_2 = 0 + 0 + 0 = 0$. The admissibility conditions force $a_{12}(x) = 0$ identically. Therefore, the two CIR components cannot have correlated Brownian motions in this affine framework. Their diffusions are necessarily independent.

---

**Exercise 6.** Prove that condition (A1) is necessary for state space invariance. That is, if $(b_0)_i < 0$ for some CIR-type component $i$, construct a scenario (starting state near the boundary $x_i = 0$) where the drift pushes $x_i$ negative, violating $x_i \geq 0$.

??? success "Solution to Exercise 6"
    Suppose $(b_0)_i < 0$ for some CIR-type component $i \in I$. Consider starting the process at the point $x_0 \in D$ where $x_0^{(i)} = 0$ and $x_0^{(j)} = 0$ for all $j \in I$ and $x_0^{(j)} = 0$ for all $j \in J$.

    At this point, the drift of the $i$-th component is

    $$
    \mu_i(x_0) = (b_0)_i + \sum_{j=1}^d B_{ij} x_0^{(j)} = (b_0)_i < 0
    $$

    By the necessity of vanishing boundary diffusion (conditions A4, A5, already proved), the diffusion at the boundary satisfies $a_{ii}(x_0) = 0$. With zero diffusion and strictly negative drift at $x_0$, the process evolves locally as

    $$
    X_t^{(i)} \approx x_0^{(i)} + \mu_i(x_0)\,t = (b_0)_i \cdot t < 0 \quad \text{for } t > 0
    $$

    The process immediately enters the region $X_t^{(i)} < 0$, violating the state space constraint $X_t^{(i)} \geq 0$. More rigorously, since the diffusion is continuous and vanishes at the boundary, the drift dominates for small $t$. By the comparison theorem for SDEs, $X_t^{(i)} \leq (b_0)_i\,t < 0$ for small $t > 0$, proving that the process leaves $D$. This establishes the necessity of $(b_0)_i \geq 0$ for state space invariance. $\square$
