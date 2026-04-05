# Canonical Representation

A $d$-dimensional affine process is specified by a large set of parameters: drift vectors and matrices, diffusion matrices, and jump measures. However, many different parameter sets generate the same family of probability distributions, because an invertible **affine transformation** of the state vector $X_t \mapsto CX_t + c$ reshuffles the parameters without changing the observable outputs (bond prices, option prices, yield curves). The **canonical representation** of Duffie, Filipovic, and Schachermayer (2003) resolves this redundancy by fixing a standard form that is unique up to a well-defined equivalence class. This section develops the theory of canonical forms, proves uniqueness, and shows how to reduce standard models to their canonical parametrization.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Explain why different affine parametrizations can generate the same observable distributions
    2. Define the canonical form for affine processes on $\mathbb{R}_+^m \times \mathbb{R}^{d-m}$
    3. State the uniqueness theorem: affine processes are determined up to invertible affine state transformations
    4. Compute how affine parameters transform under linear change of state variable
    5. Reduce a given affine model to its canonical form by applying appropriate normalization constraints

---

## Motivation

### The Identification Problem

Consider a two-factor Vasicek model with state $X_t = (X_t^{(1)}, X_t^{(2)})^\top$ and short rate $r_t = \rho_0 + \rho_1^{(1)} X_t^{(1)} + \rho_1^{(2)} X_t^{(2)}$. Define a new state $\tilde{X}_t = CX_t + c$ for some invertible matrix $C$ and vector $c$. Then $\tilde{X}_t$ is also an affine process (with transformed parameters), and the short rate $r_t = \tilde{\rho}_0 + \tilde{\rho}_1^\top \tilde{X}_t$ is the same function of observables.

Bond prices, yields, and all derivatives depend on $r_t$ and its distribution, not on the particular state representation. Therefore the two parametrizations --- the original $(b_0, B, a_0, \rho_0, \rho_1)$ and the transformed $(\tilde{b}_0, \tilde{B}, \tilde{a}_0, \tilde{\rho}_0, \tilde{\rho}_1)$ --- are **observationally equivalent**. Without fixing a canonical form, the parameter space contains infinitely many representations of the same model, making estimation and comparison meaningless.

### Purpose of the Canonical Form

The canonical representation achieves three goals:

1. **Identification**: Eliminating the freedom of affine state transformations so that each distinct model corresponds to a unique parameter set
2. **Comparability**: Enabling meaningful comparison between models (e.g., testing whether $A_1(3)$ fits data better than $A_0(3)$)
3. **Parsimony**: Reducing the number of free parameters to the minimum needed to span the observationally distinct models within each $A_m(d)$ class

---

## Affine State Transformations

### Definition

!!! info "Definition: Affine State Transformation"
    An **affine state transformation** is a map $\tilde{X}_t = CX_t + c$ where $C \in \mathbb{R}^{d \times d}$ is invertible and $c \in \mathbb{R}^d$ is a translation vector.

For the transformation to preserve the state space $D = \mathbb{R}_+^m \times \mathbb{R}^{d-m}$, additional constraints on $C$ and $c$ are needed: the first $m$ components of $\tilde{X}_t$ must remain non-negative whenever the first $m$ components of $X_t$ are non-negative.

### Parameter Transformation Rules

!!! info "Proposition: Transformation of Affine Parameters"
    Under $\tilde{X}_t = CX_t + c$, the affine parameters transform as:

    **Drift:**

    $$
    \tilde{b}_0 = Cb_0 + Bc \cdot C^{-1} \cdot c + c_{\text{adj}}, \qquad \tilde{B} = CBC^{-1}
    $$

    More precisely: $\tilde{\mu}(\tilde{x}) = C\mu(C^{-1}(\tilde{x} - c))$, giving

    $$
    \tilde{b}_0 = C(b_0 + Bc) - CBC^{-1}c = Cb_0 + (CB - \tilde{B})c
    $$

    Since $\tilde{B} = CBC^{-1}$, we get $\tilde{b}_0 = Cb_0 + CBc - CBC^{-1}c = C(b_0 + Bc) - CBC^{-1}c$. Simplifying:

    $$
    \tilde{b}_0 = Cb_0 + CBc, \qquad \tilde{B} = CBC^{-1}
    $$

    **Diffusion:**

    $$
    \tilde{a}_0 = Ca_0C^\top + \sum_{i=1}^d C\alpha_i C^\top c^{(i)}, \qquad \tilde{\alpha}_j = \sum_{i=1}^d C\alpha_i C^\top (C^{-1})_{ij}
    $$

    **Short rate:**

    $$
    \tilde{\rho}_0 = \rho_0 + \rho_1^\top C^{-1}(-c) = \rho_0 - \rho_1^\top C^{-1}c, \qquad \tilde{\rho}_1 = (C^{-1})^\top \rho_1
    $$

