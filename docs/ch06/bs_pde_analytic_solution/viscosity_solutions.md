# Viscosity Solutions: Complete Mathematical Treatment


Viscosity solutions provide a **rigorous framework** for nonlinear PDEs that handles **non-smooth data**, **degenerate equations**, and **optimal control problems**—all central to modern mathematical finance.

---

## **1. Motivation: Why Classical Solutions Fail**


### 1. **The Problem with Non-Smooth Payoffs**


Consider a digital option with payoff:

$$\Phi(S) = \mathbb{1}_{S > K}$$



The Black-Scholes PDE:

$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} - rV = 0$$



with terminal condition $V(S,T) = \mathbb{1}_{S > K}$ has **no classical solution**—the payoff is discontinuous!

### 2. **American Options**


The free boundary problem:

$$\max\left\{-\frac{\partial V}{\partial t} - rS\frac{\partial V}{\partial S} - \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} + rV, \, V - \Phi(S)\right\} = 0$$



The solution $V$ is typically **not $C^2$** at the free boundary, so classical derivatives don't exist.

### 3. **Transaction Costs**


With proportional transaction costs, the Hamilton-Jacobi-Bellman equation:

$$\frac{\partial V}{\partial t} + \sup_{\alpha}\left[\alpha \sigma S \frac{\partial V}{\partial S} - c|\alpha|\right] + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} - rV = 0$$



involves a **non-smooth Hamiltonian** (absolute value).

### 4. **The Gap**


**Classical theory**: Requires $C^2$ solutions
**Reality**: Financial PDEs rarely have $C^2$ solutions

**Viscosity theory**: Fills this gap!

---

## **2. Fundamental Definitions**


### 1. **General Parabolic PDE**


Consider:

$$\boxed{F\left(x, t, u, Du, D^2u\right) = 0 \quad \text{in } \Omega \times (0,T)}$$



where:
- $u: \Omega \times [0,T] \to \mathbb{R}$ is the unknown
- $Du = \nabla u$ is the gradient
- $D^2u$ is the Hessian matrix
- $F$ is the **PDE operator** (possibly nonlinear)

**Boundary condition**: $u(x,T) = g(x)$

### 2. **Upper/Lower Semicontinuity**


A function $u$ is:
- **Upper semicontinuous (USC)** if $\limsup_{y \to x}u(y) \leq u(x)$
- **Lower semicontinuous (LSC)** if $\liminf_{y \to x}u(y) \geq u(x)$

**Intuition**: USC functions don't have upward jumps; LSC functions don't have downward jumps.

### 3. **Test Functions**


A function $\phi \in C^2(\Omega \times [0,T])$ is a **test function** for $u$ at $(x_0, t_0)$ if:

$$u(x,t) - \phi(x,t) \text{ has a local maximum (or minimum) at } (x_0,t_0)$$



---

## **3. Viscosity Subsolutions**


### 1. **Definition**


A USC function $u$ is a **viscosity subsolution** of $F(x,t,u,Du,D^2u) = 0$ if:

For every $(x_0,t_0) \in \Omega \times (0,T)$ and every $\phi \in C^2$ such that $u - \phi$ has a **local maximum** at $(x_0,t_0)$:


$$\boxed{F(x_0, t_0, u(x_0,t_0), D\phi(x_0,t_0), D^2\phi(x_0,t_0)) \leq 0}$$



### 2. **Intuition**


At points where we can "touch from above" with a smooth function, the PDE inequality $F \leq 0$ holds in the **viscosity sense**.

### 3. **Why "Viscosity"?**


Historically, this notion arose from adding **artificial viscosity** $\epsilon \Delta u$ to make the equation:

$$F(x,t,u,Du,D^2u) - \epsilon \Delta u = 0$$



which has smooth solutions. Taking $\epsilon \to 0$ gives the viscosity solution.

### 4. **Black-Scholes Example**


For the operator:

$$F = \frac{\partial u}{\partial t} + rS\frac{\partial u}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 u}{\partial S^2} - ru$$



A function $u$ is a viscosity subsolution if for every test function $\phi$ touching from above:

$$\frac{\partial \phi}{\partial t} + rS\frac{\partial \phi}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 \phi}{\partial S^2} - r\phi \leq 0$$



at the touching point.

---

## **4. Viscosity Supersolutions**


### 1. **Definition**


A LSC function $u$ is a **viscosity supersolution** of $F(x,t,u,Du,D^2u) = 0$ if:

For every $(x_0,t_0) \in \Omega \times (0,T)$ and every $\phi \in C^2$ such that $u - \phi$ has a **local minimum** at $(x_0,t_0)$:


$$\boxed{F(x_0, t_0, u(x_0,t_0), D\phi(x_0,t_0), D^2\phi(x_0,t_0)) \geq 0}$$



### 2. **Intuition**


At points where we can "touch from below" with a smooth function, $F \geq 0$ in the viscosity sense.

---

## **5. Viscosity Solutions**


### 1. **Definition**


A continuous function $u$ is a **viscosity solution** if it is both:
1. A viscosity subsolution
2. A viscosity supersolution


