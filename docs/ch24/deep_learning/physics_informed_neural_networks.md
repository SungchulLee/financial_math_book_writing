# Physics-Informed Neural Networks

**Physics-informed neural networks (PINNs)** embed known differential equations directly into the training loss, ensuring that the learned solution respects the underlying physics or financial law. Rather than relying solely on data, PINNs penalize violations of the PDE, boundary conditions, and terminal conditions, producing solutions that are consistent with first principles even in data-sparse regions. In finance, PINNs enforce pricing PDEs (Black-Scholes, Heston, HJB) without mesh generation, handling free boundaries, multi-dimensional domains, and exotic payoff structures.

---

## Motivation: PDE Constraints as Regularization

A standard neural network trained on data alone faces two challenges in financial PDE problems:

1. **Data scarcity:** Derivative prices are observed at sparse $(K, T)$ grid points, leaving large regions of the domain unconstrained.
2. **Arbitrage violations:** Without structural constraints, the network may produce prices that violate no-arbitrage conditions (negative butterfly spreads, calendar spread violations).

PINNs address both problems by requiring the network output to satisfy the governing PDE everywhere in the domain, not just at observed data points.

---

## General PINN Framework

### Problem Formulation

Consider a PDE on domain $\Omega \subset \mathbb{R}^d$ with boundary $\partial\Omega$:

$$
\mathcal{L}[u](x) = 0, \quad x \in \Omega
$$

$$
\mathcal{B}[u](x) = g(x), \quad x \in \partial\Omega
$$

where $\mathcal{L}$ is a differential operator and $\mathcal{B}$ specifies boundary/terminal conditions.

### Neural Network Ansatz

Approximate the solution by a neural network:

$$
u(x) \approx u_\theta(x)
$$

where $u_\theta : \mathbb{R}^d \to \mathbb{R}$ is a feedforward network with parameters $\theta$.

The key insight is that all partial derivatives of $u_\theta$ are computable via **automatic differentiation** (backpropagation through the network). For instance, if $u_\theta(t, S)$ approximates an option price:

$$
\frac{\partial u_\theta}{\partial t}, \quad \frac{\partial u_\theta}{\partial S}, \quad \frac{\partial^2 u_\theta}{\partial S^2}
$$

are all obtained exactly (up to floating-point precision) by differentiating the computational graph.

### The PINN Loss Function

**Definition (PINN Loss).** The total loss is a weighted sum of PDE residual, boundary condition, and data-fitting terms:

$$
\mathcal{L}_{\text{total}}(\theta) = \lambda_{\text{PDE}} \, \mathcal{L}_{\text{PDE}}(\theta) + \lambda_{\text{BC}} \, \mathcal{L}_{\text{BC}}(\theta) + \lambda_{\text{data}} \, \mathcal{L}_{\text{data}}(\theta)
$$

where:

**PDE residual loss** (evaluated at collocation points $\{x_j^r\}_{j=1}^{N_r} \subset \Omega$):

$$
\mathcal{L}_{\text{PDE}}(\theta) = \frac{1}{N_r} \sum_{j=1}^{N_r} \left|\mathcal{L}[u_\theta](x_j^r)\right|^2
$$

**Boundary/terminal condition loss** (evaluated at boundary points $\{x_j^b\}_{j=1}^{N_b} \subset \partial\Omega$):

$$
\mathcal{L}_{\text{BC}}(\theta) = \frac{1}{N_b} \sum_{j=1}^{N_b} \left|u_\theta(x_j^b) - g(x_j^b)\right|^2
$$

**Data loss** (evaluated at observed data points $\{(x_j^d, u_j^d)\}_{j=1}^{N_d}$):

$$
\mathcal{L}_{\text{data}}(\theta) = \frac{1}{N_d} \sum_{j=1}^{N_d} \left|u_\theta(x_j^d) - u_j^d\right|^2
$$

The collocation points $\{x_j^r\}$ are sampled (uniformly or adaptively) from the interior of the domain. No mesh is required.

---

## Black-Scholes PINN

### The PDE

Recall (see [§ BS PDE via Replication](../../ch06/bs_pde_derivation/replication.md)) the Black-Scholes PDE for a European option price $V(t, S)$:

$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
$$

on $(t, S) \in [0, T) \times (0, \infty)$ with terminal condition $V(T, S) = h(S)$.

### PINN Formulation

Define the PDE residual operator:

$$
\mathcal{R}_\theta(t, S) = \frac{\partial u_\theta}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 u_\theta}{\partial S^2} + rS\frac{\partial u_\theta}{\partial S} - r\,u_\theta
$$

The PINN loss becomes:

$$
\mathcal{L}(\theta) = \frac{\lambda_r}{N_r}\sum_{j=1}^{N_r} \left|\mathcal{R}_\theta(t_j, S_j)\right|^2 + \frac{\lambda_T}{N_T}\sum_{j=1}^{N_T} \left|u_\theta(T, S_j) - h(S_j)\right|^2 + \frac{\lambda_0}{N_0}\sum_{j=1}^{N_0} \left|u_\theta(t_j, 0) - 0\right|^2
$$

where the last term enforces the boundary condition at $S = 0$ (for a call option).

### Collocation Point Sampling

For financial PDEs, adaptive sampling is important:

- **Near the strike:** The solution has high curvature (the "kink" at $S = K$), requiring denser collocation
- **Near maturity:** Rapid time variation as $t \to T$
- **Log-price coordinates:** Using $x = \log(S/K)$ improves conditioning and sampling efficiency

**Proposition.** Working in log-price coordinates $x = \log S$, the Black-Scholes PDE becomes:

$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 \frac{\partial^2 V}{\partial x^2} + \left(r - \frac{\sigma^2}{2}\right)\frac{\partial V}{\partial x} - rV = 0
$$

which has constant coefficients, improving both the conditioning of the PINN and the uniformity of the PDE residual magnitude across the domain.

---

## Boundary Condition Enforcement

### Soft Enforcement

The standard approach penalizes boundary violations in the loss (as above). This is simple but the boundary conditions are satisfied only approximately.

### Hard Enforcement

An alternative is to build the boundary conditions into the network architecture:

**Definition (Hard-Constrained PINN).** Construct the ansatz:

$$
u_\theta(t, S) = A(t, S) + B(t, S) \cdot \mathcal{N}_\theta(t, S)
$$

where $A(t, S)$ satisfies the boundary conditions exactly, and $B(t, S)$ vanishes on the boundary so that $\mathcal{N}_\theta$ (the unconstrained network) does not affect boundary values.

**Example:** For a European call with $V(T, S) = (S - K)^+$ and $V(t, 0) = 0$:

$$
u_\theta(t, S) = (T - t) \cdot S \cdot \mathcal{N}_\theta(t, S) + e^{-r(T-t)}(S - K)^+
$$

The factor $(T-t)$ vanishes at $t = T$, so $u_\theta(T, S) = (S - K)^+$ exactly. The factor $S$ vanishes at $S = 0$, so $u_\theta(t, 0) = 0$ exactly.

!!! tip "Advantages of Hard Enforcement"
    Hard enforcement eliminates the need to tune boundary loss weights $\lambda_{\text{BC}}$, guarantees exact satisfaction of no-arbitrage boundary conditions, and focuses the network capacity entirely on learning the interior solution.

---

## Multi-Dimensional and Stochastic Volatility PINNs

### Heston Model PINN

The Heston stochastic volatility model gives a two-dimensional PDE for the option price $V(t, S, v)$:

$$
\frac{\partial V}{\partial t} + \frac{1}{2}vS^2\frac{\partial^2 V}{\partial S^2} + \rho\xi v S\frac{\partial^2 V}{\partial S \partial v} + \frac{1}{2}\xi^2 v\frac{\partial^2 V}{\partial v^2} + rS\frac{\partial V}{\partial S} + \kappa(\bar{v} - v)\frac{\partial V}{\partial v} - rV = 0
$$

The PINN approach handles this naturally: the network $u_\theta(t, S, v)$ has three inputs, and all mixed partial derivatives are computed via automatic differentiation. No grid is needed in the $(S, v)$ domain.

### Advantages Over Finite Differences

| Feature | Finite Differences | PINN |
|---|---|---|
| Mesh generation | Required, complex for irregular domains | Not needed |
| Curse of dimensionality | Exponential in $d$ | Polynomial in $d$ |
| Free boundaries | Special treatment (penalty methods) | Naturally handled via loss |
| Parameter sensitivity | Separate computation | Free via autodiff |
| Exotic boundary conditions | Case-by-case implementation | Generic loss terms |

---

## Training Strategies and Challenges

### Weight Balancing

The loss weights $\lambda_{\text{PDE}}, \lambda_{\text{BC}}, \lambda_{\text{data}}$ critically affect convergence. If $\lambda_{\text{PDE}}$ is too large relative to $\lambda_{\text{BC}}$, the network may satisfy the PDE but violate terminal conditions.

**Adaptive weighting** (Wang, Teng & Perdikaris 2021) adjusts weights based on gradient statistics:

$$
\lambda_i^{(k+1)} = \frac{\max_i \|\nabla_\theta \mathcal{L}_i\|_2}{\|\nabla_\theta \mathcal{L}_i\|_2} \cdot \lambda_i^{(k)}
$$

balancing the gradient magnitudes across loss components.

### Residual-Based Adaptive Refinement

Place more collocation points where the PDE residual is large:

1. Train for $K$ iterations with uniform collocation points
2. Evaluate $|\mathcal{R}_\theta(t, S)|$ on a fine grid
3. Sample new collocation points with probability proportional to $|\mathcal{R}_\theta|$
4. Repeat

This concentrates computational effort near regions of high error (e.g., near the strike, near maturity).

### Network Architecture Choices

- **Activation functions:** $\tanh$ or Swish ($x \cdot \sigma(x)$) are preferred over ReLU for PINNs because smooth activations produce smooth derivatives, matching the regularity of PDE solutions
- **Depth and width:** Typically 4--8 layers with 20--50 neurons per layer for 2D financial PDEs
- **Fourier features:** Prepending a Fourier feature layer $[\sin(2\pi B x), \cos(2\pi B x)]$ helps capture high-frequency components

---

## Error Analysis

### Approximation and Generalization

**Theorem (PINN Error Bound -- Shin, Darbon & Karniadakis 2020).** Let $u^*$ be the true PDE solution and $u_\theta$ the PINN approximation. Under sufficient regularity of the PDE operator, if $\mathcal{L}_{\text{total}}(\theta) \leq \varepsilon^2$, then:

$$
\|u_\theta - u^*\|_{L^2(\Omega)}^2 \leq C(\mathcal{L}) \cdot \varepsilon^2
$$

where $C(\mathcal{L})$ depends on the stability constant of the PDE operator (the inverse of the coercivity constant).

For well-posed parabolic PDEs such as Black-Scholes, $C(\mathcal{L})$ is bounded, so small training loss implies small approximation error.

### Spectral Bias

Neural networks tend to learn low-frequency components first (**spectral bias** or **frequency principle**). For financial PDEs, this means:

- Smooth regions of the solution converge quickly
- Sharp features (the payoff kink at $S = K$, barriers) converge slowly
- Fourier features and adaptive refinement mitigate this issue

---

## Example: American Option via PINN

American option pricing involves a free boundary problem. The PINN formulation uses a penalty method:

$$
\mathcal{R}_\theta(t, S) = \max\!\left(\frac{\partial u_\theta}{\partial t} + \mathcal{L}_{\text{BS}}[u_\theta], \; h(S) - u_\theta(t, S)\right)
$$

where $h(S)$ is the intrinsic value and $\mathcal{L}_{\text{BS}}$ is the Black-Scholes operator. The residual is zero when:

- The PDE holds and $u_\theta \geq h$ (continuation region), or
- $u_\theta = h$ and the PDE inequality holds (exercise region)

The PINN loss $\sum |\mathcal{R}_\theta|^2$ simultaneously learns the option price and the exercise boundary without explicit tracking of the free boundary.

---

## Key Takeaways

1. **PINNs embed PDE constraints** in the training loss, producing solutions consistent with financial laws (Black-Scholes, HJB) even with sparse data.

2. **No mesh generation** is required: collocation points are sampled freely, enabling multi-dimensional problems (stochastic volatility, multi-asset).

3. **Automatic differentiation** computes all partial derivatives exactly, eliminating finite-difference approximation errors in the PDE residual.

4. **Hard enforcement** of boundary conditions through architectural design guarantees no-arbitrage constraints and improves training stability.

5. **Challenges** include loss weight balancing, spectral bias for non-smooth payoffs, and computational cost of higher-order derivatives.

---

## Further Reading

- Raissi, Perdikaris & Karniadakis (2019), "Physics-Informed Neural Networks"
- Sirignano & Spiliopoulos (2018), "DGM: A Deep Learning Algorithm for Solving PDEs"
- Salvador, Pinto & Teixeira (2021), "Financial Option Valuation by Unsupervised Learning with PINNs"
- Shin, Darbon & Karniadakis (2020), "On the Convergence of PINNs"
- Wang, Teng & Perdikaris (2021), "Understanding and Mitigating Gradient Pathologies in PINNs"

---

## Exercises

**Exercise 1.** Write the PINN residual for the Black-Scholes PDE in log-price coordinates $x = \log S$:

$$
\mathcal{R}_\theta(t, x) = \frac{\partial u_\theta}{\partial t} + \frac{1}{2}\sigma^2 \frac{\partial^2 u_\theta}{\partial x^2} + \left(r - \frac{\sigma^2}{2}\right)\frac{\partial u_\theta}{\partial x} - ru_\theta
$$

Explain why constant coefficients (as opposed to the $S^2$ factor in the original coordinates) improve the conditioning of the PINN. If $\sigma = 0.2$, $r = 0.03$, and the network outputs $u_\theta = 10.0$ with derivatives $\partial u_\theta/\partial t = -0.5$, $\partial u_\theta/\partial x = 8.0$, $\partial^2 u_\theta/\partial x^2 = -3.0$ at a point, compute the residual $\mathcal{R}_\theta$.

