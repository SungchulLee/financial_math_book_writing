# Small Noise and Large Deviations

## Concept Definition

Consider the **small-noise diffusion** on $[0,T]$:

$$
\mathrm{d}X_t^{\varepsilon}
= b(X_t^{\varepsilon})\,\mathrm{d}t + \sqrt{\varepsilon}\,\sigma(X_t^{\varepsilon})\,\mathrm{d}W_t,
\qquad X_0^{\varepsilon} = x_0,
$$

where $\varepsilon > 0$ is a small parameter. As $\varepsilon \downarrow 0$, $X^{\varepsilon}$ concentrates around the **deterministic skeleton** (the ODE solution):

$$
\dot{\bar{x}}(t) = b(\bar{x}(t)), \qquad \bar{x}(0) = x_0.
$$

Large deviations theory (Freidlin–Wentzell) makes precise how **exponentially unlikely** it is for $X^{\varepsilon}$ to deviate from $\bar{x}$.

!!! info "Definition: Rate Function (Freidlin–Wentzell Action)"
    For $\phi \in C([0,T]; \mathbb{R}^d)$, define the **rate function**

    $$
    I_{0,T}(\phi) :=
    \begin{cases}
    \dfrac{1}{2}\displaystyle\int_0^T
    \bigl\|\sigma(\phi(t))^{-1}\bigl(\dot{\phi}(t) - b(\phi(t))\bigr)\bigr\|^2\,\mathrm{d}t
    & \text{if } \phi \text{ is abs.\ continuous and } \sigma(\phi(t)) \text{ invertible a.e.}, \\[6pt]
    +\infty & \text{otherwise.}
    \end{cases}
    $$

    Equivalently, using the control representation: if $\dot{\phi}(t) = b(\phi(t)) + \sigma(\phi(t))\,u(t)$ for some $u \in L^2([0,T]; \mathbb{R}^m)$, then

    $$
    I_{0,T}(\phi) = \frac{1}{2}\int_0^T \|u(t)\|^2\,\mathrm{d}t.
    $$

    This is the **minimum energy** (in $L^2$ of the control) needed to force the system along the path $\phi$.

---

## Explanation

### The Freidlin–Wentzell LDP

!!! theorem "Theorem (Freidlin–Wentzell, 1970)"
    Assume $b$ and $\sigma$ are bounded and Lipschitz, and $\sigma(x)$ is uniformly invertible. The family $(X^{\varepsilon})_{\varepsilon > 0}$, viewed as random variables in $C([0,T]; \mathbb{R}^d)$, satisfies a **Large Deviation Principle (LDP)** with speed $\varepsilon$ and good rate function $I_{0,T}$:

    - **(Upper bound)** For every closed set $F \subset C([0,T];\mathbb{R}^d)$:

    $$
    \limsup_{\varepsilon \downarrow 0}\;\varepsilon \log \mathbb{P}(X^{\varepsilon} \in F) \le -\inf_{\phi \in F} I_{0,T}(\phi).
    $$

    - **(Lower bound)** For every open set $G \subset C([0,T];\mathbb{R}^d)$:

    $$
    \liminf_{\varepsilon \downarrow 0}\;\varepsilon \log \mathbb{P}(X^{\varepsilon} \in G) \ge -\inf_{\phi \in G} I_{0,T}(\phi).
    $$

!!! warning "On the Invertibility Assumption"
    The formula for $I_{0,T}(\phi)$ requires $\sigma(\phi(t))$ to be invertible along the path. For degenerate diffusions (where $a(x) = \sigma(x)\sigma(x)^\top$ is not strictly positive definite), the rate function must be defined differently (as a variational infimum over controls). The above theorem applies in the uniformly elliptic case.

### Informal Interpretation

Combining upper and lower bounds: for a set $A$ satisfying $\inf_{\phi \in \mathrm{int}(A)} I_{0,T}(\phi) = \inf_{\phi \in \bar{A}} I_{0,T}(\phi)$ (a **continuity set** of $I_{0,T}$, meaning the infimum is the same over the interior and the closure),

