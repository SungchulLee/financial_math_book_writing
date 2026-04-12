# Monotone Schemes and Viscosity Solutions


When classical smooth solutions fail (e.g. obstacle problems), **viscosity solutions** give the correct weak notion, and **monotone schemes** are a key route to convergence.

---

## Viscosity Solutions (Idea)


For a PDE $F(t,x,u,Du,D^2u)=0$, viscosity sub/supersolutions are defined via smooth test functions touching from above/below. Comparison principles yield uniqueness.

---

## Monotone Schemes


A scheme $\mathcal{S}_\Delta$ is monotone if increasing input data cannot decrease the output (discrete comparison). Practically this is tied to nonnegative stencil coefficients and discrete maximum principles.

---

## Consistency + Stability + Monotonicity


A foundational convergence principle (orientation) is that:

$$
\boxed{
\text{consistent} + \text{stable} + \text{monotone}
\Longrightarrow
\text{convergence to the viscosity solution}
}
$$


when a comparison principle holds.

---

## Application to American Options


Obstacle problems require monotone discretizations and constraint enforcement (projection/LCP) to ensure convergence to the correct viscosity solution.

---

## What to Remember


- Viscosity solutions handle nonsmoothness and inequalities.
- Monotone schemes preserve comparison principles discretely.
- This pairing is central for reliable American option numerics.

---

## Exercises

**Exercise 1.** State the convergence principle: consistent + stable + monotone implies convergence to the viscosity solution. Explain why each of the three conditions is necessary by describing what can go wrong if one is removed.

??? success "Solution to Exercise 1"
    The convergence principle states that if a numerical scheme $\mathcal{S}_\Delta$ is **consistent**, **stable**, and **monotone**, and a comparison principle holds for the underlying PDE, then the numerical solution converges to the unique viscosity solution as the mesh is refined.

    Each condition is necessary:

    - **Without consistency**: The scheme may be stable and monotone, but it approximates the wrong PDE. For example, a monotone scheme with an incorrect discretization of the drift term $rS V_S$ would converge to the solution of a different PDE with a wrong drift coefficient. The limiting function would satisfy a different equation, not the one intended.

    - **Without stability**: Even if the scheme is consistent and monotone, the numerical solutions may grow without bound. For instance, removing the CFL condition from an explicit scheme can cause the numerical values to oscillate with exponentially growing amplitude. No convergent subsequence to a bounded function can be extracted.

    - **Without monotonicity**: The scheme may be consistent and stable yet converge to the wrong weak solution. The Crank-Nicolson scheme is a classic example: it is second-order consistent and unconditionally stable, but it is not monotone. Near a payoff kink (e.g., at $S = K$ for a call option), it can produce spurious oscillations that do not diminish under mesh refinement, converging to a function that fails to be the viscosity solution. Monotonicity is what enforces the discrete comparison principle, linking the scheme to the viscosity solution framework.

---

**Exercise 2.** Consider the explicit scheme $u_j^{n+1} = a_j u_{j-1}^n + b_j u_j^n + c_j u_{j+1}^n$. Under what conditions on the coefficients $a_j$, $b_j$, $c_j$ is the scheme monotone? Show that the CFL condition $\Delta\tau \leq (\Delta S)^2 / (\sigma^2 S_{\max}^2)$ is related to the non-negativity of $b_j$.

??? success "Solution to Exercise 2"
    Consider the explicit scheme

    $$
    u_j^{n+1} = a_j u_{j-1}^n + b_j u_j^n + c_j u_{j+1}^n
    $$

    The scheme is **monotone** if and only if all coefficients are non-negative: $a_j \geq 0$, $b_j \geq 0$, $c_j \geq 0$.

    For the Black-Scholes PDE discretized on a uniform grid with spacing $\Delta S$ and time step $\Delta\tau$, using central differences for the diffusion and drift terms at node $S_j = j\Delta S$, the coefficients are

    $$
    a_j = \Delta\tau \left(\frac{\sigma^2 S_j^2}{2(\Delta S)^2} - \frac{rS_j}{2\Delta S}\right), \quad c_j = \Delta\tau \left(\frac{\sigma^2 S_j^2}{2(\Delta S)^2} + \frac{rS_j}{2\Delta S}\right)
    $$

    $$
    b_j = 1 - \Delta\tau \left(\frac{\sigma^2 S_j^2}{(\Delta S)^2} + r\right)
    $$

    The coefficients $a_j$ and $c_j$ are non-negative provided $\sigma^2 S_j \geq r \Delta S$ (which holds for sufficiently fine grids or when upwinding is used). The critical constraint is $b_j \geq 0$, which requires

    $$
    \Delta\tau \left(\frac{\sigma^2 S_j^2}{(\Delta S)^2} + r\right) \leq 1
    $$

    Since $S_j \leq S_{\max}$, a sufficient condition is

    $$
    \Delta\tau \leq \frac{(\Delta S)^2}{\sigma^2 S_{\max}^2 + r(\Delta S)^2}
    $$

    For small $\Delta S$, the $r(\Delta S)^2$ term is negligible, giving the CFL condition

    $$
    \Delta\tau \leq \frac{(\Delta S)^2}{\sigma^2 S_{\max}^2}
    $$

    This is precisely the condition ensuring $b_j \geq 0$, which is the binding constraint for monotonicity.

