# State Space and Regularity

Affine processes live on carefully structured state spaces that encode the positivity constraints required by financial models---non-negative variance, non-negative interest rates, and non-negative default intensities. This section develops the canonical state space, the regularity conditions that ensure well-posedness, and the stochastic continuity property that underpins the entire affine framework.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Describe the canonical state space $D = \mathbb{R}^m_+ \times \mathbb{R}^{d-m}$ and explain why non-negative components are essential
    2. State the admissibility conditions on drift, diffusion, and jump coefficients
    3. Define stochastic continuity and relate it to the Feller property
    4. Explain the role of the affine semigroup in preserving exponential-affine structure

---

## Intuition

In financial applications, many state variables must remain non-negative: the variance process in the Heston model, the short rate in the CIR model, and default intensities in credit risk models. At the same time, other state variables---such as the log stock price or a Gaussian factor---are free to take any real value. The canonical state space for affine processes formalizes this distinction by splitting the state into two groups: $m$ components constrained to $[0, \infty)$ and $d - m$ unconstrained components on $(-\infty, \infty)$.

This split is not merely a convenience. The non-negative components drive stochastic volatility through square-root diffusion terms, and the regularity conditions we impose ensure that these components never become negative. Without these conditions, the model would be mathematically ill-posed and financially meaningless.

---

## The Canonical State Space

### Definition

**Definition (Canonical State Space).** Let $d \geq 1$ and $0 \leq m \leq d$. The canonical state space for a $d$-dimensional affine process is

$$
D = \mathbb{R}^m_+ \times \mathbb{R}^{d-m}
$$

where $\mathbb{R}_+ = [0, \infty)$. A generic element $x \in D$ is written as $x = (x_I, x_{II})$ with $x_I = (x_1, \ldots, x_m) \in \mathbb{R}^m_+$ and $x_{II} = (x_{m+1}, \ldots, x_d) \in \mathbb{R}^{d-m}$.

The integer $m$ counts the number of **CIR-type components**---those that are non-negative and can drive state-dependent volatility. The remaining $d - m$ components are **Gaussian-type**, free to take any real value.

### The Boundary Structure

The boundary of the state space plays a central role. The boundary $\partial D$ consists of points where at least one of the first $m$ components equals zero:

$$
\partial D = \{x \in D : x_i = 0 \text{ for some } i \in \{1, \ldots, m\}\}
$$

At the boundary, the diffusion coefficient of the corresponding CIR-type component vanishes (since it is proportional to $x_i$), and the drift must push the process back into the interior. This is the multidimensional generalization of the Feller boundary condition.

### Financial Interpretation

The table below summarizes common financial models and their state space structure:

| Model | State Space $D$ | $m$ | $d$ | CIR Components | Gaussian Components |
|-------|-----------------|-----|-----|-----------------|---------------------|
| Vasicek | $\mathbb{R}$ | 0 | 1 | None | Short rate $r_t$ |
| CIR | $\mathbb{R}_+$ | 1 | 1 | Short rate $r_t$ | None |
| Heston | $\mathbb{R}_+ \times \mathbb{R}$ | 1 | 2 | Variance $V_t$ | Log-price $\log S_t$ |
| Two-factor CIR | $\mathbb{R}^2_+$ | 2 | 2 | Both factors | None |

---

## Affine Coefficient Structure

### The Admissibility Framework

An affine process $X = (X_t)_{t \geq 0}$ on $D$ has drift, diffusion, and jump characteristics that are affine (linear plus constant) in the state variable. Specifically, the coefficients take the form:

$$
b(x) = b_0 + \sum_{i=1}^{d} b_i x_i, \qquad a(x) = a_0 + \sum_{i=1}^{d} a_i x_i
$$

where $b_0 \in \mathbb{R}^d$, $b_i \in \mathbb{R}^d$, $a_0 \in \mathbb{S}^d_+$ (the cone of positive semidefinite $d \times d$ matrices), and $a_i \in \mathbb{S}^d_+$ for each $i$. The jump measure has the analogous affine structure:

$$
m(x, dz) = m_0(dz) + \sum_{i=1}^{d} x_i \, m_i(dz)
$$

where $m_0, m_1, \ldots, m_d$ are Levy measures on $D \setminus \{0\}$.

### Admissibility Conditions

Not every choice of parameters $(b_0, b_i, a_0, a_i, m_0, m_i)$ produces a valid affine process on $D$. The following conditions are necessary and sufficient for the process to remain in $D$.

**Definition (Admissible Parameters).** The parameter set $(b_0, b_i, a_0, a_i, m_0, m_i)$ is *admissible* for the state space $D = \mathbb{R}^m_+ \times \mathbb{R}^{d-m}$ if:

**(A1) Drift inward at the boundary.** For each CIR-type component $i \in \{1, \ldots, m\}$:

$$
(b_0)_i \geq 0
$$

This ensures that when $x_i = 0$, the drift in the $i$-th direction is non-negative, pushing the process back into the interior.

**(A2) Diffusion vanishes at the boundary.** For each CIR-type component $i \in \{1, \ldots, m\}$, only the $i$-th state variable may contribute to the diffusion of component $i$. Formally:

$$
(a_0)_{ii} = 0, \qquad (a_j)_{ii} = 0 \quad \text{for all } j \neq i, \; j \in \{1, \ldots, m\}
$$

The only nonzero contribution to $(a(x))_{ii}$ for a CIR-type component $i$ comes from $x_i$ itself through $(a_i)_{ii} \geq 0$.

**(A3) Jumps preserve the state space.** Each Levy measure $m_i$ is supported on $D - e_i$, where $e_i$ is the $i$-th standard basis vector, ensuring that jumps do not take the process outside $D$.

**(A4) Integrability of jumps.** For each $i \in \{0, 1, \ldots, d\}$:

$$
\int_{D \setminus \{0\}} (\|z\| \wedge 1) \, m_i(dz) < \infty
$$

??? example "Admissibility Check for the CIR Process"
    The CIR process $dr_t = \kappa(\theta - r_t)\,dt + \xi\sqrt{r_t}\,dW_t$ lives on $D = \mathbb{R}_+$ with $m = d = 1$. The parameters are:

    - $b_0 = \kappa\theta$, $b_1 = -\kappa$
    - $a_0 = 0$, $a_1 = \xi^2$
    - No jumps: $m_0 = m_1 = 0$

    Checking **(A1)**: $(b_0)_1 = \kappa\theta \geq 0$ since $\kappa > 0$ and $\theta > 0$. The drift at $r = 0$ equals $\kappa\theta > 0$, pushing the process upward.

    Checking **(A2)**: $(a_0)_{11} = 0$, so the diffusion vanishes at $r = 0$. The state-dependent part $(a_1)_{11} = \xi^2 > 0$ contributes $\xi^2 r_t$, giving diffusion coefficient $\xi\sqrt{r_t}$ that vanishes at the boundary.

    All admissibility conditions are satisfied. $\square$

---

## Stochastic Continuity

### Motivation

A Markov process can, in principle, have deterministic jumps---the process could teleport from one state to another at a fixed time. Stochastic continuity rules out this pathological behavior, requiring that the transition probabilities vary continuously in time. This is a weaker condition than path continuity (sample paths can still jump), but it is strong enough to guarantee the existence of a well-defined infinitesimal generator.

### Definition

**Definition (Stochastic Continuity).** A Markov process $(X_t)_{t \geq 0}$ with state space $D$ is *stochastically continuous* if for every $x \in D$ and every $\varepsilon > 0$:

$$
\lim_{t \to 0} \mathbb{P}^x\!\left(\|X_t - x\| > \varepsilon\right) = 0
$$

Equivalently, $X_t \to X_0 = x$ in probability as $t \to 0$ under $\mathbb{P}^x$.