??? success "Solution to Exercise 1"
    **PINN residual in log-price coordinates.**

    In log-price coordinates $x = \log S$, the Black-Scholes PDE becomes:

    $$
    \mathcal{R}_\theta(t, x) = \frac{\partial u_\theta}{\partial t} + \frac{1}{2}\sigma^2 \frac{\partial^2 u_\theta}{\partial x^2} + \left(r - \frac{\sigma^2}{2}\right)\frac{\partial u_\theta}{\partial x} - ru_\theta
    $$

    **Why constant coefficients improve conditioning.**

    In the original $(t, S)$ coordinates, the PDE is:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS \frac{\partial V}{\partial S} - rV = 0
    $$

    The coefficient $\frac{1}{2}\sigma^2 S^2$ varies by many orders of magnitude across the domain (e.g., from $0.02 \times 1^2 = 0.02$ at $S = 1$ to $0.02 \times 10{,}000^2 = 2 \times 10^6$ at $S = 10{,}000$). This means the PDE residual magnitude depends strongly on where it is evaluated, making the PINN loss highly non-uniform: collocation points at large $S$ dominate the loss while points at small $S$ contribute almost nothing.

    In log-price coordinates, all coefficients are constants ($\sigma^2/2$, $r - \sigma^2/2$, and $r$). The PDE residual has comparable magnitude everywhere in the domain, so all collocation points contribute roughly equally to the loss. This improves:

    - Gradient balancing (no single region dominates optimization)
    - Numerical stability (no large/small coefficient ratios)
    - Sampling efficiency (uniform collocation is effective)

    **Computing the residual at the given point.**

    With $\sigma = 0.2$, $r = 0.03$, and the network outputs $u_\theta = 10.0$, $\partial u_\theta/\partial t = -0.5$, $\partial u_\theta/\partial x = 8.0$, $\partial^2 u_\theta/\partial x^2 = -3.0$:

    $$
    \mathcal{R}_\theta = (-0.5) + \frac{1}{2}(0.04)(-3.0) + (0.03 - 0.02)(8.0) - (0.03)(10.0)
    $$

    Computing each term:

    - $\partial u_\theta / \partial t = -0.5$
    - $\frac{1}{2}\sigma^2 \cdot \partial^2 u_\theta/\partial x^2 = 0.02 \times (-3.0) = -0.06$
    - $(r - \sigma^2/2) \cdot \partial u_\theta/\partial x = 0.01 \times 8.0 = 0.08$
    - $-r \cdot u_\theta = -0.03 \times 10.0 = -0.30$

    $$
    \mathcal{R}_\theta = -0.5 - 0.06 + 0.08 - 0.30 = -0.78
    $$

    The residual $\mathcal{R}_\theta = -0.78$ is nonzero, indicating that the network does not yet satisfy the PDE at this point. The squared residual contribution to the loss from this point is $(-0.78)^2 = 0.6084$.

---

**Exercise 2.** Design a hard-constrained PINN ansatz for a European put option with terminal condition $V(T, S) = (K - S)^+$ and boundary conditions $V(t, 0) = Ke^{-r(T-t)}$ and $V(t, \infty) = 0$. Your ansatz should have the form $u_\theta(t, S) = A(t, S) + B(t, S) \cdot \mathcal{N}_\theta(t, S)$ where $A$ satisfies the boundary conditions and $B$ vanishes on the boundary. Verify that your ansatz satisfies all three boundary/terminal conditions exactly.

??? success "Solution to Exercise 2"
    **Designing the hard-constrained ansatz for a European put.**

    We need $u_\theta(t, S)$ satisfying:

    1. Terminal condition: $u_\theta(T, S) = (K - S)^+$
    2. Boundary at $S = 0$: $u_\theta(t, 0) = Ke^{-r(T-t)}$
    3. Boundary at $S \to \infty$: $u_\theta(t, \infty) = 0$

    **Construction.** Use the ansatz:

    $$
    u_\theta(t, S) = A(t, S) + B(t, S) \cdot \mathcal{N}_\theta(t, S)
    $$

    Choose $A(t, S)$ to satisfy all boundary/terminal conditions, and $B(t, S)$ to vanish on the boundary so that $\mathcal{N}_\theta$ does not affect boundary values.

    Set:

    $$
    A(t, S) = e^{-r(T-t)}(K - S)^+
    $$

    This satisfies:

    - $A(T, S) = (K - S)^+$ (terminal condition)
    - $A(t, 0) = e^{-r(T-t)} K$ (boundary at $S = 0$)
    - $A(t, S) = 0$ for $S \geq K$ (in particular, $A(t, \infty) = 0$)

    Set:

    $$
    B(t, S) = (T - t) \cdot S \cdot e^{-S/S_{\max}}
    $$

    where $S_{\max}$ is a large constant defining the practical upper boundary. This vanishes on all boundaries:

    - $B(T, S) = 0$ (factor $T - t = 0$)
    - $B(t, 0) = 0$ (factor $S = 0$)
    - $B(t, S) \to 0$ as $S \to \infty$ (exponential decay)

    **Verification:**

    1. *Terminal condition ($t = T$):* $u_\theta(T, S) = A(T, S) + 0 \cdot \mathcal{N}_\theta(T, S) = (K - S)^+$. Satisfied exactly.

    2. *Boundary at $S = 0$:* $u_\theta(t, 0) = A(t, 0) + 0 \cdot \mathcal{N}_\theta(t, 0) = Ke^{-r(T-t)}$. Satisfied exactly.

    3. *Boundary at $S \to \infty$:* $u_\theta(t, \infty) = A(t, \infty) + B(t, \infty) \cdot \mathcal{N}_\theta(t, \infty) = 0 + 0 = 0$, provided $\mathcal{N}_\theta$ is bounded (which neural networks with bounded weights are). Satisfied exactly.

    With this ansatz, the PINN loss only contains the PDE residual term (boundary and terminal losses are zero by construction), and all network capacity is devoted to learning the interior solution.

