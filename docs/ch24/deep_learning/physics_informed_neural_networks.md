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

The Black-Scholes PDE for a European option price $V(t, S)$ is:

$$
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
$$

on the domain $(t, S) \in [0, T) \times (0, \infty)$ with terminal condition $V(T, S) = h(S)$.

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

---

**Exercise 2.** Design a hard-constrained PINN ansatz for a European put option with terminal condition $V(T, S) = (K - S)^+$ and boundary conditions $V(t, 0) = Ke^{-r(T-t)}$ and $V(t, \infty) = 0$. Your ansatz should have the form $u_\theta(t, S) = A(t, S) + B(t, S) \cdot \mathcal{N}_\theta(t, S)$ where $A$ satisfies the boundary conditions and $B$ vanishes on the boundary. Verify that your ansatz satisfies all three boundary/terminal conditions exactly.

---

**Exercise 3.** The PINN loss has three components with weights $\lambda_{\text{PDE}}$, $\lambda_{\text{BC}}$, and $\lambda_{\text{data}}$. Explain the effect of setting $\lambda_{\text{PDE}} \gg \lambda_{\text{BC}}$ versus $\lambda_{\text{BC}} \gg \lambda_{\text{PDE}}$. In the extreme case $\lambda_{\text{PDE}} = 0$, what does the PINN reduce to? In the extreme $\lambda_{\text{data}} = 0$, what does it reduce to? Describe the adaptive weighting strategy and why it balances gradient magnitudes.

---

**Exercise 4.** A PINN is used to solve the Heston PDE with 3 inputs $(t, S, v)$. The PDE residual involves second-order derivatives $\partial^2 V/\partial S^2$, $\partial^2 V/\partial v^2$, and the mixed derivative $\partial^2 V/\partial S \partial v$. Explain how automatic differentiation computes these quantities through the neural network. Compare the computational cost to finite differences on a $(t, S, v)$ grid with $M$ points per dimension, noting that the PINN avoids the $O(M^3)$ grid storage.

---

**Exercise 5.** The spectral bias of neural networks means that low-frequency components of the PDE solution are learned first, while high-frequency components (e.g., the payoff kink at $S = K$) converge slowly. For a call option with $K = 100$, the payoff $(S - K)^+$ has a discontinuity in the first derivative at $S = 100$. Discuss: (a) why smooth activations ($\tanh$) are preferred over ReLU for PINNs, (b) how Fourier feature layers can accelerate learning of sharp features, and (c) how residual-based adaptive refinement concentrates collocation points near $S = K$.

---

**Exercise 6.** Explain how the PINN penalty method handles the American option free boundary. The residual

$$
\mathcal{R}_\theta(t, S) = \max\left(\frac{\partial u_\theta}{\partial t} + \mathcal{L}_{\text{BS}}[u_\theta], \; h(S) - u_\theta(t, S)\right)
$$

is zero in both the continuation region (PDE holds, $u \ge h$) and the exercise region ($u = h$). Why does minimizing $\sum |\mathcal{R}_\theta|^2$ simultaneously determine the price and the exercise boundary? Compare this to the finite-difference penalty method.

---

**Exercise 7.** A PINN is trained on the Black-Scholes PDE with 5,000 interior collocation points, 1,000 terminal condition points, and 200 observed market prices of European options at various strikes and maturities. After training, the PDE residual loss is $10^{-5}$ and the data loss is $10^{-3}$. Discuss whether the PINN is correctly calibrated. How could the PINN be used to extrapolate option prices to strikes and maturities not observed in the market? What ensures that the extrapolated prices are arbitrage-free?