Stochastic continuity is strictly weaker than almost-sure path continuity. A compound Poisson process, for example, is stochastically continuous (the probability of a jump in a small interval $[0, t]$ tends to zero as $t \to 0$), even though its paths are discontinuous.

### Stochastic Continuity and the Feller Property

For affine processes, stochastic continuity is closely related to the Feller property of the transition semigroup.

**Proposition (Stochastic Continuity Implies Feller).** Let $X$ be an affine process on $D$ with transition semigroup $(P_t)_{t \geq 0}$. If $X$ is stochastically continuous, then the semigroup $(P_t)$ restricted to the space of continuous functions vanishing at infinity, $C_0(D)$, is a Feller semigroup: for every $f \in C_0(D)$,

$$
\lim_{t \to 0} \|P_t f - f\|_\infty = 0
$$

*Proof sketch.* Fix $f \in C_0(D)$ and $\varepsilon > 0$. Since $f$ vanishes at infinity, there exists a compact set $K$ such that $|f(y)| < \varepsilon$ for $y \notin K$. For $x \in D$:

$$
|P_t f(x) - f(x)| = \left|\mathbb{E}^x[f(X_t)] - f(x)\right| \leq \mathbb{E}^x\!\left[|f(X_t) - f(x)|\right]
$$

Split the expectation over $\{\|X_t - x\| \leq \delta\}$ and its complement. On the first event, uniform continuity of $f$ on compact sets gives $|f(X_t) - f(x)| < \varepsilon$ for small $\delta$. On the complement, stochastic continuity ensures the probability is less than $\varepsilon$ for small $t$. The bound $|P_t f(x) - f(x)| \leq \varepsilon + 2\|f\|_\infty \cdot \varepsilon$ follows, and since $\varepsilon$ is arbitrary, the claim holds. $\square$

---

## The Affine Semigroup

### Transition Semigroup and Exponential-Affine Structure

The transition semigroup $(P_t)_{t \geq 0}$ of a Markov process is defined by

$$
P_t f(x) = \mathbb{E}^x[f(X_t)]
$$

For an affine process, the key structural property is that exponential-affine functions are mapped to exponential-affine functions. Specifically, for $u \in \mathbb{C}^d$ in the appropriate domain:

$$
P_t\!\left(e^{\langle u, \cdot \rangle}\right)(x) = \mathbb{E}^x\!\left[e^{\langle u, X_t \rangle}\right] = \exp\!\left(\phi(t, u) + \langle \psi(t, u), x \rangle\right)
$$

where $\phi : \mathbb{R}_+ \times \mathbb{C}^d \to \mathbb{C}$ and $\psi : \mathbb{R}_+ \times \mathbb{C}^d \to \mathbb{C}^d$ satisfy:

- **Initial conditions**: $\phi(0, u) = 0$ and $\psi(0, u) = u$
- **Semiflow property**: $\phi(t+s, u) = \phi(t, \psi(s, u)) + \phi(s, u)$ and $\psi(t+s, u) = \psi(t, \psi(s, u))$

The semiflow property follows from the Chapman-Kolmogorov equation (the semigroup property $P_{t+s} = P_t P_s$) applied to exponential functions.

### The Semiflow Property

**Proposition (Semiflow).** The functions $\phi$ and $\psi$ satisfy the semiflow equations:

$$
\phi(t+s, u) = \phi(t, \psi(s, u)) + \phi(s, u)
$$

$$
\psi(t+s, u) = \psi(t, \psi(s, u))
$$

*Proof.* By the Markov property and the tower law of conditional expectation:

$$
\mathbb{E}^x\!\left[e^{\langle u, X_{t+s} \rangle}\right] = \mathbb{E}^x\!\left[\mathbb{E}^{X_s}\!\left[e^{\langle u, X_t \rangle}\right]\right]
$$

