# Viscosity Solutions

This subsubsection does not introduce another solution method. Instead, it provides the **rigorous foundation** under which every representation in this chapter agrees. The heat-kernel, Fourier, Mellin, Laplace, separation-of-variables, and probabilistic ([§ Feynman-Kac](feynman_kac.md)) approaches all give formulas for the pricing operator $\mathcal{P}_\tau$ introduced in [§ Introduction](intro.md). When the payoff is smooth, these formulas coincide because the PDE has a unique classical solution. When the payoff is *not* smooth---digital options, American obstacles, degenerate diffusion at $S=0$---classical $C^{2,1}$ solutions do not exist, and one needs a weaker but still uniquely-defined notion of "solution" to make all the chapter's representations agree on the same object. Viscosity solutions are that notion. They guarantee existence, uniqueness, and stability of $\mathcal{P}_\tau$ on payoffs the classical theory cannot handle.

---

## 1. Motivation: Why Classical Solutions Fail

### 1.1 A toy failure: the absolute-value kink

Before any finance, work the simplest possible example of a function that "almost" solves a PDE. Consider

$$
u(x) = -|x|, \qquad x \in \mathbb{R}
$$

and ask whether it satisfies the trivial PDE $u''(x) = 0$. Classically the answer is partial: the equation holds at every point *except* $x = 0$, where the kink prevents the second derivative from existing.

$$
u''(x) = 0 \quad \text{for } x \neq 0; \qquad u''(0)\ \text{undefined (classically)}
$$

In the language of distributions $u'' = -2\delta_0$ — a Dirac mass concentrated at the kink — but distributional derivatives are unwieldy under the *nonlinear* operators that arise in stochastic control and obstacle problems. What we want is a sharper question whose answer survives the kink.

**The viscosity move.** Instead of asking what $u''(0)$ *is* — undefined — ask what every smooth $\phi \in C^2$ *that touches $u$ from above at $0$* must satisfy there.

A test function $\phi$ touching $u = -|x|$ from above at $x_0 = 0$ obeys $\phi(0) = 0$ and $\phi(x) \geq -|x|$ in a neighborhood. The cusp opens downward, so $\phi$ is forced to be locally concave-at-the-top there: $\phi''(0) \leq 0$. We have **captured a one-sided constraint on the would-be second derivative without needing $u$ to be twice differentiable**. That is the entire mechanism.

!!! tip "The viscosity principle in one sentence"
    Viscosity solutions replace **"having derivatives"** with **"being locally trapped by smooth test functions."** Where classical $u''$ would have been a single number, the viscosity definition delivers a one-sided inequality coming from every $\phi \in C^2$ that touches $u$.

Classical derivatives at $0$ do not exist — but *comparison* with smooth tangent functions still makes sense. Section 2 formalizes this for the parabolic Black–Scholes operator.

### 1.2 The same failure in finance: digital and American options

The same gap shows up the moment we leave smooth European calls.

**Digital payoffs.** A digital call has $\Phi(S) = \mathbb{1}_{S > K}$. The Black–Scholes PDE with this terminal data has **no classical solution**: the payoff is discontinuous at $S = K$, and any $C^{2,1}$ candidate up to $t = T$ would have to be continuous there. Yet the Gil–Pelaez / Fourier price $V(S, t) = e^{-r(T - t)}\mathcal{N}(d_2)$ exists, is smooth for $t < T$, and is unambiguously *the* price every practitioner uses. Some weaker solution concept must be making the formula well-defined.

**American options.** For an American option the value satisfies an obstacle problem coupling the Black–Scholes operator $\mathcal{L}$ (recall [§ Introduction](intro.md)) with the payoff constraint $V \geq \Phi(S)$. The value $V$ is typically only $C^1$ — not $C^2$ — across the optimal exercise boundary, so classical second derivatives do not exist there. Trees and finite-difference solvers still converge to a well-defined price; what notion of solution are they converging to? The full variational inequality is written out in §6.

### 1.3 The gap

Classical theory requires $C^2$ solutions; the payoffs that matter in practice routinely violate this. Viscosity theory fills the gap by replacing pointwise derivatives with **test-function comparisons** (the §1.1 mechanism), while preserving uniqueness via a comparison principle. Every other representation in this chapter — heat kernel, Fourier, Feynman–Kac, separation, Mellin, Laplace — produces *some* candidate function for the pricing operator $\mathcal{P}_\tau\Phi$ even when $\Phi$ is non-smooth; viscosity theory is the structure that says all of those candidates are the same function.

---

## 2. Definitions via Test Functions

