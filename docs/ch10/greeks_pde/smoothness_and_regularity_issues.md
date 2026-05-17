# Smoothness and Regularity Issues


Regularity of $V$ and Greeks depends on:

- regularity of payoff $\Phi$,
- ellipticity/smoothness of coefficients,
- time distance to maturity.

---

## Diffusion smoothing: precise statement


Parabolic equations smooth initial/terminal data for $t<T$. Even if $\Phi$ is not $C^1$, $V(t,\cdot)$ is often smooth for $t<T$ (away from degeneracies such as $S=0$).

**Schauder estimates.** For the Black–Scholes equation with bounded, measurable terminal data $\Phi$, the solution satisfies:

$$
V \in C^{\infty}((0,T) \times (0,\infty))
$$

More precisely, for any $\alpha \in (0,1)$ and compact $K \subset (0,T) \times (0,\infty)$, we have interior Hölder estimates:

$$
\|V\|_{C^{2+\alpha, 1+\alpha/2}(K)} \leq C_K \|\Phi\|_{L^\infty}
$$

where the parabolic Hölder space $C^{2+\alpha, 1+\alpha/2}$ captures two spatial derivatives and one time derivative with Hölder continuity.

**Heat kernel interpretation.** In log-coordinates the operator has a Gaussian fundamental solution (heat kernel), and convolution with any $L^1$ terminal data produces a $C^\infty$ function for $t < T$ (the explicit kernel is written out in Exercise 1 and used again under "Degenerate coefficients" below).

---

## Kinks and gamma concentration


For $\Phi(S)=(S-K)^+$, the second derivative at maturity is distributional:

$$
\Phi''(S) = \delta(S-K) \quad \text{(Dirac mass)}
$$

For $t<T$, diffusion replaces this by a narrow bump.

