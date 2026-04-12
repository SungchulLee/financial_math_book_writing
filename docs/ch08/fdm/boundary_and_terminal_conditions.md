# Boundary and Terminal Conditions


Numerical PDE pricing requires:
- a **terminal condition** at $t=T$,
- **boundary conditions** in $S$ after truncating $(0,\infty)$ to $[0,S_{\max}]$.

---

## Terminal Condition


For a European payoff $\Phi(S)$,

$$
\boxed{V(T,S)=\Phi(S).}
$$


In time-to-maturity $\tau=T-t$, this becomes $u(0,S)=\Phi(S)$.

Payoffs often have kinks (e.g. $(S-K)^+$), affecting accuracy near $\tau=0$.

---

## Truncation


Choose $S_{\max}$ large enough to make truncation error negligible in the region of interest.

---

## Vanilla Boundary Conditions


Call:

$$
\boxed{
V(t,0)=0,
\qquad
V(t,S_{\max})\approx S_{\max}-Ke^{-r(T-t)}
}
$$



Put:

$$
\boxed{
V(t,0)\approx Ke^{-r(T-t)},
\qquad
V(t,S_{\max})\approx 0
}
$$



---

## Neumann-Type Alternatives


Call delta tends to $1$ as $S\to\infty$:

$$
\boxed{V_S(t,S_{\max})\approx 1.}
$$


Put delta tends to $0$:

$$
\boxed{V_S(t,S_{\max})\approx 0.}
$$



---

## Implementation Notes


At boundaries, use one-sided differences, ghost points, or enforce asymptotic formulas. Boundary choices interact with stability and monotonicity.

---

## What to Remember


- Terminal payoff regularity matters.
- Boundary conditions are part of the model numerically.
- Dirichlet and Neumann conditions are both used in practice.

---

## Exercises

**Exercise 1.** For a European call with $K = 100$, $r = 0.05$, and $T = 0.5$, compute the Dirichlet boundary values at $S = 0$ and $S_{\max} = 300$ at times $t = 0$, $t = 0.25$, and $t = 0.5$. How do the boundary values change as $t$ approaches maturity?

??? success "Solution to Exercise 1"
    For a European call with $K = 100$, $r = 0.05$, $T = 0.5$:

    **At $S = 0$ (Dirichlet)**: $V(t, 0) = 0$ for all $t$ (the call is worthless if the underlying is zero).

    **At $S_{\max} = 300$ (Dirichlet)**:

    $$
    V(t, 300) \approx S_{\max} - Ke^{-r(T-t)} = 300 - 100\,e^{-0.05(0.5 - t)}
    $$

    At $t = 0$:

    $$
    V(0, 300) \approx 300 - 100\,e^{-0.025} = 300 - 97.53 = 202.47
    $$

    At $t = 0.25$:

    $$
    V(0.25, 300) \approx 300 - 100\,e^{-0.0125} = 300 - 98.76 = 201.24
    $$

    At $t = 0.5$ (maturity):

    $$
    V(0.5, 300) = (300 - 100)^+ = 200
    $$

    As $t$ approaches maturity, the discount factor $e^{-r(T-t)} \to 1$, so the boundary value at $S_{\max}$ decreases toward the intrinsic value $S_{\max} - K = 200$. The boundary value at $S = 0$ remains $0$ throughout.

---

**Exercise 2.** Explain why the terminal condition for a European option in the time-to-maturity formulation becomes an initial condition $u(0, S) = \Phi(S)$. Write down the initial condition explicitly for a put option with strike $K$.

??? success "Solution to Exercise 2"
    The Black-Scholes PDE is posed as a **backward** problem in calendar time $t$: the equation is solved from the known terminal condition $V(T, S) = \Phi(S)$ backward to $t = 0$.

    Define $\tau = T - t$, so $\tau = 0$ corresponds to maturity and $\tau = T$ corresponds to the valuation date. Let $u(\tau, S) = V(T - \tau, S)$. Then

    $$
    \frac{\partial u}{\partial \tau} = -\frac{\partial V}{\partial t}
    $$

    Since the Black-Scholes PDE states $\frac{\partial V}{\partial t} = -\mathcal{L}V$ (where $\mathcal{L}$ is the spatial operator), we get $\frac{\partial u}{\partial \tau} = \mathcal{L}u$, which is a **forward** parabolic equation.

    At $\tau = 0$: $u(0, S) = V(T, S) = \Phi(S)$. So the terminal condition in $t$ becomes an **initial** condition in $\tau$.

    For a European put with strike $K$:

    $$
    u(0, S) = \Phi(S) = (K - S)^+ = \max(K - S, 0)
    $$

    This forward formulation is standard for numerical methods because one marches forward from the known initial state $u(0, S)$ using any time-stepping scheme, which is the natural direction for explicit and implicit integrators.

---