The inner expectation, by the affine property, equals $\exp(\phi(t, u) + \langle \psi(t, u), X_s \rangle)$. Taking the outer expectation:

$$
\mathbb{E}^x\!\left[\exp\!\left(\phi(t, u) + \langle \psi(t, u), X_s \rangle\right)\right] = e^{\phi(t, u)} \cdot \mathbb{E}^x\!\left[e^{\langle \psi(t, u), X_s \rangle}\right]
$$

Applying the affine property again with argument $\psi(t, u)$:

$$
= e^{\phi(t, u)} \cdot \exp\!\left(\phi(s, \psi(t, u)) + \langle \psi(s, \psi(t, u)), x \rangle\right)
$$

Comparing with $\exp(\phi(t+s, u) + \langle \psi(t+s, u), x \rangle)$ and matching the constant and linear-in-$x$ terms gives the semiflow equations. $\square$

---

## Regularity of the Affine Semigroup

### From Stochastic Continuity to Differentiability

Stochastic continuity of the process guarantees that the functions $\phi(t, u)$ and $\psi(t, u)$ are continuous in $t$. Under the admissibility conditions, one can strengthen this to differentiability, which leads to the Riccati ODE system.

**Theorem (Regularity, Duffie-Filipovic-Schachermayer 2003).** Let $X$ be a stochastically continuous affine process on $D = \mathbb{R}^m_+ \times \mathbb{R}^{d-m}$ with admissible parameters. Then:

1. The functions $t \mapsto \phi(t, u)$ and $t \mapsto \psi(t, u)$ are differentiable for all $t \geq 0$ and all $u$ in the admissible domain.
2. There exist functions $F : \mathbb{C}^d \to \mathbb{C}$ and $R : \mathbb{C}^d \to \mathbb{C}^d$ such that

$$
\frac{\partial \phi}{\partial t}(t, u) = F(\psi(t, u)), \qquad \frac{\partial \psi}{\partial t}(t, u) = R(\psi(t, u))
$$

3. The functions $F$ and $R$ are determined by the parameters $(b_0, b_i, a_0, a_i, m_0, m_i)$ through

$$
F(u) = \langle b_0, u \rangle + \frac{1}{2}\langle u, a_0 u \rangle + \int_{D \setminus \{0\}} \left(e^{\langle u, z \rangle} - 1\right) m_0(dz)
$$

$$
R_i(u) = \langle b_i, u \rangle + \frac{1}{2}\langle u, a_i u \rangle + \int_{D \setminus \{0\}} \left(e^{\langle u, z \rangle} - 1\right) m_i(dz), \quad i = 1, \ldots, d
$$

This theorem is the foundation of the Riccati ODE approach: once we know $F$ and $R$, we solve the ODEs $\phi' = F(\psi)$ and $\psi' = R(\psi)$ to obtain the characteristic function of the process. The derivation of the Riccati system and its solutions are developed in subsequent sections.

??? example "Regularity Check for the Vasicek Model"
    For the Vasicek model $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$ on $D = \mathbb{R}$ (so $m = 0$, $d = 1$):

    - $b_0 = \kappa\theta$, $b_1 = -\kappa$, $a_0 = \sigma^2$, $a_1 = 0$, no jumps

    The functions $F$ and $R$ are:

    $$
    F(u) = \kappa\theta \cdot u + \frac{1}{2}\sigma^2 u^2
    $$

    $$
    R(u) = -\kappa \cdot u
    $$

    The Riccati system $\psi'(\tau) = R(\psi(\tau)) = -\kappa\psi(\tau)$ with $\psi(0) = u$ gives $\psi(\tau) = u e^{-\kappa\tau}$, and integrating $\phi' = F(\psi)$ yields a closed-form expression in terms of $\tau$. Both $\phi$ and $\psi$ are smooth in $\tau$, confirming the regularity theorem. $\square$

---

## Summary