$$\boxed{u \text{ is a viscosity solution} \iff \text{subsolution AND supersolution}}$$



### 2. **Equivalent Definition (Semijets)**


Define the **second-order superdifferential**:

$$\overline{D^2}u(x_0,t_0) = \{(p, A) : u(x,t) \leq u(x_0,t_0) + \langle p, (x-x_0,t-t_0) \rangle + \frac{1}{2}\langle A(x-x_0,t-t_0), (x-x_0,t-t_0)\rangle + o(|(x-x_0,t-t_0)|^2)\}$$



Then $u$ is a viscosity subsolution if:

$$F(x_0,t_0,u(x_0,t_0), p, A) \leq 0 \quad \forall (p,A) \in \overline{D^2}u(x_0,t_0)$$



Similarly for supersolutions using the **subdifferential** $\underline{D^2}u$.

### 3. **Classical Solutions are Viscosity Solutions**


**Proposition**: If $u \in C^2$ is a classical solution, then $u$ is a viscosity solution.

**Proof**: At any point, $\phi(x,t) = u(x,t)$ is a test function, so:

$$F(x,t,u,Du,D^2u) = 0$$



This satisfies both $F \leq 0$ (subsolution) and $F \geq 0$ (supersolution).

---

## **6. Comparison Principle**


### 1. **Statement**


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



### 2. **Degenerate Ellipticity**


This means adding more "convexity" (larger $D^2u$) makes $F$ larger. For Black-Scholes:

$$F = u_t + rSu_S + \frac{\sigma^2 S^2}{2}u_{SS} - ru$$



We have $\frac{\partial F}{\partial u_{SS}} = \frac{\sigma^2 S^2}{2} \geq 0$, so it's degenerate elliptic.

### 3. **Uniqueness Corollary**


If viscosity solutions exist, the comparison principle implies **uniqueness**:

If $u_1$ and $u_2$ are both viscosity solutions with the same boundary data, then $u_1 \leq u_2$ and $u_2 \leq u_1$, so $u_1 = u_2$.

---

## **7. Existence Theory**


### 1. **Perron's Method**


Define:

$$\underline{u}(x,t) = \sup\{v(x,t) : v \text{ is a viscosity subsolution with } v(x,T) \leq g(x)\}$$




$$\overline{u}(x,t) = \inf\{w(x,t) : w \text{ is a viscosity supersolution with } w(x,T) \geq g(x)\}$$



**Theorem**: Under appropriate conditions:
1. $\underline{u}$ is a viscosity subsolution
2. $\overline{u}$ is a viscosity supersolution
3. If $\underline{u} = \overline{u}$, then $u = \underline{u} = \overline{u}$ is the **unique** viscosity solution

### 2. **Vanishing Viscosity Method**


Add artificial viscosity:

$$F(x,t,u^\epsilon, Du^\epsilon, D^2u^\epsilon) - \epsilon \Delta u^\epsilon = 0$$



This has smooth solutions $u^\epsilon$. Under suitable conditions:

$$u^\epsilon \to u \quad \text{as } \epsilon \to 0$$



and $u$ is the viscosity solution.

### 3. **Approximation by Smooth Functions**


Replace the terminal data $g(x)$ by smooth approximations $g_n \in C^\infty$ with $g_n \to g$ uniformly.

Solve for smooth solutions $u_n$ with terminal data $g_n$.

Then $u_n \to u$ where $u$ is the viscosity solution with terminal data $g$.

---

## **8. Connection to Stochastic Control**


### 1. **Dynamic Programming Principle (DPP)**


For the stochastic control problem:

$$V(x,t) = \sup_{\alpha \in \mathcal{A}}\mathbb{E}\left[\int_t^T f(X_s^\alpha, \alpha_s)e^{-\int_t^s r(\tau)d\tau}ds + g(X_T^\alpha)e^{-\int_t^T r(\tau)d\tau} \mid X_t = x\right]$$



where $X^\alpha$ satisfies:

$$dX_s = b(X_s, \alpha_s)ds + \sigma(X_s, \alpha_s)dW_s$$



The DPP states:

$$V(x,t) = \sup_{\alpha}\mathbb{E}\left[\int_t^{t+h}f(X_s^\alpha,\alpha_s)e^{-\int_t^s r d\tau}ds + V(X_{t+h}^\alpha, t+h)e^{-\int_t^{t+h}r d\tau} \mid X_t = x\right]$$



### 2. **HJB Equation**


Taking $h \to 0$ formally gives the **Hamilton-Jacobi-Bellman equation**:

$$\boxed{\frac{\partial V}{\partial t} + \sup_{\alpha \in A}\left[b(x,\alpha) \cdot DV + \frac{1}{2}\text{tr}(\sigma\sigma^T(x,\alpha)D^2V) + f(x,\alpha)\right] - rV = 0}$$



### 3. **Viscosity Solution Connection**


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


### 1. **Obstacle Problem**


For an American option with payoff $\Phi(S)$:

$$V(S,t) = \sup_{\tau \in [t,T]}\mathbb{E}^{\mathbb{Q}}[e^{-r(\tau-t)}\Phi(S_\tau) \mid S_t = S]$$