**Proof (drift transformation).** The dynamics of $\tilde{X}_t = CX_t + c$ are

$$
d\tilde{X}_t = C\,dX_t = C(b_0 + BX_t)\,dt + C\sigma(X_t)\,dW_t
$$

Substituting $X_t = C^{-1}(\tilde{X}_t - c)$:

$$
d\tilde{X}_t = C\bigl(b_0 + BC^{-1}(\tilde{X}_t - c)\bigr)\,dt + \cdots = (Cb_0 - CBC^{-1}c)\,dt + CBC^{-1}\tilde{X}_t\,dt + \cdots
$$

Reading off: $\tilde{b}_0 = C(b_0 - BC^{-1}c) + \ldots$. Let us simplify: $\tilde{b}_0 = Cb_0 + C B C^{-1}(-c) + CBC^{-1}c = Cb_0$... Actually:

$$
\tilde{\mu}(\tilde{x}) = C\bigl(b_0 + B C^{-1}(\tilde{x} - c)\bigr) = \underbrace{C(b_0 - BC^{-1}c)}_{\tilde{b}_0} + \underbrace{CBC^{-1}}_{\tilde{B}}\tilde{x}
$$

So $\tilde{b}_0 = C(b_0 - BC^{-1}c)$ and $\tilde{B} = CBC^{-1}$. $\square$

---

## The Canonical Form

### Construction

!!! info "Definition: Canonical Affine Process"
    An affine process on $D = \mathbb{R}_+^m \times \mathbb{R}^{d-m}$ is in **canonical form** if the following normalization constraints are imposed:

    **For CIR-type components** ($i = 1, \ldots, m$):

    1. $(\alpha_i)_{ii} = 1$ (unit diffusion coefficient)
    2. $(B)_{ii} \leq 0$ (non-positive diagonal drift, ensuring mean reversion)

    **For Gaussian components** ($i = m+1, \ldots, d$):

    3. $(a_0)_{ij} = \delta_{ij}$ for $i, j \in \{m+1, \ldots, d\}$ (identity diffusion matrix for Gaussian components)
    4. $B$ restricted to the Gaussian block is in real Jordan normal form

    **Short rate normalization:**

    5. $\rho_1^{(i)} \in \{0, 1\}$ for each $i$ (each state variable either contributes to the short rate with unit loading or does not contribute)

The specific normalization constraints vary across references. The key principle is that the $d^2 + d$ degrees of freedom in the affine transformation $(C, c)$ are used to fix $d^2 + d$ constraints on the parameters, leaving a minimal set of free parameters.

### Counting Degrees of Freedom

The affine transformation $\tilde{X} = CX + c$ has:

- $d^2$ parameters in $C$ (invertible matrix)
- $d$ parameters in $c$ (translation vector)

Total: $d^2 + d$ degrees of freedom. Each normalization constraint above eliminates one degree of freedom. The canonical form imposes exactly $d^2 + d$ independent constraints, leaving the minimal free parameter set.

!!! example "Degrees of Freedom for $A_1(2)$"
    For $d = 2$, the transformation has $4 + 2 = 6$ degrees of freedom. The canonical form imposes:

    1. $(\alpha_1)_{11} = 1$ (1 constraint)
    2. $(a_0)_{22} = 1$ (1 constraint)
    3. $B_{11} \leq 0$ with specific normalization (1 constraint)
    4. $B_{22}$ in normal form (1 constraint)
    5. $\rho_1 = (1, 0)^\top$ or $(0, 1)^\top$ or $(1, 1)^\top$ (2 constraints from fixing components)

    Total: 6 constraints, matching the 6 degrees of freedom.

