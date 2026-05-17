# Definition of Affine Process

An affine process is a class of stochastic processes with particularly tractable properties. Their defining characteristic is that both the drift and diffusion matrix are linear in the state variable, and the short rate is linear in the state.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Understand the definition and key properties of affine processes
    2. Recognize when a process is affine
    3. Apply the Duffie-Pan-Singleton framework to model interest rates
    4. Work with the characteristic function of affine processes

---

## Overview

Affine processes form a class of continuous-time stochastic processes that are particularly important in financial mathematics, especially for term structure modeling. Their tractability comes from a linearity structure that allows for closed-form or semi-closed-form solutions for bond prices and derivatives.

---

## Mathematical Framework

### Definition of an Affine Process

A state vector $\mathbf{X}_t \in \mathbb{R}^n$ follows an affine process if its dynamics under a risk-neutral measure $\mathbb{Q}$ are:

$$
d\mathbf{X}_t = \bar{\mu}(\mathbf{X}_t)dt + \bar{\sigma}(\mathbf{X}_t)d\mathbf{W}_t
$$

and satisfy the following **linearity conditions**:

$$
\begin{array}{lll}
\displaystyle \bar{\mu}(\mathbf{X}_t) = a_0 + a_1 \mathbf{X}_t & \quad & \text{(Drift is linear in } \mathbf{X}_t\text{)}\\
\displaystyle \bar{\sigma}(\mathbf{X}_t)\bar{\sigma}(\mathbf{X}_t)^T = c_0 + c_1^T \mathbf{X}_t & \quad & \text{(Diffusion is linear in } \mathbf{X}_t\text{)}\\
\displaystyle r(\mathbf{X}_t) = r_0 + r_1^T \mathbf{X}_t & \quad & \text{(Short rate is linear in } \mathbf{X}_t\text{)}\\
\end{array}
$$

where:

- $a_0 \in \mathbb{R}^n$ and $a_1 \in \mathbb{R}^{n \times n}$ are constant matrices for the drift
- $c_0 \in \mathbb{R}^{n \times n}$ and $c_1 \in \mathbb{R}^{n \times n}$ define the volatility structure
- $r_0 \in \mathbb{R}$ and $r_1 \in \mathbb{R}^n$ define the short rate

### Characteristic Function and Bond Pricing (Preview)

Recall (see [§ Characteristic Function of Affine Processes](../characteristic_function/characteristic_function.md) and [§ Generalized Riccati ODEs](../characteristic_function/generalized_riccati_odes.md)): the affine structure guarantees that the discounted characteristic function takes the exponential-affine form $\varphi(\mathbf{X}_t,t,T,\mathbf{u}) = e^{A(\tau,\mathbf{u}) + \mathbf{B}(\tau,\mathbf{u})^T\mathbf{X}_t}$ where $A$ and $\mathbf{B}$ satisfy a system of Riccati ODEs with terminal data $A(0,\mathbf{u})=0$, $\mathbf{B}(0,\mathbf{u})=\mathbf{u}$. The full derivation and explicit ODE form is given in those sections; setting $\mathbf{u}=\mathbf{0}$ recovers the zero-coupon bond price as developed in [§ Exponential-Affine Bond Price Formula](../affine_term_structure/exponential_affine_bond_price.md).

---

## Key Properties

Recall (see [§ Exponential-Affine Bond Price Formula](../affine_term_structure/exponential_affine_bond_price.md) and [§ Characteristic Function of Affine Processes](../characteristic_function/characteristic_function.md)): the linearity conditions deliver four practical payoffs — closed-form exponential-affine bond prices once the Riccati system is solved, analytical or semi-analytical solvability (analytic for Vasicek/Hull-White, semi-analytic or numerical otherwise), an explicit characteristic function enabling Fourier-based option pricing, and state-space flexibility accommodating multiple factors, regime switching, and jumps (see [§ Affine Jump-Diffusions](../extensions/boundary_behavior_feller.md)).

---

## Examples of Affine Processes

Recall (see [§ Vasicek and CIR as Affine](../examples/vasicek_cir_as_affine.md), [§ Heston Model as Affine](../examples/heston_as_affine.md), and [§ GBM and Log-Price](../examples/gbm_as_affine.md)): Vasicek and CIR are one-factor affine short-rate models, Heston is a two-factor affine stochastic-volatility model, and $\log S_t$ is affine even though $S_t$ itself is not. Full parameter identification, Riccati closed forms, and bond/option-price consequences are developed there.