---

**Exercise 3.** The PINN loss has three components with weights $\lambda_{\text{PDE}}$, $\lambda_{\text{BC}}$, and $\lambda_{\text{data}}$. Explain the effect of setting $\lambda_{\text{PDE}} \gg \lambda_{\text{BC}}$ versus $\lambda_{\text{BC}} \gg \lambda_{\text{PDE}}$. In the extreme case $\lambda_{\text{PDE}} = 0$, what does the PINN reduce to? In the extreme $\lambda_{\text{data}} = 0$, what does it reduce to? Describe the adaptive weighting strategy and why it balances gradient magnitudes.

??? success "Solution to Exercise 3"
    **Effect of extreme weight settings.**

    *Case $\lambda_{\text{PDE}} \gg \lambda_{\text{BC}}$:* The optimization strongly penalizes PDE violations but weakly penalizes boundary/terminal condition errors. The network will learn a function that approximately satisfies the PDE everywhere but may not match the terminal condition (payoff) or boundary values. This is problematic because the PDE alone has infinitely many solutions -- the boundary/terminal conditions select the unique financial solution.

    *Case $\lambda_{\text{BC}} \gg \lambda_{\text{PDE}}$:* The network matches the payoff and boundary conditions accurately but may violate the PDE in the interior. The solution will be correct at the boundaries but may be inaccurate for intermediate times and prices. In the extreme, if the PDE is completely ignored, the network simply interpolates between boundary conditions without any dynamics.

    *Case $\lambda_{\text{PDE}} = 0$:* The PINN reduces to a standard supervised learning problem: the network is trained only on boundary/terminal data and any observed prices. With no PDE constraint, the network is a pure interpolator with no physical law guiding the solution in the interior. This is equivalent to a standard neural network regression.

    *Case $\lambda_{\text{data}} = 0$:* The PINN becomes a pure PDE solver -- no market data is used, and the solution comes entirely from the PDE and boundary conditions. This is the "unsupervised" or "physics-only" mode. The network discovers the PDE solution from the differential equation and boundary conditions alone, similar to how a finite-difference method works but without a mesh.

    **Adaptive weighting strategy.**

    The problem with fixed weights is that different loss components may have vastly different gradient magnitudes. If $\|\nabla_\theta \mathcal{L}_{\text{PDE}}\| \gg \|\nabla_\theta \mathcal{L}_{\text{BC}}\|$, the optimizer primarily reduces the PDE loss while the boundary loss stagnates (or vice versa).

    The adaptive strategy adjusts:

    $$
    \lambda_i^{(k+1)} = \frac{\max_i \|\nabla_\theta \mathcal{L}_i\|_2}{\|\nabla_\theta \mathcal{L}_i\|_2} \cdot \lambda_i^{(k)}
    $$

    This increases the weight of the component with the smallest gradient and decreases the weight of the component with the largest gradient. After the update, all components have comparable gradient magnitudes, ensuring that each gradient step makes progress on all loss terms simultaneously.

    The balancing ensures that no single loss component dominates the optimization, leading to more uniform convergence across the PDE residual, boundary conditions, and data fit.

---

**Exercise 4.** A PINN is used to solve the Heston PDE with 3 inputs $(t, S, v)$. The PDE residual involves second-order derivatives $\partial^2 V/\partial S^2$, $\partial^2 V/\partial v^2$, and the mixed derivative $\partial^2 V/\partial S \partial v$. Explain how automatic differentiation computes these quantities through the neural network. Compare the computational cost to finite differences on a $(t, S, v)$ grid with $M$ points per dimension, noting that the PINN avoids the $O(M^3)$ grid storage.