---

**Exercise 3.** The Crank-Nicolson scheme is second-order accurate but not monotone in general. Give an example of how non-monotonicity can produce spurious oscillations in the numerical solution of an American option problem.

??? success "Solution to Exercise 3"
    The Crank-Nicolson scheme averages the explicit and implicit discretizations:

    $$
    \frac{u_j^{n+1} - u_j^n}{\Delta\tau} = \frac{1}{2}\mathcal{L}_h u_j^{n+1} + \frac{1}{2}\mathcal{L}_h u_j^n
    $$

    While this achieves second-order accuracy in time, the effective stencil coefficients on the explicit side can become negative when the mesh ratio $\lambda = \sigma^2 S_j^2 \Delta\tau / (\Delta S)^2$ is large. Specifically, the amplification factor for high-frequency modes ($\theta = \pi$) is

    $$
    g(\pi) = \frac{1 - 2\lambda}{1 + 2\lambda}
    $$

    which is negative when $\lambda > 1/2$.

    For an American put option with strike $K = 100$, $\sigma = 0.3$, $r = 0.05$, consider a grid with $\Delta S = 1$ near $S = 100$. If $\Delta\tau$ is chosen so that $\lambda = \sigma^2 S^2 \Delta\tau / (\Delta S)^2 = 0.09 \times 10000 \times \Delta\tau > 0.5$, i.e., $\Delta\tau > 0.000556$, then $g(\pi) < 0$.

    The payoff $(K - S)^+$ has a kink at $S = K$. The high-frequency Fourier components of this kink are amplified and sign-reversed by the negative amplification factor. This produces oscillations: the numerical solution alternates above and below the true value near $S = K$. After projection onto the obstacle $\Phi = (K - S)^+$, these oscillations can create a jagged early-exercise boundary, producing prices that are systematically too high or exhibit non-physical wiggles in the Greeks ($\Delta$, $\Gamma$).

---

**Exercise 4.** Define what it means for a function $u$ to be a viscosity subsolution of a PDE $F(x, u, Du, D^2u) = 0$. Why is the viscosity framework necessary for American option pricing, where the solution satisfies an inequality rather than an equation?

??? success "Solution to Exercise 4"
    A function $u$ (upper semicontinuous) is a **viscosity subsolution** of $F(x, u, Du, D^2u) = 0$ if for every smooth test function $\varphi \in C^2(\Omega)$ and every point $x_0$ where $u - \varphi$ attains a local maximum:

    $$
    F(x_0, u(x_0), D\varphi(x_0), D^2\varphi(x_0)) \leq 0
    $$

    The idea is that if $\varphi$ touches $u$ from above at $x_0$ (meaning $\varphi \geq u$ near $x_0$ with equality at $x_0$), then the derivatives of $\varphi$ at $x_0$ serve as "generalized derivatives" of $u$, even though $u$ itself may not be differentiable.

    The viscosity framework is necessary for American option pricing because the value function $V$ satisfies the variational inequality

    $$
    \min(-V_\tau + \mathcal{L}V, \; V - \Phi) = 0
    $$

    rather than a standard PDE. At any point, either $V$ satisfies the PDE (in the continuation region) or $V = \Phi$ (in the exercise region). The boundary between these two regions --- the free boundary $S^*(\tau)$ --- is not known a priori and is part of the solution.

    At the free boundary, the solution typically has a discontinuity in $V_{SS}$ (the second derivative has a jump), so $V \notin C^2$. Classical solutions require $C^2$ regularity and cannot handle the $\min$ condition. The viscosity framework replaces pointwise PDE satisfaction with test-function inequalities, naturally encoding the switching between the two regimes: the subsolution condition ensures $V$ does not exceed what the PDE allows, while the supersolution condition ensures $V$ does not fall below the payoff. Together they characterize the unique American option price without requiring smoothness at the free boundary.