This is an **optimal stopping problem**.

### 2. **Variational Inequality**


The value function satisfies:

$$\boxed{\min\left\{-\frac{\partial V}{\partial t} - \mathcal{L}V, \, V - \Phi\right\} = 0}$$



where $\mathcal{L}$ is the Black-Scholes operator:

$$\mathcal{L}V = rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} - rV$$



### 3. **Regions**


- **Continuation region**: $\mathcal{C} = \{(S,t) : V(S,t) > \Phi(S)\}$
  - Here: $-\frac{\partial V}{\partial t} - \mathcal{L}V = 0$
  
- **Stopping region**: $\mathcal{S} = \{(S,t) : V(S,t) = \Phi(S)\}$
  - Here: $-\frac{\partial V}{\partial t} - \mathcal{L}V \leq 0$

### 4. **Free Boundary**


The boundary $\partial \mathcal{C}$ is the **optimal exercise boundary** $S^*(t)$.

At $S = S^*(t)$, $V$ is typically **not $C^2$**—only $C^1$ (smooth fit).

### 5. **Viscosity Solution**


$V$ is the unique viscosity solution of the variational inequality with terminal condition $V(S,T) = \Phi(S)$.

**Key properties**:
1. $V \geq \Phi$ (no-arbitrage)
2. $V$ is continuous
3. In $\mathcal{C}$: $V$ is $C^{2,1}$ and satisfies the PDE
4. At the free boundary: only viscosity derivatives exist

---

## **10. Detailed Example: American Put**


### 1. **Setup**


Payoff: $\Phi(S) = (K - S)^+$

The variational inequality:

$$\min\left\{\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} - rV, \, (K-S) - V\right\} = 0$$



### 2. **Properties**


1. **Early exercise**: Optimal to exercise when $S \leq S^*(t)$ for some boundary $S^*(t)$
2. **Smooth fit**: $V(S^*(t), t) = K - S^*(t)$ and $\frac{\partial V}{\partial S}(S^*(t), t) = -1$
3. **Non-smooth second derivative**: $\frac{\partial^2 V}{\partial S^2}$ jumps at $S^*(t)$

### 3. **Viscosity Formulation**


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

### 4. **Comparison Principle**


Ensures uniqueness: any two viscosity solutions must coincide.

This guarantees that:

$$V_{\text{viscosity}} = V_{\text{probabilistic}} = \sup_\tau \mathbb{E}[e^{-r\tau}\Phi(S_\tau)]$$



---

## **11. Regularity Theory**


### 1. **When is the Viscosity Solution Classical?**


**Theorem**: If:
1. The payoff $\Phi$ is $C^2$
2. The coefficients are smooth
3. The operator is uniformly elliptic: $\sigma^2 S^2 \geq c > 0$

Then the viscosity solution is **classical** ($C^{2,1}$).

### 2. **Degenerate Case**


For Black-Scholes, $\sigma^2 S^2 \to 0$ as $S \to 0$ (**degeneracy**).

The solution may fail to be $C^2$ at $S = 0$ even with smooth payoffs.

### 3. **Hölder Continuity**


**Theorem**: Under mild conditions, viscosity solutions are **locally Hölder continuous**:

$$|u(x,t) - u(y,s)| \leq C(|x-y|^\alpha + |t-s|^{\alpha/2})$$



for some $\alpha \in (0,1)$.

### 4. **C²,α Interior Regularity**


Away from boundaries and degeneracies, viscosity solutions are typically **$C^{2,\alpha}$** (classical).

Singularities only occur at:
- Boundaries
- Degeneracy points
- Free boundaries
- Non-smooth payoffs

---

## **12. Numerical Methods**


### 1. **Finite Difference Schemes**


For the scheme:

$$\frac{V_j^{n+1} - V_j^n}{\Delta t} + \mathcal{L}_h V_j^{n+1} = 0$$



**Consistency**: The scheme approximates the PDE
**Monotonicity**: Increasing $V$ at neighboring points increases the scheme
**Stability**: Bounded growth of errors

**Theorem (Barles-Souganidis)**: A consistent, monotone, stable scheme **converges** to the viscosity solution.

### 2. **Monotone Schemes**


For Black-Scholes, a **monotone scheme** might be:

$$\frac{V_j^{n+1} - V_j^n}{\Delta t} + r S_j \frac{V_{j+1}^{n+1} - V_{j-1}^{n+1}}{2\Delta S} + \frac{\sigma^2 S_j^2}{2}\frac{V_{j+1}^{n+1} - 2V_j^{n+1} + V_{j-1}^{n+1}}{(\Delta S)^2} - rV_j^{n+1} = 0$$



provided the **CFL condition** ensures monotonicity.

### 3. **American Options**


At each time step:

$$V_j^{n+1} = \max\left\{\Phi(S_j), \text{continuation value}\right\}$$



This automatically enforces the obstacle constraint.

### 4. **Convergence**


**Theorem**: The discrete scheme converges to the viscosity solution of the continuous variational inequality.

This justifies **practical algorithms** like:
- Finite differences
- Binomial trees
- Trinomial trees

---