??? success "Solution to Exercise 4"
    **Automatic differentiation for the Heston PDE.**

    The neural network $u_\theta(t, S, v)$ is a composition of affine transformations and activation functions. Automatic differentiation (autodiff) computes derivatives by applying the chain rule through the computational graph.

    For first derivatives:

    $$
    \frac{\partial u_\theta}{\partial S} = \frac{\partial u_\theta}{\partial h^{(L)}} \cdot \frac{\partial h^{(L)}}{\partial h^{(L-1)}} \cdots \frac{\partial h^{(1)}}{\partial S}
    $$

    This is computed in one backward pass through the network (standard backpropagation). The result is exact up to floating-point precision -- no finite-difference approximation is needed.

    For second derivatives, we differentiate the first derivative:

    $$
    \frac{\partial^2 u_\theta}{\partial S^2} = \frac{\partial}{\partial S}\left(\frac{\partial u_\theta}{\partial S}\right)
    $$

    This requires a second backward pass through the graph that computed $\partial u_\theta / \partial S$. Modern autodiff frameworks (PyTorch, JAX, TensorFlow) support this natively via `torch.autograd.grad` with `create_graph=True`.

    The mixed derivative $\partial^2 u_\theta / \partial S \partial v$ is computed similarly: first compute $\partial u_\theta / \partial S$, then differentiate with respect to $v$.

    **Computational cost.** For a network with $P$ parameters and $L$ layers, each derivative computation costs $O(P)$ (one backward pass). The Heston PDE residual requires:

    - $\partial u/\partial t$: $O(P)$
    - $\partial u/\partial S$: $O(P)$
    - $\partial u/\partial v$: $O(P)$
    - $\partial^2 u/\partial S^2$: $O(P)$ (second backward pass)
    - $\partial^2 u/\partial v^2$: $O(P)$
    - $\partial^2 u/\partial S \partial v$: $O(P)$

    Total per collocation point: $O(6P)$. For $N_r$ collocation points: $O(6P \cdot N_r)$.

    **Comparison to finite differences on a $(t, S, v)$ grid.**

    With $M$ points per dimension, the grid has $M^3$ points. Storing the solution requires $O(M^3)$ memory. At each time step, solving the implicit system requires $O(M^3)$ operations (with sparse solvers).

    For $M = 100$: $M^3 = 10^6$ grid points. For $M = 1{,}000$: $M^3 = 10^9$ points. This is feasible for 3D but becomes prohibitive for higher dimensions.

    The PINN avoids grid storage entirely: memory is $O(P + N_r)$ where $P$ is the network parameter count and $N_r$ is the number of collocation points. Both are independent of the dimensionality scaling $M^d$. For the Heston model ($d = 3$ including time), the advantage is modest, but for higher-dimensional problems (multi-factor stochastic volatility, multi-asset PDEs), the PINN's polynomial scaling is decisive.

---

**Exercise 5.** The spectral bias of neural networks means that low-frequency components of the PDE solution are learned first, while high-frequency components (e.g., the payoff kink at $S = K$) converge slowly. For a call option with $K = 100$, the payoff $(S - K)^+$ has a discontinuity in the first derivative at $S = 100$. Discuss: (a) why smooth activations ($\tanh$) are preferred over ReLU for PINNs, (b) how Fourier feature layers can accelerate learning of sharp features, and (c) how residual-based adaptive refinement concentrates collocation points near $S = K$.