---

## Summary

An affine process is defined by linearity of:

- Drift in the state variable
- Diffusion matrix in the state variable
- Short rate in the state variable

This structure guarantees that the characteristic function (and hence bond prices) have a closed-form exponential-affine structure, leading to tractable analytical and numerical methods. The Duffie-Pan-Singleton framework provides the theoretical foundation for both single and multi-factor affine term structure models.

---

## Further Reading

- Duffie, D., Pan, J., & Singleton, K. (2000). "Transform Analysis and Asset Pricing for Affine Jump-Diffusions." *Econometrica*, 68(6), 1343-1376.
- Filipović, D. *Term-Structure Models: A Graduate Course*. Springer, 2009.
- Brigo, D., & Mercurio, F. *Interest Rate Models - Theory and Practice*. Springer, 2007.

---

## Exercises

**Exercise 1.** Consider a one-dimensional process $X_t$ with dynamics $dX_t = (\alpha + \beta X_t)\,dt + \sqrt{\gamma + \delta X_t}\,dW_t$. Identify the affine parameters $a_0, a_1, c_0, c_1$ and state the conditions on $\alpha, \beta, \gamma, \delta$ that ensure the process is well-defined on $\mathbb{R}_{\geq 0}$.

??? success "Solution to Exercise 1"
    The process $dX_t = (\alpha + \beta X_t)\,dt + \sqrt{\gamma + \delta X_t}\,dW_t$ has diffusion coefficient $(\bar{\sigma}\bar{\sigma}^T)(X_t) = \gamma + \delta X_t$. Comparing with the affine form:

    - **Drift**: $\bar{\mu}(X_t) = \alpha + \beta X_t$, so $a_0 = \alpha$ and $a_1 = \beta$
    - **Diffusion**: $\bar{\sigma}\bar{\sigma}^T(X_t) = \gamma + \delta X_t$, so $c_0 = \gamma$ and $c_1 = \delta$

    For the process to be well-defined on $\mathbb{R}_{\geq 0}$, we need:

    1. **Non-negative diffusion**: $\gamma + \delta x \geq 0$ for all $x \geq 0$. This requires $\gamma \geq 0$ and $\delta \geq 0$.
    2. **Drift inward at the boundary**: When $X_t = 0$, the drift must be non-negative to prevent the process from going negative. This requires $\alpha \geq 0$.
    3. **Feller condition** (to ensure the boundary at zero is unattainable or instantly reflecting): $2\alpha \geq \gamma$. When $\gamma = 0$ and $\delta > 0$, this reduces to the standard CIR condition $2\alpha \geq 0$, which is automatic from condition 2.

    There is no sign restriction on $\beta$; negative $\beta$ provides mean reversion.

---

**Exercise 2.** Starting from the Riccati system

$$
\frac{dA}{d\tau} = -r_0 + B\,a_0 + \tfrac{1}{2}B^2\,c_0, \qquad \frac{dB}{d\tau} = -r_1 + a_1 B + \tfrac{1}{2}c_1 B^2
$$

with terminal conditions $A(0) = 0$ and $B(0) = 0$, solve explicitly for $A(\tau)$ and $B(\tau)$ in the Vasicek model where $a_0 = \kappa\theta$, $a_1 = -\kappa$, $c_0 = \sigma^2$, $c_1 = 0$, $r_0 = 0$, $r_1 = 1$.

