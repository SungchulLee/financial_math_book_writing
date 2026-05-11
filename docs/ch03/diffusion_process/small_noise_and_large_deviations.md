# Small Noise and Large Deviations

## Concept Definition

Consider the [diffusion](diffusion_process_overview.md) from earlier with scaled noise:

$$
\mathrm{d}X_t^{\varepsilon}
= b(X_t^{\varepsilon})\,\mathrm{d}t + \sqrt{\varepsilon}\,\sigma(X_t^{\varepsilon})\,\mathrm{d}W_t,
\qquad X_0^{\varepsilon} = x_0
$$

where $\varepsilon > 0$ is a small parameter. As $\varepsilon \downarrow 0$, $X^{\varepsilon}$ concentrates around the **deterministic skeleton** (the ODE solution):

$$
\dot{\bar{x}}(t) = b(\bar{x}(t)), \qquad \bar{x}(0) = x_0
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
    I_{0,T}(\phi) = \frac{1}{2}\int_0^T \|u(t)\|^2\,\mathrm{d}t
    $$

    This is the **minimum energy** (in $L^2$ of the control) needed to force the system along the path $\phi$.

---

## Explanation

### The Freidlin–Wentzell LDP

!!! tip "Theorem (Freidlin–Wentzell, 1970)"
    Assume $b$ and $\sigma$ are bounded and Lipschitz, and $\sigma(x)$ is uniformly invertible. The family $(X^{\varepsilon})_{\varepsilon > 0}$, viewed as random variables in $C([0,T]; \mathbb{R}^d)$, satisfies a **Large Deviation Principle (LDP)** with speed $\varepsilon$ and good rate function $I_{0,T}$:

    - **(Upper bound)** For every closed set $F \subset C([0,T];\mathbb{R}^d)$:

    $$
    \limsup_{\varepsilon \downarrow 0}\;\varepsilon \log \mathbb{P}(X^{\varepsilon} \in F) \le -\inf_{\phi \in F} I_{0,T}(\phi)
    $$

    - **(Lower bound)** For every open set $G \subset C([0,T];\mathbb{R}^d)$:

    $$
    \liminf_{\varepsilon \downarrow 0}\;\varepsilon \log \mathbb{P}(X^{\varepsilon} \in G) \ge -\inf_{\phi \in G} I_{0,T}(\phi)
    $$

!!! warning "On the Invertibility Assumption"
    The formula for $I_{0,T}(\phi)$ requires $\sigma(\phi(t))$ to be invertible along the path. For degenerate diffusions (where $a(x) = \sigma(x)\sigma(x)^\top$ is not strictly positive definite), the rate function must be defined differently (as a variational infimum over controls). The above theorem applies in the uniformly elliptic case.

### Informal Interpretation

Combining upper and lower bounds: for a set $A$ satisfying $\inf_{\phi \in \mathrm{int}(A)} I_{0,T}(\phi) = \inf_{\phi \in \bar{A}} I_{0,T}(\phi)$ (a **continuity set** of $I_{0,T}$, meaning the infimum is the same over the interior and the closure),

$$
\mathbb{P}(X^{\varepsilon} \in A) \approx \exp\!\left(-\frac{1}{\varepsilon}\inf_{\phi \in A} I_{0,T}(\phi)\right) \quad (\varepsilon \downarrow 0)
$$

The **most likely atypical path** (the **instanton** or **optimal fluctuation path**) is the minimiser of $I_{0,T}$ over the constrained set $A$. All other paths in $A$ are exponentially less likely.

### Why the Rate Function Has This Form

The Itô SDE says $\dot{X}^{\varepsilon} \approx b(X^{\varepsilon}) + \sqrt{\varepsilon}\,\sigma(X^{\varepsilon})\,\dot{W}$. To force the path along $\phi \ne \bar{x}$, one must effectively supply a "fake" Brownian increment $\sqrt{\varepsilon}\,\sigma\,u\,\mathrm{d}t$ at each time. The Radon–Nikodym density of the original measure $\mathbb{P}$ with respect to the shifted measure $\mathbb{Q}^u$ is

