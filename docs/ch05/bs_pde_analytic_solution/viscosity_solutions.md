# Viscosity Solutions: Complete Mathematical Treatment

Viscosity solutions provide a **rigorous framework** for nonlinear PDEs that handles **non-smooth data**, **degenerate equations**, and **optimal control problems**—all central to modern mathematical finance.

---

## **1. Motivation: Why Classical Solutions Fail**

### **The Problem with Non-Smooth Payoffs**

Consider a digital option with payoff:

$$\Phi(S) = \mathbb{1}_{S > K}$$



The Black-Scholes PDE:

$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} - rV = 0$$



with terminal condition $V(S,T) = \mathbb{1}_{S > K}$ has **no classical solution**—the payoff is discontinuous!

### **American Options**

The free boundary problem:

$$\max\left\{-\frac{\partial V}{\partial t} - rS\frac{\partial V}{\partial S} - \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} + rV, \, V - \Phi(S)\right\} = 0$$



The solution $V$ is typically **not $C^2$** at the free boundary, so classical derivatives don't exist.

### **Transaction Costs**

With proportional transaction costs, the Hamilton-Jacobi-Bellman equation:

$$\frac{\partial V}{\partial t} + \sup_{\alpha}\left[\alpha \sigma S \frac{\partial V}{\partial S} - c|\alpha|\right] + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} - rV = 0$$



involves a **non-smooth Hamiltonian** (absolute value).

### **The Gap**

**Classical theory**: Requires $C^2$ solutions
**Reality**: Financial PDEs rarely have $C^2$ solutions

**Viscosity theory**: Fills this gap!

---

## **2. Fundamental Definitions**

### **General Parabolic PDE**

Consider:

$$\boxed{F\left(x, t, u, Du, D^2u\right) = 0 \quad \text{in } \Omega \times (0,T)}$$



where:
- $u: \Omega \times [0,T] \to \mathbb{R}$ is the unknown
- $Du = \nabla u$ is the gradient
- $D^2u$ is the Hessian matrix
- $F$ is the **PDE operator** (possibly nonlinear)

**Boundary condition**: $u(x,T) = g(x)$

### **Upper/Lower Semicontinuity**

A function $u$ is:
- **Upper semicontinuous (USC)** if $\limsup_{y \to x}u(y) \leq u(x)$
- **Lower semicontinuous (LSC)** if $\liminf_{y \to x}u(y) \geq u(x)$

**Intuition**: USC functions don't have upward jumps; LSC functions don't have downward jumps.

### **Test Functions**

A function $\phi \in C^2(\Omega \times [0,T])$ is a **test function** for $u$ at $(x_0, t_0)$ if:

$$u(x,t) - \phi(x,t) \text{ has a local maximum (or minimum) at } (x_0,t_0)$$



---

## **3. Viscosity Subsolutions**

### **Definition**

A USC function $u$ is a **viscosity subsolution** of $F(x,t,u,Du,D^2u) = 0$ if:

For every $(x_0,t_0) \in \Omega \times (0,T)$ and every $\phi \in C^2$ such that $u - \phi$ has a **local maximum** at $(x_0,t_0)$:


$$\boxed{F(x_0, t_0, u(x_0,t_0), D\phi(x_0,t_0), D^2\phi(x_0,t_0)) \leq 0}$$



### **Intuition**

At points where we can "touch from above" with a smooth function, the PDE inequality $F \leq 0$ holds in the **viscosity sense**.

### **Why "Viscosity"?**

Historically, this notion arose from adding **artificial viscosity** $\epsilon \Delta u$ to make the equation:

$$F(x,t,u,Du,D^2u) - \epsilon \Delta u = 0$$



which has smooth solutions. Taking $\epsilon \to 0$ gives the viscosity solution.

### **Black-Scholes Example**

For the operator:

$$F = \frac{\partial u}{\partial t} + rS\frac{\partial u}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 u}{\partial S^2} - ru$$



