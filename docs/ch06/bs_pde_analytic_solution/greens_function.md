# Green's Function and Fundamental Solution

The deepest statement of this subsection is one sentence:

> **For a linear PDE, the response to a unit impulse determines the response to every payoff by superposition.**

The Black–Scholes equation is linear, so a single object — the **fundamental solution**, equivalently the **Green's function** — does all the pricing work. Once it is known, every European option price is one integral away: the payoff against the Green's function. Other subsections compute this object indirectly via heat-equation transforms, Fourier inversion, or probabilistic expectations; here we study the object itself.

!!! tip "Toy mechanism: impulse response + superposition"
    The whole construction is the continuous version of one finite-dimensional fact. Consider the linear system $L\mathbf{x} = \mathbf{b}$, and let $\mathbf{e}_k$ be the $k$-th unit basis vector — the **impulse**. Let $\mathbf{g}_k$ be the **response** to that impulse: the vector solving $L\mathbf{g}_k = \mathbf{e}_k$. Then by linearity, the response to a general right-hand side $\mathbf{b} = \sum_k b_k\, \mathbf{e}_k$ is $\mathbf{x} = \sum_k b_k\, \mathbf{g}_k$ — the *sum* of responses, weighted by the data.

    Replace "vector" with "function," the unit basis vector $\mathbf{e}_k$ with the impulse $\delta(x - z)$, and the sum $\sum_k$ with the integral $\int dz$. The corresponding response is the Green's function $G(\cdot, \cdot;\, z)$ solving $\mathcal{L}\, G = \delta(\cdot - z)$, and the general solution is $u = \int b(z)\, G(\cdot, \cdot;\, z)\, dz$ — the same sum-of-responses formula in continuous form. Every Green's-function formula below is this single template applied to a specific PDE.

---

## 1. Fundamental Solution: Definition

A **fundamental solution** of a linear differential operator $\mathcal{L}$ acting on functions of $(x, t)$ is a function $G(x, t;\, z)$ satisfying

$$
\mathcal{L}\, G(x, t;\, z) = 0 \quad \text{for } t > 0, \qquad G(x, 0;\, z) = \delta(x - z)
$$

The argument $z$ is the location of the impulse; $(x, t)$ is the observation point. By translation invariance, $G(x, t;\, z) = G(x - z, t)$ when the coefficients of $\mathcal{L}$ do not depend on $x$, and we often write just $G(x, t)$ for the impulse located at the origin.

The **Green's function** is the same object viewed through a slightly different lens: for boundary value problems (Dirichlet, Neumann, or initial conditions on a bounded domain) the Green's function additionally encodes the boundary data — it is the impulse response of the *full* problem, boundary conditions included. On all of $\mathbb{R}$ the two notions coincide, and we use them interchangeably.

!!! note "Why the delta"
    The delta function $\delta(x - z)$ is the linear-algebra unit basis lifted to function space: $\int \psi(z)\, \delta(x - z)\, dz = \psi(x)$ for every test function $\psi$. So writing the initial condition as $G(x, 0;\, z) = \delta(x - z)$ is the natural choice that makes the convolution representation below mechanical. The delta is not itself a function but a distribution; rigorous treatments are in the [§ Viscosity Solutions](viscosity_solutions.md) subsection.

---

## 2. The Superposition Representation

Given the fundamental solution and an initial condition $\psi(x)$, linearity forces the solution to be

$$
\boxed{u(x, t) = \int_{-\infty}^{\infty} \psi(z)\, G(x, t;\, z)\, dz}
$$

This is the **Green's function representation**. Two ways to read it:

- **From the data:** decompose $\psi(x) = \int \psi(z)\, \delta(x - z)\, dz$ — a continuous sum of impulses weighted by $\psi$. Each impulse at $z$ evolves into $G(\cdot, t;\, z)$, so by linearity the evolution of $\psi$ is the same sum of those responses.
- **At the observation point:** $u(x, t)$ is the average of $\psi$ over the source locations $z$, weighted by $G(x, t;\, z)$ — the *influence kernel* of $z$ on $(x, t)$.