Consider a general parabolic PDE $F(x,t,u,Du,D^2u) = 0$ with terminal data $u(x,T) = g(x)$. A **test function** is any $\phi \in C^2$, and one studies points where $u - \phi$ has a local maximum (touch from above) or local minimum (touch from below).

A USC function $u$ is a **viscosity subsolution** if at every local maximum of $u - \phi$,

$$
F(x_0,t_0,u(x_0,t_0),D\phi(x_0,t_0),D^2\phi(x_0,t_0)) \leq 0.
$$

An LSC function $u$ is a **viscosity supersolution** if at every local minimum of $u - \phi$, the same inequality reverses to $\geq 0$. A continuous $u$ that is both a subsolution and a supersolution is a **viscosity solution**.

**Why "viscosity"?** Historically the concept arises by adding artificial viscosity $-\epsilon\Delta u$ to $F$ (which makes solutions smooth) and sending $\epsilon \to 0$.

**Classical $\Rightarrow$ viscosity.** If $u \in C^2$ solves $F = 0$ pointwise, taking $\phi = u$ shows $F \leq 0$ and $F \geq 0$ at every point, so $u$ is automatically a viscosity solution. $\square$

For the Black-Scholes operator $\mathcal{L}$ from [§ Introduction](intro.md), $u$ is a viscosity subsolution iff $\phi_t + \mathcal{L}\phi \leq 0$ at every point where a test function $\phi$ touches $u$ from above; the supersolution condition reverses the inequality for touches from below.

??? note "Advanced Remark: Semijets"

    The test-function formulation has an equivalent pointwise reformulation via **semijets**, the technical device used in the modern theory (Crandall--Ishii--Lions). The second-order superjet of $u$ at $(x_0,t_0)$ is

    $$
    \overline{D^2}u(x_0,t_0) = \big\{(p,A) : u(x,t) \leq u(x_0,t_0) + \langle p, (x-x_0,t-t_0)\rangle + \tfrac{1}{2}\langle A(x-x_0,t-t_0),(x-x_0,t-t_0)\rangle + o(|(x,t)-(x_0,t_0)|^2)\big\},
    $$

    and the subjet $\underline{D^2}u$ is defined with the reversed inequality. $u$ is a viscosity subsolution iff $F(x_0,t_0,u,p,A) \leq 0$ for every $(p,A) \in \overline{D^2}u$, and similarly a supersolution iff $F \geq 0$ on $\underline{D^2}u$. Semijets are essential for the *Crandall--Ishii lemma*, which underlies modern proofs of the comparison principle, but the test-function definition above is sufficient for everything we use in finance.

---

## 3. Comparison Principle and Uniqueness

The **comparison principle** is the analytic cornerstone of the theory: it gives uniqueness essentially for free.

**Theorem (comparison).** Suppose $F$ is *degenerate elliptic*, meaning $F(x,t,r,p,A) \geq F(x,t,r,p,B)$ whenever $A \geq B$, and continuous with suitable growth. If $u$ is a viscosity subsolution and $v$ a viscosity supersolution with $u(\cdot,T) \leq v(\cdot,T)$ and $u \leq v$ on the parabolic boundary, then $u \leq v$ in $\Omega \times [0,T]$.

For the Black-Scholes operator (see [§ Introduction](intro.md)), $\partial F / \partial u_{SS} = \sigma^2 S^2 / 2 \geq 0$, so degenerate ellipticity holds. (It is *degenerate* rather than uniformly elliptic precisely because the coefficient vanishes at $S = 0$.)

**Uniqueness.** If $u_1, u_2$ are both viscosity solutions with the same data, applying comparison both ways gives $u_1 \leq u_2$ and $u_2 \leq u_1$, hence $u_1 = u_2$.

---

## 4. Existence: Perron and Vanishing Viscosity

Two constructions give existence.

**Perron's method.** Define

$$
\underline{u}(x,t) = \sup\{v : v \text{ subsolution with } v(\cdot,T) \leq g\}, \qquad \overline{u}(x,t) = \inf\{w : w \text{ supersolution with } w(\cdot,T) \geq g\}.
$$

Under standard hypotheses $\underline u$ is a subsolution and $\overline u$ a supersolution; when comparison forces $\underline u = \overline u$, the common function is the unique viscosity solution.

**Vanishing viscosity.** Solve the regularized equation $F(\cdot,u^\epsilon, Du^\epsilon, D^2u^\epsilon) - \epsilon \Delta u^\epsilon = 0$, which has smooth solutions, and pass $\epsilon \to 0$. The limit (under mild conditions) is the viscosity solution. This is also the origin of the name.