The state space $D = \mathbb{R}^m_+ \times \mathbb{R}^{d-m}$ partitions the state vector into non-negative CIR-type components and unconstrained Gaussian-type components. Admissibility conditions---inward-pointing drift at the boundary, vanishing diffusion at the boundary, and jump measures preserving the state space---ensure the process remains in $D$. Stochastic continuity guarantees the Feller property of the transition semigroup and, combined with admissibility, the differentiability of $\phi$ and $\psi$ that leads to the Riccati ODE system. The semiflow equations for $\phi$ and $\psi$ encode the Markov and semigroup properties in the exponential-affine setting.

---

## Further Reading

- Duffie, D., Filipovic, D., & Schachermayer, W. (2003). "Affine Processes and Applications in Finance." *Annals of Applied Probability*, 13(3), 984-1053.
- Filipovic, D. *Term-Structure Models: A Graduate Course*. Springer, 2009, Chapter 10.
- Keller-Ressel, M. (2011). "Moment Explosions and Long-Term Behavior of Affine Stochastic Volatility Models." *Mathematical Finance*, 21(1), 73-98.

---

## Exercises

**Exercise 1.** Consider a three-factor affine model with state space $D = \mathbb{R}^2_+ \times \mathbb{R}$. The first two components are CIR-type and the third is Gaussian. Write down the most general admissible drift vector $b(x) = b_0 + b_1 x_1 + b_2 x_2 + b_3 x_3$ specifying which entries of $b_0$ must be non-negative according to condition (A1).

??? success "Solution to Exercise 1"
    The state space is $D = \mathbb{R}^2_+ \times \mathbb{R}$, so $m = 2$ and $d = 3$. The CIR-type components are $x_1$ and $x_2$ (both non-negative), and $x_3$ is Gaussian.

    The drift vector has the general form $b(x) = b_0 + b_1 x_1 + b_2 x_2 + b_3 x_3$, where $b_0, b_1, b_2, b_3 \in \mathbb{R}^3$.

    Condition **(A1)** requires that for each CIR-type component $i \in \{1, 2\}$, we have $(b_0)_i \geq 0$. This ensures that the drift pushes the process away from the boundary when $x_i = 0$. Specifically:

    - $(b_0)_1 \geq 0$: the constant part of the drift in the first component must be non-negative
    - $(b_0)_2 \geq 0$: the constant part of the drift in the second component must be non-negative

    There is **no sign restriction** on $(b_0)_3$, since $x_3$ lives on all of $\mathbb{R}$ and has no boundary to protect.

    For example, in a concrete three-factor model where $x_1$ and $x_2$ are independent CIR processes with parameters $(\kappa_i, \theta_i, \xi_i)$ and $x_3$ is an OU process with parameter $(\kappa_3, \theta_3, \sigma_3)$:

    $$
    b_0 = \begin{pmatrix} \kappa_1\theta_1 \\ \kappa_2\theta_2 \\ \kappa_3\theta_3 \end{pmatrix}
    $$

    Here $(b_0)_1 = \kappa_1\theta_1 \geq 0$ and $(b_0)_2 = \kappa_2\theta_2 \geq 0$ since $\kappa_i > 0$ and $\theta_i > 0$, while $(b_0)_3 = \kappa_3\theta_3$ can be any real number.

---

**Exercise 2.** For the Heston model on $D = \mathbb{R}_+ \times \mathbb{R}$ (variance $V_t$ and log-price $\log S_t$), write down the diffusion matrix $a(x) = a_0 + a_1 x_1$ explicitly. Verify that condition (A2) is satisfied: the $(1,1)$ entry of $a_0$ is zero and the only nonzero contribution to the $(1,1)$ entry comes from $a_1$.

