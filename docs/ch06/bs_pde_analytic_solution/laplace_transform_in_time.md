# Laplace Transform in Time

Everything in this subsection follows from one sentence:

> **The Laplace transform turns the time derivative $\partial_\tau$ into multiplication by $p$.**

Where Fourier and Mellin diagonalize the *spatial* operator in the Black–Scholes PDE and leave an ODE in time, the Laplace transform does the opposite — it **freezes time** and leaves an ODE in $S$. For the constant-coefficient Black–Scholes operator that ODE is an **Euler–Cauchy** equation with power-law solutions $S^\lambda$. Inversion (the Bromwich integral) reassembles $V(S, \tau)$ by integrating contributions from every $p$.

We build the picture in the same order a reader naturally builds intuition: a toy first-order ODE in $\tau$, then the BS PDE, and only at the end the operator-theoretic interpretation that names what we have done a **resolvent calculation**.

---

## A Toy Time-Evolution Problem

Before any finance, work the simplest possible time-evolution problem:

$$
u'(\tau) = -a\, u(\tau), \qquad u(0) = u_0
$$

— a first-order ODE with constant coefficient $a$ and known initial datum. Its solution is of course $u(\tau) = u_0\, e^{-a\tau}$, but deriving it through the Laplace transform demonstrates the mechanism that will lift to the BS PDE essentially unchanged.

### The Mechanism

Apply the Laplace transform $\tilde u(p) = \int_0^\infty e^{-p\tau} u(\tau)\, d\tau$ to both sides. The defining identity of the Laplace transform — the only one we will need — is