Both readings give the same formula. The whole content of "solving the PDE" reduces to *computing $G$ once*.

---

## 3. The Heat-Equation Fundamental Solution

For the heat equation $u_t = \kappa\, u_{xx}$ on $\mathbb{R}$, the fundamental solution is the **Gaussian kernel**

$$
\boxed{G(x, t;\, z) = \frac{1}{\sqrt{4\pi\kappa\, t}}\, \exp\!\left(-\frac{(x - z)^2}{4\kappa\, t}\right)}
$$

Recall (see [§ Heat Equation](heat_equation.md)): this is a normal density centered at $z$ with variance $2\kappa\, t$, satisfying $\int G\, dx = 1$ (mass conservation), $G(x, 0;\, z) = \delta(x - z)$ (point-source limit), and $G_t = \kappa\, G_{xx}$ (direct verification). The Green's function representation $u(x, t) = \int \psi(z)\, G(x, t;\, z)\, dz$ is the Gaussian-convolution form of the heat-equation solution.

### 3.1 Derivation by Fourier

The Fourier transform converts the heat equation into an ordinary differential equation in $\omega$:

$$
\hat{u}_t(\omega, t) = -\kappa\, \omega^2\, \hat{u}(\omega, t) \quad\Longrightarrow\quad \hat{u}(\omega, t) = \hat{u}(\omega, 0)\, e^{-\kappa\, \omega^2\, t}
$$

For the impulse $\hat{\delta}(\omega) = 1$, this gives $\hat{G}(\omega, t) = e^{-\kappa\, \omega^2\, t}$ — a Gaussian in $\omega$. Inverting the Fourier transform yields the Gaussian in $x$ above. So the fundamental solution and the characteristic function are *the same object* in different coordinates:

$$
G(x, t;\, 0) \;=\; \mathcal{F}^{-1}\bigl[e^{-\kappa\, \omega^2\, t}\bigr](x)
$$

This is one face of the Core Identity (see [§ Introduction](intro.md)).

### 3.2 Why a Gaussian?

The kernel is Gaussian for a structural reason: the heat equation generates a **convolution semigroup**, and the central limit theorem identifies the only such semigroup with finite second moments. Equivalently, the operator $\partial_t - \kappa\, \partial_{xx}$ is invariant under the parabolic scaling $x \to \lambda x$, $t \to \lambda^2 t$, and the only kernel with this self-similarity and unit mass is the Gaussian. The full scaling argument is the subject of [§ Similarity Solutions](similarity_solutions.md).

---

## 4. The Black–Scholes Fundamental Solution

The Black–Scholes PDE

$$
V_t + \tfrac{1}{2}\sigma^2 S^2\, V_{SS} + r S\, V_S - r V = 0, \qquad V(S, T) = \Phi(S)
$$

reduces to the heat equation under the change of variables

$$
x = \ln(S/K) + (r - \tfrac{1}{2}\sigma^2)\, \tau, \qquad \tau = T - t, \qquad U(x, \tau) = e^{r\tau}\, V(S, t)
$$

(see [§ Heat Equation](heat_equation.md) for the full derivation). The transformed PDE is $U_\tau = \tfrac{1}{2}\sigma^2\, U_{xx}$ — heat with $\kappa = \tfrac{1}{2}\sigma^2$. Its fundamental solution is

$$
G_{\text{heat}}(x, \tau;\, z) = \frac{1}{\sigma\sqrt{2\pi\, \tau}}\, \exp\!\left(-\frac{(x - z)^2}{2\sigma^2\, \tau}\right)
$$

Pulling the change of variables back to $(S, t)$ gives the **Black–Scholes Green's function**:

$$
\boxed{G_{\text{BS}}(S, t;\, S') = \frac{e^{-r\tau}}{S'\, \sigma\sqrt{2\pi\, \tau}}\, \exp\!\left(-\frac{[\ln(S/S') + (r - \tfrac{1}{2}\sigma^2)\, \tau]^2}{2\sigma^2\, \tau}\right)}
$$

with $\tau = T - t$. The factor $1/S'$ comes from the Jacobian $dz/dS' = 1/S'$ of the log transformation; the $e^{-r\tau}$ from the discount factor pulled out of $U = e^{r\tau} V$.

The price of *any* European-style payoff $\Phi(S_T)$ is now one integral:

$$
\boxed{V(S, t) = \int_0^\infty \Phi(S')\, G_{\text{BS}}(S, t;\, S')\, dS'}
$$

Plug in $\Phi(S') = (S' - K)^+$ and the integral collapses to the Black–Scholes call formula $C = S\,\mathcal{N}(d_1) - K e^{-r\tau}\,\mathcal{N}(d_2)$ after completing the square — the same calculation as in [§ Heat Equation](heat_equation.md), recast as a Green's function evaluation.

---

## 5. Three Faces of the Same Object

The Black–Scholes Green's function appears in this chapter under three different names. They are the same object viewed from three different angles:

$$
\underbrace{G_{\text{BS}}(S, t;\, S')}_{\text{Green's function}}
\;=\;
\underbrace{e^{-r\tau}\, p_\tau(S' \mid S)}_{\text{discounted transition density}}
\;=\;
\underbrace{e^{-r\tau}\, \mathcal{F}^{-1}\!\bigl[\varphi(\omega, \tau)\bigr]}_{\text{discounted inverse characteristic function}}
$$

| Viewpoint | Name | Where developed |
|---|---|---|
| PDE | Fundamental solution / Green's function | this subsection |
| Probability | Risk-neutral transition density $p_\tau(S' \mid S)$ of $S_T$ | [§ Feynman–Kac](feynman_kac.md) |
| Spectral | Inverse Fourier transform of $\varphi(\omega, \tau)$ | [§ Fourier Transform](fourier_transform.md) |

The equality is the **Core Identity** of the chapter. Each subsection computes the same kernel by a different route; the discount factor $e^{-r\tau}$ converts an unnormalised diffusion density into the actual pricing kernel. The Green's function viewpoint is the most explicit: it states unambiguously that the option value is *the integral of the payoff against the kernel*.

---

## 6. Properties of the BS Green's Function

The Green's function satisfies a small list of properties that make pricing-by-integration mechanical.

### 6.1 Positivity

$G_{\text{BS}}(S, t;\, S') > 0$ for all $S, S' > 0$ and $\tau > 0$. This is just the positivity of the Gaussian; financially, it expresses the fact that *every* future state has positive risk-neutral probability.

### 6.2 Discounted Mass

Integrating over $S'$ gives the discount factor:

$$
\int_0^\infty G_{\text{BS}}(S, t;\, S')\, dS' = e^{-r\tau}
$$

(not 1, because of the discounting). The probability density $p_\tau(S' \mid S) = e^{r\tau}\, G_{\text{BS}}$ integrates to 1 by construction. Pricing the constant payoff $\Phi \equiv 1$ recovers the zero-coupon bond $e^{-r\tau}$.

### 6.3 Forward Pricing

Pricing the payoff $\Phi(S') = S'$ recovers the spot:

$$
\int_0^\infty S'\, G_{\text{BS}}(S, t;\, S')\, dS' = S
$$

This is the *martingale property* of the discounted stock: $e^{-r\tau}\, \mathbb{E}^{\mathbb{Q}}[S_T] = S$, written as a Green's-function integral. Verifying it by hand is a useful Gaussian-integral exercise (Exercise 4).

### 6.4 Semigroup Composition

For $0 \leq s \leq u \leq t \leq T$, the Green's function composes:

$$
G_{\text{BS}}(S, s;\, S') = e^{r(u-s)} \int_0^\infty G_{\text{BS}}(S, s;\, S'')\, G_{\text{BS}}(S'', u;\, S')\, dS''
$$

This is the **Chapman–Kolmogorov equation** for the BS pricing operator — propagating from $s$ to $t$ in one step equals propagating $s \to u \to t$, with one discount factor restored. It is the operator-theoretic form of $e^{(t-s)\mathcal{L}} = e^{(u-s)\mathcal{L}}\, e^{(t-u)\mathcal{L}}$ (see [§ Introduction § Unifying View](intro.md#a-unifying-view-one-operator-three-representations)).

---

## 7. Bounded Domains and Boundary Value Problems

On all of $\mathbb{R}$ the Green's function method is straightforward; on bounded domains it becomes more delicate. The image method, eigenfunction expansion, and method of reflection are three standard techniques.

### 7.1 Image Method: Single Reflecting Barrier

Consider the heat equation on $x > 0$ with absorbing barrier $u(0, t) = 0$. To make the Green's function vanish at $x = 0$, place a *negative image source* at $-z$:

$$
G_{\text{abs}}(x, t;\, z) = G(x, t;\, z) - G(x, t;\, -z), \qquad x > 0
$$

By the odd symmetry around $x = 0$, the combined kernel satisfies $G_{\text{abs}}(0, t;\, z) = 0$ — exactly the Dirichlet boundary condition. For Neumann conditions $u_x(0, t) = 0$ the image source is positive (a reflected source instead of an inverted one).

### 7.2 Down-and-Out Barrier Option

The down-and-out call with barrier $B < S_0$ has payoff $(S_T - K)^+\, \mathbf{1}_{\{\min_{t \leq T} S_t > B\}}$. Under the log transformation the barrier becomes $\ln(B/K)$ and the absorbing-Green's-function technique above produces a closed-form price as a difference of two BS-style integrals — the standard barrier option formula. The mechanism is exactly: replace $G_{\text{BS}}$ by $G_{\text{BS}}^{\text{abs}}$ in the pricing integral.

### 7.3 Eigenfunction Expansion: Double Barrier

When both ends are absorbing (a corridor), the image method requires *infinitely many* mirrored sources and the cleanest representation is the spectral one — expand the Green's function in eigenfunctions of the spatial operator. This is developed in [§ Separation of Variables](separation_of_variables.md). The eigenvalues, eigenfunctions, and Green's function form one package: the spectral representation of the same pricing operator.

---

## 8. Inhomogeneous Problems: Duhamel's Principle

For PDEs with a source term

$$
u_t - \mathcal{L} u = f(x, t), \qquad u(x, 0) = \psi(x)
$$

the solution decomposes into the homogeneous evolution of the initial data plus the *time-integrated* response to the source:

$$
\boxed{u(x, t) = \int G(x, t;\, z)\, \psi(z)\, dz + \int_0^t \!\!\int G(x, t - s;\, z)\, f(z, s)\, dz\, ds}
$$

This is **Duhamel's principle**: the source term $f$ is treated as a continuous family of impulses, one at each $(z, s)$, and the response of each impulse is propagated forward by the Green's function. In financial applications, the source term encodes continuous dividend payments, deterministic carry, or — when the discounting is absorbed differently — the killing term of the BS PDE itself. The double integral collapses to a single one once $f$ is specified.

---

## 9. Summary

The Green's function is the **single object** that determines all European-option prices under Black–Scholes:

$$
V(S, t) = \int_0^\infty \Phi(S')\, G_{\text{BS}}(S, t;\, S')\, dS'
$$

It is computed explicitly via the heat-equation transform, equivalently obtained as the discounted transition density of geometric Brownian motion, equivalently obtained as the discounted inverse Fourier transform of the characteristic function. These three viewpoints are the central spine of the chapter; the Green's function is their common point.

| Method | Computes the Green's function via |
|---|---|
| Heat equation | Reduction to heat + Gaussian kernel |
| Feynman–Kac | Transition density of GBM under $\mathbb{Q}$ |
| Fourier transform | Inverse Fourier of characteristic function |
| Image method | Add mirrored sources for absorbing/reflecting barriers |
| Eigenfunction expansion | Spectral representation on bounded domains |

The mechanism never changes: solve for the impulse response once, then integrate against the payoff.

---

## Exercises

**Exercise 1.** Verify by direct differentiation that the Gaussian kernel

$$
G(x, t) = \frac{1}{\sqrt{4\pi\kappa\, t}}\, \exp\!\left(-\frac{x^2}{4\kappa\, t}\right)
$$

satisfies the heat equation $G_t = \kappa\, G_{xx}$ for $t > 0$.

??? success "Solution to Exercise 1"
    Write $G(x, t) = (4\pi\kappa t)^{-1/2}\, \exp(-x^2/(4\kappa t))$ and compute the partial derivatives.

    **Time derivative.** Using the product rule on $t^{-1/2}\, \exp(-x^2/(4\kappa t))$:

    $$
    G_t = -\frac{1}{2t}\, G + \frac{x^2}{4\kappa t^2}\, G = G\!\left[-\frac{1}{2t} + \frac{x^2}{4\kappa t^2}\right]
    $$

    **Second spatial derivative.** First $G_x = -\frac{x}{2\kappa t}\, G$, then

    $$
    G_{xx} = -\frac{1}{2\kappa t}\, G + \left(\frac{x}{2\kappa t}\right)^2 G = G\!\left[-\frac{1}{2\kappa t} + \frac{x^2}{4\kappa^2 t^2}\right]
    $$

    Multiply by $\kappa$:

    $$
    \kappa\, G_{xx} = G\!\left[-\frac{1}{2t} + \frac{x^2}{4\kappa t^2}\right] = G_t \quad \checkmark
    $$

---

**Exercise 2.** Use the Green's function representation to verify that the constant payoff $\Phi(S') = 1$ prices the zero-coupon bond:

$$
\int_0^\infty G_{\text{BS}}(S, t;\, S')\, dS' = e^{-r\tau}
$$

??? success "Solution to Exercise 2"
    Under the substitution $z = \ln(S'/K) + (r - \tfrac{1}{2}\sigma^2)\tau$ used to reduce BS to the heat equation, $dS' = S'\, dz$ and the BS Green's function becomes the heat kernel multiplied by $e^{-r\tau}/S'$:

    $$
    \int_0^\infty G_{\text{BS}}(S, t;\, S')\, dS' = e^{-r\tau} \int_{-\infty}^\infty \frac{1}{\sigma\sqrt{2\pi\tau}}\, \exp\!\left(-\frac{(x - z)^2}{2\sigma^2 \tau}\right) dz = e^{-r\tau}
    $$

    where the inner integral equals $1$ because it is the integral of a Gaussian density. The result is the price of a unit cash flow at time $T$, i.e. the zero-coupon bond.

---

**Exercise 3.** Show that the heat-equation Green's function $G(x, t;\, z) = G(x - z, t)$ satisfies the **semigroup property**

$$
\int_{-\infty}^\infty G(x - y, t_1)\, G(y - z, t_2)\, dy = G(x - z, t_1 + t_2)
$$

This is the Chapman–Kolmogorov equation for the heat semigroup.

??? success "Solution to Exercise 3"
    The convolution of two Gaussians is a Gaussian whose variance is the sum of the variances. Concretely:

    $$
    G(x - y, t_1) = \frac{1}{\sqrt{4\pi\kappa t_1}}\, e^{-(x-y)^2/(4\kappa t_1)}, \quad G(y - z, t_2) = \frac{1}{\sqrt{4\pi\kappa t_2}}\, e^{-(y-z)^2/(4\kappa t_2)}
    $$

    Both are normal densities — the first in $y$ with mean $x$ and variance $2\kappa t_1$, the second in $y$ with mean $z$ and variance $2\kappa t_2$. The convolution of $\mathcal{N}(x, 2\kappa t_1)$ and $\mathcal{N}(z, 2\kappa t_2)$ as a function of $y$ integrated out gives $\mathcal{N}(x, 2\kappa (t_1 + t_2))$ evaluated at $z$ (or equivalently $\mathcal{N}(z, 2\kappa(t_1 + t_2))$ evaluated at $x$):

    $$
    \int G(x - y, t_1)\, G(y - z, t_2)\, dy = \frac{1}{\sqrt{4\pi\kappa(t_1 + t_2)}}\, e^{-(x-z)^2/(4\kappa(t_1 + t_2))} = G(x - z, t_1 + t_2)
    $$

    Operator-theoretically, this is the identity $e^{t_1\mathcal{L}}\, e^{t_2\mathcal{L}} = e^{(t_1 + t_2)\mathcal{L}}$ for the heat-equation generator.

---

**Exercise 4.** Verify the forward-pricing identity

$$
\int_0^\infty S'\, G_{\text{BS}}(S, t;\, S')\, dS' = S
$$

by computing the Gaussian integral after the log transformation $z = \ln(S'/K) + (r - \tfrac{1}{2}\sigma^2)\tau$.

??? success "Solution to Exercise 4"
    Under the substitution $S' = K\, e^{z - (r - \tfrac{1}{2}\sigma^2)\tau}$, the integral becomes

    $$
    \int_0^\infty S'\, G_{\text{BS}}\, dS' = e^{-r\tau} \int_{-\infty}^\infty K\, e^{z - (r - \tfrac{1}{2}\sigma^2)\tau}\, \frac{1}{\sigma\sqrt{2\pi\tau}}\, e^{-(x - z)^2/(2\sigma^2\tau)}\, dz
    $$

    where $x = \ln(S/K) + (r - \tfrac{1}{2}\sigma^2)\tau$. Pulling constants out and completing the square in the exponent $z - \frac{(x-z)^2}{2\sigma^2\tau}$:

    $$
    z - \frac{(x-z)^2}{2\sigma^2\tau} = -\frac{(z - x - \sigma^2\tau)^2}{2\sigma^2\tau} + x + \frac{\sigma^2\tau}{2}
    $$

    The Gaussian integral in $z$ evaluates to $1$, leaving

    $$
    e^{-r\tau}\, K\, e^{-(r - \tfrac{1}{2}\sigma^2)\tau}\, e^{x + \sigma^2\tau/2} = e^{-r\tau}\, K\, e^{-r\tau + \tfrac{1}{2}\sigma^2\tau}\, e^{\ln(S/K) + (r - \tfrac{1}{2}\sigma^2)\tau + \sigma^2\tau/2}
    $$

    The exponents collect to $\ln(S/K)$, so the product is $e^{-r\tau}\, K\, (S/K)\, e^{r\tau} = S$, confirming the martingale property of the discounted stock under $\mathbb{Q}$.

---

**Exercise 5.** Derive the Green's function for the heat equation on the half-line $x > 0$ with the absorbing boundary condition $u(0, t) = 0$ using the image method. State and verify the boundary condition.

??? success "Solution to Exercise 5"
    Place a positive source at $z > 0$ and a negative image source at $-z$. The candidate Green's function is

    $$
    G_{\text{abs}}(x, t;\, z) = G(x, t;\, z) - G(x, t;\, -z) = \frac{1}{\sqrt{4\pi\kappa t}}\!\left[e^{-(x-z)^2/(4\kappa t)} - e^{-(x+z)^2/(4\kappa t)}\right]
    $$

    **PDE.** Each term solves the heat equation, so by linearity $G_{\text{abs}}$ does too on $x > 0$.

    **Initial condition.** At $t = 0^+$, only the term centred at $z$ contributes to points $x > 0$ (the image at $-z$ has support on $x < 0$ in the singular limit), so $G_{\text{abs}}(x, 0;\, z) = \delta(x - z)$ on the half-line.

    **Boundary condition.** At $x = 0$:

    $$
    G_{\text{abs}}(0, t;\, z) = \frac{1}{\sqrt{4\pi\kappa t}}\!\left[e^{-z^2/(4\kappa t)} - e^{-z^2/(4\kappa t)}\right] = 0 \quad \checkmark
    $$

    The two terms cancel exactly because $(x - z)^2$ and $(x + z)^2$ agree at $x = 0$. This is the standard image-method construction for Dirichlet conditions on the half-line.

---

**Exercise 6.** State Duhamel's principle for the inhomogeneous heat equation $u_t = \kappa u_{xx} + f(x, t)$ with $u(x, 0) = 0$, and verify the formula by plugging $f(x, t) = \delta(x - z_0)\, \delta(t - s_0)$ for fixed $(z_0, s_0)$ with $0 < s_0 < t$.

??? success "Solution to Exercise 6"
    **Duhamel's principle.** For the inhomogeneous heat equation with zero initial data,

    $$
    u(x, t) = \int_0^t \!\!\int_{-\infty}^\infty G(x - z, t - s)\, f(z, s)\, dz\, ds
    $$

    The integrand treats the source $f(z, s)$ as a continuous family of impulses at $(z, s)$; the kernel $G(x - z, t - s)$ propagates each impulse from time $s$ forward to time $t$.

    **Verification with $f(x, t) = \delta(x - z_0)\, \delta(t - s_0)$.** Plug into the formula:

    $$
    u(x, t) = \int_0^t \!\!\int G(x - z, t - s)\, \delta(z - z_0)\, \delta(s - s_0)\, dz\, ds = G(x - z_0, t - s_0)
    $$

    (using both delta functions to pick out $z = z_0$ and $s = s_0$). This is precisely the heat-equation evolution of an impulse located at $(z_0, s_0)$, observed at $(x, t)$ — which is the definition of the Green's function shifted to source time $s_0$. Duhamel's principle is therefore consistent with the impulse-response definition.

---

**Exercise 7.** A European call on a stock paying a continuous dividend yield $q$ satisfies the PDE $V_t + \tfrac{1}{2}\sigma^2 S^2 V_{SS} + (r - q) S V_S - r V = 0$ with $V(S, T) = (S - K)^+$. Derive the Green's function of this PDE by modifying the no-dividend kernel, and write down the resulting pricing integral.

??? success "Solution to Exercise 7"
    The change of variables $x = \ln(S/K) + (r - q - \tfrac{1}{2}\sigma^2)\tau$, $\tau = T - t$, $U = e^{r\tau}\, V$ reduces the dividend PDE to the heat equation $U_\tau = \tfrac{1}{2}\sigma^2 U_{xx}$ — *exactly* as in the no-dividend case, but with the drift coefficient in $x$ now $r - q$ instead of $r$. The Green's function is therefore the heat kernel pulled back through the new transformation:

    $$
    G_{\text{BS},q}(S, t;\, S') = \frac{e^{-r\tau}}{S'\, \sigma\sqrt{2\pi\tau}}\, \exp\!\left(-\frac{[\ln(S/S') + (r - q - \tfrac{1}{2}\sigma^2)\tau]^2}{2\sigma^2\tau}\right)
    $$

    The only change from the no-dividend formula is the replacement $r \to r - q$ in the drift term inside the exponent; the leading $e^{-r\tau}$ factor (discount) is unchanged because cash flows are still discounted at $r$.

    **Pricing integral.** For the European call:

    $$
    C(S, t) = \int_0^\infty (S' - K)^+\, G_{\text{BS},q}(S, t;\, S')\, dS' = S\, e^{-q\tau}\, \mathcal{N}(d_1^q) - K\, e^{-r\tau}\, \mathcal{N}(d_2^q)
    $$

    where $d_1^q = \frac{\ln(S/K) + (r - q + \tfrac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}$ and $d_2^q = d_1^q - \sigma\sqrt{\tau}$. This is the standard dividend-adjusted Black–Scholes formula, recovered as one Green's-function integral.
