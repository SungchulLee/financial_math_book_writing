# Laplace Transform in Time

The Laplace transform in the time variable provides a distinctive approach to solving
the Black-Scholes PDE: it freezes the time evolution and studies the pricing operator through its **resolvent**. While the Fourier and Mellin transforms act on the spatial
variable (log-price or stock price) and reduce the PDE to an ODE in time, the Laplace
transform acts on time-to-maturity $\tau = T - t$ and reduces the PDE to an ODE in the
spatial variable $S$. The resulting equation is an **Euler-Cauchy ODE** whose solutions
are power laws $S^{\lambda}$, connecting option pricing to classical ODE theory.

This approach is especially valuable when the interest rate $r$ or volatility $\sigma$
depends on time, because the Laplace transform in $\tau$ still removes the
time derivative even when the spatial coefficients vary with $t$. It also provides
the natural framework for perpetual options and for problems where the time structure
is more complex than the spatial structure.

---

## Laplace Transform Definition

The **Laplace transform** of the option value $V(S,\tau)$ with respect to time-to-maturity
$\tau = T - t$ is defined by

$$
\tilde{V}(S,p) = \mathcal{L}[V](S,p) = \int_0^{\infty} V(S,\tau) e^{-p\tau} \, d\tau
$$

where $p \in \mathbb{C}$ with $\operatorname{Re}(p)$ sufficiently large to ensure convergence
of the integral.

The **inverse Laplace transform** (Bromwich integral) recovers $V$ from $\tilde{V}$:

$$
V(S,\tau) = \frac{1}{2\pi i} \int_{c - i\infty}^{c + i\infty} \tilde{V}(S,p) \, e^{p\tau} \, dp
$$

where $c > 0$ is chosen so that the vertical contour lies to the right of all
singularities of $\tilde{V}(S,p)$ in the complex $p$-plane.

The key operational property for our purposes is the transform of the time derivative:

$$
\mathcal{L}\!\left[\frac{\partial V}{\partial \tau}\right] = p \, \tilde{V}(S,p) - V(S,0)
$$

This identity converts the time derivative into an algebraic expression involving
the initial condition $V(S,0) = \Phi(S)$.

---

## Transforming the Black-Scholes PDE

Write the Black-Scholes PDE in terms of time-to-maturity $\tau = T - t$:

$$
\frac{\partial V}{\partial \tau} = \frac{\sigma^2}{2} S^2 \frac{\partial^2 V}{\partial S^2} + r S \frac{\partial V}{\partial S} - r V
$$

Apply the Laplace transform in $\tau$. Because $S$ is not the transform variable,
the $S$-derivatives pass through the integral. Using the operational property above:

$$
p \, \tilde{V} - V(S,0) = \frac{\sigma^2}{2} S^2 \frac{d^2 \tilde{V}}{dS^2} + r S \frac{d \tilde{V}}{dS} - r \, \tilde{V}
$$

Substituting the terminal (initial in $\tau$) condition $V(S,0) = \Phi(S)$ and
rearranging:

$$
\frac{\sigma^2}{2} S^2 \frac{d^2 \tilde{V}}{dS^2} + r S \frac{d \tilde{V}}{dS} - (r + p) \, \tilde{V} = -\Phi(S)
$$

This is a **second-order ODE in** $S$. The time variable has been completely
eliminated. Note the contrast with the Fourier and Mellin approaches, which
eliminate the spatial variable and leave an ODE in time.

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

For a European call with payoff $\Phi(S) = (S - K)^+$, the full solution consists of
the homogeneous solution plus a particular solution $\tilde{V}_p$ driven by the
right-hand side $-\Phi(S)$:

$$
\tilde{V}(S,p) = A(p) \, S^{\lambda_+} + B(p) \, S^{\lambda_-} + \tilde{V}_p(S,p)
$$

The particular solution can be constructed via **variation of parameters** or the
**Green's function** of the Euler-Cauchy operator.