## **13. Obstacle Problems and Penalization**


### 1. **Penalization Method**


Replace the obstacle problem:

$$\min\{-u_t - \mathcal{L}u, u - g\} = 0$$



with the penalized equation:

$$-u_t^\epsilon - \mathcal{L}u^\epsilon - \frac{1}{\epsilon}(u^\epsilon - g)^- = 0$$



where $(x)^- = \max(-x, 0)$.

### 2. **Convergence**


As $\epsilon \to 0$:

$$u^\epsilon \to u$$



where $u$ is the viscosity solution of the obstacle problem.

**Proof sketch**: 
- $u^\epsilon$ is smooth
- Comparison principle for penalized equation
- Stability under limits

### 3. **Regularization by Penalty**


The penalty term $-\frac{1}{\epsilon}(u^\epsilon - g)^-$ acts as:
- A large negative force when $u^\epsilon < g$ (pushing $u^\epsilon$ up)
- Zero when $u^\epsilon \geq g$ (inactive)

As $\epsilon \to 0$, this enforces $u \geq g$ exactly.

---

## **14. Transaction Costs**


### 1. **Hodges-Neuberger Model**


With proportional transaction costs, the value function satisfies:

$$\frac{\partial V}{\partial t} + \sup_{\alpha \in \mathbb{R}}\left\{\alpha\left(\sigma S\frac{\partial V}{\partial S} - c\text{sgn}(\alpha)\right)\right\} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} - rV = 0$$



where $c$ is the transaction cost rate.

### 2. **Hamilton-Jacobi-Bellman Structure**


The supremum over $\alpha$ gives:

$$\sup_\alpha\left\{\alpha\left(\sigma S\frac{\partial V}{\partial S} - c\text{sgn}(\alpha)\right)\right\} = \begin{cases}
0 & \text{if } |\sigma S\frac{\partial V}{\partial S}| \leq c \\
+\infty & \text{otherwise}
\end{cases}$$



This forces:

$$\boxed{\left|\sigma S\frac{\partial V}{\partial S}\right| \leq c}$$



in the viscosity sense—a **gradient constraint**.

### 3. **No-Transaction Region**


There's a region where:

$$\left|\Delta\right| = \left|\frac{\partial V}{\partial S}\right| < \frac{c}{\sigma S}$$



and no trading occurs.

Outside this region, trade to return to the boundary.

### 4. **Viscosity Solution**


The value function is the unique viscosity solution satisfying:
1. The gradient constraint
2. The PDE in regions where it's classical
3. Appropriate boundary conditions

---

## **15. Portfolio Optimization**


### 1. **Merton Problem**


Maximize expected utility:

$$V(x,t) = \sup_{\pi}\mathbb{E}\left[U(X_T) \mid X_t = x\right]$$



subject to:

$$dX_t = [rX_t + \pi_t(\mu - r)]dt + \pi_t \sigma dW_t$$



### 2. **HJB Equation**



$$\boxed{\frac{\partial V}{\partial t} + \sup_\pi\left[rx\frac{\partial V}{\partial x} + \pi(\mu-r)\frac{\partial V}{\partial x} + \frac{\pi^2\sigma^2}{2}\frac{\partial^2 V}{\partial x^2}\right] = 0}$$



### 3. **First-Order Condition**


The supremum is achieved at:

$$\pi^* = -\frac{(\mu-r)\frac{\partial V}{\partial x}}{\sigma^2\frac{\partial^2 V}{\partial x^2}}$$



provided $\frac{\partial^2 V}{\partial x^2} < 0$ (concavity).

### 4. **Non-Smooth Terminal Utility**


For non-smooth $U$ (e.g., power utility with constraints), classical solutions may not exist.

The value function is a **viscosity solution** of the HJB equation.

---

## **16. Comparison with Other Solution Concepts**


### 1. **Classical Solutions**


- **Requires**: $C^2$ regularity
- **Applies**: Smooth data, non-degenerate operators
- **Unique**: Yes, when exists
- **Finance**: European options with smooth payoffs

### 2. **Weak Solutions**


- **Requires**: $H^1$ (Sobolev space)
- **Applies**: Variational formulations
- **Unique**: Not always
- **Finance**: Less common

### 3. **Viscosity Solutions**


- **Requires**: Only continuity
- **Applies**: Non-smooth data, degenerate/singular operators, optimal control
- **Unique**: Yes, under comparison principle
- **Finance**: American options, transaction costs, stochastic control

### 4. **Strong vs. Viscosity**


If $u \in C^2$ solves the PDE classically, then:

$$\text{Classical} \implies \text{Viscosity} \implies \text{Weak}$$



But the converse is false—viscosity solutions are **more general**.

---

## **17. User's Guide to Viscosity Solutions**


### 1. **When to Use Viscosity Theory**


Use viscosity solutions when:
1. **Non-smooth payoffs**: Digital options, barriers
2. **Optimal stopping**: American options
3. **Optimal control**: Portfolio optimization, consumption
4. **Free boundaries**: Exercise boundaries
5. **Degenerate operators**: $\sigma \to 0$ near boundaries
6. **Transaction costs**: Gradient constraints