**Exercise 3.** The Neumann boundary condition for a call at the upper boundary is $V_S(t, S_{\max}) \approx 1$. Using a backward finite difference at $j = M$, express $V_M^n$ in terms of $V_{M-1}^n$ and $\Delta S$. Compare this to the Dirichlet condition $V_M^n = S_{\max} - Ke^{-r(T - t_n)}$ and discuss which is more appropriate when $S_{\max}$ is not sufficiently large.

??? success "Solution to Exercise 3"
    Using a backward (one-sided) finite difference at $j = M$:

    $$
    V_S(t_n, S_{\max}) \approx \frac{V_M^n - V_{M-1}^n}{\Delta S} = 1
    $$

    Solving for $V_M^n$:

    $$
    V_M^n = V_{M-1}^n + \Delta S
    $$

    The Dirichlet condition gives:

    $$
    V_M^n = S_{\max} - Ke^{-r(T - t_n)}
    $$

    **Comparison**: When $S_{\max}$ is sufficiently large, both conditions produce similar values because the call value is nearly linear in $S$ for $S \gg K$, so $V_S \approx 1$ and $V \approx S - Ke^{-r(T-t)}$.

    However, when $S_{\max}$ is **not** sufficiently large, the Dirichlet condition $V_M^n = S_{\max} - Ke^{-r(T-t_n)}$ ignores the remaining time value of the option and underestimates the true price. The Neumann condition $V_S = 1$ is more robust because it encodes the asymptotic behavior of the delta rather than the absolute price level. The Neumann condition allows the numerical solution to determine the price level at the boundary, which is more accurate when the boundary is not far enough from the strike. In practice, for well-chosen $S_{\max} \geq 3K$, the two conditions produce nearly identical results.

---

**Exercise 4.** Consider a domain $[0, S_{\max}]$ with $S_{\max} = 200$ and $K = 100$. Estimate the truncation error at $S = 100$ caused by the artificial boundary at $S_{\max}$ for a European put. Why is this error negligible for puts but potentially problematic for calls if $S_{\max}$ is too small?

??? success "Solution to Exercise 4"
    For a European put with $K = 100$ on $[0, S_{\max}]$ with $S_{\max} = 200$:

    The true put price satisfies $V(t, S) = Ke^{-r(T-t)}N(-d_2) - SN(-d_1)$, where $N$ is the standard normal CDF. For $S = 100$ (at the money), the option has significant time value and depends on boundary conditions only through their influence on the interior solution.

    The truncation error at $S = 100$ from the artificial boundary at $S_{\max} = 200$ is the difference between the solution on $[0, \infty)$ and the solution on $[0, 200]$ with $V(t, 200) = 0$. Since the true put value at $S = 200$ is extremely small (deep out of the money — e.g., for $\sigma = 0.3$, $r = 0.05$, $T = 1$, the put price at $S = 200$ is essentially zero), the imposed boundary condition $V(t, 200) = 0$ is nearly exact, so the truncation error at $S = 100$ is negligible.

    **Why negligible for puts**: The put payoff $(K - S)^+$ is zero for $S > K$, and the put value decays exponentially for $S \gg K$ because $N(-d_1) \to 0$ rapidly. Hence the boundary condition $V = 0$ at $S_{\max}$ is essentially exact.

    **Why problematic for calls if $S_{\max}$ is too small**: The call value grows linearly as $S \to \infty$, with $V \approx S - Ke^{-rT}$. If $S_{\max}$ is close to $K$, the approximation $V(t, S_{\max}) \approx S_{\max} - Ke^{-r(T-t)}$ ignores the option's time value at the boundary, and this error propagates inward through the diffusion operator. The error decays with distance from the boundary but can be significant if $S_{\max}$ is not large enough.

---

**Exercise 5.** The payoff $\Phi(S) = (S - K)^+$ has a discontinuous first derivative at $S = K$. Explain how this kink affects the accuracy of the FDM solution near $\tau = 0$. Describe the Rannacher smoothing technique and explain why it helps.

??? success "Solution to Exercise 5"
    The payoff $\Phi(S) = (S - K)^+$ has a discontinuous first derivative at $S = K$ (slope jumps from $0$ to $1$) and a distributional second derivative (a Dirac delta at $K$). The finite difference second-derivative approximation

    $$
    \frac{u_{j+1} - 2u_j + u_{j-1}}{(\Delta S)^2}
    $$

    produces an $O(1/\Delta S)$ spike at nodes near $K$, rather than the $O((\Delta S)^2)$ accuracy expected for smooth functions. This large initial error is propagated by the time-stepping scheme.

    For the Crank-Nicolson scheme, which is not $L$-stable, high-frequency error components are damped only slowly (the amplification factor approaches $-1$ for large eigenvalues rather than $0$). This causes **oscillations** in the numerical solution near $K$ for small $\tau$.

    **Rannacher smoothing**: Replace the first few (typically 2-4) Crank-Nicolson time steps with fully implicit (backward Euler) steps. The implicit scheme is $L$-stable: its amplification factor $1/(1 + \lambda\Delta\tau)$ tends to $0$ as $\lambda \to \infty$, which strongly damps high-frequency components. After these initial smoothing steps, the solution has become smooth enough that Crank-Nicolson can be applied without generating oscillations.

    **Overall accuracy**: The backward Euler steps introduce $O(\Delta\tau)$ local error, but only for a fixed number of steps ($p$ steps of size $\Delta\tau$). The global contribution of these steps is $O(p \cdot \Delta\tau) = O(\Delta\tau)$, which does not degrade the overall $O((\Delta\tau)^2)$ convergence rate of the remaining Crank-Nicolson steps. In fact, a more careful analysis shows that using half-steps for the implicit phase (2 implicit half-steps = 1 full step) preserves second-order accuracy globally.