---

## 5. Connection to Stochastic Control (and a Word on HJB)

The key bridge to probability: the discounted risk-neutral expectation of [§ Feynman-Kac](feynman_kac.md) is automatically a viscosity solution of the Black-Scholes PDE---no smoothness of the payoff required. This is why the probabilistic and PDE representations agree even for discontinuous data.

The same machinery extends well beyond Black-Scholes to stochastic control, optimal stopping, and the nonlinear Hamilton--Jacobi--Bellman (HJB) equation. We do not pursue stochastic control here, but we record the result that motivates the entire modern theory.

??? note "Advanced Remark: HJB equations and stochastic control"

    For the controlled diffusion $dX_s = b(X_s,\alpha_s)\,ds + \sigma(X_s,\alpha_s)\,dW_s$ and the value function

    $$
    V(x,t) = \sup_{\alpha}\mathbb{E}\left[\int_t^T f(X_s^\alpha,\alpha_s)e^{-\int_t^s r\,d\tau}\,ds + g(X_T^\alpha)e^{-\int_t^T r\,d\tau}\,\Big|\,X_t = x\right],
    $$

    the dynamic programming principle, combined with Ito's formula on a smooth test function, yields the HJB equation

    $$
    V_t + \sup_{\alpha \in A}\left[b(x,\alpha)\cdot DV + \tfrac{1}{2}\mathrm{tr}(\sigma\sigma^T(x,\alpha)D^2V) + f(x,\alpha)\right] - rV = 0.
    $$

    **Theorem.** $V$ is a viscosity solution of this HJB equation, and---when the comparison principle applies---the unique one.

    This is the historical reason viscosity solutions were developed: classical $C^2$ solutions of HJB equations rarely exist, but value functions of stochastic control problems are continuous and well-behaved. The Black-Scholes obstacle problem (American options, Section 6 below) is a special case in which the "control" is the binary decision to exercise or continue.

---

## 6. American Options as an Obstacle Problem

The American option is the canonical finance example in which viscosity solutions are unavoidable. With payoff $\Phi(S)$, the value admits an optimal-stopping representation (the Feynman--Kac formula generalized to a sup over stopping times $\tau$; see [§ Feynman-Kac](feynman_kac.md))

$$
V(S,t) = \sup_{\tau \in [t,T]}\mathbb{E}^{\mathbb{Q}}\!\left[e^{-r(\tau-t)}\Phi(S_\tau) \,\big|\, S_t = S\right]
$$

and equivalently solves the variational inequality

$$
\min\!\left\{-V_t - \mathcal{L}V,\; V - \Phi\right\} = 0
$$

with $V(S,T) = \Phi(S)$, where $\mathcal{L}$ is the Black-Scholes operator of [§ Introduction](intro.md). The state space splits into

- **Continuation region** $\mathcal{C} = \{V > \Phi\}$, where $-V_t - \mathcal{L}V = 0$;
- **Stopping region** $\mathcal{S} = \{V = \Phi\}$, where $-V_t - \mathcal{L}V \leq 0$.

The boundary $\partial \mathcal{C} = S^*(t)$ is the optimal exercise boundary. Across it the *smooth fit* condition gives $V \in C^1$ but $V_{SS}$ jumps, so $V$ is not $C^2$ and the classical PDE formulation fails on the boundary itself. $V$ is, however, the *unique* viscosity solution of the variational inequality, and by comparison

$$
V_{\text{viscosity}} = V_{\text{probabilistic}} = \sup_{\tau} \mathbb{E}\!\left[e^{-r(\tau-t)}\Phi(S_\tau)\right].
$$

This identification---two completely different definitions of the same object, agreeing by uniqueness---is the chapter's central theme in its sharpest form.

---

## 7. Regularity

Under uniform ellipticity and smooth data, viscosity solutions coincide with classical $C^{2,1}$ solutions. For Black-Scholes the diffusion coefficient $\sigma^2 S^2$ vanishes at $S = 0$, so the equation is *degenerate*: even smooth payoffs can produce solutions that fail to be $C^2$ at $S = 0$.

In the interior, away from boundaries and degeneracies, viscosity solutions are at least locally Holder continuous,

$$
|u(x,t) - u(y,s)| \leq C\!\left(|x-y|^\alpha + |t-s|^{\alpha/2}\right),
$$

and typically $C^{2,\alpha}$. Singularities are confined to (i) boundaries, (ii) degeneracy points such as $S = 0$, (iii) free boundaries, and (iv) points where the terminal data is non-smooth.

