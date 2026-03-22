# Log-Affine Expectation Property

The defining characteristic of an affine process is that its log-moment generating function is linear in the current state. This single property---seemingly a modest algebraic constraint---is the engine that reduces option pricing and term structure computation from solving partial differential equations to solving ordinary differential equations. This section states the log-affine expectation property precisely, derives it from the backward Kolmogorov equation, and explores its consequences.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State the log-affine expectation formula $\mathbb{E}[e^{\langle u, X_T \rangle} \mid X_t = x] = \exp(\phi(\tau, u) + \langle \psi(\tau, u), x \rangle)$ with correct domains and initial conditions
    2. Derive the exponential-affine form from the backward Kolmogorov equation using an affine ansatz
    3. Distinguish the moment generating function (real $u$) from the characteristic function (imaginary $u$)
    4. Explain why linearity of the log-transform in $x$ is the key computational advantage

---

## Intuition

Consider a Markov process $X_t$ and the conditional expectation $\mathbb{E}[e^{\langle u, X_T \rangle} \mid X_t = x]$. For a general process, this expectation is some complicated, possibly intractable function of $x$. For an affine process, something remarkable happens: the logarithm of this expectation is a linear function of $x$. In other words, the state $x$ enters only through a dot product $\langle \psi, x \rangle$, with the coefficient $\psi$ depending on the time horizon and the transform variable $u$, but not on $x$ itself.

This linearity means that once we compute the two functions $\phi$ and $\psi$ (which depend on time and $u$ but not on $x$), we can evaluate the conditional expectation at any starting point $x$ instantly. In financial terms, this translates to: once we solve the Riccati ODEs for a given maturity, we can price bonds, options, and other derivatives across all current states of the economy without re-solving anything.

---

## The Log-Affine Expectation Formula

### Statement

**Definition (Log-Affine Property).** A Markov process $(X_t)_{t \geq 0}$ on $D = \mathbb{R}^m_+ \times \mathbb{R}^{d-m}$ is *affine* if there exist functions $\phi : \mathbb{R}_+ \times \mathcal{U} \to \mathbb{C}$ and $\psi : \mathbb{R}_+ \times \mathcal{U} \to \mathbb{C}^d$ such that for all $x \in D$, all $\tau = T - t \geq 0$, and all $u$ in the admissible set $\mathcal{U} \subseteq \mathbb{C}^d$:

$$
\mathbb{E}\!\left[e^{\langle u, X_T \rangle} \mid X_t = x\right] = \exp\!\left(\phi(\tau, u) + \langle \psi(\tau, u), x \rangle\right)
$$

with the initial conditions

$$
\phi(0, u) = 0, \qquad \psi(0, u) = u
$$

The function $\phi$ captures the contribution that is independent of the current state, while $\psi$ captures the state-dependent part. The initial conditions ensure consistency at $\tau = 0$: setting $T = t$ gives $\mathbb{E}[e^{\langle u, X_t \rangle} \mid X_t = x] = e^{\langle u, x \rangle}$, which is trivially true.

### The Admissible Set

The admissible set $\mathcal{U}$ consists of those $u \in \mathbb{C}^d$ for which the expectation $\mathbb{E}[e^{\langle u, X_T \rangle} \mid X_t = x]$ is finite. For the moment generating function, we take $u \in \mathbb{R}^d$ (or a subset thereof); for the characteristic function, we take $u = iv$ with $v \in \mathbb{R}^d$, giving:

$$
\mathbb{E}\!\left[e^{i\langle v, X_T \rangle} \mid X_t = x\right] = \exp\!\left(\phi(\tau, iv) + \langle \psi(\tau, iv), x \rangle\right)
$$

The characteristic function always exists (no integrability issues), so $iv \in \mathcal{U}$ for all $v \in \mathbb{R}^d$. The moment generating function may only exist for $u$ in a proper subset of $\mathbb{R}^d$, determined by the tail behavior of $X_T$.

---

## Derivation from the Backward Kolmogorov Equation

### Setup

To see why affine coefficients produce the log-affine form, consider a scalar affine diffusion (the argument extends to the multidimensional case):

$$
dX_t = (\kappa_0 + \kappa_1 X_t)\,dt + \sqrt{\sigma_0 + \sigma_1 X_t}\,dW_t
$$

Define the function

$$
g(\tau, x) = \mathbb{E}\!\left[e^{u X_{t+\tau}} \mid X_t = x\right]
$$

By the backward Kolmogorov equation, $g$ satisfies the PDE:

$$
\frac{\partial g}{\partial \tau} = (\kappa_0 + \kappa_1 x)\frac{\partial g}{\partial x} + \frac{1}{2}(\sigma_0 + \sigma_1 x)\frac{\partial^2 g}{\partial x^2}
$$

with initial condition $g(0, x) = e^{ux}$.

### The Affine Ansatz

Motivated by the initial condition, we try the ansatz