---

**Exercise 6.** A ghost-point implementation of the Neumann condition $V_S(t, S_{\max}) = 1$ introduces a fictitious node $S_{M+1}$ and uses the central difference $(V_{M+1}^n - V_{M-1}^n)/(2\Delta S) = 1$ to express $V_{M+1}^n$. Derive the resulting equation for $V_M^n$ in the implicit scheme.

??? success "Solution to Exercise 6"
    The ghost point $S_{M+1} = S_M + \Delta S$ is a fictitious node outside the domain. The Neumann condition using a central difference at $j = M$ gives:

    $$
    \frac{V_{M+1}^n - V_{M-1}^n}{2\Delta S} = 1 \implies V_{M+1}^n = V_{M-1}^n + 2\Delta S
    $$

    In the implicit scheme, the PDE discretization at $j = M$ reads:

    $$
    \frac{V_M^{n+1} - V_M^n}{\Delta\tau} = \frac{\sigma^2 S_M^2}{2}\frac{V_{M+1}^{n+1} - 2V_M^{n+1} + V_{M-1}^{n+1}}{(\Delta S)^2} + rS_M\frac{V_{M+1}^{n+1} - V_{M-1}^{n+1}}{2\Delta S} - rV_M^{n+1}
    $$

    Substituting $V_{M+1}^{n+1} = V_{M-1}^{n+1} + 2\Delta S$ from the Neumann condition:

    The second-derivative term becomes:

    $$
    \frac{(V_{M-1}^{n+1} + 2\Delta S) - 2V_M^{n+1} + V_{M-1}^{n+1}}{(\Delta S)^2} = \frac{2V_{M-1}^{n+1} - 2V_M^{n+1} + 2\Delta S}{(\Delta S)^2}
    $$

    The first-derivative term becomes:

    $$
    \frac{(V_{M-1}^{n+1} + 2\Delta S) - V_{M-1}^{n+1}}{2\Delta S} = \frac{2\Delta S}{2\Delta S} = 1
    $$

    Substituting back:

    $$
    \frac{V_M^{n+1} - V_M^n}{\Delta\tau} = \frac{\sigma^2 S_M^2}{2}\cdot\frac{2V_{M-1}^{n+1} - 2V_M^{n+1} + 2\Delta S}{(\Delta S)^2} + rS_M - rV_M^{n+1}
    $$

    Rearranging to isolate unknowns at level $n+1$ on the left:

    $$
    V_M^{n+1}\left(1 + \Delta\tau\frac{\sigma^2 S_M^2}{(\Delta S)^2} + r\Delta\tau\right) - V_{M-1}^{n+1}\cdot\Delta\tau\frac{\sigma^2 S_M^2}{(\Delta S)^2} = V_M^n + \Delta\tau\frac{\sigma^2 S_M^2\,\Delta S}{(\Delta S)^2}\cdot 1 + rS_M\Delta\tau
    $$

    Simplifying $\frac{\sigma^2 S_M^2 \cdot \Delta S}{(\Delta S)^2} = \frac{\sigma^2 S_M^2}{\Delta S}$:

    $$
    V_M^{n+1}\left(1 + \Delta\tau\frac{\sigma^2 S_M^2}{(\Delta S)^2} + r\Delta\tau\right) - V_{M-1}^{n+1}\cdot\Delta\tau\frac{\sigma^2 S_M^2}{(\Delta S)^2} = V_M^n + \Delta\tau\left(\frac{\sigma^2 S_M^2}{\Delta S} + rS_M\right)
    $$

    This modifies the last row of the tridiagonal system: the diagonal entry involves $(1 + \Delta\tau\sigma^2 S_M^2/(\Delta S)^2 + r\Delta\tau)$, the sub-diagonal entry involves $-\Delta\tau\sigma^2 S_M^2/(\Delta S)^2$, and the right-hand side includes the known terms $V_M^n + \Delta\tau(\sigma^2 S_M^2/\Delta S + rS_M)$ arising from the ghost-point elimination.