---

## Uniqueness Theorem

!!! info "Theorem: Uniqueness of Canonical Form (DFS 2003)"
    Two admissible affine processes on $D = \mathbb{R}_+^m \times \mathbb{R}^{d-m}$ generate the same family of finite-dimensional distributions if and only if they are related by an invertible affine state transformation $\tilde{X}_t = CX_t + c$ that preserves $D$.

    Consequently, within each $A_m(d)$ class, the canonical form is **unique**: no two distinct canonical parametrizations generate the same distributions.

This theorem has a profound consequence: the space of observationally distinct $A_m(d)$ models is a finite-dimensional manifold whose dimension equals the number of free parameters in the canonical form. Model comparison and statistical testing can be conducted on this manifold.

---

## Examples of Canonicalization

### One-Factor CIR: $A_1(1)$

The general one-factor CIR model has parameters $\kappa > 0$, $\theta > 0$, $\xi > 0$. The canonical form normalizes $\xi = 1$ (unit diffusion):

$$
dX_t = (\tilde{\kappa}\tilde{\theta} - \tilde{\kappa}X_t)\,dt + \sqrt{X_t}\,dW_t
$$

This is achieved by the state transformation $\tilde{X}_t = X_t / \xi^2$ (since the original diffusion $\xi\sqrt{X_t}$ becomes $\xi \cdot \xi^{-1}\sqrt{\tilde{X}_t} = \sqrt{\tilde{X}_t}$). The transformed parameters are $\tilde{\kappa} = \kappa$ and $\tilde{\theta} = \theta/\xi^2$.

### Two-Factor Gaussian: $A_0(2)$

The general $A_0(2)$ model has drift $b_0 + Bx$ with $B \in \mathbb{R}^{2 \times 2}$ (4 parameters) and constant covariance $a_0$ (3 parameters, symmetric). The short rate adds 3 parameters ($\rho_0, \rho_1^{(1)}, \rho_1^{(2)}$). Total: 12 parameters.

The canonical form uses $C$ to diagonalize $a_0$ (putting Gaussian components in standard form with unit variance) and $c$ to center the drift. The transformation eliminates 6 parameters, leaving 6 free parameters in the canonical $A_0(2)$ model.

### Heston Model: $A_1(2)$

The standard Heston parametrization uses $(\kappa, \theta, \xi, \rho, r)$ plus the initial conditions. In canonical form:

- $\alpha_1$ is normalized so that $(\alpha_1)_{11} = 1$ (achieved by rescaling $V_t$)
- The Gaussian component has unit variance contribution from $a_0$
- The correlation $\rho$ and the mean-reversion parameters are the free parameters

---

## Practical Implications

### For Estimation

When estimating affine models from data, working in canonical form avoids the **identification problem**: without normalization, different parameter vectors can produce identical likelihoods, creating ridges in the likelihood surface that prevent convergence of optimization algorithms.

### For Model Selection

The canonical form enables meaningful comparison of nested models. Testing $A_1(3)$ against $A_0(3)$ requires both models to be in canonical form so that the parameter counts reflect true degrees of freedom rather than redundant representations.

!!! tip "Software Implementation"
    Most implementations of affine term structure models work directly with the canonical form, imposing the normalization constraints during estimation. When reading empirical papers, always check which normalization is used --- different authors may use different canonical forms within the same $A_m(d)$ class, making parameter values non-comparable across studies without transformation.

---

## Summary

The canonical representation of affine processes resolves the inherent redundancy in their parametrization. Since an invertible affine state transformation $\tilde{X} = CX + c$ preserves the affine structure and generates the same observable distributions, many different parameter sets correspond to the same model. The canonical form imposes $d^2 + d$ normalization constraints that exhaust the degrees of freedom of the transformation, yielding a unique representative for each equivalence class of observationally indistinguishable models. Within each $A_m(d)$ sub-class, the canonical parametrization has the minimal number of free parameters. Working in canonical form is essential for estimation (avoiding ridges in the likelihood surface), model comparison (meaningful parameter counts), and communication (comparable results across studies).