### 2. **How to Verify a Solution**


To show $u$ is a viscosity solution:

**Step 1**: Show $u$ is continuous

**Step 2**: For subsolution, take any test function $\phi$ touching from above at $(x_0,t_0)$:
- Compute $F(x_0, t_0, u(x_0,t_0), D\phi(x_0,t_0), D^2\phi(x_0,t_0))$
- Verify $F \leq 0$

**Step 3**: For supersolution, take any test function $\phi$ touching from below:
- Verify $F \geq 0$

**Step 4**: Check boundary conditions

**Step 5**: Apply comparison principle for uniqueness

### 3. **Common Pitfalls**


1. **Forgetting semi-continuity**: Subsolutions must be USC, supersolutions LSC
2. **Using global test functions**: Only need local max/min
3. **Ignoring degeneracy**: Standard elliptic theory doesn't apply
4. **Assuming smoothness**: The whole point is to avoid this!

---

## **18. Advanced Topics**


### 1. **Fully Nonlinear Equations**


For general $F(D^2u, Du, u, x)$, the Bellman equation:

$$F(D^2u) = \sup_{\alpha \in A}F_\alpha(D^2u)$$



Each $F_\alpha$ corresponds to a control choice.

Viscosity theory handles **fully nonlinear** operators naturally.

### 2. **Geometric Flows**


The **mean curvature flow**:

$$u_t = |\nabla u|\text{div}\left(\frac{\nabla u}{|\nabla u|}\right)$$



can develop singularities. Viscosity solutions extend through singularities.

### 3. **Differential Games**


For two-player zero-sum games:

$$\frac{\partial V}{\partial t} + \sup_{\alpha}\inf_{\beta}[F(x,\alpha,\beta,V,DV,D^2V)] = 0$$



The value function is a viscosity solution.

### 4. **Singular Control**


For impulse control or singular control problems, the HJB involves **quasi-variational inequalities**:

$$\min\{-u_t - \mathcal{L}u, u - Mu\} = 0$$



where $Mu$ is the **intervention operator**.

---

## **19. Probabilistic Interpretation**


### 1. **Perron-Frobenius Formula**


For the obstacle problem:

$$u(x,t) = \sup_{\tau \leq T-t}\mathbb{E}\left[\int_t^\tau f(X_s)e^{-r(s-t)}ds + g(X_\tau)e^{-r(\tau-t)}\right]$$



The viscosity solution $u$ **is** the value function.

### 2. **Comparison via Probability**


To prove comparison, use:

$$u(x,t) \leq \mathbb{E}[\cdots] \quad \text{for all strategies}$$



$$v(x,t) \geq \mathbb{E}[\cdots] \quad \text{for optimal strategy}$$



Therefore $u \leq v$.

### 3. **Martingale Characterization**


A function $u$ is a viscosity solution iff the process:

$$M_t = e^{-rt}u(X_t,t) + \int_0^t e^{-rs}f(X_s,s)ds$$



is a **supermartingale** for all strategies and a **martingale** for optimal strategies.

---

## **20. The Deep Beauty**


### 1. **Unified Framework**


Viscosity theory **unifies**:
- PDE theory (analysis)
- Stochastic control (probability)
- Optimal stopping (decision theory)
- Game theory (strategic interaction)

### 2. **The Fundamental Equivalence**



$$\boxed{\text{Viscosity solution of HJB} \iff \text{Value function of stochastic control}}$$



This is the **modern foundation** of mathematical finance.

### 3. **Why It Works**


The genius of viscosity solutions:
1. **Weak enough**: Applies to non-smooth functions
2. **Strong enough**: Guarantees uniqueness (comparison principle)
3. **Stable**: Approximations converge
4. **Computable**: Numerical schemes work
5. **Probabilistically meaningful**: Connects to value functions

### 4. **The Philosophy**


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

### 1. **The Master Theorem**


For a stochastic control problem with value function $V$:

1. $V$ is **continuous**
2. $V$ is a **viscosity solution** of the HJB equation
3. $V$ is the **unique** viscosity solution (comparison principle)
4. Numerical approximations **converge** to $V$

This is the **complete theory** in four statements!

---

---

## Exercises

**Exercise 1.** A digital call option has payoff $\Phi(S) = \mathbf{1}_{\{S > K\}}$, which is discontinuous at $S = K$. Explain why the Black-Scholes PDE with this terminal condition has no classical ($C^{2,1}$) solution. Then describe how the viscosity solution framework resolves this issue, and verify that $V(S,t) = e^{-r(T-t)}\mathcal{N}(d_2)$ is the viscosity solution.

---

**Exercise 2.** State the definition of a viscosity subsolution and supersolution for the Black-Scholes PDE. Using these definitions, explain why the maximum of two viscosity solutions is a viscosity subsolution but not necessarily a viscosity solution.

---

**Exercise 3.** For an American put option, the value function satisfies the variational inequality $\min\left(-\mathcal{L}V, \, V - (K - S)^+\right) = 0$, where $\mathcal{L}$ is the Black-Scholes differential operator. Interpret each of the two conditions in this inequality financially, and explain why the obstacle problem formulation is natural for early exercise.