$$
\mathbb{P}(X^{\varepsilon} \in A) \approx \exp\!\left(-\frac{1}{\varepsilon}\inf_{\phi \in A} I_{0,T}(\phi)\right) \quad (\varepsilon \downarrow 0).
$$

The **most likely atypical path** (the **instanton** or **optimal fluctuation path**) is the minimiser of $I_{0,T}$ over the constrained set $A$. All other paths in $A$ are exponentially less likely.

### Why the Rate Function Has This Form

The Itô SDE says $\dot{X}^{\varepsilon} \approx b(X^{\varepsilon}) + \sqrt{\varepsilon}\,\sigma(X^{\varepsilon})\,\dot{W}$. To force the path along $\phi \ne \bar{x}$, one must effectively supply a "fake" Brownian increment $\sqrt{\varepsilon}\,\sigma\,u\,\mathrm{d}t$ at each time. The Radon–Nikodym density of the original measure $\mathbb{P}$ with respect to the shifted measure $\mathbb{Q}^u$ is

$$
\frac{\mathrm{d}\mathbb{P}}{\mathrm{d}\mathbb{Q}^u}\bigg|_{\mathcal{F}_T}
= \exp\!\left(-\frac{1}{2\varepsilon}\int_0^T \|u(t)\|^2\,\mathrm{d}t\right)
= \exp\!\left(-\frac{I_{0,T}(\phi)}{\varepsilon}\right),
$$