??? success "Solution to Exercise 5"
    **(a) Why smooth activations are preferred over ReLU for PINNs.**

    PINNs require computing second (and sometimes higher) derivatives of the network output. The PDE residual involves $\partial^2 u_\theta / \partial x^2$, which requires the activation function to be twice differentiable.

    - **ReLU:** $\sigma(z) = \max(0, z)$ has $\sigma'(z) = \mathbf{1}_{z > 0}$ (a step function) and $\sigma''(z) = 0$ everywhere except at $z = 0$ where it is undefined. A ReLU network is piecewise linear, so its second derivative is zero almost everywhere. This means the PDE residual $\mathcal{R}_\theta$ cannot capture the diffusion term $\frac{1}{2}\sigma^2 \partial^2 u/\partial x^2$, which is identically zero for a piecewise linear function. The PINN would fail to enforce the PDE.

    - **$\tanh$:** Infinitely differentiable with $\tanh''(z) = -2\tanh(z)(1 - \tanh^2(z))$, which is smooth and nonzero. All derivatives are well-defined and informative.

    - **Swish:** $\sigma(z) = z/(1 + e^{-z})$ is also smooth with nonzero second derivative.

    Smooth activations produce smooth network outputs, whose second derivatives provide meaningful PDE residuals that guide training.

    **(b) How Fourier feature layers accelerate learning of sharp features.**

    The spectral bias means that the network first learns low-frequency modes of the solution and slowly converges to high-frequency features. A Fourier feature layer maps the input $x$ to:

    $$
    \gamma(x) = [\sin(2\pi b_1 x), \cos(2\pi b_1 x), \ldots, \sin(2\pi b_k x), \cos(2\pi b_k x)]
    $$

    where $b_1, \ldots, b_k$ are frequency parameters (often sampled from a Gaussian distribution). This mapping:

    - Projects the input into a higher-dimensional space where high-frequency patterns become linearly separable
    - Allows the first hidden layer to immediately represent oscillatory functions, bypassing the spectral bias
    - The standard deviation of the frequency distribution $b_j \sim \mathcal{N}(0, \sigma_b^2)$ controls the frequency range: larger $\sigma_b$ enables higher frequencies

    For the call option payoff kink at $S = K$ (or $x = \log K$ in log-coordinates), the Fourier features allow the network to represent the sharp transition rapidly, rather than slowly building it through many training epochs.

    **(c) Residual-based adaptive refinement near $S = K$.**

    The payoff kink causes the PDE solution to have high curvature near $S = K$, especially for short maturities. The PDE residual $|\mathcal{R}_\theta(t, S)|$ will be largest in this region because the network struggles to satisfy the PDE where the solution changes rapidly.

    The adaptive refinement algorithm:

    1. Initially, uniform collocation points are used. After some training, the residual is large near $S = K$ and small elsewhere.
    2. Evaluate $|\mathcal{R}_\theta|$ on a fine evaluation grid.
    3. Sample new collocation points with probability proportional to $|\mathcal{R}_\theta|$. This places many more points near $S = K$ where the error is highest.
    4. Retrain with the enriched point set. The increased density near the kink forces the network to reduce the residual there.

    This is analogous to adaptive mesh refinement in finite elements, but without the complexity of mesh management. The result is that computational effort concentrates where it is most needed, dramatically improving convergence for non-smooth features.

---

**Exercise 6.** Explain how the PINN penalty method handles the American option free boundary. The residual

$$
\mathcal{R}_\theta(t, S) = \max\left(\frac{\partial u_\theta}{\partial t} + \mathcal{L}_{\text{BS}}[u_\theta], \; h(S) - u_\theta(t, S)\right)
$$

is zero in both the continuation region (PDE holds, $u \ge h$) and the exercise region ($u = h$). Why does minimizing $\sum |\mathcal{R}_\theta|^2$ simultaneously determine the price and the exercise boundary? Compare this to the finite-difference penalty method.

??? success "Solution to Exercise 6"
    **How the penalty method handles the American option free boundary.**

    The American option value $V(t, S)$ satisfies the linear complementarity problem:

    $$
    \min\!\left(-\frac{\partial V}{\partial t} - \mathcal{L}_{\text{BS}}V, \; V - h(S)\right) = 0
    $$

    This means at every $(t, S)$, exactly one of two conditions holds:

    - *Continuation region:* The PDE holds ($\frac{\partial V}{\partial t} + \mathcal{L}_{\text{BS}}V = 0$) and $V > h(S)$.
    - *Exercise region:* The option is at intrinsic value ($V = h(S)$) and the PDE inequality holds ($\frac{\partial V}{\partial t} + \mathcal{L}_{\text{BS}}V \leq 0$).

    The PINN residual $\mathcal{R}_\theta = \max(\frac{\partial u_\theta}{\partial t} + \mathcal{L}_{\text{BS}}u_\theta, \; h(S) - u_\theta)$ is designed so that $\mathcal{R}_\theta = 0$ when and only when the linear complementarity conditions are satisfied:

    - If $u_\theta > h(S)$ (continuation), then $h(S) - u_\theta < 0$, so $\mathcal{R}_\theta = \max(\text{PDE residual}, \text{negative number}) = \text{PDE residual}$ if $\text{PDE residual} \geq 0$. Setting this to zero enforces the PDE.
    - If $u_\theta = h(S)$ (exercise), then $h(S) - u_\theta = 0$ and the PDE inequality ensures $\frac{\partial u}{\partial t} + \mathcal{L}_{\text{BS}}u \leq 0$, so $\mathcal{R}_\theta = \max(\text{non-positive}, 0) = 0$.

    **Why minimizing $\sum|\mathcal{R}_\theta|^2$ determines both price and boundary.**

    The loss $\sum_{j} |\mathcal{R}_\theta(t_j, S_j)|^2$ forces $\mathcal{R}_\theta \approx 0$ at all collocation points. This simultaneously:

    - Enforces the PDE in the continuation region (collocation points where $u_\theta > h$)
    - Enforces the early exercise constraint in the exercise region (collocation points where $u_\theta \approx h$)
    - Determines the exercise boundary: it is the curve $(t, S^*(t))$ where the network transitions from PDE-holding to exercise-constraint-holding behavior

    The exercise boundary emerges implicitly from the optimization. No explicit tracking or parameterization of $S^*(t)$ is needed -- it is defined by where the network's behavior switches from one regime to the other.

    **Comparison to finite-difference penalty method.**

    The finite-difference penalty method also reformulates the complementarity as a penalized PDE:

    $$
    \frac{\partial V}{\partial t} + \mathcal{L}_{\text{BS}}V + \frac{1}{\epsilon}\max(h(S) - V, 0) = 0
    $$

    where $1/\epsilon$ is a large penalty parameter. As $\epsilon \to 0$, the solution converges to the American option price. This requires:

    - Choosing $\epsilon$ (too large: inaccurate; too small: stiff system, slow convergence)
    - A spatial grid for $S$ (curse of dimensionality for multi-asset)
    - Iterative solution of the nonlinear system at each time step

    The PINN approach avoids grid construction and directly enforces the $\max$ condition through the loss, without needing to tune a penalty parameter. However, the $\max$ operator in the PINN residual is non-smooth, which can make optimization harder. In practice, a smooth approximation like $\max(a, b) \approx \frac{1}{2}(a + b + \sqrt{(a-b)^2 + \epsilon^2})$ is often used.