??? success "Solution to Exercise 2"
    In the Heston model, $V_t$ is CIR-type ($x_1 = V_t \in \mathbb{R}_+$) and $\log S_t$ is Gaussian-type ($x_2 = \log S_t \in \mathbb{R}$). The dynamics are:

    $$
    dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^{(1)}
    $$

    $$
    d\log S_t = \left(\mu - \frac{1}{2}V_t\right)dt + \sqrt{V_t}\left(\rho\,dW_t^{(1)} + \sqrt{1-\rho^2}\,dW_t^{(2)}\right)
    $$

    The instantaneous covariance matrix of $(dV_t, d\log S_t)$ is:

    $$
    a(x) = V_t \begin{pmatrix} \xi^2 & \rho\xi \\ \rho\xi & 1 \end{pmatrix}
    $$

    In the affine decomposition $a(x) = a_0 + a_1 x_1$:

    $$
    a_0 = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}, \qquad a_1 = \begin{pmatrix} \xi^2 & \rho\xi \\ \rho\xi & 1 \end{pmatrix}
    $$

    **Checking (A2)**: The $(1,1)$ entry of $a_0$ is $(a_0)_{11} = 0$, as required. The only nonzero contribution to the $(1,1)$ entry of $a(x)$ comes from $a_1$ through the term $(a_1)_{11} \cdot x_1 = \xi^2 V_t$, which vanishes when $V_t = 0$. Condition (A2) is satisfied.

    Note that $a_1$ is positive semidefinite since its determinant is $\xi^2 \cdot 1 - (\rho\xi)^2 = \xi^2(1 - \rho^2) \geq 0$ for $|\rho| \leq 1$.

---

**Exercise 3.** Let $(X_t)_{t \geq 0}$ be a compound Poisson process with jump intensity $\lambda$ and jump sizes distributed as $Z \sim \text{Exp}(1)$ on $\mathbb{R}_+$. Show that $X_t$ is stochastically continuous by computing $\mathbb{P}(\|X_t - X_0\| > \varepsilon)$ and verifying it tends to zero as $t \to 0$. Is this process path-continuous?

??? success "Solution to Exercise 3"
    Let $X_t$ be a compound Poisson process with intensity $\lambda$ and $\text{Exp}(1)$ jump sizes, starting at $X_0 = 0$. Then $X_t = \sum_{k=1}^{N_t} Z_k$ where $N_t \sim \text{Poisson}(\lambda t)$ and $Z_k \sim \text{Exp}(1)$ are i.i.d.

    For $\varepsilon > 0$:

    $$
    \mathbb{P}(\|X_t - X_0\| > \varepsilon) = \mathbb{P}(X_t > \varepsilon) \leq \mathbb{P}(N_t \geq 1) = 1 - e^{-\lambda t}
    $$

    As $t \to 0$:

    $$
    1 - e^{-\lambda t} \to 0
    $$

    Therefore $\mathbb{P}(\|X_t - X_0\| > \varepsilon) \to 0$ as $t \to 0$, confirming stochastic continuity.

    **Path continuity**: The process is **not** path-continuous. The sample paths of a compound Poisson process are piecewise constant with finitely many jumps on any bounded interval. At each jump time, the path has a discontinuity of random size $Z_k > 0$. This illustrates that stochastic continuity (a property of transition probabilities) is strictly weaker than path continuity (a property of sample paths).

---

**Exercise 4.** Prove directly from the semiflow equations

$$
\phi(t+s, u) = \phi(t, \psi(s, u)) + \phi(s, u), \qquad \psi(t+s, u) = \psi(t, \psi(s, u))
$$

that the initial conditions $\phi(0, u) = 0$ and $\psi(0, u) = u$ are the only ones consistent with the semigroup property $P_0 = \text{Id}$.