??? success "Solution to Exercise 2"
    In the Vasicek model the Riccati equation for $B$ (with $c_1 = 0$, $r_1 = 1$, $a_1 = -\kappa$) is:

    $$
    \frac{dB}{d\tau} = -1 + (-\kappa)B = -1 - \kappa B, \qquad B(0) = 0
    $$

    This is a first-order linear ODE. Solving by the integrating factor $e^{\kappa\tau}$:

    $$
    \frac{d}{d\tau}(e^{\kappa\tau} B) = -e^{\kappa\tau}
    $$

    Integrating from $0$ to $\tau$:

    $$
    e^{\kappa\tau} B(\tau) = -\frac{1}{\kappa}(e^{\kappa\tau} - 1)
    $$

    $$
    B(\tau) = -\frac{1}{\kappa}(1 - e^{-\kappa\tau})
    $$

    For $A(\tau)$, with $r_0 = 0$, $a_0 = \kappa\theta$, $c_0 = \sigma^2$:

    $$
    \frac{dA}{d\tau} = B(\tau)\,\kappa\theta + \frac{1}{2}\sigma^2 B(\tau)^2
    $$

    Substituting $B(\tau) = -\frac{1}{\kappa}(1 - e^{-\kappa\tau})$:

    $$
    \frac{dA}{d\tau} = -\theta(1 - e^{-\kappa\tau}) + \frac{\sigma^2}{2\kappa^2}(1 - e^{-\kappa\tau})^2
    $$

    Integrating term by term with $A(0) = 0$:

    $$
    A(\tau) = -\theta\left[\tau - \frac{1}{\kappa}(1 - e^{-\kappa\tau})\right] + \frac{\sigma^2}{2\kappa^2}\left[\tau - \frac{2}{\kappa}(1 - e^{-\kappa\tau}) + \frac{1}{2\kappa}(1 - e^{-2\kappa\tau})\right]
    $$

    Defining $\bar{B}(\tau) = \frac{1}{\kappa}(1-e^{-\kappa\tau})$ so that $B(\tau)=-\bar{B}(\tau)$, this can be written more compactly as:

    $$
    A(\tau) = (\bar{B}(\tau) - \tau)\left(\theta - \frac{\sigma^2}{2\kappa^2}\right) - \frac{\sigma^2}{4\kappa}\bar{B}(\tau)^2
    $$

---

**Exercise 3.** Verify that the zero-coupon bond price $P(t,T) = e^{A(\tau) + B(\tau)\,r_t}$ in the Vasicek model satisfies the fundamental PDE

$$
\frac{\partial P}{\partial t} + \kappa(\theta - r)\frac{\partial P}{\partial r} + \frac{1}{2}\sigma^2\frac{\partial^2 P}{\partial r^2} - rP = 0
$$

by computing the partial derivatives and substituting.

??? success "Solution to Exercise 3"
    Let $P(t,T) = e^{A(\tau) + B(\tau)r_t}$ with $\tau = T - t$. Compute the partial derivatives:

    $$
    \frac{\partial P}{\partial t} = \left(-A'(\tau) - B'(\tau)r_t\right)P
    $$

    $$
    \frac{\partial P}{\partial r} = B(\tau)P, \qquad \frac{\partial^2 P}{\partial r^2} = B(\tau)^2 P
    $$

    Substituting into the PDE and dividing by $P$:

    $$
    -A'(\tau) - B'(\tau)r_t + \kappa(\theta - r)B(\tau) + \frac{1}{2}\sigma^2 B(\tau)^2 - r = 0
    $$

    Collecting constant terms and terms proportional to $r$:

    **Terms independent of $r$**:

    $$
    -A'(\tau) + \kappa\theta B(\tau) + \frac{1}{2}\sigma^2 B(\tau)^2 = 0
    $$

    **Terms proportional to $r$**:

    $$
    -B'(\tau) - \kappa B(\tau) - 1 = 0
    $$

    The second equation gives $B'(\tau) = -1 - \kappa B(\tau)$, and the first gives $A'(\tau) = \kappa\theta B(\tau) + \frac{1}{2}\sigma^2 B(\tau)^2$. These are exactly the Riccati equations derived in Exercise 2 (with the sign convention $\frac{d}{d\tau}$ since $\tau = T - t$ and $\frac{\partial}{\partial t} = -\frac{d}{d\tau}$). Since $A(\tau)$ and $B(\tau)$ were obtained as solutions of these ODEs, the PDE is satisfied identically.

---

**Exercise 4.** Let $\mathbf{X}_t = (X_t^{(1)}, X_t^{(2)})^T$ be a two-factor affine process with independent components, each following a Vasicek process with parameters $(\kappa_i, \theta_i, \sigma_i)$ for $i=1,2$. Suppose the short rate is $r_t = X_t^{(1)} + X_t^{(2)}$. Write down the matrices $a_0, a_1, c_0, c_1$ and vectors $r_0, r_1$ for this model, and explain why the Riccati system decouples into two independent scalar ODEs.