---

**Exercise 5.** Explain the discrete maximum principle: $\min_j u_j^n \leq u_j^{n+1} \leq \max_j u_j^n$. Show that this holds for the explicit scheme when all stencil coefficients are non-negative and sum to one. Why does this property guarantee that option prices remain non-negative?

??? success "Solution to Exercise 5"
    The discrete maximum principle states that for the explicit scheme

    $$
    u_j^{n+1} = a_j u_{j-1}^n + b_j u_j^n + c_j u_{j+1}^n
    $$

    with $a_j, b_j, c_j \geq 0$ and $a_j + b_j + c_j = 1$, we have

    $$
    \min_j u_j^n \leq u_j^{n+1} \leq \max_j u_j^n
    $$

    **Proof of the upper bound**: Let $M = \max_j u_j^n$. Then $u_{j-1}^n \leq M$, $u_j^n \leq M$, and $u_{j+1}^n \leq M$. Since all coefficients are non-negative:

    $$
    u_j^{n+1} = a_j u_{j-1}^n + b_j u_j^n + c_j u_{j+1}^n \leq a_j M + b_j M + c_j M = (a_j + b_j + c_j)M = M
    $$

    **Proof of the lower bound**: Let $m = \min_j u_j^n$. Then $u_{j-1}^n \geq m$, $u_j^n \geq m$, and $u_{j+1}^n \geq m$. Since all coefficients are non-negative:

    $$
    u_j^{n+1} = a_j u_{j-1}^n + b_j u_j^n + c_j u_{j+1}^n \geq a_j m + b_j m + c_j m = m
    $$

    This guarantees option prices remain non-negative because if the initial data (terminal payoff) satisfies $u_j^0 \geq 0$ for all $j$, then $\min_j u_j^0 \geq 0$, and inductively $u_j^n \geq 0$ for all $n$ and $j$. Since option payoffs are non-negative (e.g., $(S - K)^+ \geq 0$), the discrete maximum principle ensures that computed option prices can never become negative, which is a fundamental no-arbitrage requirement.

---

**Exercise 6.** For the American option obstacle problem $\min(-u_\tau + \mathcal{L}u,\; u - \Phi) = 0$, explain how the projection $u_j^{n+1} \leftarrow \max(u_j^{n+1}, \Phi_j)$ preserves monotonicity when applied after a monotone time-stepping scheme.

??? success "Solution to Exercise 6"
    Consider a monotone time-stepping scheme that produces an intermediate value $\tilde{u}_j^{n+1}$ from the data $\{u_j^n\}$. The American option scheme applies the projection:

    $$
    u_j^{n+1} = \max(\tilde{u}_j^{n+1}, \Phi_j)
    $$

    **Monotonicity is preserved** because both operations in the composition are monotone:

    1. **The time-stepping is monotone by assumption**: If $\{u_j^n\} \leq \{v_j^n\}$ pointwise, then $\tilde{u}_j^{n+1} \leq \tilde{v}_j^{n+1}$ for all $j$.

    2. **The $\max$ operation is monotone**: If $a \leq b$, then $\max(a, \Phi_j) \leq \max(b, \Phi_j)$ for any fixed $\Phi_j$. This follows because either both $a$ and $b$ exceed $\Phi_j$ (so the result is $a \leq b$), or both are below $\Phi_j$ (so the result is $\Phi_j = \Phi_j$), or $a \leq \Phi_j \leq b$ (so $\Phi_j \leq b$).

    Composing these two monotone operations: if $\{u_j^n\} \leq \{v_j^n\}$, then

    $$
    u_j^{n+1} = \max(\tilde{u}_j^{n+1}, \Phi_j) \leq \max(\tilde{v}_j^{n+1}, \Phi_j) = v_j^{n+1}
    $$

    This means the full American option scheme (time-step followed by projection) is monotone, and the Barles-Souganidis theorem applies. The projection enforces the obstacle constraint $u \geq \Phi$ at each time step, encoding the early exercise feature while maintaining the discrete comparison principle that is essential for convergence to the viscosity solution.