??? success "Solution to Exercise 4"
    Setting $s = 0$ in the semiflow equations:

    $$
    \psi(t + 0, u) = \psi(t, \psi(0, u)) \implies \psi(t, u) = \psi(t, \psi(0, u))
    $$

    This requires $\psi(0, u) = u$ for all $u$, since $\psi(t, \cdot)$ must act as the identity when composed with $\psi(0, \cdot)$.

    Similarly, setting $s = 0$ in the $\phi$ equation:

    $$
    \phi(t + 0, u) = \phi(t, \psi(0, u)) + \phi(0, u) \implies \phi(t, u) = \phi(t, u) + \phi(0, u)
    $$

    This forces $\phi(0, u) = 0$ for all $u$.

    Now setting $t = 0$:

    $$
    \psi(0 + s, u) = \psi(0, \psi(s, u)) = \psi(s, u)
    $$

    This is automatically satisfied by $\psi(0, u) = u$. And:

    $$
    \phi(0 + s, u) = \phi(0, \psi(s, u)) + \phi(s, u) = 0 + \phi(s, u) = \phi(s, u)
    $$

    This is also automatically satisfied. The semigroup property $P_0 = \text{Id}$ means $P_0 f(x) = f(x)$ for all $f$, and applied to $f(x) = e^{\langle u, x \rangle}$:

    $$
    e^{\phi(0, u) + \langle \psi(0, u), x \rangle} = e^{\langle u, x \rangle}
    $$

    Matching terms: $\phi(0, u) = 0$ and $\psi(0, u) = u$. These are the unique initial conditions consistent with $P_0 = \text{Id}$.

---

**Exercise 5.** Consider a candidate affine process on $D = \mathbb{R}_+$ with drift $b(x) = -\alpha$ (constant, $\alpha > 0$) and diffusion $a(x) = \sigma^2 x$. Does this specification satisfy the admissibility conditions? If not, identify which condition fails and explain the financial consequence (what happens to the process at the boundary $x = 0$?).

??? success "Solution to Exercise 5"
    The candidate has $b(x) = b_0 + b_1 x$ with $b_0 = -\alpha < 0$ and diffusion $a(x) = \sigma^2 x$.

    **Condition (A1)** requires $(b_0)_1 \geq 0$ for the CIR-type component on $\mathbb{R}_+$. Here $(b_0)_1 = -\alpha < 0$, so **(A1) fails**.

    **Financial consequence**: When $x = 0$ (the boundary), the drift is $b(0) = -\alpha < 0$, pushing the process in the negative direction. Since the diffusion $a(0) = 0$ vanishes at the boundary, there is no stochastic fluctuation to counteract the negative drift. The process is deterministically pushed below zero, exiting the state space $\mathbb{R}_+$.

    In financial terms, if $x$ represents a variance or interest rate that must be non-negative, this specification allows the variable to become negative, which is economically meaningless. A well-posed CIR-type model requires $b_0 = \kappa\theta \geq 0$ (positive mean-reversion level times speed), ensuring that the drift is non-negative at the origin.

---

**Exercise 6.** For the two-factor CIR model on $D = \mathbb{R}^2_+$ with independent components $dX_t^{(i)} = \kappa_i(\theta_i - X_t^{(i)})\,dt + \xi_i\sqrt{X_t^{(i)}}\,dW_t^{(i)}$, write down the $2 \times 2$ diffusion matrix $a(x) = a_0 + a_1 x_1 + a_2 x_2$ and verify all four admissibility conditions. Under what parameter constraints does the Feller condition $2\kappa_i\theta_i \geq \xi_i^2$ hold for each component?