A function $u$ is a viscosity subsolution if for every test function $\phi$ touching from above:

$$\frac{\partial \phi}{\partial t} + rS\frac{\partial \phi}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 \phi}{\partial S^2} - r\phi \leq 0$$



at the touching point.

---

## **4. Viscosity Supersolutions**

### **Definition**

A LSC function $u$ is a **viscosity supersolution** of $F(x,t,u,Du,D^2u) = 0$ if:

For every $(x_0,t_0) \in \Omega \times (0,T)$ and every $\phi \in C^2$ such that $u - \phi$ has a **local minimum** at $(x_0,t_0)$:


$$\boxed{F(x_0, t_0, u(x_0,t_0), D\phi(x_0,t_0), D^2\phi(x_0,t_0)) \geq 0}$$



### **Intuition**

At points where we can "touch from below" with a smooth function, $F \geq 0$ in the viscosity sense.

---

## **5. Viscosity Solutions**

### **Definition**

A continuous function $u$ is a **viscosity solution** if it is both:
1. A viscosity subsolution
2. A viscosity supersolution


$$\boxed{u \text{ is a viscosity solution} \iff \text{subsolution AND supersolution}}$$



### **Equivalent Definition (Semijets)**

Define the **second-order superdifferential**:

$$\overline{D^2}u(x_0,t_0) = \{(p, A) : u(x,t) \leq u(x_0,t_0) + \langle p, (x-x_0,t-t_0) \rangle + \frac{1}{2}\langle A(x-x_0,t-t_0), (x-x_0,t-t_0)\rangle + o(|(x-x_0,t-t_0)|^2)\}$$



Then $u$ is a viscosity subsolution if:

$$F(x_0,t_0,u(x_0,t_0), p, A) \leq 0 \quad \forall (p,A) \in \overline{D^2}u(x_0,t_0)$$



Similarly for supersolutions using the **subdifferential** $\underline{D^2}u$.

### **Classical Solutions are Viscosity Solutions**

**Proposition**: If $u \in C^2$ is a classical solution, then $u$ is a viscosity solution.

**Proof**: At any point, $\phi(x,t) = u(x,t)$ is a test function, so:

$$F(x,t,u,Du,D^2u) = 0$$



This satisfies both $F \leq 0$ (subsolution) and $F \geq 0$ (supersolution).

---

## **6. Comparison Principle**

### **Statement**

The **comparison principle** is the cornerstone of uniqueness theory.

**Theorem**: Let $u$ be a viscosity subsolution and $v$ be a viscosity supersolution of:

$$F(x,t,w,Dw,D^2w) = 0 \quad \text{in } \Omega \times (0,T)$$



Assume:
1. $F$ is **degenerate elliptic**: $F(x,t,r,p,A) \geq F(x,t,r,p,B)$ whenever $A \geq B$
2. $F$ is **continuous** and satisfies appropriate growth conditions
3. $u(x,T) \leq v(x,T)$ for all $x \in \Omega$
4. $u \leq v$ on the parabolic boundary

Then:

$$\boxed{u \leq v \quad \text{in } \Omega \times [0,T]}$$



### **Degenerate Ellipticity**

This means adding more "convexity" (larger $D^2u$) makes $F$ larger. For Black-Scholes:

$$F = u_t + rSu_S + \frac{\sigma^2 S^2}{2}u_{SS} - ru$$



We have $\frac{\partial F}{\partial u_{SS}} = \frac{\sigma^2 S^2}{2} \geq 0$, so it's degenerate elliptic.

### **Uniqueness Corollary**

If viscosity solutions exist, the comparison principle implies **uniqueness**:

If $u_1$ and $u_2$ are both viscosity solutions with the same boundary data, then $u_1 \leq u_2$ and $u_2 \leq u_1$, so $u_1 = u_2$.

---

## **7. Existence Theory**

### **Perron's Method**

Define:

$$\underline{u}(x,t) = \sup\{v(x,t) : v \text{ is a viscosity subsolution with } v(x,T) \leq g(x)\}$$




$$\overline{u}(x,t) = \inf\{w(x,t) : w \text{ is a viscosity supersolution with } w(x,T) \geq g(x)\}$$



**Theorem**: Under appropriate conditions:
1. $\underline{u}$ is a viscosity subsolution
2. $\overline{u}$ is a viscosity supersolution
3. If $\underline{u} = \overline{u}$, then $u = \underline{u} = \overline{u}$ is the **unique** viscosity solution

### **Vanishing Viscosity Method**

Add artificial viscosity:

$$F(x,t,u^\epsilon, Du^\epsilon, D^2u^\epsilon) - \epsilon \Delta u^\epsilon = 0$$



This has smooth solutions $u^\epsilon$. Under suitable conditions:

$$u^\epsilon \to u \quad \text{as } \epsilon \to 0$$



and $u$ is the viscosity solution.

### **Approximation by Smooth Functions**

Replace the terminal data $g(x)$ by smooth approximations $g_n \in C^\infty$ with $g_n \to g$ uniformly.

Solve for smooth solutions $u_n$ with terminal data $g_n$.

Then $u_n \to u$ where $u$ is the viscosity solution with terminal data $g$.

---

## **8. Connection to Stochastic Control**

### **Dynamic Programming Principle (DPP)**

For the stochastic control problem:

$$V(x,t) = \sup_{\alpha \in \mathcal{A}}\mathbb{E}\left[\int_t^T f(X_s^\alpha, \alpha_s)e^{-\int_t^s r(\tau)d\tau}ds + g(X_T^\alpha)e^{-\int_t^T r(\tau)d\tau} \mid X_t = x\right]$$



where $X^\alpha$ satisfies:

$$dX_s = b(X_s, \alpha_s)ds + \sigma(X_s, \alpha_s)dW_s$$



The DPP states:

$$V(x,t) = \sup_{\alpha}\mathbb{E}\left[\int_t^{t+h}f(X_s^\alpha,\alpha_s)e^{-\int_t^s r d\tau}ds + V(X_{t+h}^\alpha, t+h)e^{-\int_t^{t+h}r d\tau} \mid X_t = x\right]$$



### **HJB Equation**

Taking $h \to 0$ formally gives the **Hamilton-Jacobi-Bellman equation**:

$$\boxed{\frac{\partial V}{\partial t} + \sup_{\alpha \in A}\left[b(x,\alpha) \cdot DV + \frac{1}{2}\text{tr}(\sigma\sigma^T(x,\alpha)D^2V) + f(x,\alpha)\right] - rV = 0}$$



### **Viscosity Solution Connection**

**Theorem**: The value function $V$ defined via the stochastic control problem is a **viscosity solution** of the HJB equation.

**Proof sketch**: 
- Use DPP with smooth test functions
- For subsolution: if $\phi$ touches $V$ from above at $(x_0,t_0)$, then for small $h$:

  $$\phi(x_0,t_0) \geq \mathbb{E}[\cdots + \phi(X_{t_0+h}, t_0+h)e^{-rh}]$$


  Itô's formula + supremum over $\alpha$ gives $F(\phi) \leq 0$
- Similarly for supersolution

This is why viscosity solutions are **natural** for finance!

---

## **9. American Options**

### **Obstacle Problem**

For an American option with payoff $\Phi(S)$:

$$V(S,t) = \sup_{\tau \in [t,T]}\mathbb{E}^{\mathbb{Q}}[e^{-r(\tau-t)}\Phi(S_\tau) \mid S_t = S]$$



This is an **optimal stopping problem**.

### **Variational Inequality**

The value function satisfies:

$$\boxed{\min\left\{-\frac{\partial V}{\partial t} - \mathcal{L}V, \, V - \Phi\right\} = 0}$$



where $\mathcal{L}$ is the Black-Scholes operator:

$$\mathcal{L}V = rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} - rV$$



### **Regions**

- **Continuation region**: $\mathcal{C} = \{(S,t) : V(S,t) > \Phi(S)\}$
  - Here: $-\frac{\partial V}{\partial t} - \mathcal{L}V = 0$
  
- **Stopping region**: $\mathcal{S} = \{(S,t) : V(S,t) = \Phi(S)\}$
  - Here: $-\frac{\partial V}{\partial t} - \mathcal{L}V \leq 0$

### **Free Boundary**

The boundary $\partial \mathcal{C}$ is the **optimal exercise boundary** $S^*(t)$.

At $S = S^*(t)$, $V$ is typically **not $C^2$**—only $C^1$ (smooth fit).

### **Viscosity Solution**

$V$ is the unique viscosity solution of the variational inequality with terminal condition $V(S,T) = \Phi(S)$.

**Key properties**:
1. $V \geq \Phi$ (no-arbitrage)
2. $V$ is continuous
3. In $\mathcal{C}$: $V$ is $C^{2,1}$ and satisfies the PDE
4. At the free boundary: only viscosity derivatives exist

---

## **10. Detailed Example: American Put**

### **Setup**

Payoff: $\Phi(S) = (K - S)^+$

The variational inequality:

$$\min\left\{\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} - rV, \, (K-S) - V\right\} = 0$$



### **Properties**

1. **Early exercise**: Optimal to exercise when $S \leq S^*(t)$ for some boundary $S^*(t)$
2. **Smooth fit**: $V(S^*(t), t) = K - S^*(t)$ and $\frac{\partial V}{\partial S}(S^*(t), t) = -1$
3. **Non-smooth second derivative**: $\frac{\partial^2 V}{\partial S^2}$ jumps at $S^*(t)$

### **Viscosity Formulation**

For $S > S^*(t)$ (continuation region):
- Test functions touching from above: $F(\phi) \leq 0$
- Test functions touching from below: $F(\phi) \geq 0$
- Classical solution holds: $F = 0$

At $S = S^*(t)$ (free boundary):
- From above: $\phi$ satisfies $F(\phi) \leq 0$ (or $\phi = K - S$ which gives $V - \Phi = 0$)
- From below: $\phi$ satisfies $F(\phi) \geq 0$

For $S < S^*(t)$ (stopping region):
- $V = K - S$ (payoff)
- Any test function must satisfy the obstacle constraint

### **Comparison Principle**

Ensures uniqueness: any two viscosity solutions must coincide.

This guarantees that:

$$V_{\text{viscosity}} = V_{\text{probabilistic}} = \sup_\tau \mathbb{E}[e^{-r\tau}\Phi(S_\tau)]$$



---

## **11. Regularity Theory**

### **When is the Viscosity Solution Classical?**

**Theorem**: If:
1. The payoff $\Phi$ is $C^2$
2. The coefficients are smooth
3. The operator is uniformly elliptic: $\sigma^2 S^2 \geq c > 0$

Then the viscosity solution is **classical** ($C^{2,1}$).

### **Degenerate Case**

For Black-Scholes, $\sigma^2 S^2 \to 0$ as $S \to 0$ (**degeneracy**).

The solution may fail to be $C^2$ at $S = 0$ even with smooth payoffs.

### **Hölder Continuity**

**Theorem**: Under mild conditions, viscosity solutions are **locally Hölder continuous**:

$$|u(x,t) - u(y,s)| \leq C(|x-y|^\alpha + |t-s|^{\alpha/2})$$



for some $\alpha \in (0,1)$.

### **$C^{2,\alpha}$ Interior Regularity**

Away from boundaries and degeneracies, viscosity solutions are typically **$C^{2,\alpha}$** (classical).

Singularities only occur at:
- Boundaries
- Degeneracy points
- Free boundaries
- Non-smooth payoffs

---

## **12. Numerical Methods**

### **Finite Difference Schemes**

For the scheme:

$$\frac{V_j^{n+1} - V_j^n}{\Delta t} + \mathcal{L}_h V_j^{n+1} = 0$$



**Consistency**: The scheme approximates the PDE
**Monotonicity**: Increasing $V$ at neighboring points increases the scheme
**Stability**: Bounded growth of errors

**Theorem (Barles-Souganidis)**: A consistent, monotone, stable scheme **converges** to the viscosity solution.

### **Monotone Schemes**

For Black-Scholes, a **monotone scheme** might be:

$$\frac{V_j^{n+1} - V_j^n}{\Delta t} + r S_j \frac{V_{j+1}^{n+1} - V_{j-1}^{n+1}}{2\Delta S} + \frac{\sigma^2 S_j^2}{2}\frac{V_{j+1}^{n+1} - 2V_j^{n+1} + V_{j-1}^{n+1}}{(\Delta S)^2} - rV_j^{n+1} = 0$$



provided the **CFL condition** ensures monotonicity.

### **American Options**

At each time step:

$$V_j^{n+1} = \max\left\{\Phi(S_j), \text{continuation value}\right\}$$



This automatically enforces the obstacle constraint.

### **Convergence**

**Theorem**: The discrete scheme converges to the viscosity solution of the continuous variational inequality.

This justifies **practical algorithms** like:
- Finite differences
- Binomial trees
- Trinomial trees

---

## **13. Obstacle Problems and Penalization**

### **Penalization Method**

Replace the obstacle problem:

$$\min\{-u_t - \mathcal{L}u, u - g\} = 0$$



with the penalized equation:

$$-u_t^\epsilon - \mathcal{L}u^\epsilon - \frac{1}{\epsilon}(u^\epsilon - g)^- = 0$$



where $(x)^- = \max(-x, 0)$.

### **Convergence**

As $\epsilon \to 0$:

$$u^\epsilon \to u$$



where $u$ is the viscosity solution of the obstacle problem.

**Proof sketch**: 
- $u^\epsilon$ is smooth
- Comparison principle for penalized equation
- Stability under limits

### **Regularization by Penalty**

The penalty term $-\frac{1}{\epsilon}(u^\epsilon - g)^-$ acts as:
- A large negative force when $u^\epsilon < g$ (pushing $u^\epsilon$ up)
- Zero when $u^\epsilon \geq g$ (inactive)

As $\epsilon \to 0$, this enforces $u \geq g$ exactly.

---

## **14. Transaction Costs**

### **Hodges-Neuberger Model**

With proportional transaction costs, the value function satisfies:

$$\frac{\partial V}{\partial t} + \sup_{\alpha \in \mathbb{R}}\left\{\alpha\left(\sigma S\frac{\partial V}{\partial S} - c\text{sgn}(\alpha)\right)\right\} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} - rV = 0$$



where $c$ is the transaction cost rate.

### **Hamilton-Jacobi-Bellman Structure**

The supremum over $\alpha$ gives:

$$\sup_\alpha\left\{\alpha\left(\sigma S\frac{\partial V}{\partial S} - c\text{sgn}(\alpha)\right)\right\} = \begin{cases}
0 & \text{if } |\sigma S\frac{\partial V}{\partial S}| \leq c \\
+\infty & \text{otherwise}
\end{cases}$$



This forces:

$$\boxed{\left|\sigma S\frac{\partial V}{\partial S}\right| \leq c}$$



in the viscosity sense—a **gradient constraint**.

### **No-Transaction Region**

There's a region where:

$$\left|\Delta\right| = \left|\frac{\partial V}{\partial S}\right| < \frac{c}{\sigma S}$$



and no trading occurs.

Outside this region, trade to return to the boundary.

### **Viscosity Solution**

The value function is the unique viscosity solution satisfying:
1. The gradient constraint
2. The PDE in regions where it's classical
3. Appropriate boundary conditions

---

## **15. Portfolio Optimization**

### **Merton Problem**