**Boundary conditions** in the Laplace domain mirror those in the time domain:

- As $S \to 0$: $\tilde{V}(S,p) \to 0$ (the call is worthless for zero stock price).
- As $S \to \infty$: $\tilde{V}(S,p) \sim S/p$ (the call behaves like $S$ for large $S$, and $\mathcal{L}[S] = S/p$).

Since $\lambda_+ > 0$, the term $S^{\lambda_+}$ grows as $S \to \infty$ faster than $S$
(for large $p$), so typically $A(p) = 0$ or is absorbed into the particular solution.
Since $\lambda_- < 0$, the term $S^{\lambda_-}$ blows up as $S \to 0$, so $B(p) = 0$.
The constants are thereby determined, and the full solution $\tilde{V}(S,p)$ is fixed.

---

## Log-Price Formulation

An equivalent formulation uses the log-price $x = \ln S$. In this coordinate,
the Black-Scholes PDE becomes

$$
\frac{\partial V}{\partial \tau} = \frac{\sigma^2}{2} \frac{\partial^2 V}{\partial x^2} + \left(r - \frac{\sigma^2}{2}\right) \frac{\partial V}{\partial x} - r V
$$

Applying the Laplace transform in $\tau$:

$$
\frac{\sigma^2}{2} \frac{d^2 \tilde{V}}{dx^2} + \left(r - \frac{\sigma^2}{2}\right) \frac{d\tilde{V}}{dx} - (r + p) \, \tilde{V} = -\Phi(e^x)
$$

This is a **constant-coefficient** second-order ODE (no longer Euler-Cauchy, because
the change to log-price absorbs the $S$-dependence). The characteristic equation is
the same quadratic as before, and the homogeneous solutions are $e^{\lambda_+ x}$
and $e^{\lambda_- x}$.

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

After determining $\tilde{V}(S,p)$ (or $\tilde{V}(x,p)$), the option price is
recovered via the Bromwich integral:

$$
V(S,\tau) = \frac{1}{2\pi i} \int_{c - i\infty}^{c + i\infty} \tilde{V}(S,p) \, e^{p\tau} \, dp
$$

For the Black-Scholes model with constant parameters, this integral can in principle
be evaluated by closing the contour and applying the residue theorem. However, in
practice the singularity structure (branch points from the square root in
$\lambda_{\pm}$) makes analytic inversion delicate.

**Numerical inversion** methods are therefore essential. The principal approaches are the **Gaver-Stehfest algorithm** (uses only real evaluations of $\tilde{V}$, simple but limited precision), **Talbot's method** (deforms the Bromwich contour for rapid convergence), and the **Euler method of Abate-Whitt** (trapezoidal rule with Euler summation). For Black-Scholes with constant parameters, the Gaver-Stehfest method with $N = 12$ terms typically gives 5--6 digits of accuracy.

---

## Combined Fourier-Laplace Transform

A powerful technique applies **both** the Fourier transform (in the log-price
variable $x$) and the Laplace transform (in time $\tau$) simultaneously. Define
the double transform:

$$
\tilde{\hat{V}}(\omega, p) = \int_0^{\infty} \int_{-\infty}^{\infty} V(x,\tau) \, e^{-i\omega x} \, e^{-p\tau} \, dx \, d\tau
$$

Applying both transforms to the PDE reduces it to a purely **algebraic** equation:

$$
p \, \tilde{\hat{V}} - \hat{\Phi}(\omega) = \left[-\frac{\sigma^2 \omega^2}{2} + i\omega\!\left(r - \frac{\sigma^2}{2}\right) - r\right] \tilde{\hat{V}}
$$

where $\hat{\Phi}(\omega) = \mathcal{F}[\Phi(e^x)](\omega)$ is the Fourier transform
of the payoff. Solving:

$$
\tilde{\hat{V}}(\omega, p) = \frac{\hat{\Phi}(\omega)}{p - \psi(\omega)}
$$

where $\psi(\omega) = -\frac{\sigma^2 \omega^2}{2} + i\omega(r - \frac{\sigma^2}{2}) - r$
is the characteristic exponent.

The option price is recovered by double inversion:

$$
V(x,\tau) = \frac{1}{2\pi} \cdot \frac{1}{2\pi i} \int_{c - i\infty}^{c + i\infty} \int_{-\infty}^{\infty} \frac{\hat{\Phi}(\omega)}{p - \psi(\omega)} \, e^{i\omega x} \, e^{p\tau} \, d\omega \, dp
$$

The $p$-integral can be evaluated first using the residue theorem. The integrand
has a simple pole at $p = \psi(\omega)$, so

$$
\frac{1}{2\pi i} \int_{c - i\infty}^{c + i\infty} \frac{e^{p\tau}}{p - \psi(\omega)} \, dp = e^{\psi(\omega)\tau}
$$

Substituting back:

$$
V(x,\tau) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \hat{\Phi}(\omega) \, e^{\psi(\omega)\tau} \, e^{i\omega x} \, d\omega
$$

This recovers the Fourier-only solution, confirming the consistency of the two
approaches. The combined Fourier-Laplace viewpoint is conceptually illuminating:
it shows that the resolvent $(p - \psi(\omega))^{-1}$ encodes the full time evolution
of the pricing operator.

---

## Perpetual Options as the Zero-Frequency Limit

The Laplace transform connects naturally to **perpetual** (infinite-maturity) options.
For a perpetual option, the value $V(S)$ is independent of $\tau$, so
$\frac{\partial V}{\partial \tau} = 0$ and the PDE reduces directly to the ODE

$$
\frac{\sigma^2}{2} S^2 V'' + r S V' - r V = 0
$$

This is exactly the homogeneous Euler-Cauchy equation obtained from the Laplace
transform with $p = 0$. The Laplace parameter $p$ can therefore be interpreted as
a **frequency variable conjugate to time**: $p = 0$ corresponds to the
time-independent (perpetual) case, while $p \neq 0$ captures the transient
behavior that decays as $\tau \to \infty$.

For a perpetual American put with strike $K$, the boundary conditions are
$V(0) = K$ and $V(S^*) = K - S^*$, $V'(S^*) = -1$ (smooth pasting), where $S^*$ is
the optimal exercise boundary. The solution is $V(S) = (K - S^*)(S/S^*)^{\lambda_-}$
for $S > S^*$, with $\lambda_- = \lambda_-(0)$.

---

## Advantages and Limitations

The Laplace-in-time approach has several distinctive features compared with
spatial transforms (Fourier, Mellin):

| Aspect | Laplace in time | Fourier / Mellin in space |
|---|---|---|
| Variable removed | Time $\tau$ | Spatial $x$ or $S$ |
| Resulting equation | ODE in $S$ (Euler-Cauchy) | ODE in $\tau$ (first-order) |
| Time-dependent coefficients | Handled naturally | Destroy the approach |
| Inversion | Numerical (Bromwich integral) | FFT or contour integration |
| Multiple strikes | One ODE solve per strike | All strikes simultaneously |
| Free-boundary problems | Natural (ODE boundary conditions) | Difficult |

The main limitation is the need for numerical Laplace inversion, which is
inherently ill-conditioned. For constant-parameter European options, the Fourier
approach (with FFT) is generally more efficient. The Laplace approach shines for
problems with time-dependent parameters, free boundaries (American options), or
perpetual structures. In the operator framework of the introduction, the Laplace transform yields the **resolvent** $(p - \mathcal{L})^{-1}$ of the Black--Scholes generator $\mathcal{L}$, providing yet another representation of the pricing semigroup $\mathcal{P}_\tau = e^{\tau\mathcal{L}}$.

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