??? success "Solution to Exercise 6"
    With independent CIR components, the diffusion matrix is diagonal. Since $(dV^{(1)}, dV^{(2)})$ have volatilities $\xi_1\sqrt{x_1}$ and $\xi_2\sqrt{x_2}$ respectively:

    $$
    a(x) = a_0 + a_1 x_1 + a_2 x_2
    $$

    where:

    $$
    a_0 = \begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}, \qquad a_1 = \begin{pmatrix} \xi_1^2 & 0 \\ 0 & 0 \end{pmatrix}, \qquad a_2 = \begin{pmatrix} 0 & 0 \\ 0 & \xi_2^2 \end{pmatrix}
    $$

    **Checking admissibility**:

    **(A1)**: The drift is $b(x) = b_0 + b_1 x_1 + b_2 x_2$ with $b_0 = (\kappa_1\theta_1, \kappa_2\theta_2)^T$. Since $\kappa_i > 0$ and $\theta_i > 0$, both $(b_0)_1 = \kappa_1\theta_1 \geq 0$ and $(b_0)_2 = \kappa_2\theta_2 \geq 0$. Satisfied.

    **(A2)**: $(a_0)_{11} = 0$ and $(a_0)_{22} = 0$. For $i = 1$: $(a_2)_{11} = 0$, so the only contribution to $(a(x))_{11}$ is $(a_1)_{11} x_1 = \xi_1^2 x_1$. For $i = 2$: $(a_1)_{22} = 0$, so the only contribution to $(a(x))_{22}$ is $(a_2)_{22} x_2 = \xi_2^2 x_2$. Satisfied.

    **(A3)**: No jumps, so trivially satisfied.

    **(A4)**: No jumps, so trivially satisfied.

    **Feller condition**: The standard Feller condition for the $i$-th CIR component is:

    $$
    2\kappa_i\theta_i \geq \xi_i^2
    $$

    When this holds, the origin $x_i = 0$ is unattainable, meaning the process never reaches zero. If $2\kappa_i\theta_i < \xi_i^2$, the process can touch zero but is instantaneously reflected back. Both conditions require $\kappa_i > 0$, $\theta_i > 0$, and $\xi_i > 0$, with the Feller condition being the additional quantitative constraint on the relative strength of mean reversion versus volatility.

---

**Exercise 7.** The regularity theorem states that $F(u) = \langle b_0, u \rangle + \frac{1}{2}\langle u, a_0 u \rangle + \int_{D \setminus \{0\}} (e^{\langle u, z \rangle} - 1)\,m_0(dz)$. For a one-dimensional affine process on $\mathbb{R}_+$ with no diffusion ($a_0 = a_1 = 0$) but with a Poisson jump component $m_0(dz) = \lambda \cdot \mu e^{-\mu z}\,dz$ (exponential jumps), compute $F(u)$ explicitly and determine the domain of $u$ for which $F(u)$ is well-defined.

??? success "Solution to Exercise 7"
    With $a_0 = 0$ (no diffusion from the constant part), the formula reduces to:

    $$
    F(u) = b_0 \cdot u + \int_0^{\infty} (e^{uz} - 1)\,\lambda\mu e^{-\mu z}\,dz
    $$

    Computing the integral:

    $$
    \int_0^{\infty} (e^{uz} - 1)\lambda\mu e^{-\mu z}\,dz = \lambda\mu\left[\int_0^{\infty} e^{(u-\mu)z}\,dz - \int_0^{\infty} e^{-\mu z}\,dz\right]
    $$

    The first integral converges if and only if $\operatorname{Re}(u - \mu) < 0$, i.e., $\operatorname{Re}(u) < \mu$. In that case:

    $$
    \int_0^{\infty} e^{(u-\mu)z}\,dz = \frac{1}{\mu - u}
    $$

    The second integral gives $\frac{1}{\mu}$. Therefore:

    $$
    F(u) = b_0 u + \lambda\mu\left(\frac{1}{\mu - u} - \frac{1}{\mu}\right) = b_0 u + \lambda\mu \cdot \frac{u}{\mu(\mu - u)}
    $$

    $$
    = b_0 u + \frac{\lambda u}{\mu - u}
    $$

    **Domain**: $F(u)$ is well-defined for $\operatorname{Re}(u) < \mu$. For real $u$, this means $u < \mu$. At $u = \mu$, the integral diverges because the exponential damping from $e^{-\mu z}$ is exactly canceled by $e^{uz}$. For the characteristic function ($u = iv$, $v \in \mathbb{R}$), we have $\operatorname{Re}(iv) = 0 < \mu$, so $F$ is always well-defined on the imaginary axis.