Maximize expected utility:

$$V(x,t) = \sup_{\pi}\mathbb{E}\left[U(X_T) \mid X_t = x\right]$$



subject to:

$$dX_t = [rX_t + \pi_t(\mu - r)]dt + \pi_t \sigma dW_t$$



### **HJB Equation**


$$\boxed{\frac{\partial V}{\partial t} + \sup_\pi\left[rx\frac{\partial V}{\partial x} + \pi(\mu-r)\frac{\partial V}{\partial x} + \frac{\pi^2\sigma^2}{2}\frac{\partial^2 V}{\partial x^2}\right] = 0}$$



### **First-Order Condition**

The supremum is achieved at:

$$\pi^* = -\frac{(\mu-r)\frac{\partial V}{\partial x}}{\sigma^2\frac{\partial^2 V}{\partial x^2}}$$



provided $\frac{\partial^2 V}{\partial x^2} < 0$ (concavity).

### **Non-Smooth Terminal Utility**

For non-smooth $U$ (e.g., power utility with constraints), classical solutions may not exist.

The value function is a **viscosity solution** of the HJB equation.

---

## **16. Comparison with Other Solution Concepts**

### **Classical Solutions**

- **Requires**: $C^2$ regularity
- **Applies**: Smooth data, non-degenerate operators
- **Unique**: Yes, when exists
- **Finance**: European options with smooth payoffs

### **Weak Solutions**

- **Requires**: $H^1$ (Sobolev space)
- **Applies**: Variational formulations
- **Unique**: Not always
- **Finance**: Less common

### **Viscosity Solutions**

- **Requires**: Only continuity
- **Applies**: Non-smooth data, degenerate/singular operators, optimal control
- **Unique**: Yes, under comparison principle
- **Finance**: American options, transaction costs, stochastic control

### **Strong vs. Viscosity**

If $u \in C^2$ solves the PDE classically, then:

$$\text{Classical} \implies \text{Viscosity} \implies \text{Weak}$$



But the converse is false—viscosity solutions are **more general**.

---

## **17. User's Guide to Viscosity Solutions**

### **When to Use Viscosity Theory**

Use viscosity solutions when:
1. **Non-smooth payoffs**: Digital options, barriers
2. **Optimal stopping**: American options
3. **Optimal control**: Portfolio optimization, consumption
4. **Free boundaries**: Exercise boundaries
5. **Degenerate operators**: $\sigma \to 0$ near boundaries
6. **Transaction costs**: Gradient constraints

### **How to Verify a Solution**

To show $u$ is a viscosity solution:

**Step 1**: Show $u$ is continuous

**Step 2**: For subsolution, take any test function $\phi$ touching from above at $(x_0,t_0)$:
- Compute $F(x_0, t_0, u(x_0,t_0), D\phi(x_0,t_0), D^2\phi(x_0,t_0))$
- Verify $F \leq 0$

**Step 3**: For supersolution, take any test function $\phi$ touching from below:
- Verify $F \geq 0$

**Step 4**: Check boundary conditions

**Step 5**: Apply comparison principle for uniqueness

### **Common Pitfalls**

1. **Forgetting semi-continuity**: Subsolutions must be USC, supersolutions LSC
2. **Using global test functions**: Only need local max/min
3. **Ignoring degeneracy**: Standard elliptic theory doesn't apply
4. **Assuming smoothness**: The whole point is to avoid this!

---

## **18. Advanced Topics**

### **Fully Nonlinear Equations**

For general $F(D^2u, Du, u, x)$, the Bellman equation:

$$F(D^2u) = \sup_{\alpha \in A}F_\alpha(D^2u)$$



Each $F_\alpha$ corresponds to a control choice.

Viscosity theory handles **fully nonlinear** operators naturally.

### **Geometric Flows**

The **mean curvature flow**:

$$u_t = |\nabla u|\text{div}\left(\frac{\nabla u}{|\nabla u|}\right)$$