**Recall** (see [§ Greeks in the Black–Scholes Model](../greeks/greeks_in_black_scholes_model.md) for the closed-form $\Gamma = N'(d_1)/(S\sigma\sqrt{\tau})$, and [§ Blow-Up of Gamma Near Expiry](../greeks_asympt/blow_up_of_gamma_near_expiry.md) for the ATM scaling): the regularized Dirac mass becomes a bump with height $\mathcal{O}(\tau^{-1/2})$, width $\mathcal{O}(\sqrt{\tau})$, and unit area, with maximum $\Gamma_{\max}(t) = 1/(K\sigma\sqrt{2\pi\tau})$ near $S=K$.

---

## Degenerate coefficients


The Black–Scholes operator

$$
\mathcal{L} = \frac{1}{2}\sigma^2 S^2 \partial_{SS} + rS\partial_S
$$

degenerates at $S = 0$ (the coefficient of $\partial_{SS}$ vanishes). This creates:

- **Boundary layer effects** near $S = 0$
- **Reduced regularity** compared to uniformly elliptic equations
- **Need for weighted Sobolev spaces** for rigorous analysis

The standard approach is to work in log-coordinates $x = \ln S$, where the operator becomes uniformly elliptic:

$$
\widetilde{\mathcal{L}} = \frac{1}{2}\sigma^2 \partial_{xx} + (r - \frac{1}{2}\sigma^2)\partial_x
$$

---

## American options and free boundaries


Free boundaries reduce regularity; viscosity solutions provide the right weak framework.

**Free boundary regularity.** For the American put, the optimal exercise boundary $S^*(t)$ satisfies:

- $S^* \in C^{0,1/2}$ (Lipschitz in $\sqrt{T-t}$) near maturity
- $S^*$ is smooth away from maturity

**Greeks across the boundary.** At the exercise boundary:

- $V$ is $C^1$ (smooth pasting): $\Delta$ is continuous
- $V$ is generally not $C^2$: $\Gamma$ has a jump discontinuity
- The jump in $\Gamma$ relates to the local time of $S$ at the boundary

---

## Function space classification


| Domain | Price regularity | Greek regularity |
|:-------|:-----------------|:-----------------|
| $t < T$, European | $C^\infty$ in $(t,S)$ | All Greeks smooth |
| $t = T$, kinked payoff | $C^0$ only | $\Delta$ discontinuous, $\Gamma$ distributional |
| American, continuation region | $C^\infty$ | All Greeks smooth |
| American, at exercise boundary | $C^1$ | $\Delta$ continuous, $\Gamma$ may jump |

---

## What to remember


- Smoothness improves for $t<T$ but deteriorates as $t\uparrow T$.
- Interior regularity follows from Schauder estimates; $V \in C^\infty$ for $t < T$.
- Payoff kinks create large gamma near maturity: height $\sim \tau^{-1/2}$, width $\sim \sqrt{\tau}$.
- The Black–Scholes operator degenerates at $S=0$; log-transform restores uniform ellipticity.
- Early exercise introduces weaker regularity and free boundary effects; $\Gamma$ may be discontinuous.

---

## Exercises

**Exercise 1.** The heat kernel for the log-transformed Black--Scholes equation is Gaussian. Explain why convolution of any bounded measurable terminal data with this kernel produces a $C^\infty$ function for $t < T$, and relate this to the Schauder estimate $\|V\|_{C^{2+\alpha, 1+\alpha/2}(K)} \leq C_K \|\Phi\|_{L^\infty}$.

??? success "Solution to Exercise 1"
    In log-coordinates $x = \ln S$, the Black--Scholes PDE becomes the constant-coefficient parabolic equation:

    $$
    \frac{\partial u}{\partial t} + \frac{1}{2}\sigma^2 \frac{\partial^2 u}{\partial x^2} + \left(r - \frac{1}{2}\sigma^2\right)\frac{\partial u}{\partial x} - ru = 0
    $$

    The fundamental solution (Green's function) is the Gaussian kernel:

    $$
    G(t,x;T,y) = \frac{1}{\sqrt{2\pi\sigma^2(T-t)}}\exp\!\left(-\frac{(y - x - (r - \frac{1}{2}\sigma^2)(T-t))^2}{2\sigma^2(T-t)}\right)
    $$

    For any bounded measurable terminal data $\Phi$, the solution is:

    $$
    u(t,x) = e^{-r(T-t)}\int_{-\infty}^{\infty} G(t,x;T,y)\,\Phi(e^y)\,dy
    $$

    This is $C^\infty$ for $t < T$ because:

    1. The Gaussian $G$ is $C^\infty$ in $(t,x)$ for $t < T$, since the exponential of a polynomial is smooth and $T - t > 0$ prevents any singularity.
    2. Differentiation passes under the integral sign by dominated convergence: for any multi-index of derivatives, $|\partial_t^j \partial_x^k G(t,x;T,y)| \leq C_{j,k}(T-t)^{-(j+k/2)}G_\epsilon(t,x;T,y)$ for a slightly wider Gaussian $G_\epsilon$, which is integrable against bounded $\Phi$.
    3. Each derivative produces another smooth function, so $u \in C^\infty((0,T) \times \mathbb{R})$.

    The Schauder estimate $\|V\|_{C^{2+\alpha,1+\alpha/2}(K)} \leq C_K\|\Phi\|_{L^\infty}$ quantifies this smoothing. It states that on any compact set $K$ strictly inside the domain (bounded away from $t = T$), the $C^{2+\alpha}$ norm of the solution is controlled solely by the $L^\infty$ norm of the terminal data. This is a hallmark of parabolic regularity: even discontinuous or merely bounded initial data produces solutions with two spatial derivatives in Holder spaces, with the constant $C_K$ depending on the distance from $K$ to the boundary $t = T$.

---

**Exercise 2.** For the call payoff $\Phi(S) = (S-K)^+$, the gamma at time $t < T$ has height $\mathcal{O}(\tau^{-1/2})$, width $\mathcal{O}(\sqrt{\tau})$, and area $\mathcal{O}(1)$. Verify the area claim by computing $\int_0^\infty \Gamma(t,S) \, dS$ for the Black--Scholes gamma formula and showing it equals $1/S$ (or a constant independent of $\tau$).

??? success "Solution to Exercise 2"
    The Black--Scholes gamma for a European call is:

    $$
    \Gamma(t,S) = \frac{N'(d_1)}{S\sigma\sqrt{\tau}}
    $$

    where $N'(d_1) = \frac{1}{\sqrt{2\pi}}e^{-d_1^2/2}$ and $d_1 = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}$.

    Compute the integral:

    $$
    \int_0^\infty \Gamma(t,S)\,dS = \int_0^\infty \frac{N'(d_1)}{S\sigma\sqrt{\tau}}\,dS
    $$

    Substitute $u = d_1$, which gives $du = \frac{1}{S\sigma\sqrt{\tau}}\,dS$ (since $d_1 = \frac{\ln(S/K) + (r+\frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}$ and $\frac{\partial d_1}{\partial S} = \frac{1}{S\sigma\sqrt{\tau}}$). As $S$ ranges from $0$ to $\infty$, $d_1$ ranges from $-\infty$ to $+\infty$. Therefore:

    $$
    \int_0^\infty \Gamma(t,S)\,dS = \int_{-\infty}^{\infty} N'(u)\,du = \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi}}e^{-u^2/2}\,du = 1
    $$

    The area under the gamma curve equals 1, independent of $\tau$, $\sigma$, $r$, or $K$. This is consistent with the fact that $\int_0^\infty \Gamma\,dS = \int_0^\infty V_{SS}\,dS = V_S\big|_0^\infty = \Delta(\infty) - \Delta(0) = 1 - 0 = 1$ for a call option. As $\tau \to 0$, the height grows as $\tau^{-1/2}$ and the width shrinks as $\sqrt{\tau}$, but their product (the area) remains constant at 1, consistent with the distributional limit $\Gamma(T,S) = \delta(S-K)$ which also has unit integral.

---

**Exercise 3.** The Black--Scholes operator degenerates at $S = 0$. Explain why the change of variable $x = \ln S$ transforms the operator into a uniformly elliptic one. Write down the transformed PDE explicitly.

??? success "Solution to Exercise 3"
    The Black--Scholes operator in the original $S$ variable is:

    $$
    \mathcal{L} = \frac{1}{2}\sigma^2 S^2 \frac{\partial^2}{\partial S^2} + rS\frac{\partial}{\partial S}
    $$

    The coefficient of $\frac{\partial^2}{\partial S^2}$ is $\frac{1}{2}\sigma^2 S^2$, which vanishes at $S = 0$. This means the operator is **degenerate elliptic** at $S = 0$: the second-order term that provides diffusion (and thus smoothing) disappears. Standard elliptic regularity theory requires **uniform ellipticity**, meaning the coefficient of the second-order term is bounded away from zero.

    Under $x = \ln S$ (so $S = e^x$, $x \in (-\infty, \infty)$), we use:

    $$
    \frac{\partial}{\partial S} = \frac{1}{S}\frac{\partial}{\partial x}, \qquad \frac{\partial^2}{\partial S^2} = \frac{1}{S^2}\frac{\partial^2}{\partial x^2} - \frac{1}{S^2}\frac{\partial}{\partial x}
    $$

    Substituting into the PDE $\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 V_{SS} + rSV_S - rV = 0$:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2\!\left(\frac{\partial^2 V}{\partial x^2} - \frac{\partial V}{\partial x}\right) + r\frac{\partial V}{\partial x} - rV = 0
    $$

    Simplifying:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 \frac{\partial^2 V}{\partial x^2} + \left(r - \frac{1}{2}\sigma^2\right)\frac{\partial V}{\partial x} - rV = 0
    $$

    The coefficient of $\frac{\partial^2 V}{\partial x^2}$ is now $\frac{1}{2}\sigma^2$, a positive constant independent of $x$. This makes the operator **uniformly elliptic** on all of $\mathbb{R}$, so standard parabolic regularity theory (Schauder estimates, maximum principles) applies without any special treatment of boundary layers.

---

**Exercise 4.** For an American put, the exercise boundary $S^*(t)$ creates a jump in gamma. Using the smooth-pasting condition ($V$ is $C^1$ across the boundary), explain why $\Delta$ is continuous but $\Gamma$ has a discontinuity. What is the sign of the gamma jump?

??? success "Solution to Exercise 4"
    For an American put with exercise boundary $S^*(t)$, the smooth-pasting condition states that the option price $V(t,S)$ is $C^1$ across the boundary: both $V$ and $V_S = \Delta$ are continuous at $S = S^*(t)$.

    **Why delta is continuous.** In the exercise region ($S \leq S^*$), $V(t,S) = K - S$, so $\Delta = -1$. In the continuation region ($S > S^*$), $\Delta$ is determined by the PDE solution. Smooth pasting requires that $\Delta$ approaches $-1$ continuously as $S \downarrow S^*$ from the continuation region. This is not automatic -- it is a condition that determines the free boundary $S^*$ itself.

    **Why gamma is discontinuous.** In the exercise region, $V = K - S$ is linear, so $\Gamma = V_{SS} = 0$. In the continuation region, the PDE is active and $V$ has non-trivial curvature. At the boundary, we can compute:

    $$
    \Gamma^+ = \lim_{S \downarrow S^*} V_{SS}(t,S) > 0, \qquad \Gamma^- = \lim_{S \uparrow S^*} V_{SS}(t,S) = 0
    $$

    The jump in gamma is:

    $$
    [\Gamma] = \Gamma^+ - \Gamma^- = \Gamma^+ > 0
    $$

    The sign is positive because the put price in the continuation region is convex (curving upward away from the linear intrinsic value). Mathematically, $V \geq K - S$ everywhere with equality at the boundary, so $V - (K-S)$ is non-negative and vanishes at $S^*$, implying $(V-(K-S))_{SS} \geq 0$ at the boundary, which gives $\Gamma^+ \geq 0$. Strict inequality holds because the diffusion term is active in the continuation region.

    This gamma discontinuity is a fundamental feature of American options and creates practical challenges for hedging near the exercise boundary.

---

**Exercise 5.** Consider a digital call with payoff $\Phi(S) = \mathbf{1}_{S > K}$, which is discontinuous at $S = K$. Describe the regularity of the digital call price $V(t,S)$ for $t < T$. Is delta smooth? How does the delta of a digital call behave as $\tau \to 0$?

??? success "Solution to Exercise 5"
    The digital call payoff $\Phi(S) = \mathbf{1}_{S > K}$ is discontinuous at $S = K$ with a jump of size 1.

    **Regularity for $t < T$.** Despite the discontinuous terminal data, the digital call price:

    $$
    V(t,S) = e^{-r\tau}N(d_2)
    $$

    is $C^\infty$ in both $t$ and $S$ for any $t < T$. This follows from the parabolic smoothing property: convolution of $\mathbf{1}_{S>K}$ with the smooth heat kernel produces a smooth function. The Schauder estimate guarantees $V \in C^{2+\alpha,1+\alpha/2}$ on compact subsets of $(0,T) \times (0,\infty)$.

    **Delta is smooth for $t < T$.** The delta of the digital call is:

    $$
    \Delta = \frac{\partial V}{\partial S} = e^{-r\tau}\frac{N'(d_2)}{S\sigma\sqrt{\tau}} = \frac{e^{-r\tau}}{S\sigma\sqrt{2\pi\tau}}\exp\!\left(-\frac{d_2^2}{2}\right)
    $$

    This is a smooth, positive, bell-shaped function of $S$ centered near $S = K$, identical in shape to the gamma of a vanilla call (up to a factor of $e^{-r\tau}$).

    **Behavior as $\tau \to 0$.** As $\tau \to 0$, the delta of the digital call concentrates:

    - At $S = K$ (ATM): $\Delta_{\text{ATM}} = \frac{e^{-r\tau}}{K\sigma\sqrt{2\pi\tau}} \sim \tau^{-1/2} \to \infty$
    - For $S \neq K$: $\Delta \to 0$ exponentially fast

    The delta converges to a Dirac delta $\delta(S - K)$ in the distributional sense, reflecting the fact that $\Phi'(S) = \delta(S-K)$. The digital delta becomes unhedgeable near expiry: it requires infinite rebalancing at the strike. In practice, this means digital options near expiry cannot be delta-hedged with the underlying alone, motivating the use of call spreads as approximate replication.

---

**Exercise 6.** A finite-difference scheme for the Black--Scholes PDE must handle the terminal condition $V(T,S) = (S-K)^+$, which has a kink at $S = K$. Explain why using the exact payoff as initial data can introduce oscillations in the numerical gamma, and propose two remedies.

??? success "Solution to Exercise 6"
    **Why oscillations arise.** The kink in $(S-K)^+$ at $S = K$ means that the numerical second difference:

    $$
    \frac{V_T(S_{i+1}) - 2V_T(S_i) + V_T(S_{i-1})}{(\Delta S)^2}
    $$

    is approximately $1/\Delta S$ at the grid point nearest $K$ and zero elsewhere. This is a crude approximation to $\delta(S-K)$ that creates a numerical gamma with large spurious oscillations. When this discontinuous initial gamma is propagated one time step backward, the finite-difference scheme (especially explicit schemes) can produce alternating positive and negative values -- the classic Gibbs phenomenon for parabolic equations with non-smooth data.

    The problem is particularly severe for gamma because the exact solution transitions smoothly from $\Gamma = 0$ (far from strike) to $\Gamma_{\max}$ (at strike), but the numerical approximation inherits the grid-scale oscillations from the non-smooth initial condition.

    **Remedy 1: Rannacher time-stepping.** Use a few (typically 2--4) implicit Euler steps at the start of the backward time-marching (near $t = T$), then switch to the more accurate Crank--Nicolson scheme. The fully implicit steps are strongly damping and eliminate the high-frequency oscillations introduced by the kink, at the cost of only first-order accuracy for those few steps. The subsequent Crank--Nicolson steps restore second-order accuracy once the solution has been smoothed.

    **Remedy 2: Payoff smoothing (cell averaging).** Replace the pointwise payoff values with cell-averaged values near the kink:

    $$
    \bar{V}_T(S_i) = \frac{1}{\Delta S}\int_{S_i - \Delta S/2}^{S_i + \Delta S/2}(S - K)^+\,dS
    $$

    For grid points away from $K$, this equals $(S_i - K)^+$. For the grid point nearest $K$, the integral smooths the kink over one cell width. This produces a consistent numerical gamma that is $\mathcal{O}(1/\Delta S)$ at the kink point (matching the true Dirac scaling) without oscillations in neighboring cells.