---

## 8. Numerical Schemes: Barles-Souganidis

Viscosity theory delivers what is, for practitioners, its most concrete payoff: a clean convergence criterion for finite-difference and tree-based pricers.

**Theorem (Barles-Souganidis).** A discretization that is *consistent* (locally approximates the PDE), *monotone* (the update is non-decreasing in each neighboring value), and *stable* (bounded under refinement) converges to the unique viscosity solution.

For Black-Scholes the standard explicit finite-difference discretization of $\mathcal{L}$ is monotone under a CFL condition on $\Delta t / (\Delta S)^2$ (see Exercise 5). For American options one imposes $V_j^{n+1} = \max\{\Phi(S_j),\text{continuation value}\}$ at each step, which enforces the obstacle. This is exactly the recipe behind binomial and trinomial trees, and Barles-Souganidis is what guarantees they converge to the right price.

An equivalent regularization route is **penalization**: replace the obstacle problem with

$$
-u^\epsilon_t - \mathcal{L}u^\epsilon - \tfrac{1}{\epsilon}(u^\epsilon - \Phi)^- = 0,
$$

which has smooth solutions for $\epsilon > 0$ and converges to the viscosity solution as $\epsilon \to 0$. The penalty $-\tfrac{1}{\epsilon}(u^\epsilon - \Phi)^-$ acts as a strong restoring force whenever $u^\epsilon$ tries to fall below the payoff.

---

## 9. Summary

Three solution concepts coexist: classical (requires $C^2$), weak/Sobolev (uses integration against test functions, less convenient under nonlinearity), and viscosity (requires only continuity, handles degeneracy and free boundaries, comes with a comparison principle). For the smooth European payoffs of this chapter all three coincide; for digital and American payoffs only the viscosity notion applies.

| **Problem** | **Classical** | **Viscosity** |
|---|---|---|
| European call (smooth payoff) | works | identical |
| Digital option | fails (discontinuous payoff) | unique solution |
| American put | free boundary, needs ad-hoc fit | obstacle problem, unique solution |
| Stochastic control / HJB | typically no $C^2$ solution | value function is the unique solution |
| Numerical convergence | case-by-case | Barles-Souganidis |

This closes the chapter's central thread. Every preceding subsubsection produced a different representation of the same pricing operator $\mathcal{P}_\tau = e^{\tau \mathcal{L}}$ (see [§ Introduction](intro.md) for the operator framing, [§ Heat Equation](heat_equation.md) for the kernel form, and [§ Feynman-Kac](feynman_kac.md) for the probabilistic form). Viscosity theory is the rigorous foundation under which all of these representations are guaranteed to define the *same* function---even when the payoff is discontinuous or the diffusion degenerates. The diversity of techniques is not redundancy; it is the reflection of a single, well-posed operator viewed in different coordinates.

---

## Exercises

**Exercise 1.** A digital call option has payoff $\Phi(S) = \mathbf{1}_{\{S > K\}}$, which is discontinuous at $S = K$. Explain why the Black-Scholes PDE with this terminal condition has no classical ($C^{2,1}$) solution. Then describe how the viscosity solution framework resolves this issue, and verify that $V(S,t) = e^{-r(T-t)}\mathcal{N}(d_2)$ is the viscosity solution.

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

---

**Exercise 2.** State the definition of a viscosity subsolution and supersolution for the Black-Scholes PDE. Using these definitions, explain why the maximum of two viscosity solutions is a viscosity subsolution but not necessarily a viscosity solution.

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

---

**Exercise 3.** For an American put option, the value function satisfies the variational inequality $\min\left(-\mathcal{L}V, \, V - (K - S)^+\right) = 0$, where $\mathcal{L}$ is the Black-Scholes differential operator. Interpret each of the two conditions in this inequality financially, and explain why the obstacle problem formulation is natural for early exercise.

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

---

**Exercise 4.** The comparison principle for viscosity solutions states that if $u$ is a subsolution and $v$ is a supersolution with $u(S,T) \leq v(S,T)$, then $u \leq v$ everywhere. Explain why this principle is essential for proving uniqueness of viscosity solutions. Give a financial example where non-uniqueness of PDE solutions would lead to arbitrage.

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

---

**Exercise 5.** The Barles-Souganidis theorem guarantees convergence of numerical schemes to the viscosity solution if the scheme is monotone, consistent, and stable. For the explicit finite-difference scheme applied to the Black-Scholes PDE, state the CFL condition that ensures monotonicity and explain what happens when it is violated.

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