can develop singularities. Viscosity solutions extend through singularities.

### **Differential Games**

For two-player zero-sum games:

$$\frac{\partial V}{\partial t} + \sup_{\alpha}\inf_{\beta}[F(x,\alpha,\beta,V,DV,D^2V)] = 0$$



The value function is a viscosity solution.

### **Singular Control**

For impulse control or singular control problems, the HJB involves **quasi-variational inequalities**:

$$\min\{-u_t - \mathcal{L}u, u - Mu\} = 0$$



where $Mu$ is the **intervention operator**.

---

## **19. Probabilistic Interpretation**

### **Perron-Frobenius Formula**

For the obstacle problem:

$$u(x,t) = \sup_{\tau \leq T-t}\mathbb{E}\left[\int_t^\tau f(X_s)e^{-r(s-t)}ds + g(X_\tau)e^{-r(\tau-t)}\right]$$



The viscosity solution $u$ **is** the value function.

### **Comparison via Probability**

To prove comparison, use:

$$u(x,t) \leq \mathbb{E}[\cdots] \quad \text{for all strategies}$$



$$v(x,t) \geq \mathbb{E}[\cdots] \quad \text{for optimal strategy}$$



Therefore $u \leq v$.

### **Martingale Characterization**

A function $u$ is a viscosity solution iff the process:

$$M_t = e^{-rt}u(X_t,t) + \int_0^t e^{-rs}f(X_s,s)ds$$



is a **supermartingale** for all strategies and a **martingale** for optimal strategies.

---

## **20. The Deep Beauty**

### **Unified Framework**

Viscosity theory **unifies**:
- PDE theory (analysis)
- Stochastic control (probability)
- Optimal stopping (decision theory)
- Game theory (strategic interaction)

### **The Fundamental Equivalence**


$$\boxed{\text{Viscosity solution of HJB} \iff \text{Value function of stochastic control}}$$



This is the **modern foundation** of mathematical finance.

### **Why It Works**

The genius of viscosity solutions:
1. **Weak enough**: Applies to non-smooth functions
2. **Strong enough**: Guarantees uniqueness (comparison principle)
3. **Stable**: Approximations converge
4. **Computable**: Numerical schemes work
5. **Probabilistically meaningful**: Connects to value functions

### **The Philosophy**

Classical PDE theory asks: "What is the smoothest solution?"

Viscosity theory asks: "What is the **economically correct** solution?"

For finance, the **economically correct** solution is:

$$V = \text{sup over strategies} \ \mathbb{E}[\text{payoff}]$$



which is **always** a viscosity solution, even when it's not classical.

---

## **21. Summary: The Viscosity Toolkit**

| **Problem** | **Classical Approach** | **Viscosity Approach** |
|-------------|------------------------|------------------------|
| European call (smooth) | PDE + Feynman-Kac | Same (viscosity = classical) |
| Digital option | Fails (discontinuous) | Viscosity solution exists |
| American put | Free boundary problem | Obstacle problem (viscosity) |
| Transaction costs | Gradient constraints | HJB with constraints |
| Stochastic control | Verify HJB formally | Value function is viscosity solution |
| Numerical methods | Ad hoc convergence | Barles-Souganidis theorem |

### **The Master Theorem**

For a stochastic control problem with value function $V$:

1. $V$ is **continuous**
2. $V$ is a **viscosity solution** of the HJB equation
3. $V$ is the **unique** viscosity solution (comparison principle)
4. Numerical approximations **converge** to $V$

This is the **complete theory** in four statements!

---

Would you like me to explore:
- Detailed proof of the comparison principle for Black-Scholes
- Specific numerical schemes and their monotonicity properties
- Multi-dimensional obstacle problems (e.g., multi-asset Americans)
- Connection to backward stochastic differential equations (BSDEs)
- Singular control and impulse control in detail
- Viscosity solutions for path-dependent options
- The relationship with weak formulations and Sobolev spaces?