---

**Exercise 7.** A PINN is trained on the Black-Scholes PDE with 5,000 interior collocation points, 1,000 terminal condition points, and 200 observed market prices of European options at various strikes and maturities. After training, the PDE residual loss is $10^{-5}$ and the data loss is $10^{-3}$. Discuss whether the PINN is correctly calibrated. How could the PINN be used to extrapolate option prices to strikes and maturities not observed in the market? What ensures that the extrapolated prices are arbitrage-free?

??? success "Solution to Exercise 7"
    **Assessing calibration quality.**

    The PDE residual loss of $10^{-5}$ is small, indicating that the network output nearly satisfies the Black-Scholes PDE throughout the domain. This is good -- the solution is physically consistent.

    The data loss of $10^{-3}$ is two orders of magnitude larger, meaning the network does not perfectly match observed market prices. This needs interpretation:

    - If the data loss corresponds to price errors of $\sqrt{10^{-3}} \approx 0.032$ (in appropriate units), this may or may not be acceptable depending on the price scale. For options priced around \$10, this is a 0.3% error, which is reasonable. For options priced around \$0.10, this is a 32% error, which is unacceptable.

    - The discrepancy between PDE and data losses suggests the model (Black-Scholes with constant $\sigma$) may not perfectly fit market prices. Real markets exhibit a volatility smile, which a constant-$\sigma$ Black-Scholes PINN cannot capture. The PINN correctly solves the PDE but the PDE itself (with constant $\sigma$) is inconsistent with market prices.

    - To improve calibration, one could: (1) use a more flexible PDE (e.g., local volatility or Heston), (2) increase $\lambda_{\text{data}}$ to force better data fit at the expense of PDE satisfaction, or (3) make $\sigma$ a learnable parameter or function.

    **Extrapolation to unobserved strikes and maturities.**

    Once trained, the PINN $u_\theta(t, S)$ can be evaluated at any $(t, S)$, including strikes and maturities not present in the training data. This is extrapolation in the $(K, T)$ space.

    The PINN extrapolates by:

    1. Satisfying the PDE everywhere (including in unobserved regions), which constrains the solution through the dynamics
    2. Matching the terminal condition (payoff), which anchors the solution at maturity
    3. Matching observed prices where available, which calibrates the model

    In regions without data, the PDE residual loss alone determines the network output. The solution is the unique function satisfying both the PDE and the boundary conditions, which is well-posed for parabolic PDEs.

    **What ensures arbitrage-free extrapolation.**

    The extrapolated prices are arbitrage-free because:

    1. *PDE consistency:* The Black-Scholes PDE is derived from no-arbitrage arguments. Any function satisfying the PDE (with correct boundary conditions) is the price of a self-financing replicating portfolio, which is arbitrage-free by construction.

    2. *Terminal condition:* The payoff function $(S - K)^+$ is convex in $S$ (for calls), and the PDE preserves convexity backward in time. So $V(t, \cdot)$ is convex in $S$ for all $t < T$, ensuring positive butterfly spreads.

    3. *Time monotonicity:* The PDE ensures that total variance increases with maturity (for the constant-$\sigma$ case, $\sigma^2(T - t)$ is monotonically decreasing backward in time), preventing calendar spread arbitrage.

    However, these guarantees rely on the PINN solving the PDE accurately (small PDE residual). If the PDE residual is not sufficiently small, the network may produce slight arbitrage violations. Hard enforcement of boundary conditions (as in Exercise 2) strengthens these guarantees. Additionally, if the model is misspecified (constant $\sigma$ when the market exhibits a smile), the extrapolated prices may be internally consistent but economically incorrect -- they satisfy Black-Scholes arbitrage constraints but not the market's actual dynamics.