$$
\mathcal{L}[u'(\tau)] = p\, \tilde u(p) - u(0)
$$

**Time differentiation becomes multiplication by $p$, minus the initial value.** Substituting:

$$
p\, \tilde u(p) - u_0 = -a\, \tilde u(p) \quad\Longrightarrow\quad \tilde u(p) = \frac{u_0}{p + a}
$$

The differential equation has become a single algebraic equation in $p$. To recover $u(\tau)$, invert via the Bromwich integral:

$$
u(\tau) = \frac{1}{2\pi i}\int_{c - i\infty}^{c + i\infty} \frac{u_0}{p + a}\, e^{p\tau}\, dp = u_0\, e^{-a\tau}
$$

closing the contour around the simple pole at $p = -a$ and reading off the residue. The decay rate of the original time-evolution problem is the *location of the pole* of its Laplace transform.

### What Carries Forward

Two observations lift directly to the BS PDE without modification:

- **Pole structure encodes time decay.** A simple pole at $p = -a$ corresponds to an exponential $e^{-a\tau}$. The inverse Laplace transform — sum of residues, or a Bromwich contour — *is* the spectral decomposition of the time-evolution operator. When we lift to a PDE, the algebraic poles of the toy problem become *branch points and resolvent singularities* of the spatial operator.
- **The coefficient $a$ becomes a spatial operator.** In the toy ODE, the right-hand side is $-a\, u$ with $a$ a number. In the BS PDE, the right-hand side is $\mathcal{L} V$ with $\mathcal{L}$ a *differential operator in $S$*. Laplace transforming still gives an "algebraic" equation, but it is now an ODE in $S$ — one ODE for every value of $p$.

### Why Laplace and Not Fourier

Two reasons the time-axis problem $u' = -a u$ wants Laplace, not Fourier:

- **Causality.** The problem is set on $[0, \infty)$ with initial data at $\tau = 0$, not on the full real line. Laplace integrates over $[0, \infty)$ and treats the initial condition explicitly via the $-u(0)$ term in the differentiation identity. Fourier on the half-line would require an artificial extension and lose the initial condition as a clean object.
- **Exponential growth is allowed.** $u(\tau) = u_0 e^{a\tau}$ ($a > 0$) is fine for Laplace as long as $\operatorname{Re}(p) > a$; Fourier would require boundedness, which $u$ lacks.

Whenever the time axis is one-sided and the initial condition is the natural data, Laplace is the right transform. Black–Scholes time-to-maturity $\tau \in [0, T]$ is exactly that setup.

### Spatial Modes and Temporal Decay

Fourier and Laplace are not competitors but complementary halves of one picture. The cleanest illustration is the heat equation $u_t = \kappa\, u_{xx}$. Decompose the spatial profile $u(\cdot, t)$ into Fourier modes:

$$
u(x, t) = \int \hat u(\omega, t)\, e^{i\omega x}\, d\omega
$$

Substituting one mode into the PDE gives $\hat u_t(\omega, t) = -\kappa\omega^2\, \hat u(\omega, t)$ — a *first-order ODE in $\tau$* of exactly the form $u' = -a u$ from the toy above, with decay rate $a = \kappa\omega^2$. Solving:

$$
\hat u(\omega, t) = \hat u(\omega, 0)\, e^{-\kappa\omega^2 t} \quad\Longrightarrow\quad u(x, t) = \int \hat u(\omega, 0)\, e^{-\kappa\omega^2 t}\, e^{i\omega x}\, d\omega
$$

This is the **spectral-semigroup picture**: *oscillation in space, exponential decay in time*. Fourier decomposes space into eigenmodes $e^{i\omega x}$; each mode evolves by multiplication by an exponential whose rate depends on the wavenumber; Laplace is the natural transform of those exponentials. High frequencies decay faster ($\omega^2$ scaling) — *which is exactly why heat smooths sharp features*.

For Black–Scholes the same picture holds verbatim, with log-price coordinates supplying the spatial modes:

- **Fourier/Mellin** $\to$ spatial modes (plane waves $e^{i\omega x}$ or power laws $S^s$);
- **Time evolution** $\to$ each mode multiplied by an exponential $e^{\psi(\omega)\tau}$ (characteristic exponent of the diffusion);
- **Laplace** $\to$ treats those exponentials algebraically via poles and resolvents — the eigenvalues of the time-translation semigroup.

The kernel duality is exact: writing $p = i\omega$ in the Bromwich integral recovers the Fourier transform, so

$$
\text{Fourier} = \text{Laplace restricted to } p = i\omega
$$

Laplace handles what Fourier cannot — exponentially decaying or growing initial data, one-sided time axes, transient pole structure — while sharing the same spectral decomposition once $\operatorname{Re}(p) > 0$. The full Combined Fourier–Laplace section below makes the two-variable factorisation $\tilde{\hat V}(\omega, p) = \hat\Phi(\omega) / (p - \psi(\omega))$ explicit.

!!! tip "Core principle"
    Laplace transforms convert one-sided time evolution into an algebraic problem in the Laplace variable $p$. For a PDE in $(S, \tau)$ the algebra becomes an ODE in $S$ — one ODE per value of $p$ — and the inverse transform reassembles the solution from contributions across all $p$. Combined with a spatial Fourier (or Mellin) transform, this gives the **spectral-semigroup picture** of pricing: spatial oscillations multiplied by exponential decays whose rates are the characteristic exponents of the underlying diffusion.

This is the mechanism. Black–Scholes is the application.

---

## Laplace Transform Definition

The **Laplace transform** of $V(S,\tau)$ in time-to-maturity $\tau = T - t$ is

$$
\tilde{V}(S,p) = \int_0^{\infty} V(S,\tau) e^{-p\tau} \, d\tau, \qquad \operatorname{Re}(p) \text{ large enough for convergence}
$$

with inverse given by the **Bromwich integral**

$$
V(S,\tau) = \frac{1}{2\pi i} \int_{c - i\infty}^{c + i\infty} \tilde{V}(S,p) \, e^{p\tau} \, dp
$$

where $c$ lies to the right of all singularities of $\tilde{V}$. The key
operational property is

$$
\mathcal{L}\!\left[\partial_\tau V\right] = p \, \tilde{V}(S,p) - V(S,0)
$$

with $V(S,0) = \Phi(S)$ the payoff — this is what converts time differentiation
into multiplication by $p$.

---

## Transforming the Black-Scholes PDE

!!! note "Recall"
    The Black–Scholes PDE in $\tau = T - t$ form,
    $\partial_\tau V = \mathcal{L} V$ with
    $\mathcal{L} = \tfrac{\sigma^2}{2} S^2 \partial_{SS} + r S \partial_S - r$,
    and the initial condition $V(S,0) = \Phi(S)$, are the canonical
    [§ Heat Equation](heat_equation.md) setup carried over to $S$-coordinates.

Because $S$ is not the transform variable, $S$-derivatives pass through the integral.
Applying the Laplace transform in $\tau$ and using $\mathcal{L}[\partial_\tau V] = p\tilde{V} - \Phi(S)$
turns the PDE into the resolvent equation

$$
\frac{\sigma^2}{2} S^2 \frac{d^2 \tilde{V}}{dS^2} + r S \frac{d \tilde{V}}{dS} - (r + p) \, \tilde{V} = -\Phi(S)
$$

a **second-order ODE in** $S$ — the time variable has been completely eliminated.
This is the mirror of Fourier/Mellin, which eliminate the spatial variable and
leave an ODE in time.

---

## The Euler-Cauchy Structure

The homogeneous part of the transformed equation,

$$
\frac{\sigma^2}{2} S^2 \tilde{V}'' + r S \tilde{V}' - (r + p) \tilde{V} = 0
$$

is an **Euler-Cauchy** (equidimensional) equation. Its solutions are power laws
$\tilde{V} = S^{\lambda}$. Substituting this ansatz:

$$
\frac{\sigma^2}{2} \lambda(\lambda - 1) + r\lambda - (r + p) = 0
$$

Expanding:

$$
\frac{\sigma^2}{2} \lambda^2 + \left(r - \frac{\sigma^2}{2}\right) \lambda - (r + p) = 0
$$

This is a quadratic in $\lambda$ with roots

$$
\lambda_{\pm}(p) = \frac{-\!\left(r - \dfrac{\sigma^2}{2}\right) \pm \sqrt{\left(r - \dfrac{\sigma^2}{2}\right)^2 + 2\sigma^2(r + p)}}{\sigma^2}
$$

For $\operatorname{Re}(p)$ sufficiently large, the discriminant is positive and the
two roots are real with $\lambda_+ > 0$ and $\lambda_- < 0$.

The **general homogeneous solution** is therefore

$$
\tilde{V}_h(S,p) = A(p) \, S^{\lambda_+(p)} + B(p) \, S^{\lambda_-(p)}
$$

where $A(p)$ and $B(p)$ are determined by boundary conditions and the payoff.

---

## Solving for the European Call

For $\Phi(S) = (S - K)^+$, write
$\tilde{V}(S,p) = A(p) S^{\lambda_+} + B(p) S^{\lambda_-} + \tilde{V}_p(S,p)$, with
$\tilde{V}_p$ a particular solution built from the Euler–Cauchy Green's function.
Boundary conditions $\tilde{V} \to 0$ as $S \to 0$ and $\tilde{V} \sim S/p$ as
$S \to \infty$ fix the constants. Bromwich inversion then recovers the
Black–Scholes formula; the $(d_1, d_2)$ structure is the canonical
[§ Heat Equation](heat_equation.md) derivation and is not reproved here.

---

## Log-Price Formulation

In log-price coordinates $x = \ln S$ — the same change of variables that converts
Black–Scholes to the [§ Heat Equation](heat_equation.md) — the resolvent ODE becomes

$$
\frac{\sigma^2}{2} \frac{d^2 \tilde{V}}{dx^2} + \left(r - \frac{\sigma^2}{2}\right) \frac{d\tilde{V}}{dx} - (r + p) \, \tilde{V} = -\Phi(e^x)
$$

a **constant-coefficient** ODE (the Euler–Cauchy $S$-dependence is absorbed). The
characteristic quadratic is unchanged and the homogeneous solutions are
$e^{\lambda_\pm x}$.

The Green's function on $x \in (-\infty, \infty)$ is

$$
\tilde{G}(x, y; p) = \frac{1}{\frac{\sigma^2}{2}(\lambda_+ - \lambda_-)}
\begin{cases}
e^{\lambda_-(x - y)}, & x > y \\[4pt]
e^{\lambda_+(x - y)}, & x < y
\end{cases}
$$

and the particular solution is
$\tilde{V}(x,p) = \int_{-\infty}^{\infty} \tilde{G}(x,y;p) \, \Phi(e^y) \, dy$.

---

## Laplace Inversion and Numerical Methods

The option price is recovered from $\tilde{V}(S,p)$ via the Bromwich integral

$$
V(S,\tau) = \frac{1}{2\pi i} \int_{c - i\infty}^{c + i\infty} \tilde{V}(S,p) \, e^{p\tau} \, dp
$$

In practice, **numerical inversion** is the working tool. The standard methods are
the **Gaver–Stehfest** algorithm (real evaluations only, limited precision),
**Talbot's method** (deformed contour, rapid convergence), and the **Abate–Whitt
Euler method** (trapezoidal rule with Euler summation). For Black–Scholes with
constant parameters, Gaver–Stehfest with $N = 12$ typically gives 5–6 digits.

??? note "Advanced Remark: Bromwich Contour Inversion"
    A rigorous analytic inversion is more delicate than the integral suggests, and
    the discussion below is a sketch rather than a proof.

    *Region of analyticity.* The transform $\tilde{V}(S,p) = (p - \mathcal{L})^{-1}\Phi$
    is analytic on the resolvent set of $\mathcal{L}$, which for Black–Scholes contains
    a right half-plane $\operatorname{Re}(p) > \omega_0$ for some growth bound $\omega_0$
    determined by the payoff. The Bromwich abscissa $c$ must lie in this region.

    *Singular structure.* The roots $\lambda_\pm(p)$ involve the square root
    $\sqrt{(r - \sigma^2/2)^2 + 2\sigma^2(r + p)}$, which has a **branch point** at
    $p^* = -r - (r - \sigma^2/2)^2/(2\sigma^2)$. The natural choice is a branch cut
    along $(-\infty, p^*]$. Beyond the branch point there may also be poles from
    boundary conditions or from the payoff transform.

    *Contour deformation.* To extract large-$\tau$ asymptotics, the vertical
    Bromwich contour is deformed leftward past poles (contributing residues) and
    wrapped around the branch cut (contributing a Hankel-type integral). The
    branch-cut integral produces the $\tau^{-1/2} e^{p^* \tau}$ decay derived in
    Exercise 6.

    A careful treatment — analytic continuation, deformation, and asymptotic
    expansion — belongs to a course on operational calculus; see Doetsch,
    *Introduction to the Theory and Application of the Laplace Transformation*,
    or Widder, *The Laplace Transform*, for the full machinery.

---

## Combined Fourier–Laplace Transform

Applying Fourier in $x$ *and* Laplace in $\tau$ together gives a **complete spectral
decomposition**: Fourier diagonalises the spatial generator $\mathcal{L}$ in
$\omega$-space (each plane wave $e^{i\omega x}$ is an eigenfunction with eigenvalue
$\psi(\omega)$ — see [§ Fourier Transform](fourier_transform.md)), while Laplace
diagonalises the time-translation semigroup in $p$-space.

The double transform reduces the PDE to the **algebraic** equation
$(p - \psi(\omega))\tilde{\hat{V}}(\omega,p) = \hat{\Phi}(\omega)$ with characteristic
exponent
$\psi(\omega) = -\tfrac{\sigma^2 \omega^2}{2} + i\omega(r - \tfrac{\sigma^2}{2}) - r$,
so

$$
\tilde{\hat{V}}(\omega, p) = \frac{\hat{\Phi}(\omega)}{p - \psi(\omega)}
$$

Inverting first in $p$ (simple pole at $p = \psi(\omega)$) yields
$\hat{V}(\omega,\tau) = \hat{\Phi}(\omega)e^{\psi(\omega)\tau}$, which is the
[§ Fourier Transform](fourier_transform.md) solution. The two inversions
**commute**, and the resolvent factorisation makes the consistency manifest. The
subsequent inversion in $\omega$ that recovers the heat-kernel representation is
the canonical [§ Heat Equation](heat_equation.md) calculation; we do not repeat
it here.

Geometrically: $\omega$ parametrises spatial modes, $p$ parametrises temporal modes,
and the pole locus $p = \psi(\omega)$ is the **dispersion relation** of the pricing
operator. This is the same structure as in the Schrödinger / heat-equation
literature, transplanted to finance.

### The Semigroup-Resolvent Identity

The Laplace transform and the pricing semigroup are linked by a single identity that unifies semigroup theory, Green's functions, and Laplace inversion:

$$
\boxed{(pI - \mathcal{L})^{-1} = \int_0^\infty e^{-p\tau}\, e^{\tau\mathcal{L}}\, d\tau}
$$

Read both sides as operators on payoffs. The right-hand side is the **Laplace transform of the pricing semigroup** $\mathcal{P}_\tau = e^{\tau\mathcal{L}}$ (recall [§ Introduction § A Unifying View](intro.md#a-unifying-view-one-operator-three-representations)); the left-hand side is the **resolvent** $R_p := (pI - \mathcal{L})^{-1}$ of the generator $\mathcal{L}$. The identity holds whenever $\operatorname{Re}(p) > \omega(\mathcal{L})$ (the growth bound of the semigroup), and the integral converges in the operator norm. It is the operator-valued version of the elementary scalar identity $1/(p - a) = \int_0^\infty e^{-p\tau}\, e^{a\tau}\, d\tau$ that drove the toy ODE above.

Three of the chapter's representations collapse onto this one identity:

- **Semigroup view.** $e^{\tau\mathcal{L}}$ is the pricing operator; its Laplace transform is the resolvent.
- **Green's-function view.** Applied to a payoff $\Phi$, the right-hand side is $\int_0^\infty e^{-p\tau}\, V(\cdot, \tau)\, d\tau = \tilde V(\cdot, p)$ — the Laplace transform of the price — and the left-hand side is the Green's function of the *modified* operator $(pI - \mathcal{L})$, namely the time-independent BS PDE with shift $-p$. The Euler–Cauchy structure of §"The Euler-Cauchy Structure" is exactly the resolvent of $\mathcal{L}$ acting on power-law payoffs.
- **Spectral view.** The poles of $R_p$ on the real axis are the (generalised) eigenvalues of $\mathcal{L}$; the Bromwich integral that inverts $\tilde V(\cdot, p)$ is the **spectral decomposition** of the pricing semigroup. For pure BS, the spectrum is continuous (along the parabola $p = \psi(\omega)$); for bounded-domain problems (barrier options, [§ Separation of Variables](separation_of_variables.md)) it becomes discrete.

The resolvent identity is therefore the bridge between "solve the time-independent ODE in $S$ at each $p$" (the calculation we have been doing) and the abstract operator picture in which Black–Scholes pricing is *Laplace inversion of the resolvent of a parabolic generator*. The perpetual-options limit below is the $p = 0$ case: the resolvent at zero, $\mathcal{L}^{-1}$, is exactly the Green's function of the time-independent BS PDE.

---

## Perpetual Options as the Zero-Frequency Limit

The Laplace transform connects naturally to **perpetual** (infinite-maturity) options.
For a perpetual option, $\partial_\tau V = 0$ and the PDE reduces to

$$
\frac{\sigma^2}{2} S^2 V'' + r S V' - r V = 0
$$

which is exactly the homogeneous Euler–Cauchy equation at $p = 0$. The Laplace
parameter $p$ thus acts as a **frequency conjugate to time**: $p = 0$ is the
stationary (perpetual) case; $p \neq 0$ captures transient decay.

For a perpetual American put with strike $K$, smooth pasting at $S^*$
($V(S^*) = K - S^*$, $V'(S^*) = -1$) and $V \to 0$ as $S \to \infty$ select the
$\lambda_-(0)$ branch, giving $V(S) = (K - S^*)(S/S^*)^{\lambda_-}$ for $S > S^*$
(see Exercise 5).

### Where Laplace Genuinely Helps

The two settings where the Laplace approach dominates Fourier are worth naming
explicitly.

- **Time-dependent coefficients.** When $\sigma = \sigma(t)$ or $r = r(t)$, the
  Fourier-only approach fails because the characteristic exponent itself becomes
  time-dependent and the ODE in $\tau$ no longer has exponential solutions. But
  the Laplace transform in $\tau$ still removes the time derivative, leaving an
  ODE in $S$ whose *coefficients* depend on $p$ in a controlled way. A concrete
  case: deterministic volatility $\sigma(t)$ entering through an *integrated*
  variance $\Sigma(\tau) = \int_0^\tau \sigma^2(s)\,ds$. A change of time variable
  $\tau \mapsto \Sigma$ followed by Laplace transform reduces the problem to the
  constant-coefficient case studied above, with $p$ as the conjugate variable.

- **First-passage and barrier problems.** For barrier and stopping-time problems
  the Laplace transform of the *hitting-time distribution* is naturally a power
  $S^{\lambda_\pm(p)}$ — the same Euler–Cauchy roots reappear. The perpetual put
  above is in fact the simplest such example (with $p = 0$). For Parisian and
  occupation-time options, the Laplace framework is essentially the only tractable
  one.

In short: whenever the time structure resists separation of variables, Laplace
turns the obstruction into an algebraic dependence on $p$.

---

## Advantages and Limitations

| Aspect | Laplace in $\tau$ | Fourier / Mellin in $x, S$ |
|---|---|---|
| Variable removed | Time $\tau$ | Spatial $x$ or $S$ |
| Resulting equation | ODE in $S$ (Euler–Cauchy) | ODE in $\tau$ (first-order) |
| Time-dependent coefficients | Handled naturally | Destroy the approach |
| Inversion | Numerical (Bromwich) | FFT or residues |
| Free-boundary problems | Natural | Difficult |

For constant-parameter European options the Fourier route with FFT is typically
faster; numerical Laplace inversion is inherently ill-conditioned. Laplace earns
its place on problems where the time structure resists separation: time-dependent
parameters, American/free-boundary problems, and perpetual structures.

The unifying picture is the **resolvent identity** $\tilde{V}(S,p) = (p - \mathcal{L})^{-1}\Phi$.
Inversion via the Bromwich integral is the operator-theoretic statement
$\mathcal{P}_\tau = \frac{1}{2\pi i} \oint e^{p\tau}(p - \mathcal{L})^{-1} dp$, expressing
the semigroup as a contour integral of its resolvent — exactly the
Hille–Yosida / Dunford functional calculus, specialised to the Black–Scholes generator.

---

## Exercises

**Exercise 1.** Starting from the log-price Black-Scholes PDE, apply the Laplace transform in the time variable $\tau$ and derive the resulting constant-coefficient ODE in $x = \ln S$. Find the characteristic equation and its roots $\lambda_{\pm}(p)$. Verify that $\lambda_+(p) > 0 > \lambda_-(p)$ when $p > 0$.

??? success "Solution to Exercise 1"
    Starting from the log-price formulation with $x = \ln S$ and $\tau = T - t$:

    $$
    \frac{\partial V}{\partial \tau} = \frac{\sigma^2}{2}\frac{\partial^2 V}{\partial x^2} + \left(r - \frac{\sigma^2}{2}\right)\frac{\partial V}{\partial x} - rV
    $$

    Apply the Laplace transform in $\tau$: $\tilde{V}(x,p) = \int_0^{\infty}V(x,\tau)e^{-p\tau}d\tau$. Using $\mathcal{L}\!\left[\frac{\partial V}{\partial \tau}\right] = p\tilde{V}(x,p) - V(x,0)$ and the fact that $x$-derivatives pass through the $\tau$-integral:

    $$
    p\tilde{V} - \Phi(e^x) = \frac{\sigma^2}{2}\frac{d^2 \tilde{V}}{dx^2} + \left(r - \frac{\sigma^2}{2}\right)\frac{d\tilde{V}}{dx} - r\tilde{V}
    $$

    Rearranging:

    $$
    \frac{\sigma^2}{2}\frac{d^2 \tilde{V}}{dx^2} + \left(r - \frac{\sigma^2}{2}\right)\frac{d\tilde{V}}{dx} - (r+p)\tilde{V} = -\Phi(e^x)
    $$

    The characteristic equation of the homogeneous part is

    $$
    \frac{\sigma^2}{2}\lambda^2 + \left(r - \frac{\sigma^2}{2}\right)\lambda - (r+p) = 0
    $$

    with roots

    $$
    \lambda_{\pm} = \frac{-\!\left(r - \frac{\sigma^2}{2}\right) \pm \sqrt{\left(r - \frac{\sigma^2}{2}\right)^2 + 2\sigma^2(r+p)}}{\sigma^2}
    $$

    To verify the sign: let $a = r - \frac{\sigma^2}{2}$ and $D = a^2 + 2\sigma^2(r+p)$. For $p > 0$, we have $D > a^2 > 0$, so $\sqrt{D} > |a|$. Then $\lambda_+ = \frac{-a + \sqrt{D}}{\sigma^2} > 0$ (since $\sqrt{D} > |a| \geq a$) and $\lambda_- = \frac{-a - \sqrt{D}}{\sigma^2} < 0$ (since $-a - \sqrt{D} < 0$ regardless of the sign of $a$). $\square$

---

**Exercise 2.** The Euler-Cauchy equation $\frac{\sigma^2}{2}S^2 \tilde{V}'' + rS\tilde{V}' - (r+p)\tilde{V} = 0$ has solutions $S^{\lambda_{\pm}}$. Verify this by direct substitution. Then show that the product $\lambda_+ \cdot \lambda_-$ equals $-2(r+p)/\sigma^2$ and explain why this implies the two solutions have different growth behavior as $S \to \infty$.

??? success "Solution to Exercise 2"
    Substitute $\tilde{V} = S^{\lambda}$ into the ODE. We need $\tilde{V}' = \lambda S^{\lambda - 1}$ and $\tilde{V}'' = \lambda(\lambda - 1)S^{\lambda - 2}$:

    $$
    \frac{\sigma^2}{2}S^2 \cdot \lambda(\lambda-1)S^{\lambda-2} + rS \cdot \lambda S^{\lambda-1} - (r+p)S^{\lambda} = 0
    $$

    $$
    \left[\frac{\sigma^2}{2}\lambda(\lambda-1) + r\lambda - (r+p)\right]S^{\lambda} = 0
    $$

    For this to hold for all $S > 0$, the bracket must vanish, giving the characteristic equation $\frac{\sigma^2}{2}\lambda^2 + (r - \frac{\sigma^2}{2})\lambda - (r+p) = 0$. $\checkmark$

    By Vieta's formulas for the quadratic $\frac{\sigma^2}{2}\lambda^2 + (r - \frac{\sigma^2}{2})\lambda - (r+p) = 0$:

    $$
    \lambda_+ \cdot \lambda_- = \frac{-(r+p)}{\sigma^2/2} = -\frac{2(r+p)}{\sigma^2}
    $$

    Since $r + p > 0$ (for $p > 0$ and $r \geq 0$), we have $\lambda_+ \cdot \lambda_- < 0$, confirming the roots have opposite signs. As $S \to \infty$: $S^{\lambda_+} \to \infty$ (growing) and $S^{\lambda_-} \to 0$ (decaying). As $S \to 0$: $S^{\lambda_+} \to 0$ (decaying) and $S^{\lambda_-} \to \infty$ (blowing up). This asymmetric behavior is what allows the boundary conditions to select a unique solution. $\square$

---

**Exercise 3.** For the combined Fourier-Laplace transform, show that the double transform $\tilde{\hat{V}}(\omega,p) = \hat{\Phi}(\omega)/(p - \psi(\omega))$ has a simple pole in the $p$-variable at $p = \psi(\omega)$. Evaluate the Bromwich integral in $p$ using the residue theorem and verify that one recovers the standard Fourier-only solution $\hat{V}(\omega,\tau) = \hat{\Phi}(\omega)e^{\psi(\omega)\tau}$.

??? success "Solution to Exercise 3"
    The double transform is $\tilde{\hat{V}}(\omega,p) = \frac{\hat{\Phi}(\omega)}{p - \psi(\omega)}$. For fixed $\omega$, this is a function of $p$ with a **simple pole** at $p = \psi(\omega)$, since the denominator vanishes to first order there and the numerator $\hat{\Phi}(\omega)$ does not depend on $p$.

    To invert in $p$, compute the Bromwich integral:

    $$
    \hat{V}(\omega,\tau) = \frac{1}{2\pi i}\int_{c-i\infty}^{c+i\infty} \frac{\hat{\Phi}(\omega)}{p - \psi(\omega)} \, e^{p\tau} \, dp
    $$

    Choose $c > \operatorname{Re}(\psi(\omega))$ so the contour lies to the right of the pole. Close the contour with a large semicircle to the left. For $\tau > 0$, $|e^{p\tau}|$ decays as $\operatorname{Re}(p) \to -\infty$, so the semicircular arc contributes nothing (by Jordan's lemma).

    The only enclosed singularity is the simple pole at $p = \psi(\omega)$. The residue is:

    $$
    \operatorname{Res}_{p = \psi(\omega)} \frac{\hat{\Phi}(\omega) \, e^{p\tau}}{p - \psi(\omega)} = \hat{\Phi}(\omega) \, e^{\psi(\omega)\tau}
    $$

    By the residue theorem (contour traversed counterclockwise encloses the pole):

    $$
    \hat{V}(\omega,\tau) = \hat{\Phi}(\omega) \, e^{\psi(\omega)\tau}
    $$

    This is exactly the Fourier-only solution, confirming consistency. $\square$

---

**Exercise 4.** The Gaver-Stehfest method approximates the inverse Laplace transform using only real-valued evaluations: $V(S,\tau) \approx \frac{\ln 2}{\tau}\sum_{k=1}^{N} c_k \, \tilde{V}(S, k\ln 2/\tau)$. Explain why this method requires high-precision arithmetic when $N$ is large. For the Black-Scholes call in Laplace space, describe how you would compute $\tilde{V}(S,p)$ for a given real $p > 0$.

??? success "Solution to Exercise 4"
    **Why high-precision arithmetic is needed.** The Gaver-Stehfest weights $c_k$ are given by a combinatorial formula involving alternating sums of products of factorials and binomial coefficients. For even moderate $N$ (say $N = 12$), the weights $c_k$ grow to values of order $10^6$ or larger, and they alternate in sign. The approximation therefore involves massive cancellation: the sum of terms of order $10^6$ produces a result of order $1$. In floating-point arithmetic with $d$ digits, roughly $6$ digits are lost to cancellation when $N = 12$, leaving only $d - 6$ reliable digits. For $N = 20$, the cancellation consumes about $10$ digits. This limits the achievable accuracy to roughly $0.6N$ digits in exact arithmetic, and far fewer in standard double precision ($d \approx 16$).

    **Computing $\tilde{V}(S,p)$ for a given $p > 0$.** For the European call with $\Phi(S) = (S-K)^+$:

    1. Compute $\lambda_{\pm}(p)$ from the characteristic equation.
    2. Construct the Green's function for the Euler-Cauchy operator on $(0,\infty)$ with the two homogeneous solutions $S^{\lambda_+}$ and $S^{\lambda_-}$.
    3. The particular solution is $\tilde{V}_p(S,p) = \int_0^{\infty} G(S,S';p)(S'-K)^+ dS'$, where the Green's function is built from the Wronskian of $S^{\lambda_+}$ and $S^{\lambda_-}$.
    4. Apply boundary conditions ($\tilde{V} \to 0$ as $S \to 0$; $\tilde{V} \sim S/p$ as $S \to \infty$) to eliminate the unbounded homogeneous contributions.
    5. The resulting $\tilde{V}(S,p)$ involves integrals of power functions against $(S'-K)^+$, which can be evaluated in closed form using the Beta function. $\square$

---

**Exercise 5.** Show that the Laplace transform of the Black-Scholes PDE with $p = 0$ recovers the ODE for perpetual options. For a perpetual American put with strike $K$, use the boundary conditions $V(S^*) = K - S^*$ and $V'(S^*) = -1$ (smooth pasting) together with $V(S) \to 0$ as $S \to \infty$ to find $S^*$ and $V(S)$ in closed form.

??? success "Solution to Exercise 5"
    Setting $p = 0$ in the Laplace-transformed ODE gives

    $$
    \frac{\sigma^2}{2}S^2 V'' + rSV' - rV = 0
    $$

    which is the time-independent Black-Scholes equation for a perpetual option. The characteristic equation becomes $\frac{\sigma^2}{2}\lambda^2 + (r - \frac{\sigma^2}{2})\lambda - r = 0$, which factors as $\frac{\sigma^2}{2}(\lambda - 1)(\lambda + \frac{2r}{\sigma^2}) = 0$. So $\lambda_+ = 1$ and $\lambda_- = -2r/\sigma^2$.

    For the perpetual American put, the value must satisfy $V(S) \to 0$ as $S \to \infty$, so the solution for $S > S^*$ is $V(S) = C \cdot S^{\lambda_-}$ (the $S^{\lambda_+} = S$ solution is excluded because it grows).

    **Value matching:** $V(S^*) = C(S^*)^{\lambda_-} = K - S^*$.

    **Smooth pasting:** $V'(S^*) = C\lambda_-(S^*)^{\lambda_- - 1} = -1$.

    Dividing the second equation by the first: $\frac{\lambda_-}{S^*} = \frac{-1}{K - S^*}$, which gives $\lambda_-(K - S^*) = -S^*$, hence $S^* = \frac{\lambda_- K}{\lambda_- - 1}$.

    Substituting $\lambda_- = -2r/\sigma^2$:

    $$
    S^* = \frac{(-2r/\sigma^2)K}{-2r/\sigma^2 - 1} = \frac{2rK}{2r + \sigma^2}
    $$

    From value matching: $C = (K - S^*)(S^*)^{-\lambda_-}$, and the perpetual put price for $S \geq S^*$ is

    $$
    V(S) = (K - S^*)\left(\frac{S}{S^*}\right)^{\lambda_-} = (K - S^*)\left(\frac{S}{S^*}\right)^{-2r/\sigma^2}
    $$

    $\square$

---

**Exercise 6.** The singularity structure of $\tilde{V}(S,p)$ in the complex $p$-plane determines the large-$\tau$ behavior of $V(S,\tau)$. The discriminant of the characteristic equation vanishes at $p^* = -r - \frac{(r - \sigma^2/2)^2}{2\sigma^2}$. Explain why $p^*$ is a branch point of $\tilde{V}(S,p)$, and show that for $\tau \to \infty$ the option price decays as $V(S,\tau) \sim e^{p^* \tau} \tau^{-1/2}$ (up to algebraic prefactors).

??? success "Solution to Exercise 6"
    The roots $\lambda_{\pm}(p)$ involve the square root $\sqrt{(r - \sigma^2/2)^2 + 2\sigma^2(r+p)}$. This square root vanishes when

    $$
    (r - \sigma^2/2)^2 + 2\sigma^2(r+p) = 0 \implies p = p^* = -r - \frac{(r-\sigma^2/2)^2}{2\sigma^2}
    $$

    At $p = p^*$, the two roots coalesce: $\lambda_+ = \lambda_-$. Near $p^*$, the square root behaves as $\sqrt{2\sigma^2(p - p^*)}$, which is a branch point of order $1/2$. Consequently, $\lambda_{\pm}(p)$ and therefore $\tilde{V}(S,p)$ have a branch point at $p = p^*$.

    **Large-$\tau$ behavior.** The Bromwich integral is dominated by the singularity of $\tilde{V}$ closest to the right of the contour. The branch point at $p^*$ is on the negative real axis (note $p^* < 0$ since all terms are negative). Near $p^*$:

    $$
    \tilde{V}(S,p) \sim \frac{f(S)}{\sqrt{p - p^*}} + \text{analytic terms}
    $$

    By the Tauberian theorem for Laplace transforms, a singularity $(p - p^*)^{-1/2}$ in the transform corresponds to $\tau^{-1/2}$ in the time domain. Therefore:

    $$
    V(S,\tau) \sim f(S) \cdot \frac{e^{p^*\tau}}{\sqrt{\pi\tau}} \quad \text{as } \tau \to \infty
    $$

    Since $p^* < 0$, the option value decays exponentially in $\tau$ with rate $|p^*|$, modulated by the algebraic factor $\tau^{-1/2}$. Note that $|p^*| = r + \frac{(r-\sigma^2/2)^2}{2\sigma^2}$, which combines the discounting rate $r$ with a contribution from the drift-volatility interaction. $\square$