---

**Exercise 4.** The comparison principle for viscosity solutions states that if $u$ is a subsolution and $v$ is a supersolution with $u(S,T) \leq v(S,T)$, then $u \leq v$ everywhere. Explain why this principle is essential for proving uniqueness of viscosity solutions. Give a financial example where non-uniqueness of PDE solutions would lead to arbitrage.

---

**Exercise 5.** The Barles-Souganidis theorem guarantees convergence of numerical schemes to the viscosity solution if the scheme is monotone, consistent, and stable. For the explicit finite-difference scheme applied to the Black-Scholes PDE, state the CFL condition that ensures monotonicity and explain what happens when it is violated.

---

**Exercise 6.** Consider the Black-Scholes PDE with transaction costs, leading to the nonlinear equation $\frac{\partial V}{\partial t} + \frac{1}{2}\tilde{\sigma}^2(\Gamma) S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$ where $\tilde{\sigma}$ depends on $\Gamma = \frac{\partial^2 V}{\partial S^2}$. Explain why classical solutions may not exist for this equation and why the viscosity solution framework is the appropriate mathematical setting.

---

---

## Solutions

??? success "Solution to Exercise 1"

    **Why the classical solution fails**: A classical ($C^{2,1}$) solution requires that $V(S,t)$ be twice continuously differentiable in $S$ and once in $t$ on the entire domain, including at the terminal time $T$. However, the terminal condition $V(S,T) = \mathbf{1}_{\{S > K\}}$ is discontinuous at $S = K$.

    For $V$ to be $C^{2,1}$ up to $t = T$, the terminal data must be sufficiently smooth. The discontinuity at $S = K$ means that no $C^{2,1}$ function can satisfy $V(S,T) = \mathbf{1}_{\{S > K\}}$ pointwise while also solving the PDE in the classical sense. Near $S = K$ as $t \to T^-$, the solution develops increasingly steep gradients: $\frac{\partial V}{\partial S}$ behaves like a delta function and $\frac{\partial^2 V}{\partial S^2}$ diverges.

    **Viscosity solution framework**: The viscosity approach replaces pointwise derivatives with test function comparisons. A function $V$ is a viscosity solution if for every smooth test function $\phi$ that touches $V$ from above (or below) at a point $(S_0, t_0)$, the PDE inequality holds for $\phi$ at that point. This requires only continuity of $V$, not differentiability.

    **Verification**: The candidate solution is $V(S,t) = e^{-r(T-t)}\mathcal{N}(d_2)$ where

    $$
    d_2 = \frac{\ln(S/K) + (r - \sigma^2/2)(T-t)}{\sigma\sqrt{T-t}}
    $$

    For $t < T$, this function is $C^\infty$ in both $S$ and $t$ (as a composition of smooth functions with $S > 0$ and $T - t > 0$), so it is a classical solution on $(0,\infty) \times [0,T)$. Being a classical solution on the interior automatically makes it a viscosity solution there.

    At $t = T$, we verify: as $t \to T^-$, $\sigma\sqrt{T-t} \to 0$, so $d_2 \to +\infty$ if $S > K$ (giving $\mathcal{N}(d_2) \to 1$) and $d_2 \to -\infty$ if $S < K$ (giving $\mathcal{N}(d_2) \to 0$). Thus $V(S,T^-) = \mathbf{1}_{\{S > K\}}$ for $S \neq K$, and the terminal condition is met in the viscosity sense. The viscosity framework extends the notion of solution to accommodate this boundary discontinuity through semicontinuous envelopes.

??? success "Solution to Exercise 2"

    **Definition of viscosity subsolution**: A function $u$ that is upper semicontinuous (USC) is a viscosity subsolution of the Black-Scholes PDE

    $$
    -\frac{\partial V}{\partial t} - rS\frac{\partial V}{\partial S} - \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} + rV = 0
    $$

    if for every smooth test function $\phi \in C^{2,1}$ such that $u - \phi$ has a local maximum at $(S_0, t_0)$, we have

    $$
    -\frac{\partial \phi}{\partial t}(S_0,t_0) - rS_0\frac{\partial \phi}{\partial S}(S_0,t_0) - \frac{\sigma^2 S_0^2}{2}\frac{\partial^2 \phi}{\partial S^2}(S_0,t_0) + r\,u(S_0,t_0) \leq 0
    $$

    **Definition of viscosity supersolution**: A function $v$ that is lower semicontinuous (LSC) is a viscosity supersolution if for every smooth $\phi$ such that $v - \phi$ has a local minimum at $(S_0, t_0)$:

    $$
    -\frac{\partial \phi}{\partial t}(S_0,t_0) - rS_0\frac{\partial \phi}{\partial S}(S_0,t_0) - \frac{\sigma^2 S_0^2}{2}\frac{\partial^2 \phi}{\partial S^2}(S_0,t_0) + r\,v(S_0,t_0) \geq 0
    $$

    **Why $\max(u_1, u_2)$ is a subsolution**: Let $u_1, u_2$ be viscosity subsolutions and define $w = \max(u_1, u_2)$. At any point $(S_0, t_0)$, suppose $\phi$ touches $w$ from above, i.e., $w - \phi$ has a local maximum at $(S_0, t_0)$. Without loss of generality, assume $w(S_0, t_0) = u_1(S_0, t_0) \geq u_2(S_0, t_0)$. Then $u_1 \leq w \leq \phi$ locally, and $u_1(S_0, t_0) = \phi(S_0, t_0)$, so $\phi$ also touches $u_1$ from above at $(S_0, t_0)$. Since $u_1$ is a subsolution, the subsolution inequality holds for $\phi$ at that point, making $w$ a subsolution.

    **Why it is not necessarily a viscosity solution**: Being a viscosity solution requires being both a subsolution and a supersolution. The function $w = \max(u_1, u_2)$ is generally not a supersolution because at points where $u_1 = u_2$ and the two functions cross, $w$ may develop a corner (a non-smooth kink). At such a corner, a test function touching $w$ from below must lie below the maximum of the two, but the supersolution inequality need not hold for any such test function. In particular, the second derivative of any test function touching $w$ from below at a kink point is constrained in a way that the supersolution inequality may be violated.