$$
g(\tau, x) = \exp\!\left(\phi(\tau) + \psi(\tau) x\right)
$$

with $\phi(0) = 0$ and $\psi(0) = u$. Computing the required derivatives:

$$
\frac{\partial g}{\partial \tau} = (\phi'(\tau) + \psi'(\tau) x)\,g
$$

$$
\frac{\partial g}{\partial x} = \psi(\tau)\,g, \qquad \frac{\partial^2 g}{\partial x^2} = \psi(\tau)^2\,g
$$

### Substitution and Separation

Substituting into the PDE and dividing both sides by $g$ (which is strictly positive):

$$
\phi'(\tau) + \psi'(\tau) x = (\kappa_0 + \kappa_1 x)\psi(\tau) + \frac{1}{2}(\sigma_0 + \sigma_1 x)\psi(\tau)^2
$$

Collecting terms by powers of $x$:

$$
\phi'(\tau) + \psi'(\tau) x = \left[\kappa_0 \psi(\tau) + \frac{1}{2}\sigma_0 \psi(\tau)^2\right] + \left[\kappa_1 \psi(\tau) + \frac{1}{2}\sigma_1 \psi(\tau)^2\right] x
$$

Since this must hold for all $x \in D$, we can match the constant and linear terms separately.

**Constant terms** (the $\phi$-equation):

$$
\phi'(\tau) = \kappa_0 \psi(\tau) + \frac{1}{2}\sigma_0 \psi(\tau)^2
$$

**Linear terms** (the $\psi$-equation):

$$
\psi'(\tau) = \kappa_1 \psi(\tau) + \frac{1}{2}\sigma_1 \psi(\tau)^2
$$

This separation works precisely because the drift and diffusion coefficients are affine in $x$. If the coefficients had any nonlinear dependence on $x$, the ansatz would fail and the log-affine property would not hold.

### Identification with $F$ and $R$

Writing $F(u) = \kappa_0 u + \frac{1}{2}\sigma_0 u^2$ and $R(u) = \kappa_1 u + \frac{1}{2}\sigma_1 u^2$, the system becomes

$$
\phi'(\tau) = F(\psi(\tau)), \qquad \psi'(\tau) = R(\psi(\tau))
$$

These are the **generalized Riccati ODEs**. The function $R$ is a Riccati equation when $\sigma_1 \neq 0$ (quadratic in $\psi$) and a simple linear ODE when $\sigma_1 = 0$ (Gaussian case). The detailed study of this ODE system is the subject of the next section.

---

## Why Linearity in x Matters

### Computational Advantage

The log-affine property means that to evaluate $\mathbb{E}[e^{\langle u, X_T \rangle} \mid X_t = x]$ at a new starting point $x'$, we do not need to re-solve any differential equation. We simply replace $x$ by $x'$ in the formula $\exp(\phi(\tau, u) + \langle \psi(\tau, u), x' \rangle)$. This is a single dot product plus exponentiation---an $O(d)$ operation.

For bond pricing, this means that $P(t, T) = e^{A(\tau) + B(\tau)^\top x}$ can be evaluated for any current state $x$ once $A$ and $B$ have been computed. For an entire yield curve (multiple maturities $T$), we solve the Riccati ODEs once per maturity and then evaluate the formula across all states. This is vastly more efficient than solving a PDE on a grid or running Monte Carlo simulations.

### Contrast with Non-Affine Models

In a non-affine model---for instance, the SABR model with $\sigma(X_t) = X_t^\beta$ for $\beta \notin \{0, 1/2, 1\}$---the ansatz $g = e^{\phi + \psi x}$ fails. The PDE does not separate into terms proportional to $1$ and $x$, and we cannot reduce the problem to ODEs. Instead, we must solve the full PDE numerically or use asymptotic approximations.

??? example "Log-Affine Property for the Ornstein-Uhlenbeck Process"
    The Ornstein-Uhlenbeck process $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$ has $\kappa_0 = 0$, $\kappa_1 = -\kappa$, $\sigma_0 = \sigma^2$, $\sigma_1 = 0$. The Riccati system is:

    $$
    \psi'(\tau) = -\kappa\psi(\tau), \qquad \psi(0) = u
    $$

    $$
    \phi'(\tau) = \frac{1}{2}\sigma^2\psi(\tau)^2, \qquad \phi(0) = 0
    $$

    Solving: $\psi(\tau) = u e^{-\kappa\tau}$ and

    $$
    \phi(\tau) = \frac{\sigma^2 u^2}{2} \int_0^\tau e^{-2\kappa s}\,ds = \frac{\sigma^2 u^2}{4\kappa}(1 - e^{-2\kappa\tau})
    $$

    Therefore:

    $$
    \mathbb{E}\!\left[e^{u X_{t+\tau}} \mid X_t = x\right] = \exp\!\left(\frac{\sigma^2 u^2}{4\kappa}(1 - e^{-2\kappa\tau}) + u e^{-\kappa\tau} x\right)
    $$

    The log of this expression is indeed linear in $x$: $\log \mathbb{E}[\cdots] = \frac{\sigma^2 u^2}{4\kappa}(1 - e^{-2\kappa\tau}) + u e^{-\kappa\tau} x$. This confirms that $X_T \mid X_t = x$ is Gaussian with mean $x e^{-\kappa\tau}$ and variance $\frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa\tau})$. $\square$