$$
\frac{\mathrm{d}\mathbb{P}}{\mathrm{d}\mathbb{Q}^u}\bigg|_{\mathcal{F}_T}
= \exp\!\left(-\frac{1}{2\varepsilon}\int_0^T \|u(t)\|^2\,\mathrm{d}t\right)
= \exp\!\left(-\frac{I_{0,T}(\phi)}{\varepsilon}\right)
$$

so the $\mathbb{P}$-probability of the path $\phi$ is suppressed by a factor $\exp(-I_{0,T}(\phi)/\varepsilon)$ relative to the shifted measure — directly giving the exponential rate. (Since $u$ is a deterministic $L^2$ function, Novikov's condition $\mathbb{E}\exp(\frac{1}{2\varepsilon}\int\|u\|^2\,\mathrm{d}t) < \infty$ holds automatically, ensuring $\mathbb{Q}^u$ is a true probability measure.)

---

## Diagram / Example

### Example: Escape from a Potential Well

Let $d = 1$, $b(x) = -V'(x)$ (gradient drift), $\sigma = 1$:

$$
\mathrm{d}X_t^{\varepsilon} = -V'(X_t^{\varepsilon})\,\mathrm{d}t + \sqrt{\varepsilon}\,\mathrm{d}W_t
$$

Suppose $V$ has a local minimum at $0$ and a saddle point at $x^* > 0$ with $V(x^*) > V(0)$. The **quasipotential** for escape from the well is

$$
\Delta V := V(x^*) - V(0) = I_{0,\infty}(\phi^*)
$$

where $\phi^*$ is the minimising path (the instanton). By the LDP,

$$
\mathbb{P}(X^{\varepsilon} \text{ exits the well}) \approx \exp\!\left(-\frac{\Delta V}{\varepsilon}\right)
$$

This recovers the **Kramers escape rate** from statistical physics.

### Hamilton–Jacobi Connection

The large-deviations Hamiltonian is built from the same coefficients $(b, a)$ that define the [generator](diffusion_process_overview.md#infinitesimal-generator) $\mathcal{L} = b \cdot \nabla + \frac{1}{2}a:\nabla^2$. Define the **Hamiltonian**:

$$
H(x, p) = b(x) \cdot p + \frac{1}{2}\,p^\top a(x)\,p, \qquad a = \sigma\sigma^\top
$$

The **quasipotential** $U(x) := \inf\{I_{0,\infty}(\phi) : \phi(0) = x_0,\, \phi(\infty) = x\}$ satisfies the stationary **Hamilton–Jacobi equation**:

$$
H(x, \nabla U(x)) = 0
$$

This equation has a meaningful solution when $x_0$ is a **stable equilibrium** of the ODE $\dot{x} = b(x)$ (i.e. $b(x_0) = 0$ and the linearisation at $x_0$ is stable); the quasipotential then measures the cost of reaching $x$ from the basin of attraction of $x_0$.

The time-dependent analogue: the value function $V(t, x) = -\varepsilon \log \mathbb{E}^x[e^{-g(X_T^{\varepsilon})/\varepsilon}]$ satisfies, as $\varepsilon \to 0$, the **nonlinear** Hamilton–Jacobi PDE

$$
\partial_t V + H(x, \nabla_x V) = 0
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
\right)
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

??? success "Solution to Exercise 1"
    The deterministic skeleton solves $\dot{\bar{x}}(t) = -\bar{x}(t)$ with $\bar{x}(0) = 1$, giving

    $$
    \bar{x}(t) = e^{-t}
    $$

    For the path $\phi(t) = e^{-t} + \delta\sin(\pi t/T)$, the SDE has $b(x) = -x$ and $\sigma = 1$, so the control $u(t)$ satisfies $\dot{\phi}(t) = b(\phi(t)) + u(t) = -\phi(t) + u(t)$. Therefore

    $$
    u(t) = \dot{\phi}(t) + \phi(t)
    $$

    Computing $\dot{\phi}(t) = -e^{-t} + \delta\frac{\pi}{T}\cos(\pi t/T)$:

    $$
    u(t) = -e^{-t} + \delta\frac{\pi}{T}\cos(\pi t/T) + e^{-t} + \delta\sin(\pi t/T) = \delta\left(\frac{\pi}{T}\cos(\pi t/T) + \sin(\pi t/T)\right)
    $$

    The rate function is

    $$
    I_{0,T}(\phi) = \frac{1}{2}\int_0^T u(t)^2\,\mathrm{d}t = \frac{\delta^2}{2}\int_0^T \left(\frac{\pi}{T}\cos(\pi t/T) + \sin(\pi t/T)\right)^2\mathrm{d}t
    $$

    Expanding the square and using orthogonality of $\cos$ and $\sin$ over $[0,T]$:

    $$
    I_{0,T}(\phi) = \frac{\delta^2}{2}\left(\frac{\pi^2}{T^2}\cdot\frac{T}{2} + \frac{T}{2}\right) = \frac{\delta^2}{4}\left(\frac{\pi^2}{T} + T\right)
    $$

    Note that as $\delta \to 0$, $\phi \to \bar{x}$ and $I_{0,T}(\phi) \to 0$, confirming that the skeleton has zero cost.

---

**Exercise 2.** Let $b(x) = -V'(x)$ with $V(x) = \frac{1}{2}x^2$ and $\sigma = 1$. Compute the quasipotential $U(y) = \inf\{I_{0,\infty}(\phi) : \phi(0) = 0,\, \phi(\infty) = y\}$ and verify that $U(y) = V(y) - V(0) = \frac{1}{2}y^2$. Show that the Hamiltonian $H(x, p) = -V'(x)\,p + \frac{1}{2}p^2$ satisfies $H(x, \nabla U(x)) = 0$.

??? success "Solution to Exercise 2"
    With $b(x) = -V'(x) = -x$ and $\sigma = 1$ (so $a = 1$), the rate function for a path $\phi$ from $\phi(0) = 0$ to $\phi(\infty) = y$ is

    $$
    I_{0,\infty}(\phi) = \frac{1}{2}\int_0^\infty (\dot{\phi}(t) + \phi(t))^2\,\mathrm{d}t
    $$

    The quasipotential is $U(y) = \inf_\phi I_{0,\infty}(\phi)$ over paths with $\phi(0) = 0$ and $\phi(t) \to y$ as $t \to \infty$.

    The Euler–Lagrange equation for the minimizing path gives $\ddot{\phi} = \phi$ (the "instanton equation"), with boundary conditions $\phi(0) = 0$ and $\phi(\infty) = y$. However, it is easier to use the known result for gradient systems: when $b = -\nabla V$ and $a = I$, the quasipotential is

    $$
    U(y) = 2(V(y) - V(0)) = 2\left(\frac{1}{2}y^2 - 0\right) = y^2
    $$

    Wait — let us verify more carefully. For the gradient system $\dot{\phi} = -V'(\phi) + u$, the optimal control that takes $\phi$ from $0$ to $y$ uses the time-reversed deterministic flow: $\dot{\phi} = +V'(\phi) = \phi$ with $\phi(0) = 0$, arriving at $y$ in infinite time (approaching $y$ as $t \to \infty$ via $\phi(t) = y(1 - e^{-2t})$ approximately). The control along this path is $u = \dot{\phi} - b(\phi) = \dot{\phi} + \phi = 2\phi$.

    Actually, for gradient systems with $a = I$, there is a standard identity: $U(y) = 2(V(y) - V(0))$. But let us verify via the Hamilton–Jacobi equation.

    **Hamilton–Jacobi verification:** The Hamiltonian is

    $$
    H(x, p) = b(x)p + \frac{1}{2}p^2 = -xp + \frac{1}{2}p^2
    $$

    The Hamilton–Jacobi equation $H(x, U'(x)) = 0$ with $U(x) = \frac{1}{2}x^2$ gives $U'(x) = x$:

    $$
    H(x, x) = -x \cdot x + \frac{1}{2}x^2 = -x^2 + \frac{1}{2}x^2 = -\frac{1}{2}x^2 \ne 0
    $$

    This does not vanish, so $U(y) = \frac{1}{2}y^2$ does not satisfy $H(x, \nabla U) = 0$. Let us try $U(y) = y^2$ so $U'(x) = 2x$:

    $$
    H(x, 2x) = -x(2x) + \frac{1}{2}(2x)^2 = -2x^2 + 2x^2 = 0 \checkmark
    $$

    So $U(y) = y^2 = 2V(y) - 2V(0)$ and $V(y) - V(0) = \frac{1}{2}y^2$, confirming

    $$
    U(y) = 2(V(y) - V(0)) = 2 \cdot \frac{1}{2}y^2 = y^2
    $$

    and $H(x, \nabla U(x)) = 0$ is verified. $\square$

---

**Exercise 3.** Consider the double-well potential $V(x) = \frac{1}{4}x^4 - \frac{1}{2}x^2$ with minima at $x = \pm 1$ and a saddle at $x = 0$. For the gradient diffusion $\mathrm{d}X_t^\varepsilon = -V'(X_t^\varepsilon)\,\mathrm{d}t + \sqrt{\varepsilon}\,\mathrm{d}W_t$ started at $X_0 = -1$, compute the potential barrier $\Delta V = V(0) - V(-1)$ and give the exponential rate at which $X^\varepsilon$ escapes from the left well to the right well as $\varepsilon \to 0$.

??? success "Solution to Exercise 3"
    The potential is $V(x) = \frac{1}{4}x^4 - \frac{1}{2}x^2$. The critical points satisfy $V'(x) = x^3 - x = 0$, giving $x = 0, \pm 1$.

    - $V(-1) = \frac{1}{4} - \frac{1}{2} = -\frac{1}{4}$ (local minimum)
    - $V(0) = 0$ (local maximum, i.e., saddle of the potential)
    - $V(1) = \frac{1}{4} - \frac{1}{2} = -\frac{1}{4}$ (local minimum)

    The potential barrier for escape from the left well (at $x = -1$) over the saddle (at $x = 0$) is

    $$
    \Delta V = V(0) - V(-1) = 0 - \left(-\frac{1}{4}\right) = \frac{1}{4}
    $$

    By the Freidlin–Wentzell large deviation principle, for the gradient diffusion with $a = 1$ the quasipotential for escape is $2\Delta V$ (using the identity $U = 2(V(\text{saddle}) - V(\text{minimum}))$ for gradient systems). The probability of escape satisfies

    $$
    \mathbb{P}(X^\varepsilon \text{ escapes left well}) \approx \exp\!\left(-\frac{2\Delta V}{\varepsilon}\right) = \exp\!\left(-\frac{1}{2\varepsilon}\right)
    $$

    as $\varepsilon \downarrow 0$. The exponential rate is $2\Delta V = 1/2$, so rare transitions between wells become exponentially suppressed as the noise vanishes.

---

**Exercise 4.** Explain the Girsanov-based derivation of the rate function. For the small-noise SDE $\mathrm{d}X_t^\varepsilon = b(X_t^\varepsilon)\,\mathrm{d}t + \sqrt{\varepsilon}\,\sigma(X_t^\varepsilon)\,\mathrm{d}W_t$, describe how shifting $W_t$ by $u(t)/\sqrt{\varepsilon}$ via Girsanov's theorem produces a change-of-measure density proportional to $\exp(-I_{0,T}(\phi)/\varepsilon)$. Why does Novikov's condition hold for a deterministic control $u \in L^2$?

??? success "Solution to Exercise 4"
    Consider the small-noise SDE $\mathrm{d}X_t^\varepsilon = b(X_t^\varepsilon)\,\mathrm{d}t + \sqrt{\varepsilon}\,\sigma(X_t^\varepsilon)\,\mathrm{d}W_t$. To force $X^\varepsilon$ to follow a path $\phi$ with $\dot{\phi} = b(\phi) + \sigma(\phi)u$, we shift the Brownian motion by $u(t)/\sqrt{\varepsilon}$.

    Define $\widetilde{W}_t = W_t - \frac{1}{\sqrt{\varepsilon}}\int_0^t u(s)\,\mathrm{d}s$. Under the original measure $\mathbb{P}$, this shift changes the SDE to

    $$
    \mathrm{d}X_t^\varepsilon = \bigl(b(X_t^\varepsilon) + \sigma(X_t^\varepsilon)u(t)\bigr)\mathrm{d}t + \sqrt{\varepsilon}\,\sigma(X_t^\varepsilon)\,\mathrm{d}\widetilde{W}_t
    $$

    By **Girsanov's theorem**, the Radon–Nikodym derivative for making $\widetilde{W}$ a standard BM under a new measure $\mathbb{Q}^u$ is

    $$
    \frac{\mathrm{d}\mathbb{Q}^u}{\mathrm{d}\mathbb{P}}\bigg|_{\mathcal{F}_T} = \exp\!\left(\frac{1}{\sqrt{\varepsilon}}\int_0^T u(t)^\top\,\mathrm{d}W_t - \frac{1}{2\varepsilon}\int_0^T \|u(t)\|^2\,\mathrm{d}t\right)
    $$

    Under $\mathbb{Q}^u$, the leading-order dynamics are $\dot{\phi} = b(\phi) + \sigma(\phi)u$, so $X^\varepsilon$ concentrates near $\phi$. The $\mathbb{P}$-probability of paths near $\phi$ is suppressed by

    $$
    \frac{\mathrm{d}\mathbb{P}}{\mathrm{d}\mathbb{Q}^u} = \exp\!\left(-\frac{1}{\sqrt{\varepsilon}}\int_0^T u^\top\,\mathrm{d}W_t + \frac{1}{2\varepsilon}\int_0^T \|u\|^2\,\mathrm{d}t - \frac{1}{2\varepsilon}\int_0^T\|u\|^2\,\mathrm{d}t\right)
    $$

    Taking logarithms and expectations under $\mathbb{Q}^u$, the dominant term is $-\frac{1}{2\varepsilon}\int_0^T\|u\|^2\,\mathrm{d}t = -I_{0,T}(\phi)/\varepsilon$, giving the exponential rate.

    **Novikov's condition** requires $\mathbb{E}\exp\!\left(\frac{1}{2\varepsilon}\int_0^T\|u(t)\|^2\,\mathrm{d}t\right) < \infty$. Since $u \in L^2([0,T];\mathbb{R}^m)$ is **deterministic**, $\int_0^T\|u\|^2\,\mathrm{d}t$ is a finite constant (not random). Therefore the exponential is a finite constant, and Novikov's condition holds trivially.

---

**Exercise 5.** State the upper and lower bounds of the Freidlin–Wentzell LDP. For a continuity set $A$ (where $\inf_{\mathrm{int}(A)} I = \inf_{\bar{A}} I$), show that the two bounds combine to give

$$
\lim_{\varepsilon \downarrow 0}\;\varepsilon\log\mathbb{P}(X^\varepsilon \in A) = -\inf_{\phi \in A} I_{0,T}(\phi)
$$

Give a concrete example of a set $A$ in path space that is a continuity set and one that is not.

??? success "Solution to Exercise 5"
    The Freidlin–Wentzell LDP states:

    - **Upper bound:** For every closed $F$: $\limsup_{\varepsilon \downarrow 0}\,\varepsilon\log\mathbb{P}(X^\varepsilon \in F) \le -\inf_{\phi \in F}I_{0,T}(\phi)$
    - **Lower bound:** For every open $G$: $\liminf_{\varepsilon \downarrow 0}\,\varepsilon\log\mathbb{P}(X^\varepsilon \in G) \ge -\inf_{\phi \in G}I_{0,T}(\phi)$

    For a continuity set $A$ with $\inf_{\phi \in \mathrm{int}(A)}I = \inf_{\phi \in \bar{A}}I =: c$, apply:

    - Upper bound with $F = \bar{A}$: $\limsup\,\varepsilon\log\mathbb{P}(X^\varepsilon \in A) \le \limsup\,\varepsilon\log\mathbb{P}(X^\varepsilon \in \bar{A}) \le -\inf_{\bar{A}}I = -c$
    - Lower bound with $G = \mathrm{int}(A)$: $\liminf\,\varepsilon\log\mathbb{P}(X^\varepsilon \in A) \ge \liminf\,\varepsilon\log\mathbb{P}(X^\varepsilon \in \mathrm{int}(A)) \ge -\inf_{\mathrm{int}(A)}I = -c$

    Combining: $-c \le \liminf \le \limsup \le -c$, so

    $$
    \lim_{\varepsilon \downarrow 0}\,\varepsilon\log\mathbb{P}(X^\varepsilon \in A) = -c = -\inf_{\phi \in A}I_{0,T}(\phi)
    $$

    **Continuity set example:** For the SDE $\mathrm{d}X^\varepsilon = -X^\varepsilon\,\mathrm{d}t + \sqrt{\varepsilon}\,\mathrm{d}W$ with $X_0 = 0$, consider $A = \{\phi : \|\phi - \bar{x}\|_\infty > \delta\}$ for some $\delta > 0$. This set has $\mathrm{int}(A) = A$ (it is open) and $\bar{A} = \{\phi : \|\phi - \bar{x}\|_\infty \ge \delta\}$. If the infimum of $I$ over $\bar{A}$ is not attained on the boundary $\{\|\phi - \bar{x}\|_\infty = \delta\}$ exclusively (which generically it is), then $\inf_{\mathrm{int}(A)}I = \inf_{\bar{A}}I$ and $A$ is a continuity set.

    **Non-continuity set example:** The singleton $A = \{\bar{x}\}$ (the deterministic skeleton itself). Here $\mathrm{int}(A) = \emptyset$, so $\inf_{\mathrm{int}(A)}I = +\infty$, while $\inf_{\bar{A}}I = I(\bar{x}) = 0$. Since $+\infty \ne 0$, this is not a continuity set.

---

**Exercise 6.** For the small-noise diffusion $\mathrm{d}X_t^\varepsilon = b(X_t^\varepsilon)\,\mathrm{d}t + \sqrt{\varepsilon}\,\sigma(X_t^\varepsilon)\,\mathrm{d}W_t$, define the Hamiltonian $H(x, p) = b(x) \cdot p + \frac{1}{2}p^\top a(x)\,p$ with $a = \sigma\sigma^\top$. Write down the Hamilton equations (the Euler–Lagrange equations for minimising $I_{0,T}$) and show that the instanton path $\phi^*$ satisfies

$$
\dot{\phi}^* = b(\phi^*) + a(\phi^*)\,p^*, \qquad \dot{p}^* = -(\nabla_x b)^\top p^* - \frac{1}{2}\nabla_x(p^{*\top} a\,p^*)
$$

where $p^*$ is the conjugate momentum.

??? success "Solution to Exercise 6"
    The rate function is $I_{0,T}(\phi) = \frac{1}{2}\int_0^T\|u(t)\|^2\,\mathrm{d}t$ where $\dot{\phi} = b(\phi) + \sigma(\phi)u$, i.e., $u = \sigma(\phi)^{-1}(\dot{\phi} - b(\phi))$. This is a calculus of variations problem. Define the Lagrangian

    $$
    L(\phi, \dot{\phi}) = \frac{1}{2}\|\sigma(\phi)^{-1}(\dot{\phi} - b(\phi))\|^2 = \frac{1}{2}(\dot{\phi} - b(\phi))^\top a(\phi)^{-1}(\dot{\phi} - b(\phi))
    $$

    The conjugate momentum is

    $$
    p = \frac{\partial L}{\partial \dot{\phi}} = a(\phi)^{-1}(\dot{\phi} - b(\phi))
    $$

    so $\dot{\phi} = b(\phi) + a(\phi)p$. The Hamiltonian (Legendre transform of $L$) is

    $$
    H(\phi, p) = p \cdot \dot{\phi} - L = p \cdot (b + ap) - \frac{1}{2}p^\top a\,p = b \cdot p + \frac{1}{2}p^\top a\,p
    $$

    The Hamilton equations are

    $$
    \dot{\phi}^* = \frac{\partial H}{\partial p} = b(\phi^*) + a(\phi^*)\,p^*
    $$

    $$
    \dot{p}^* = -\frac{\partial H}{\partial \phi} = -(\nabla_\phi b)^\top p^* - \frac{1}{2}\nabla_\phi(p^{*\top}a\,p^*)
    $$

    where the second equation accounts for the $\phi$-dependence of both $b$ and $a$. The instanton path $\phi^*$ satisfies this system of $2d$ ODEs with boundary conditions $\phi^*(0) = x_0$ and $\phi^*(T) \in$ target set. $\square$

---

**Exercise 7.** Consider the two-dimensional system $\mathrm{d}X_t^\varepsilon = A X_t^\varepsilon\,\mathrm{d}t + \sqrt{\varepsilon}\,\mathrm{d}W_t$ where $A$ is a $2 \times 2$ stable matrix (all eigenvalues have negative real part) and $X_0^\varepsilon = 0$. Write down the rate function $I_{0,T}(\phi)$ for a path $\phi$ with $\phi(0) = 0$. Show that the quasipotential $U(y) = \inf_{\phi(0) = 0,\, \phi(\infty) = y} I_{0,\infty}(\phi)$ is a quadratic form $U(y) = \frac{1}{2}y^\top Q\,y$ and find the matrix equation that $Q$ must satisfy in terms of $A$.

??? success "Solution to Exercise 7"
    With $b(\phi) = A\phi$ and $\sigma = I$ (so $a = I$), the rate function for a path $\phi$ with $\phi(0) = 0$ is

    $$
    I_{0,T}(\phi) = \frac{1}{2}\int_0^T \|\dot{\phi}(t) - A\phi(t)\|^2\,\mathrm{d}t
    $$

    The Hamiltonian is $H(\phi, p) = (A\phi)\cdot p + \frac{1}{2}|p|^2$. The Hamilton equations are

    $$
    \dot{\phi} = A\phi + p, \qquad \dot{p} = -A^\top p
    $$

    From the second equation: $p(t) = e^{-A^\top t}p_0$. The first equation becomes $\dot{\phi} = A\phi + e^{-A^\top t}p_0$, a linear ODE with solution

    $$
    \phi(t) = e^{At}\int_0^t e^{-As}e^{-A^\top s}\,\mathrm{d}s\;p_0
    $$

    (using $\phi(0) = 0$). As $T \to \infty$, requiring $\phi(T) \to y$ determines $p_0$. The cost along the optimal path is

    $$
    U(y) = \frac{1}{2}\int_0^\infty |p(t)|^2\,\mathrm{d}t = \frac{1}{2}p_0^\top\!\left(\int_0^\infty e^{-A^\top t}e^{-At}\,\mathrm{d}t\right) p_0
    $$

    For the quasipotential $U(y) = \frac{1}{2}y^\top Q\,y$, we use the Hamilton–Jacobi equation $H(x, Qx) = 0$:

    $$
    (Ax)\cdot(Qx) + \frac{1}{2}(Qx)\cdot(Qx) = 0 \quad \text{for all } x
    $$

    $$
    x^\top A^\top Q\,x + \frac{1}{2}x^\top Q^2 x = 0
    $$

    Since this holds for all $x$, the symmetric part must vanish:

    $$
    \frac{1}{2}(A^\top Q + QA) + \frac{1}{2}Q^2 = 0
    $$

    which gives

    $$
    A^\top Q + QA + Q^2 = 0
    $$

    This is the matrix equation that $Q$ must satisfy. Alternatively, noting that the invariant covariance $\Sigma$ of the linear SDE satisfies $A\Sigma + \Sigma A^\top + I = 0$, one can verify that $Q = \Sigma^{-1}$ satisfies the equation above (multiply the Lyapunov equation by $\Sigma^{-1}$ from both sides). This gives $U(y) = \frac{1}{2}y^\top\Sigma^{-1}y$, consistent with the Gaussian invariant measure $\pi(y) \propto \exp(-\frac{1}{2}y^\top\Sigma^{-1}y) = \exp(-U(y)/\varepsilon)$ in the large deviations scaling.