??? success "Solution to Exercise 3"

    The variational inequality is $\min\left(-\mathcal{L}V,\, V - (K-S)^+\right) = 0$ where

    $$
    \mathcal{L}V = \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} - rV
    $$

    **First condition: $V \geq (K - S)^+$**. This is the **obstacle constraint**. It states that the American put value is always at least the immediate exercise payoff. Financially, if $V < (K - S)^+$ at any point, an arbitrage opportunity would exist: buy the put for $V$, exercise immediately, and pocket $(K - S)^+ - V > 0$. The holder has the right (not obligation) to exercise at any time, so the option value must dominate the payoff.

    **Second condition: $-\mathcal{L}V \geq 0$**. This states that the option earns at least the risk-free rate in the continuation region. Equivalently, the discounted option value is a supermartingale under the risk-neutral measure. If $-\mathcal{L}V < 0$ at some point, the holder could do better by holding the option (earning more than $r$), which would contradict optimality of exercise.

    **The minimum condition**: The "min = 0" structure encodes the complementarity: at every $(S, t)$, exactly one of the following holds:

    - **Continuation region** ($V > (K-S)^+$): The option is worth more alive than dead, so $\mathcal{L}V = 0$ (the standard Black-Scholes PDE holds). The holder optimally continues.

    - **Exercise region** ($V = (K-S)^+$): The option is exercised immediately. Here $-\mathcal{L}V \geq 0$, meaning the PDE is not satisfied as an equality; instead, the holder captures the payoff.

    **Why the obstacle formulation is natural**: Early exercise creates a free boundary $S^*(t)$ separating the continuation and exercise regions. The classical free-boundary approach must explicitly track this curve, which is analytically difficult. The obstacle problem encodes both the PDE and the free boundary condition in a single variational inequality, allowing the free boundary to emerge as part of the solution rather than being specified a priori. The viscosity framework handles the non-smooth behavior at the free boundary (where $V$ is $C^1$ but not $C^2$) without requiring classical differentiability.

??? success "Solution to Exercise 4"

    **Why comparison implies uniqueness**: Suppose $u$ and $v$ are both viscosity solutions of the Black-Scholes PDE with the same terminal condition $u(S,T) = v(S,T) = g(S)$. A viscosity solution is both a subsolution and a supersolution. Applying the comparison principle:

    - Since $u$ is a subsolution and $v$ is a supersolution with $u(S,T) = g(S) \leq g(S) = v(S,T)$, we get $u \leq v$ everywhere.
    - Since $v$ is a subsolution and $u$ is a supersolution with $v(S,T) \leq u(S,T)$, we get $v \leq u$ everywhere.

    Therefore $u = v$, establishing uniqueness.

    Without comparison, uniqueness can fail: there could be multiple functions satisfying the PDE in some generalized sense. The comparison principle is the crucial analytical tool that prevents this.

    **Financial example of arbitrage from non-uniqueness**: Suppose the Black-Scholes PDE with European call terminal data $g(S) = (S - K)^+$ had two distinct viscosity solutions $V_1(S,t)$ and $V_2(S,t)$ with $V_1(S_0, 0) < V_2(S_0, 0)$ for some $S_0$. A market maker could:

    - Sell the option for $V_2(S_0, 0)$ (claiming this is the correct price)
    - Hedge using the delta from $V_1$ (the cheaper replication cost)
    - Pocket $V_2(S_0, 0) - V_1(S_0, 0) > 0$ as riskless profit

    Both $V_1$ and $V_2$ would be valid self-financing replicating strategies reaching the same terminal payoff, but at different initial costs, violating the law of one price. The comparison principle (and hence uniqueness) ensures that no-arbitrage pricing yields a single, well-defined price.