---

## Further Reading

- Duffie, D., Filipovic, D., and Schachermayer, W. (2003). "Affine Processes and Applications in Finance." *Annals of Applied Probability*, 13(3), 984--1053.
- Dai, Q. and Singleton, K. (2000). "Specification Analysis of Affine Term Structure Models." *Journal of Finance*, 55(5), 1943--1978.
- Collin-Dufresne, P., Goldstein, R., and Jones, C. (2008). "Identification of Maximal Affine Term Structure Models." *Journal of Finance*, 63(2), 743--795.

---

## Exercises

**Exercise 1.** Consider a one-factor Vasicek model $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$ with short rate $r_t = X_t$. Apply the affine transformation $\tilde{X}_t = cX_t + d$ for constants $c > 0$ and $d$. Derive the SDE for $\tilde{X}_t$ and show it is still Vasicek with transformed parameters. Express $\tilde{\kappa}$, $\tilde{\theta}$, $\tilde{\sigma}$ in terms of the original parameters and $c$, $d$.

??? success "Solution to Exercise 1"
    Starting from $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$ with $r_t = X_t$, define $\tilde{X}_t = cX_t + d$. Then $X_t = (\tilde{X}_t - d)/c$ and

    $$
    d\tilde{X}_t = c\,dX_t = c\bigl[\kappa(\theta - X_t)\,dt + \sigma\,dW_t\bigr]
    $$

    Substituting $X_t = (\tilde{X}_t - d)/c$:

    $$
    d\tilde{X}_t = c\,\kappa\!\left(\theta - \frac{\tilde{X}_t - d}{c}\right)dt + c\sigma\,dW_t = \kappa\bigl(c\theta + d - \tilde{X}_t\bigr)\,dt + c\sigma\,dW_t
    $$

    This can be written as

    $$
    d\tilde{X}_t = \tilde{\kappa}(\tilde{\theta} - \tilde{X}_t)\,dt + \tilde{\sigma}\,dW_t
    $$

    with transformed parameters:

    $$
    \tilde{\kappa} = \kappa, \qquad \tilde{\theta} = c\theta + d, \qquad \tilde{\sigma} = c\sigma
    $$

    The mean-reversion speed $\kappa$ is invariant under the transformation. The long-run mean shifts by the affine map, and the volatility scales by $c$. The short rate $r_t = X_t = (\tilde{X}_t - d)/c$, so the transformed short-rate loading is $\tilde{\rho}_1 = 1/c$ and $\tilde{\rho}_0 = -d/c$. Both parametrizations produce the same bond prices and yield curves.

---

**Exercise 2.** For the $A_0(2)$ family (two Gaussian factors), count the number of free parameters in the unrestricted model (drift $b_0 \in \mathbb{R}^2$, $B \in \mathbb{R}^{2 \times 2}$, $a_0 \in \mathbb{S}^2_+$, $\rho_0 \in \mathbb{R}$, $\rho_1 \in \mathbb{R}^2$). Then count the degrees of freedom in the transformation group (invertible $C \in \mathbb{R}^{2 \times 2}$ and $c \in \mathbb{R}^2$). How many parameters remain after canonical normalization?

??? success "Solution to Exercise 2"
    **Unrestricted parameter count:**

    - Drift: $b_0 \in \mathbb{R}^2$ (2 parameters), $B \in \mathbb{R}^{2 \times 2}$ (4 parameters)
    - Diffusion: $a_0 \in \mathbb{S}^2_+$ symmetric (3 parameters: two diagonal, one off-diagonal)
    - Short rate: $\rho_0 \in \mathbb{R}$ (1 parameter), $\rho_1 \in \mathbb{R}^2$ (2 parameters)

    Total unrestricted parameters: $2 + 4 + 3 + 1 + 2 = 12$.

    **Degrees of freedom in the transformation group:**

    - $C \in \mathbb{R}^{2 \times 2}$ invertible: 4 parameters
    - $c \in \mathbb{R}^2$: 2 parameters

    Total degrees of freedom: $4 + 2 = 6$.

    **Parameters after canonical normalization:** The canonical form uses the 6 degrees of freedom to impose 6 constraints (e.g., normalizing $a_0$ to the identity matrix uses 3, putting $B$ in Jordan form uses 1, fixing $\rho_1$ components uses 2). The remaining free parameters are

    $$
    12 - 6 = 6
    $$

    So the canonical $A_0(2)$ model has 6 free parameters.