so the $\mathbb{P}$-probability of the path $\phi$ is suppressed by a factor $\exp(-I_{0,T}(\phi)/\varepsilon)$ relative to the shifted measure — directly giving the exponential rate. (Since $u$ is a deterministic $L^2$ function, Novikov's condition $\mathbb{E}\exp(\frac{1}{2\varepsilon}\int\|u\|^2\,\mathrm{d}t) < \infty$ holds automatically, ensuring $\mathbb{Q}^u$ is a true probability measure.)

---

## Diagram / Example

### Example: Escape from a Potential Well

Let $d = 1$, $b(x) = -V'(x)$ (gradient drift), $\sigma = 1$:

$$
\mathrm{d}X_t^{\varepsilon} = -V'(X_t^{\varepsilon})\,\mathrm{d}t + \sqrt{\varepsilon}\,\mathrm{d}W_t.
$$

Suppose $V$ has a local minimum at $0$ and a saddle point at $x^* > 0$ with $V(x^*) > V(0)$. The **quasipotential** for escape from the well is

$$
\Delta V := V(x^*) - V(0) = I_{0,\infty}(\phi^*),
$$

where $\phi^*$ is the minimising path (the instanton). By the LDP,

$$
\mathbb{P}(X^{\varepsilon} \text{ exits the well}) \approx \exp\!\left(-\frac{\Delta V}{\varepsilon}\right).
$$

This recovers the **Kramers escape rate** from statistical physics.

### Hamilton–Jacobi Connection

Define the **Hamiltonian** associated to the large deviations:

$$
H(x, p) = b(x) \cdot p + \frac{1}{2}\,p^\top a(x)\,p, \qquad a = \sigma\sigma^\top.
$$

The **quasipotential** $U(x) := \inf\{I_{0,\infty}(\phi) : \phi(0) = x_0,\, \phi(\infty) = x\}$ satisfies the stationary **Hamilton–Jacobi equation**:

$$
H(x, \nabla U(x)) = 0.
$$

This equation has a meaningful solution when $x_0$ is a **stable equilibrium** of the ODE $\dot{x} = b(x)$ (i.e. $b(x_0) = 0$ and the linearisation at $x_0$ is stable); the quasipotential then measures the cost of reaching $x$ from the basin of attraction of $x_0$.

The time-dependent analogue: the value function $V(t, x) = -\varepsilon \log \mathbb{E}^x[e^{-g(X_T^{\varepsilon})/\varepsilon}]$ satisfies, as $\varepsilon \to 0$, the **nonlinear** Hamilton–Jacobi PDE

$$
\partial_t V + H(x, \nabla_x V) = 0,
$$

in contrast to the **linear** Kolmogorov backward equation satisfied by $\mathbb{E}^x[g(X_T^{\varepsilon})]$. Large deviations thus convert linear PDE problems into nonlinear Hamilton–Jacobi problems.

---

## Proof / Derivation

We sketch the Girsanov-based derivation of the rate function.

**Step 1: Girsanov change of measure.** For a deterministic control $u \in L^2([0,T];\mathbb{R}^m)$, define the controlled process $\phi$ by $\dot{\phi} = b(\phi) + \sigma(\phi)\,u$, $\phi(0) = x_0$. In the small-noise SDE $\mathrm{d}X^\varepsilon = b\,\mathrm{d}t + \sqrt{\varepsilon}\,\sigma\,\mathrm{d}W$, forcing $X^\varepsilon \approx \phi$ requires shifting the standard BM $W$ by $u/\sqrt{\varepsilon}$ — that is, replacing $\mathrm{d}W_t$ by $\mathrm{d}W_t - (u(t)/\sqrt{\varepsilon})\,\mathrm{d}t$. By Girsanov's theorem, the change-of-measure density for this shift is

$$
\frac{\mathrm{d}\mathbb{Q}^u}{\mathrm{d}\mathbb{P}}\bigg|_{\mathcal{F}_T}
= \exp\!\left(
\frac{1}{\sqrt{\varepsilon}}\int_0^T u(t)^\top\,\mathrm{d}W_t
- \frac{1}{2\varepsilon}\int_0^T \|u(t)\|^2\,\mathrm{d}t
\right).
$$

Under $\mathbb{Q}^u$, the process $\widetilde{W}_t := W_t - \frac{1}{\sqrt{\varepsilon}}\int_0^t u(s)\,\mathrm{d}s$ is a standard BM, and the SDE becomes $\mathrm{d}X^\varepsilon = (b + \sigma u)\,\mathrm{d}t + \sqrt{\varepsilon}\,\sigma\,\mathrm{d}\widetilde{W}$, which has $\phi$ as its leading-order ($\varepsilon \to 0$) solution. The log-likelihood of the shift is $-\frac{1}{2\varepsilon}\int\|u\|^2\,\mathrm{d}t = -I_{0,T}(\phi)/\varepsilon$, directly giving the exponential rate.

**Step 2: Exponential tightness.** One shows that the family $(X^{\varepsilon})$ is exponentially tight in $C([0,T];\mathbb{R}^d)$ under Lipschitz assumptions, ruling out escape to infinity.

**Step 3: Identification of the rate function.** Using Varadhan's lemma and the duality formula for the log-Laplace functional, the rate function is identified as the Legendre transform of the log-moment generating functional, yielding $I_{0,T}(\phi) = \frac{1}{2}\int_0^T \|u(t)\|^2\,\mathrm{d}t$ for the optimal control $u$ realising path $\phi$. $\square$

---

## What to Remember

- Small-noise diffusions satisfy a **path-space LDP** with speed $\varepsilon$ and rate function $I_{0,T}(\phi)$.
- The rate function measures the **minimum $L^2$-energy of the control** needed to force the path $\phi$.
- Rare events occur along **instanton paths** (minimisers of $I_{0,T}$ subject to the constraint).
- Large deviations connect stochastic dynamics to **nonlinear Hamilton–Jacobi PDEs**, replacing the linear Kolmogorov equations.
- The Freidlin–Wentzell LDP applies under **uniform ellipticity**; degenerate cases require separate treatment.

---

## Exercises

**Exercise 1.** Consider the small-noise SDE $\mathrm{d}X_t^\varepsilon = -X_t^\varepsilon\,\mathrm{d}t + \sqrt{\varepsilon}\,\mathrm{d}W_t$ with $X_0^\varepsilon = 1$. Write down the deterministic skeleton $\bar{x}(t)$ (the ODE solution with $\varepsilon = 0$). For the path $\phi(t) = e^{-t} + \delta\sin(\pi t/T)$ on $[0, T]$, compute the control $u(t)$ such that $\dot{\phi} = b(\phi) + u$ and express the rate function $I_{0,T}(\phi)$ as an integral involving $u$.

---

**Exercise 2.** Let $b(x) = -V'(x)$ with $V(x) = \frac{1}{2}x^2$ and $\sigma = 1$. Compute the quasipotential $U(y) = \inf\{I_{0,\infty}(\phi) : \phi(0) = 0,\, \phi(\infty) = y\}$ and verify that $U(y) = V(y) - V(0) = \frac{1}{2}y^2$. Show that the Hamiltonian $H(x, p) = -V'(x)\,p + \frac{1}{2}p^2$ satisfies $H(x, \nabla U(x)) = 0$.

---

**Exercise 3.** Consider the double-well potential $V(x) = \frac{1}{4}x^4 - \frac{1}{2}x^2$ with minima at $x = \pm 1$ and a saddle at $x = 0$. For the gradient diffusion $\mathrm{d}X_t^\varepsilon = -V'(X_t^\varepsilon)\,\mathrm{d}t + \sqrt{\varepsilon}\,\mathrm{d}W_t$ started at $X_0 = -1$, compute the potential barrier $\Delta V = V(0) - V(-1)$ and give the exponential rate at which $X^\varepsilon$ escapes from the left well to the right well as $\varepsilon \to 0$.

---

**Exercise 4.** Explain the Girsanov-based derivation of the rate function. For the small-noise SDE $\mathrm{d}X_t^\varepsilon = b(X_t^\varepsilon)\,\mathrm{d}t + \sqrt{\varepsilon}\,\sigma(X_t^\varepsilon)\,\mathrm{d}W_t$, describe how shifting $W_t$ by $u(t)/\sqrt{\varepsilon}$ via Girsanov's theorem produces a change-of-measure density proportional to $\exp(-I_{0,T}(\phi)/\varepsilon)$. Why does Novikov's condition hold for a deterministic control $u \in L^2$?

---

**Exercise 5.** State the upper and lower bounds of the Freidlin–Wentzell LDP. For a continuity set $A$ (where $\inf_{\mathrm{int}(A)} I = \inf_{\bar{A}} I$), show that the two bounds combine to give

$$
\lim_{\varepsilon \downarrow 0}\;\varepsilon\log\mathbb{P}(X^\varepsilon \in A) = -\inf_{\phi \in A} I_{0,T}(\phi).
$$

Give a concrete example of a set $A$ in path space that is a continuity set and one that is not.

---

**Exercise 6.** For the small-noise diffusion $\mathrm{d}X_t^\varepsilon = b(X_t^\varepsilon)\,\mathrm{d}t + \sqrt{\varepsilon}\,\sigma(X_t^\varepsilon)\,\mathrm{d}W_t$, define the Hamiltonian $H(x, p) = b(x) \cdot p + \frac{1}{2}p^\top a(x)\,p$ with $a = \sigma\sigma^\top$. Write down the Hamilton equations (the Euler–Lagrange equations for minimising $I_{0,T}$) and show that the instanton path $\phi^*$ satisfies

$$
\dot{\phi}^* = b(\phi^*) + a(\phi^*)\,p^*, \qquad \dot{p}^* = -(\nabla_x b)^\top p^* - \frac{1}{2}\nabla_x(p^{*\top} a\,p^*),
$$

where $p^*$ is the conjugate momentum.

---

**Exercise 7.** Consider the two-dimensional system $\mathrm{d}X_t^\varepsilon = A X_t^\varepsilon\,\mathrm{d}t + \sqrt{\varepsilon}\,\mathrm{d}W_t$ where $A$ is a $2 \times 2$ stable matrix (all eigenvalues have negative real part) and $X_0^\varepsilon = 0$. Write down the rate function $I_{0,T}(\phi)$ for a path $\phi$ with $\phi(0) = 0$. Show that the quasipotential $U(y) = \inf_{\phi(0) = 0,\, \phi(\infty) = y} I_{0,\infty}(\phi)$ is a quadratic form $U(y) = \frac{1}{2}y^\top Q\,y$ and find the matrix equation that $Q$ must satisfy in terms of $A$.