---

## Moment Generating Function vs Characteristic Function

The log-affine formula applies to both the moment generating function (MGF) and the characteristic function (CF), with different choices of $u$.

**Moment generating function** ($u \in \mathbb{R}^d$):

$$
M_X(\tau, u, x) = \mathbb{E}\!\left[e^{\langle u, X_T \rangle} \mid X_t = x\right] = e^{\phi(\tau, u) + \langle \psi(\tau, u), x \rangle}
$$

This exists only for $u$ in the domain where the expectation is finite. For CIR-type components, the MGF may explode in finite time for large $u$, a phenomenon called **moment explosion**.

**Characteristic function** ($u = iv$, $v \in \mathbb{R}^d$):

$$
\Phi_X(\tau, v, x) = \mathbb{E}\!\left[e^{i\langle v, X_T \rangle} \mid X_t = x\right] = e^{\phi(\tau, iv) + \langle \psi(\tau, iv), x \rangle}
$$

The characteristic function always exists and is bounded by 1 in absolute value. It is the primary tool for Fourier-based pricing methods.

!!! warning "Moment Explosion"
    For the CIR process with parameters $\kappa$, $\theta$, $\xi$, the moment generating function $\mathbb{E}[e^{u r_T}]$ is finite only for $u$ below a critical threshold that depends on $\tau$. As $\tau \to \infty$, this threshold converges to $u^* = 2\kappa/\xi^2$. For $u \geq u^*$, the expectation is infinite. This has practical consequences: heavy-tailed distributions and extreme scenarios cannot be captured by the MGF alone.

---

## The Multidimensional Case

For a $d$-dimensional affine process with drift $b(x) = b_0 + \sum_{i=1}^d b_i x_i$, diffusion $a(x) = a_0 + \sum_{i=1}^d a_i x_i$, and jump compensator $m(x, dz) = m_0(dz) + \sum_{i=1}^d x_i m_i(dz)$, the log-affine property takes the form:

$$
\mathbb{E}\!\left[e^{\langle u, X_T \rangle} \mid X_t = x\right] = \exp\!\left(\phi(\tau, u) + \langle \psi(\tau, u), x \rangle\right)
$$

where now $\phi : \mathbb{R}_+ \times \mathbb{C}^d \to \mathbb{C}$ and $\psi : \mathbb{R}_+ \times \mathbb{C}^d \to \mathbb{C}^d$ satisfy the system

$$
\frac{\partial \phi}{\partial \tau} = F(\psi), \qquad \frac{\partial \psi}{\partial \tau} = R(\psi)
$$

with

$$
F(u) = \langle b_0, u \rangle + \frac{1}{2}\langle u, a_0 u \rangle + \int_{D \setminus \{0\}} (e^{\langle u, z \rangle} - 1)\,m_0(dz)
$$

$$
R_i(u) = \langle b_i, u \rangle + \frac{1}{2}\langle u, a_i u \rangle + \int_{D \setminus \{0\}} (e^{\langle u, z \rangle} - 1)\,m_i(dz)
$$

The structure is identical to the scalar case: $\phi$ collects the state-independent terms and $\psi$ collects the state-dependent terms, with $R$ now a vector-valued function governing a coupled system of Riccati equations.

---

## Summary

The log-affine expectation property states that $\log \mathbb{E}[e^{\langle u, X_T \rangle} \mid X_t = x]$ is a linear function of $x$, decomposing into a state-independent part $\phi(\tau, u)$ and a state-dependent part $\langle \psi(\tau, u), x \rangle$. This property follows from the affine structure of the drift and diffusion coefficients: the exponential ansatz in the backward Kolmogorov equation separates into constant and linear terms, yielding the generalized Riccati ODEs $\phi' = F(\psi)$ and $\psi' = R(\psi)$. The log-affine form is the computational engine of the affine framework, enabling bond pricing, characteristic function evaluation, and Fourier inversion to be performed efficiently across all states $x$ once the Riccati solutions are known.

---

## Further Reading

- Duffie, D., Filipovic, D., & Schachermayer, W. (2003). "Affine Processes and Applications in Finance." *Annals of Applied Probability*, 13(3), 984-1053.
- Duffie, D., Pan, J., & Singleton, K. (2000). "Transform Analysis and Asset Pricing for Affine Jump-Diffusions." *Econometrica*, 68(6), 1343-1376.
- Filipovic, D. *Term-Structure Models: A Graduate Course*. Springer, 2009, Chapter 10.