??? success "Solution to Exercise 4"
    With two independent Vasicek components and $r_t = X_t^{(1)} + X_t^{(2)}$, the state vector is $\mathbf{X}_t = (X_t^{(1)}, X_t^{(2)})^T$. The affine parameters are:

    $$
    a_0 = \begin{pmatrix} \kappa_1\theta_1 \\ \kappa_2\theta_2 \end{pmatrix}, \qquad a_1 = \begin{pmatrix} -\kappa_1 & 0 \\ 0 & -\kappa_2 \end{pmatrix}
    $$

    $$
    c_0 = \begin{pmatrix} \sigma_1^2 & 0 \\ 0 & \sigma_2^2 \end{pmatrix}, \qquad c_1 = 0 \quad (\text{no state-dependent volatility})
    $$

    $$
    r_0 = 0, \qquad r_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}
    $$

    Since $c_1 = 0$, the Riccati equation for $\mathbf{B} = (B_1, B_2)^T$ is:

    $$
    \frac{d\mathbf{B}}{d\tau} = -r_1 + a_1^T \mathbf{B} = -\begin{pmatrix}1\\1\end{pmatrix} + \begin{pmatrix}-\kappa_1 & 0 \\ 0 & -\kappa_2\end{pmatrix}\begin{pmatrix}B_1\\B_2\end{pmatrix}
    $$

    This gives two independent scalar ODEs:

    $$
    B_1'(\tau) = -1 - \kappa_1 B_1(\tau), \qquad B_2'(\tau) = -1 - \kappa_2 B_2(\tau)
    $$

    The system decouples because $a_1$ is diagonal (the components are independent) and $c_1 = 0$ (no quadratic coupling term $\mathbf{B}^T c_1 \mathbf{B}$). Each ODE is identical in form to the single-factor Vasicek Riccati equation, so $B_i(\tau) = -\frac{1}{\kappa_i}(1 - e^{-\kappa_i\tau})$. The equation for $A(\tau)$ then integrates as $A'(\tau) = \mathbf{B}^T a_0 + \frac{1}{2}\mathbf{B}^T c_0 \mathbf{B}$, which is a sum of terms involving $B_1$ and $B_2$ separately.

---

**Exercise 5.** Explain why a geometric Brownian motion $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ is not itself an affine process, but the log-price $X_t = \log S_t$ is. Write down the affine parameters for $X_t$ and compute the characteristic function $\mathbb{E}[e^{iuX_T} \mid X_t]$ in closed form.

??? success "Solution to Exercise 5"
    **GBM is not affine in $S_t$**: The dynamics $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ have drift $\bar{\mu}(S) = \mu S$ and diffusion $\bar{\sigma}\bar{\sigma}^T(S) = \sigma^2 S^2$. For the process to be affine, the diffusion must be linear in $S$, i.e., of the form $c_0 + c_1 S$. But $\sigma^2 S^2$ is quadratic in $S$, so the linearity condition fails.

    **Log-price $X_t = \log S_t$ is affine**: By Ito's lemma:

    $$
    dX_t = \left(\mu - \frac{\sigma^2}{2}\right)dt + \sigma\,dW_t
    $$

    The affine parameters are:

    - $a_0 = \mu - \frac{\sigma^2}{2}$, $a_1 = 0$ (constant drift)
    - $c_0 = \sigma^2$, $c_1 = 0$ (constant diffusion)

    Since both drift and diffusion are constant (hence trivially linear in $X_t$), the process is affine.

    **Characteristic function**: The Riccati system with $a_1 = 0$ and $c_1 = 0$ gives:

    $$
    \psi'(\tau) = 0 \implies \psi(\tau) = iu
    $$

    $$
    \phi'(\tau) = a_0 \cdot iu + \frac{1}{2}c_0(iu)^2 = i\left(\mu - \frac{\sigma^2}{2}\right)u - \frac{\sigma^2 u^2}{2}
    $$

    Integrating with $\phi(0) = 0$:

    $$
    \phi(\tau) = i\left(\mu - \frac{\sigma^2}{2}\right)u\tau - \frac{\sigma^2 u^2}{2}\tau
    $$

    Therefore:

    $$
    \mathbb{E}[e^{iuX_T} \mid X_t = x] = \exp\!\left(i\left(\mu - \frac{\sigma^2}{2}\right)u\tau - \frac{\sigma^2 u^2}{2}\tau + iux\right)
    $$

    where $\tau = T - t$. This confirms that $X_T \mid X_t = x$ is Gaussian with mean $x + (\mu - \sigma^2/2)\tau$ and variance $\sigma^2\tau$.

---