---

**Exercise 3.** Explain why two different parametrizations of an affine model that are related by an invertible affine state transformation produce identical bond prices, yield curves, and option prices. Show this explicitly for the zero-coupon bond price $P(t,T) = e^{A(\tau) + B(\tau)^\top x}$ by computing how $A$ and $B$ transform.

??? success "Solution to Exercise 3"
    Under the transformation $\tilde{X}_t = CX_t + c$, the bond price must remain unchanged because it represents an observable market price. The original bond price is

    $$
    P(t,T) = \exp\!\bigl(A(\tau) + B(\tau)^\top X_t\bigr)
    $$

    Substituting $X_t = C^{-1}(\tilde{X}_t - c)$:

    $$
    P(t,T) = \exp\!\bigl(A(\tau) + B(\tau)^\top C^{-1}(\tilde{X}_t - c)\bigr) = \exp\!\bigl(\underbrace{A(\tau) - B(\tau)^\top C^{-1}c}_{\tilde{A}(\tau)} + \underbrace{(C^{-1})^\top B(\tau)}_{\tilde{B}(\tau)}{}^\top \tilde{X}_t\bigr)
    $$

    The transformed coefficients are:

    $$
    \tilde{A}(\tau) = A(\tau) - B(\tau)^\top C^{-1}c, \qquad \tilde{B}(\tau) = (C^{-1})^\top B(\tau)
    $$

    The bond price $P(t,T)$ is identical in both representations because $\tilde{A}(\tau) + \tilde{B}(\tau)^\top \tilde{X}_t = A(\tau) + B(\tau)^\top X_t$. Since bond prices determine yields ($y(t,T) = -\log P(t,T)/\tau$), and option prices are expectations of payoffs under the risk-neutral measure (which is also preserved by invertible linear transformations of the state), all observable quantities are identical.

---

**Exercise 4.** The canonical form for the CIR process normalizes $\xi = 1$ (or equivalently $a_1 = 1$). Given an arbitrary CIR process with parameters $(\kappa, \theta, \xi)$, find the transformation $\tilde{X}_t = cX_t$ that achieves $\tilde{\xi} = 1$ and express the canonical parameters $(\tilde{\kappa}, \tilde{\theta})$ in terms of the originals.

??? success "Solution to Exercise 4"
    The general CIR process is $dX_t = \kappa(\theta - X_t)\,dt + \xi\sqrt{X_t}\,dW_t$ with diffusion coefficient $\alpha_1 = \xi^2$. To achieve $\tilde{\alpha}_1 = 1$ (i.e., $\tilde{\xi} = 1$), apply $\tilde{X}_t = cX_t$.

    Then $dX_t = d\tilde{X}_t / c$ and the diffusion of $\tilde{X}_t$ is

    $$
    \tilde{\sigma}(\tilde{X}) = c \cdot \xi\sqrt{X_t} = c\xi\sqrt{\tilde{X}_t/c} = \xi\sqrt{c}\sqrt{\tilde{X}_t}
    $$

    Setting $\xi\sqrt{c} = 1$ gives $c = 1/\xi^2$. The transformation is

    $$
    \tilde{X}_t = \frac{X_t}{\xi^2}
    $$

    The transformed SDE is

    $$
    d\tilde{X}_t = \frac{1}{\xi^2}\bigl[\kappa(\theta - \xi^2\tilde{X}_t)\,dt + \xi\sqrt{\xi^2\tilde{X}_t}\,dW_t\bigr] = \kappa\!\left(\frac{\theta}{\xi^2} - \tilde{X}_t\right)dt + \sqrt{\tilde{X}_t}\,dW_t
    $$

    The canonical parameters are:

    $$
    \tilde{\kappa} = \kappa, \qquad \tilde{\theta} = \frac{\theta}{\xi^2}, \qquad \tilde{\xi} = 1
    $$

    The canonical CIR model has only two free parameters ($\tilde{\kappa}$ and $\tilde{\theta}$) instead of three, reflecting the one degree of freedom removed by the scaling transformation.