??? success "Solution to Exercise 5"

    The explicit finite-difference scheme approximates the Black-Scholes PDE on a grid $(S_i, t^n)$ with spatial step $\Delta S$ and time step $\Delta t$. After transformation to the heat equation (or working directly), the scheme updates values as:

    $$
    V_i^{n} = \alpha_i V_{i-1}^{n+1} + \beta_i V_i^{n+1} + \gamma_i V_{i+1}^{n+1}
    $$

    where the coefficients (for the untransformed BS PDE) are:

    $$
    \alpha_i = \frac{\Delta t}{2}\left(\frac{\sigma^2 i^2}{1} - ri\right)\frac{1}{1+r\Delta t}, \quad \gamma_i = \frac{\Delta t}{2}\left(\sigma^2 i^2 + ri\right)\frac{1}{1+r\Delta t}
    $$

    $$
    \beta_i = 1 - \sigma^2 i^2 \Delta t \cdot \frac{1}{1+r\Delta t}
    $$

    (where $i$ indexes the spatial grid with $S_i = i\Delta S$).

    **Monotonicity condition (CFL)**: The Barles-Souganidis theorem requires the scheme to be **monotone**: the numerical solution at time $t^n$ must be a non-decreasing function of the values at time $t^{n+1}$. This means all coefficients $\alpha_i, \beta_i, \gamma_i$ must be non-negative. The binding constraint is typically $\beta_i \geq 0$, which gives:

    $$
    \sigma^2 i^2 \Delta t \leq 1 \quad \text{for all grid points } i
    $$

    If $i_{\max}$ is the largest grid index, the **CFL condition** is:

    $$
    \Delta t \leq \frac{1}{\sigma^2 i_{\max}^2}
    $$

    Equivalently, in terms of $S_{\max} = i_{\max}\Delta S$:

    $$
    \Delta t \leq \frac{(\Delta S)^2}{\sigma^2 S_{\max}^2}
    $$

    **When CFL is violated**: If $\Delta t$ is too large, some coefficients become negative. This means the scheme is no longer monotone: increasing the future value at a neighboring node can decrease the current value, which is financially absurd (a higher future payoff should not reduce the current option price). Numerically, the scheme produces **spurious oscillations** that grow exponentially, leading to instability. More fundamentally, without monotonicity, the Barles-Souganidis convergence theorem does not apply, and the finite-difference solution may converge to the wrong function (or not converge at all), rather than to the unique viscosity solution.

??? success "Solution to Exercise 6"

    **Why classical solutions may not exist**: The Leland-type transaction cost model has modified volatility:

    $$
    \tilde{\sigma}^2(\Gamma) = \sigma^2\left(1 + c_0\,\mathrm{sgn}(\Gamma)\sqrt{\frac{2}{\pi\Delta t}}\frac{1}{\sigma}\right)
    $$

    or more generally $\tilde{\sigma}^2 = \sigma^2 + f(\Gamma)$ for some function $f$ that depends on $\Gamma = V_{SS}$. Classical solutions fail for several reasons:

    **1. Nonlinearity and degeneracy**: The equation is **quasilinear** since the coefficient of $V_{SS}$ depends on $V_{SS}$ itself. This creates a circular dependence: the diffusion coefficient depends on the solution's own curvature. Standard linear PDE existence theorems (e.g., Schauder theory) do not directly apply.

    **2. Loss of uniform ellipticity**: If $\tilde{\sigma}^2(\Gamma)$ vanishes or changes sign for certain values of $\Gamma$, the equation degenerates. For example, in some models $\tilde{\sigma}^2(\Gamma) = \sigma^2(1 + \alpha\,\mathrm{sgn}(\Gamma))$, which has a jump discontinuity at $\Gamma = 0$. At points where $\Gamma$ changes sign, the effective volatility is discontinuous, preventing $C^2$ regularity.

    **3. Non-smooth structure**: Near points where $\Gamma = 0$, the dependence $\tilde{\sigma}^2(\Gamma)$ may be non-smooth (involving $|\Gamma|$ or $\mathrm{sgn}(\Gamma)$). Solutions develop regions where $V_{SS}$ is not classically defined, particularly at the boundary between convex and concave regions of the option price surface.

    **Why viscosity solutions are appropriate**:

    - **Existence**: The viscosity framework guarantees existence of solutions for fully nonlinear, possibly degenerate elliptic/parabolic equations via Perron's method. One constructs the solution as the supremum of all subsolutions, which is itself a viscosity solution.

    - **Uniqueness**: The comparison principle extends to many nonlinear equations, provided the nonlinearity $F(x, t, u, Du, D^2u)$ is **proper** (non-decreasing in $u$) and **degenerate elliptic** (non-increasing in $D^2u$ in the matrix ordering). The transaction cost PDE satisfies these structural conditions.

    - **Stability**: The viscosity framework is closed under uniform limits: if $V^\epsilon$ are viscosity solutions of approximating equations (e.g., with smoothed transaction cost functions) and $V^\epsilon \to V$ uniformly, then $V$ is a viscosity solution of the limit equation. This is critical for the financial modeling where $\tilde{\sigma}^2$ arises as a limit of discrete rebalancing.

    - **Stochastic control interpretation**: The transaction cost problem can be formulated as a stochastic control problem where the agent chooses rebalancing times. The value function of this control problem is automatically a viscosity solution of the HJB equation, providing both existence and the financial interpretation simultaneously.