**Exercise 6.** Consider the CIR process $dX_t = \kappa(\theta - X_t)\,dt + \sigma\sqrt{X_t}\,dW_t$. Identify the affine parameters and write down the Riccati ODE for $B(\tau)$. Show that the ODE for $B$ is a scalar Riccati equation and determine the discriminant $\Delta = \kappa^2 + 2\sigma^2$ that governs the solution structure.

??? success "Solution to Exercise 6"
    The CIR process $dX_t = \kappa(\theta - X_t)\,dt + \sigma\sqrt{X_t}\,dW_t$ has affine parameters:

    - $a_0 = \kappa\theta$, $a_1 = -\kappa$ (drift)
    - $c_0 = 0$, $c_1 = \sigma^2$ (diffusion)
    - $r_0 = 0$, $r_1 = 1$ (if used for short rate)

    The Riccati ODE for $B(\tau)$ (with $\mathbf{u} = 0$ in the bond pricing case) is:

    $$
    \frac{dB}{d\tau} = -1 - \kappa B + \frac{1}{2}\sigma^2 B^2, \qquad B(0) = 0
    $$

    This is a scalar Riccati equation (quadratic in $B$) because $c_1 = \sigma^2 \neq 0$.

    To find the discriminant, write the ODE in standard form $B' = \frac{1}{2}\sigma^2 B^2 - \kappa B - 1$. The steady states satisfy:

    $$
    \frac{1}{2}\sigma^2 B^2 - \kappa B - 1 = 0
    $$

    By the quadratic formula:

    $$
    B = \frac{\kappa \pm \sqrt{\kappa^2 + 2\sigma^2}}{\sigma^2}
    $$

    The discriminant is:

    $$
    \Delta = \kappa^2 + 2\sigma^2
    $$

    Since $\kappa^2 \geq 0$ and $\sigma^2 > 0$, we have $\Delta > 0$, so the Riccati equation always has two distinct real equilibria. Defining $\gamma = \sqrt{\Delta} = \sqrt{\kappa^2 + 2\sigma^2}$, the solution can be expressed using hyperbolic functions:

    $$
    B(\tau) = \frac{-2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}
    $$

    The sign and structure of $\Delta$ determine that $B(\tau) < 0$ for all $\tau > 0$, consistent with the economic intuition that higher short rates decrease bond prices.

---

**Exercise 7.** Suppose you observe zero-coupon bond prices $P(0, T_i)$ for maturities $T_1, T_2, \ldots, T_m$ and wish to calibrate a one-factor affine model. Describe how the exponential-affine form $P(0, T_i) = e^{A(T_i) + B(T_i) X_0}$ can be used to set up a nonlinear least-squares problem. What parameters need to be estimated, and what is the role of the Riccati equations in this procedure?

??? success "Solution to Exercise 7"
    The exponential-affine form gives, for each observed maturity $T_i$:

    $$
    P(0, T_i) = e^{A(T_i) + B(T_i)X_0}
    $$

    Taking logarithms:

    $$
    \log P(0, T_i) = A(T_i) + B(T_i)X_0
    $$

    The functions $A(T_i)$ and $B(T_i)$ depend on the model parameters $\boldsymbol{\theta} = (\kappa, \theta, \sigma, \ldots)$ through the Riccati equations, and $X_0$ is the (unobserved) initial state.

    **Nonlinear least-squares formulation**: Given observed market prices $P^{\text{mkt}}(0, T_i)$ for $i = 1, \ldots, m$, minimize:

    $$
    \min_{\boldsymbol{\theta}, X_0} \sum_{i=1}^{m} \left(\log P^{\text{mkt}}(0, T_i) - A(T_i; \boldsymbol{\theta}) - B(T_i; \boldsymbol{\theta})X_0\right)^2
    $$

    **Parameters to estimate**: The model parameters $\boldsymbol{\theta}$ (e.g., $\kappa, \theta, \sigma$ for Vasicek or CIR) and the initial state $X_0$.

    **Role of the Riccati equations**: At each iteration of the optimization, the Riccati ODEs must be solved to compute $A(T_i; \boldsymbol{\theta})$ and $B(T_i; \boldsymbol{\theta})$ for the current parameter guess. For models like Vasicek, these have closed-form solutions, so the objective function can be evaluated analytically. For more complex models (e.g., multi-factor CIR), the Riccati equations may need to be solved numerically at each optimization step. The problem is nonlinear because $A$ and $B$ depend nonlinearly on $\boldsymbol{\theta}$, even though the bond price formula is linear in $X_0$.