---

**Exercise 5.** For the $A_1(2)$ model (one CIR, one Gaussian), the Dai-Singleton canonical form fixes certain entries of the drift matrix $B$ and the diffusion matrices. List the normalization constraints and count the remaining free parameters. Compare this to the number of parameters in the most general unconstrained $A_1(2)$ specification.

??? success "Solution to Exercise 5"
    The $A_1(2)$ model has state $(V_t, Y_t) \in \mathbb{R}_+ \times \mathbb{R}$ with one CIR component and one Gaussian component. The full parameter set is:

    - Drift: $b_0 \in \mathbb{R}^2$ (2), $B \in \mathbb{R}^{2 \times 2}$ (4)
    - Diffusion: $a_0 \in \mathbb{S}^2_+$ with $(a_0)_{11} = 0$ by admissibility (2 free: $(a_0)_{12}$, $(a_0)_{22}$), $\alpha_1 \in \mathbb{S}^2_+$ (3), $\alpha_2 = 0$ by A3 (0)
    - Short rate: $\rho_0$ (1), $\rho_1 \in \mathbb{R}^2$ (2)

    Accounting for additional admissibility constraints ($(a_0)_{11} = 0$ forces $(a_0)_{12} = 0$ for positive semi-definiteness unless more structure is present), the unconstrained count is approximately $2 + 4 + 2 + 3 + 1 + 2 = 14$.

    The Dai-Singleton canonical form imposes the following normalization constraints:

    1. $(\alpha_1)_{11} = 1$ (unit CIR diffusion)
    2. $(a_0)_{22} = 1$ (unit Gaussian diffusion)
    3. $(b_0)_2 = 0$ (center the Gaussian component)
    4. $\rho_1^{(1)} = 1$ (unit loading of CIR factor on short rate)
    5. Additional constraints on $B$ to remove rotational freedom

    These 6 constraints ($= d^2 + d = 4 + 2$) reduce the parameter space to approximately $14 - 6 = 8$ free parameters. The most general unconstrained $A_1(2)$ specification has 14 parameters (before admissibility), so the canonical form achieves a significant reduction, with all remaining parameters being economically meaningful and statistically identifiable.

---

**Exercise 6.** Explain why the identification problem is more severe for affine term structure models (where only bond prices are observed) than for models where the state vector itself is observed. How does the canonical representation help in maximum likelihood estimation of affine term structure models?

??? success "Solution to Exercise 6"
    **Why the identification problem is more severe for term structure models:**

    When the state vector $X_t$ is directly observed (e.g., in a physical sciences application), different parametrizations produce different state trajectories, so the likelihood function distinguishes them. The transformation $\tilde{X}_t = CX_t + c$ changes the observed data, breaking the observational equivalence.

    In affine term structure models, the state vector $X_t$ is **latent** (unobserved). Only bond prices $P(t,T) = e^{A(\tau) + B(\tau)^\top X_t}$ or yields $y(t,T) = -A(\tau)/\tau - B(\tau)^\top X_t/\tau$ are observed. As shown in Exercise 3, the transformation $\tilde{X}_t = CX_t + c$ changes the state representation but preserves all bond prices identically. Therefore, the likelihood of observed bond prices is **identical** for any two parameter sets related by an affine state transformation. The likelihood surface has ridges of constant value along the orbits of the transformation group, making optimization ill-conditioned or impossible without normalization.

    **How the canonical representation helps:** The canonical form selects exactly one representative from each equivalence class of observationally indistinguishable models. This eliminates the ridges in the likelihood surface, making the optimization problem well-posed. In maximum likelihood estimation, the canonical constraints are imposed as hard constraints, reducing the parameter space to the minimal set of identifiable parameters. The resulting estimates are unique (up to the usual statistical uncertainty), and standard errors, confidence intervals, and likelihood ratio tests are meaningful because each point in the canonical parameter space corresponds to a distinct distribution of observables.
