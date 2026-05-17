# Deep BSDE Method

The **Deep BSDE method**, introduced by E, Han, and Jentzen (2017), reformulates the numerical solution of high-dimensional partial differential equations as a stochastic optimization problem. By exploiting the connection between parabolic PDEs and backward stochastic differential equations (BSDEs) via the Feynman-Kac theorem, and parameterizing the unknown gradient process with neural networks, this approach solves problems in 100+ dimensions that are completely intractable for grid-based methods.

---

## From PDEs to BSDEs: The Feynman-Kac Connection

Recall (see [§ Feynman-Kac Formula](../../ch05/feynman_kac/feynman_kac_formula.md)) the linear Feynman-Kac representation linking parabolic PDEs to expectations of diffusions; here we use its **nonlinear** extension (see [§ 2BSDEs](../../ch23/second_order_bsdes_and_nonlinear_expectations/2bsdes.md) for the BSDE framework).

### The Semilinear Parabolic PDE

Consider the semilinear parabolic PDE on $[0,T] \times \mathbb{R}^d$:

$$
\frac{\partial u}{\partial t}(t,x) + \frac{1}{2}\operatorname{tr}\!\left[\sigma\sigma^\top(t,x)\,D^2_x u(t,x)\right] + \mu(t,x)^\top D_x u(t,x) + f\!\left(t, x, u(t,x), \sigma^\top(t,x)\,D_x u(t,x)\right) = 0
$$

with terminal condition $u(T,x) = g(x)$. This PDE arises throughout quantitative finance: Black-Scholes PDE for multi-asset derivatives, HJB equations for optimal control, and pricing under counterparty risk (CVA/DVA).

### The Associated BSDE

**Theorem (Nonlinear Feynman-Kac).** Under regularity conditions, the PDE solution $u(t,x)$ is connected to the BSDE:

$$
Y_t = g(X_T) + \int_t^T f(s, X_s, Y_s, Z_s) \, ds - \int_t^T Z_s^\top \, dW_s
$$

where the forward process satisfies $dX_s = \mu(s, X_s) \, ds + \sigma(s, X_s) \, dW_s$, $X_t = x$. The identification is $Y_s = u(s, X_s)$ and $Z_s = \sigma^\top(s, X_s) \, D_x u(s, X_s)$: $Y$ tracks the PDE solution along the forward path, $Z$ encodes the (scaled) gradient.

!!! note "Why BSDEs Are Hard"
    The BSDE is a **backward** equation: the terminal condition $Y_T = g(X_T)$ is given, but we must find $(Y_t, Z_t)$ for $t < T$. Unlike forward SDEs, backward SDEs cannot be simulated by simply stepping forward in time. Classical numerical methods (Bouchard-Touzi, Zhang) discretize backward in time and solve nested conditional expectations, which scales exponentially in dimension $d$.

---

## The Deep BSDE Algorithm

### Core Idea

The key insight is to reformulate the backward problem as a **forward** optimization. Instead of solving the BSDE backward, we:

1. Parameterize $Y_0$ (the initial value) as a learnable scalar
2. Parameterize $Z_{t_k}$ (the gradient at each time step) as neural networks
3. Simulate the BSDE forward using these parameterizations
4. Minimize the mismatch at the terminal time

### Time Discretization

Partition $[0,T]$ into $N$ steps: $0 = t_0 < t_1 < \cdots < t_N = T$ with $\Delta t_k = t_{k+1} - t_k$. Discretize the forward SDE:

$$
X_{t_{k+1}} = X_{t_k} + \mu(t_k, X_{t_k})\,\Delta t_k + \sigma(t_k, X_{t_k})\,\Delta W_k
$$

where $\Delta W_k = W_{t_{k+1}} - W_{t_k} \sim \mathcal{N}(0, \Delta t_k \, I_d)$.

Discretize the BSDE forward:

$$
Y_{t_{k+1}} = Y_{t_k} - f(t_k, X_{t_k}, Y_{t_k}, Z_{t_k})\,\Delta t_k + (Z_{t_k})^\top \Delta W_k
$$

### Neural Network Parameterization

At each time step $t_k$, parameterize the gradient process:

$$
Z_{t_k} \approx \mathcal{Z}_{\theta_k}(t_k, X_{t_k})
$$

where $\mathcal{Z}_{\theta_k} : \mathbb{R}^{d+1} \to \mathbb{R}^d$ is a feedforward neural network with parameters $\theta_k$. Additionally, $Y_0 \in \mathbb{R}$ is a learnable parameter (the initial PDE value).

The complete set of trainable parameters is:

$$
\Theta = \left(Y_0, \theta_0, \theta_1, \ldots, \theta_{N-1}\right)
$$

### The Loss Function

Given the parameterized forward evolution, the terminal value $Y_{t_N}^\Theta$ is a function of all parameters and the Brownian path. The loss is the expected squared terminal mismatch:

$$
\mathcal{L}(\Theta) = \mathbb{E}\!\left[\left|Y_{t_N}^\Theta - g(X_{t_N})\right|^2\right]
$$

If the parameterization is exact, the true parameters give $\mathcal{L}(\Theta^*) = 0$. In practice, we minimize $\mathcal{L}$ via stochastic gradient descent over mini-batches of simulated Brownian paths.

**Algorithm (Deep BSDE):**

1. Initialize $Y_0$ and network parameters $\{\theta_k\}_{k=0}^{N-1}$
2. For each training iteration:
    - Sample a batch of $M$ Brownian increments $\{\Delta W_k^{(m)}\}$
    - For each sample, propagate $X$ and $Y$ forward:
        - $X_{t_{k+1}}^{(m)} = X_{t_k}^{(m)} + \mu \, \Delta t_k + \sigma \, \Delta W_k^{(m)}$
        - $Z_{t_k}^{(m)} = \mathcal{Z}_{\theta_k}(t_k, X_{t_k}^{(m)})$
        - $Y_{t_{k+1}}^{(m)} = Y_{t_k}^{(m)} - f(\cdot)\,\Delta t_k + (Z_{t_k}^{(m)})^\top \Delta W_k^{(m)}$
    - Compute loss: $\hat{\mathcal{L}} = \frac{1}{M}\sum_{m=1}^M |Y_{t_N}^{(m)} - g(X_{t_N}^{(m)})|^2$
    - Update $\Theta$ via Adam optimizer
3. Output: $\hat{u}(0, x_0) = Y_0$ and $\hat{Z}_{t_k}(\cdot) = \mathcal{Z}_{\theta_k}(t_k, \cdot)$

---

## Architecture and Implementation Details

### Network Architecture for Each Time Step

Each sub-network $\mathcal{Z}_{\theta_k}$ is typically a feedforward network with:

- Input: $(t_k, X_{t_k}) \in \mathbb{R}^{d+1}$
- Hidden layers: 2--4 layers, each with $d + 10$ to $d + 50$ neurons
- Activation: ReLU or batch-normalized ReLU
- Output: $Z_{t_k} \in \mathbb{R}^d$

**Batch normalization** is applied before each activation to stabilize training across different time steps and scales.

### Parameter Sharing

Two common approaches:

- **Unshared:** Each time step $t_k$ has its own network $\mathcal{Z}_{\theta_k}$. More flexible but more parameters.
- **Shared:** A single network $\mathcal{Z}_\theta(t, x)$ is used for all time steps, with time $t$ as an additional input. Fewer parameters, better generalization.

### Training Considerations

- **Learning rate scheduling:** Start with larger learning rate ($10^{-3}$), decay over training
- **Mini-batch size:** Typically $M = 256$ to $4096$ paths
- **Number of time steps:** $N = 20$ to $100$ depending on problem stiffness
- **Convergence criterion:** Relative loss $\hat{\mathcal{L}}/|g|^2 < 10^{-3}$

---

## Convergence Analysis

### A Priori Error Bounds

**Theorem (Convergence of Deep BSDE -- Han, Jentzen, E 2018).** Under standard Lipschitz conditions on $\mu, \sigma, f, g$, and assuming the neural network class $\mathcal{F}_N$ can approximate the true gradient $\sigma^\top D_x u$ to accuracy $\delta$ uniformly, the Deep BSDE method satisfies:

$$
\left|\hat{u}(0, x_0) - u(0, x_0)\right|^2 \leq C\!\left(\Delta t + \delta^2\right)
$$

where $C$ depends on the Lipschitz constants and time horizon $T$.

The first term $\Delta t$ is the time discretization error (Euler scheme), and the second term $\delta^2$ is the neural network approximation error.

### Sources of Error

The total error decomposes as:

$$
\text{Total error} = \underbrace{\text{Time discretization}}_{\text{Euler: } O(\Delta t)} + \underbrace{\text{Network approximation}}_{\text{approx: } O(\delta)} + \underbrace{\text{Optimization}}_{\text{SGD convergence}} + \underbrace{\text{Statistical}}_{\text{Monte Carlo: } O(M^{-1/2})}
$$

!!! tip "Dimension Independence"
    The critical advantage is that none of these error components scale exponentially with dimension $d$. The time discretization error is $O(\Delta t)$ regardless of $d$. The network approximation error depends on the Barron norm of $\sigma^\top D_x u$, not on $d$ directly. The Monte Carlo error is $O(M^{-1/2})$ regardless of $d$. This is what makes the method feasible for $d = 100$ or $d = 1000$.

---

## Example: Black-Scholes in High Dimensions

### Problem Setup

Consider pricing a European call on the arithmetic average of $d$ correlated assets under Black-Scholes dynamics:

$$
dS_t^{(i)} = r S_t^{(i)} \, dt + \sigma_i S_t^{(i)} \, dW_t^{(i)}, \quad i = 1, \ldots, d
$$

with payoff $g(S_T) = \left(\frac{1}{d}\sum_{i=1}^d S_T^{(i)} - K\right)^{\!+}$.

The pricing PDE is $d$-dimensional. For $d = 100$, no grid-based method can solve it.

### Deep BSDE Formulation

Set $X_t = (S_t^{(1)}, \ldots, S_t^{(d)})$, so $\mu(t,x) = r \, x$ (componentwise) and $\sigma(t,x) = \operatorname{diag}(\sigma_1 x_1, \ldots, \sigma_d x_d)$. The driver $f = -r \, Y$ (linear PDE), giving:

$$
Y_{t_{k+1}} = Y_{t_k} + r Y_{t_k} \, \Delta t_k + Z_{t_k}^\top \Delta W_k
$$

The neural network $\mathcal{Z}_{\theta_k}$ outputs the $d$-dimensional hedge ratio (Delta vector) at each time step.

### Results

For $d = 100$ with $S_0^{(i)} = 100$, $K = 100$, $r = 0.05$, $\sigma_i = 0.2$, $T = 0.5$:

- The Deep BSDE method converges in approximately 2000--5000 training steps
- Relative error: $< 0.5\%$ compared to Monte Carlo benchmark
- Training time: minutes on a modern GPU
- The learned $Z$ process correctly recovers the delta hedging strategy

---

## Extensions and Variants

### Deep BSDE for Nonlinear PDEs

The method handles genuinely nonlinear PDEs where Monte Carlo fails. For example, the **Allen-Cahn equation**:

$$
\frac{\partial u}{\partial t} + \frac{1}{2}\Delta u + u - u^3 = 0, \quad u(T,x) = \frac{1}{1 + \|x\|^2}
$$

has a nonlinear reaction term $f(u) = u - u^3$. The Deep BSDE method handles this by including the nonlinearity in the driver:

$$
Y_{t_{k+1}} = Y_{t_k} - (Y_{t_k} - Y_{t_k}^3)\,\Delta t_k + Z_{t_k}^\top \Delta W_k
$$

### Deep Splitting Method

Alternatively, one can split the time step into a linear part (handled by Feynman-Kac) and a nonlinear part (handled by a separate neural network):

$$
\hat{Y}_{t_{k+1}} = \mathbb{E}\!\left[Y_{t_k} \mid X_{t_{k+1}}\right] \approx \mathcal{U}_{\phi_k}(X_{t_{k+1}})
$$

$$
Y_{t_{k+1}} = \hat{Y}_{t_{k+1}} - f(t_k, X_{t_k}, \hat{Y}_{t_{k+1}}, Z_{t_k})\,\Delta t_k
$$

### Multi-Level Picard Iteration

The MLP method combines Picard iteration for the BSDE nonlinearity with multi-level Monte Carlo for variance reduction, achieving polynomial complexity in $d$ with rigorous error bounds.

---

## Comparison with Classical Methods

| Method | Complexity | Max Dimension | Nonlinear PDE |
|---|---|---|---|
| Finite Difference | $O(M^d)$ | $d \leq 4$ | Limited |
| Finite Element | $O(M^d)$ | $d \leq 5$ | Yes |
| Standard Monte Carlo | $O(M \cdot N)$ | Any (linear) | No |
| Nested Monte Carlo | $O(M^2 \cdot N)$ | Any | Limited |
| **Deep BSDE** | $O(M \cdot N \cdot C_{\text{net}})$ | $d \geq 100$ | **Yes** |

where $M$ is the number of sample paths, $N$ the number of time steps, and $C_{\text{net}}$ the network evaluation cost (independent of $d$ up to input layer size).

---

## Key Takeaways

1. The **Feynman-Kac theorem** connects semilinear parabolic PDEs to BSDEs, transforming PDE solving into a stochastic control problem.

2. The **Deep BSDE method** parameterizes the gradient process $Z$ with neural networks and minimizes terminal mismatch, converting a backward problem into a forward optimization.

3. **Dimension independence** is the critical advantage: neither time discretization, network approximation, nor Monte Carlo errors scale exponentially with $d$.

4. The method naturally produces both the **PDE solution** ($Y_0$) and the **gradient/hedge ratio** ($Z_t$), which is directly useful for delta hedging.

5. **Nonlinear PDEs** (HJB equations, reaction-diffusion) that are inaccessible to standard Monte Carlo are handled naturally through the BSDE driver.

---

## Further Reading

- E, Han & Jentzen (2017), "Deep Learning-Based Numerical Methods for High-Dimensional Parabolic PDEs and BSDEs"
- Han, Jentzen & E (2018), "Solving High-Dimensional Partial Differential Equations Using Deep Learning"
- Beck, E & Jentzen (2019), "Machine Learning Approximation Algorithms for High-Dimensional FBSDEs"
- Pardoux & Peng (1990), "Adapted Solution of a Backward Stochastic Differential Equation"
- Bouchard & Touzi (2004), "Discrete-Time Approximation and Monte-Carlo Simulation of BSDEs"

---

## Exercises

**Exercise 1.** Write out the discretized BSDE forward step

$$
Y_{t_{k+1}} = Y_{t_k} - f(t_k, X_{t_k}, Y_{t_k}, Z_{t_k})\,\Delta t_k + Z_{t_k}^\top \Delta W_k
$$

for the Black-Scholes PDE with driver $f(t, x, y, z) = -ry$. Verify that this simplifies to $Y_{t_{k+1}} = Y_{t_k}(1 + r\Delta t_k) + Z_{t_k}^\top \Delta W_k$. Explain why $Y_0$ corresponds to the option price and $Z_{t_k}$ to the delta-hedging portfolio (scaled by $\sigma$).

??? success "Solution to Exercise 1"
    **Discretized BSDE forward step with Black-Scholes driver.**

    The general BSDE discretization is:

    $$
    Y_{t_{k+1}} = Y_{t_k} - f(t_k, X_{t_k}, Y_{t_k}, Z_{t_k}) \, \Delta t_k + Z_{t_k}^\top \Delta W_k
    $$

    For the Black-Scholes PDE, the driver is $f(t, x, y, z) = -ry$ (the term $-rV$ in the PDE). Substituting:

    $$
    Y_{t_{k+1}} = Y_{t_k} - (-rY_{t_k}) \, \Delta t_k + Z_{t_k}^\top \Delta W_k = Y_{t_k} + rY_{t_k} \, \Delta t_k + Z_{t_k}^\top \Delta W_k
    $$

    $$
    Y_{t_{k+1}} = Y_{t_k}(1 + r\Delta t_k) + Z_{t_k}^\top \Delta W_k
    $$

    This confirms the stated simplification.

    **Why $Y_0$ is the option price.** By the Feynman-Kac connection, $Y_t = u(t, X_t)$ where $u$ is the solution to the pricing PDE. At $t = 0$:

    $$
    Y_0 = u(0, X_0) = V(0, S_0)
    $$

    which is the option price at time 0. The terminal condition $Y_T = g(X_T) = h(S_T)$ is the option payoff, and the BSDE propagates the price backward (but is simulated forward in the Deep BSDE method).

    **Why $Z_{t_k}$ is the delta-hedging portfolio (scaled by $\sigma$).** The Feynman-Kac relationship gives:

    $$
    Z_t = \sigma^\top(t, X_t) \, D_x u(t, X_t)
    $$

    For the Black-Scholes model with $d$ assets, $\sigma(t, x) = \text{diag}(\sigma_1 x_1, \ldots, \sigma_d x_d)$, so:

    $$
    Z_t^{(i)} = \sigma_i S_t^{(i)} \frac{\partial V}{\partial S^{(i)}}(t, S_t) = \sigma_i S_t^{(i)} \Delta_t^{(i)}
    $$

    where $\Delta_t^{(i)} = \partial V / \partial S^{(i)}$ is the delta with respect to asset $i$. Thus $Z_t$ encodes the delta hedging portfolio, scaled by the volatility and the stock price. To recover the dollar delta, compute $\Delta_t^{(i)} = Z_t^{(i)} / (\sigma_i S_t^{(i)})$.

    The economic interpretation of the update $Y_{t_{k+1}} = Y_{t_k}(1 + r\Delta t_k) + Z_{t_k}^\top \Delta W_k$ is: the option price grows at the risk-free rate $r$ (first term) plus gains/losses from delta hedging (second term, which is the hedge P&L from exposure to the Brownian shocks).

---

**Exercise 2.** The Deep BSDE loss function is $\mathcal{L}(\Theta) = \mathbb{E}[|Y_{t_N}^\Theta - g(X_{t_N})|^2]$. Explain why minimizing this loss over parameters $\Theta = (Y_0, \theta_0, \ldots, \theta_{N-1})$ produces both the PDE solution $u(0, x_0) = Y_0$ and the gradient process $Z_{t_k} = \mathcal{Z}_{\theta_k}(t_k, X_{t_k})$. What value should the loss converge to if the neural networks can perfectly represent the true gradient?

??? success "Solution to Exercise 2"
    **Why minimizing the loss produces both the PDE solution and the gradient.**

    The loss function is:

    $$
    \mathcal{L}(\Theta) = \mathbb{E}\!\left[|Y_{t_N}^\Theta - g(X_{t_N})|^2\right]
    $$

    The forward evolution starting from $(Y_0, Z_{t_0}, Z_{t_1}, \ldots, Z_{t_{N-1}})$ produces a terminal value $Y_{t_N}^\Theta$. By the BSDE theory, the true solution satisfies $Y_T = g(X_T)$ almost surely. This means:

    - If $Y_0$ is set to the true PDE solution $u(0, x_0)$, AND
    - If $Z_{t_k}$ equals $\sigma^\top D_x u(t_k, X_{t_k})$ at every step,

    then the forward propagation produces $Y_{t_N} = u(T, X_T) = g(X_T)$ exactly, giving $\mathcal{L} = 0$.

    Conversely, if $Y_0$ or any $Z_{t_k}$ is wrong, the errors accumulate through the forward propagation, producing $Y_{t_N}^\Theta \neq g(X_{t_N})$ with positive probability, so $\mathcal{L} > 0$.

    Therefore, the global minimum $\mathcal{L}(\Theta^*) = 0$ is achieved if and only if:

    $$
    Y_0^* = u(0, x_0) \quad \text{and} \quad \mathcal{Z}_{\theta_k^*}(t_k, x) = \sigma^\top(t_k, x) D_x u(t_k, x) \text{ for all } k
    $$

    **What the loss converges to.** If the neural networks can perfectly represent the true gradient function (i.e., the approximation error $\delta = 0$), the loss converges to $\mathcal{L}(\Theta^*) = 0$. In practice, the loss converges to a small positive value reflecting the combined approximation error of the networks, the time discretization error (Euler scheme), and the Monte Carlo estimation error.

    The elegance of the Deep BSDE method is that a single scalar loss function simultaneously determines all of the unknowns: the initial value $Y_0$ (one number) and the entire gradient field $Z(t, x)$ (a function of space and time, parameterized by the networks).

---

**Exercise 3.** The convergence bound states $|\hat{u}(0,x_0) - u(0,x_0)|^2 \le C(\Delta t + \delta^2)$ where $\Delta t$ is the time step and $\delta$ the network approximation error. If $T = 1$ year and $N = 50$ time steps, compute $\Delta t$. Discuss qualitatively how increasing the network width affects $\delta$ (via universal approximation), and why neither error term depends exponentially on dimension $d$. Why is this dimension independence the key advantage over finite difference methods?

??? success "Solution to Exercise 3"
    **Computing $\Delta t$.**

    With $T = 1$ year and $N = 50$ time steps (assuming uniform spacing):

    $$
    \Delta t = \frac{T}{N} = \frac{1}{50} = 0.02 \text{ years} \approx 5 \text{ trading days}
    $$

    **Effect of increasing network width on $\delta$.**

    By the universal approximation theorem, a feedforward network with a single hidden layer of width $W$ can approximate any continuous function on a compact set to accuracy $\delta$ for sufficiently large $W$. By Barron's theorem, if the target function $\sigma^\top D_x u$ has finite Barron norm $C_Z$, then a network with $W$ neurons achieves:

    $$
    \delta^2 \lesssim \frac{C_Z^2}{W}
    $$

    So increasing $W$ decreases $\delta$ at the rate $O(1/\sqrt{W})$. In practice, deeper networks can achieve even faster rates for smooth target functions.

    **Why neither error term depends exponentially on $d$.**

    1. *Time discretization error $O(\Delta t)$:* The Euler-Maruyama scheme has weak convergence order 1, meaning $|\mathbb{E}[g(X_N)] - \mathbb{E}[g(X_T)]| = O(\Delta t)$. This rate depends on the Lipschitz constants of $\mu, \sigma, g$, which are properties of the PDE coefficients. For standard financial models (GBM, Heston), these constants are independent of or polynomial in $d$. The Euler scheme processes each dimension simultaneously, not sequentially.

    2. *Network approximation error $O(\delta)$:* The target function $Z(t, x) = \sigma^\top D_x u(t, x)$ is a function from $\mathbb{R}^{d+1}$ to $\mathbb{R}^d$. If this function has finite Barron norm (which is plausible for pricing functions, by the arguments in the approximation theory section), then the network approximation rate is $O(1/\sqrt{W})$, independent of $d$.

    3. *Monte Carlo error $O(M^{-1/2})$:* The loss is estimated by averaging over $M$ sample paths. The central limit theorem gives convergence rate $O(1/\sqrt{M})$ regardless of the dimension of the underlying process. This is the fundamental advantage of Monte Carlo methods.

    **Why this is the key advantage over finite differences.** Finite difference methods discretize the spatial domain $[0, L]^d$ with $M$ grid points per dimension, requiring $M^d$ total grid points. For $d = 100$ and even $M = 10$, this is $10^{100}$ points -- completely impossible. The Deep BSDE method bypasses this because it never constructs a spatial grid. Instead, it samples paths in $\mathbb{R}^d$ via Monte Carlo, with cost linear in $d$ per path. The neural network processes $d$-dimensional inputs, with cost polynomial (not exponential) in $d$.

---

**Exercise 4.** Consider using the Deep BSDE method for a 10-asset basket option pricing problem. The forward SDE in log-coordinates is $dX_t^{(i)} = (r - \sigma_i^2/2)dt + \sigma_i dW_t^{(i)}$ for $i = 1,\ldots,10$. Describe the input and output dimensions of the neural network $\mathcal{Z}_{\theta_k}$ at each time step. If each hidden layer has 20 neurons and there are 2 hidden layers, estimate the total number of parameters per sub-network. With $N = 50$ time steps and unshared networks, how many total parameters are there?

??? success "Solution to Exercise 4"
    **Input and output dimensions of $\mathcal{Z}_{\theta_k}$.**

    The forward SDE has state $X_t = (X_t^{(1)}, \ldots, X_t^{(10)}) \in \mathbb{R}^{10}$ (the 10 log-asset-prices). The network input at time step $k$ is $(t_k, X_{t_k}) \in \mathbb{R}^{11}$ (time plus 10-dimensional state).

    The output is $Z_{t_k} = \sigma^\top D_x u(t_k, X_{t_k}) \in \mathbb{R}^{10}$ (one component per asset, representing the scaled delta).

    So each sub-network $\mathcal{Z}_{\theta_k} : \mathbb{R}^{11} \to \mathbb{R}^{10}$.

    **Parameter count per sub-network with 2 hidden layers of 20 neurons:**

    - Input layer to hidden layer 1: $20 \times 11 + 20 = 220 + 20 = 240$ (weights + biases)
    - Hidden layer 1 to hidden layer 2: $20 \times 20 + 20 = 400 + 20 = 420$
    - Hidden layer 2 to output layer: $10 \times 20 + 10 = 200 + 10 = 210$

    Total per sub-network: $240 + 420 + 210 = 870$ parameters.

    **Total parameters with $N = 50$ time steps and unshared networks:**

    We need $N = 50$ sub-networks plus the learnable initial value $Y_0$.

    $$
    \text{Total} = 50 \times 870 + 1 = 43{,}501 \text{ parameters}
    $$

    This is very manageable for modern optimizers. For comparison, a finite-difference grid with $M = 10$ points per dimension would require $M^{10} = 10^{10}$ grid points, which is completely infeasible.

    **Additional note:** If a shared architecture is used instead, the network takes $(t_k, X_{t_k}) \in \mathbb{R}^{11}$ as input (same as above) but uses a single set of 870 parameters for all time steps. The total would be just $870 + 1 = 871$ parameters, a 50x reduction that can improve generalization but may sacrifice accuracy for problems where the gradient structure varies significantly with time.

---

**Exercise 5.** The Deep BSDE method for a nonlinear PDE with driver $f(t, x, y, z) = y - y^3$ (Allen-Cahn equation) involves the update $Y_{t_{k+1}} = Y_{t_k} - (Y_{t_k} - Y_{t_k}^3)\Delta t_k + Z_{t_k}^\top \Delta W_k$. Explain why standard Monte Carlo cannot solve this PDE (since it requires an expectation under a nonlinear Feynman-Kac formula). How does the Deep BSDE method handle the nonlinearity through the forward simulation? In what financial application does a similar nonlinear driver arise?

??? success "Solution to Exercise 5"
    **Why standard Monte Carlo cannot solve nonlinear PDEs.**

    Standard Monte Carlo is based on the linear Feynman-Kac formula:

    $$
    u(t, x) = \mathbb{E}[g(X_T) \mid X_t = x]
    $$

    This representation requires the PDE to be *linear* in $u$, specifically of the form:

    $$
    \frac{\partial u}{\partial t} + \mathcal{L} u = 0
    $$

    where $\mathcal{L}$ is a second-order linear operator. The solution is an expectation, which Monte Carlo can estimate.

    For the Allen-Cahn equation with driver $f(y) = y - y^3$, the PDE is:

    $$
    \frac{\partial u}{\partial t} + \frac{1}{2}\Delta u + u - u^3 = 0
    $$

    The term $u^3$ makes the PDE nonlinear in $u$. There is no Feynman-Kac representation of the form $u = \mathbb{E}[\cdot]$ because the nonlinearity means the solution cannot be written as a simple expectation. The *nonlinear* Feynman-Kac formula gives a BSDE representation, but the BSDE involves the unknown $(Y, Z)$ coupled through the driver, so it cannot be solved by simple forward Monte Carlo.

    Specifically, to compute $\mathbb{E}[g(X_T)]$, one would need $u$ itself at intermediate times (because $f$ depends on $Y_t = u(t, X_t)$), creating a circular dependency: you need the solution to compute the solution.

    **How Deep BSDE handles the nonlinearity.**

    The Deep BSDE method breaks the circular dependency by parameterizing $Y_0$ and $Z_{t_k}$, then simulating forward:

    $$
    Y_{t_{k+1}} = Y_{t_k} - (Y_{t_k} - Y_{t_k}^3) \, \Delta t_k + Z_{t_k}^\top \Delta W_k
    $$

    At each step, $Y_{t_k}$ is known from the previous step (starting from the learnable $Y_0$), so the nonlinear driver $f(Y_{t_k}) = Y_{t_k} - Y_{t_k}^3$ can be evaluated explicitly. The forward simulation is purely mechanical -- no conditional expectations or nested Monte Carlo are needed. The nonlinearity is simply a deterministic function applied to the current $Y$ value.

    The terminal mismatch loss $|Y_{t_N} - g(X_{t_N})|^2$ then drives the optimization to find the correct $Y_0$ and $Z$ process that makes the forward evolution consistent with the terminal condition.

    **Financial application with similar nonlinear driver.**

    A prominent example is **Credit Valuation Adjustment (CVA)**. The pre-default value $V$ of a portfolio with counterparty credit risk satisfies:

    $$
    \frac{\partial V}{\partial t} + \mathcal{L}V - rV + \lambda(t)(V - V^-)^+ = 0
    $$

    where $\lambda(t)$ is the default intensity and $V^- = \min(V, 0)$ is the negative part. The driver $f(V) = \lambda \cdot \text{LGD} \cdot V^+$ (or similar nonlinear expressions involving $V^+$ or $V^-$) is nonlinear because the adjustment depends on whether the portfolio has positive or negative value -- you need to know $V$ to compute the credit adjustment to $V$. This creates the same circular dependency that the Deep BSDE method resolves.

---

**Exercise 6.** Compare the shared and unshared network architectures for the Deep BSDE method. In the shared architecture, a single network $\mathcal{Z}_\theta(t, x)$ is used for all time steps with time $t$ as an additional input. In the unshared architecture, each time step has its own network $\mathcal{Z}_{\theta_k}(x)$. Discuss the tradeoffs in terms of: (a) total number of parameters, (b) ability to capture time-varying gradient structure, (c) generalization performance, and (d) training time. Which architecture would you recommend for a long-dated (30-year) problem with $N = 120$ quarterly steps?

??? success "Solution to Exercise 6"
    **(a) Total number of parameters.**

    - *Unshared:* Each of $N$ time steps has its own network with $P$ parameters. Total: $N \times P + 1$.
    - *Shared:* A single network with $P'$ parameters (slightly larger due to the time input). Total: $P' + 1$.

    For $N = 120$ quarterly steps, the unshared architecture has 120x more parameters. If each sub-network has 1,000 parameters, unshared uses 120,000 while shared uses about 1,000.

    **(b) Ability to capture time-varying gradient structure.**

    - *Unshared:* Each network independently adapts to the gradient structure at its specific time step. This is important when the gradient function $Z(t, x) = \sigma^\top D_x u(t, x)$ changes qualitatively with time (e.g., near maturity where option gamma peaks, or at payment dates in structured products).
    - *Shared:* Must encode all time variation through the single time input $t$. If the gradient structure varies smoothly with time, this works well. If there are abrupt changes (e.g., at coupon dates), the shared network may struggle to represent the discontinuity.

    **(c) Generalization performance.**

    - *Unshared:* Each sub-network sees only the data at its specific time step. With $M$ Monte Carlo paths, each sub-network has $M$ training examples. This can be insufficient for complex gradient structures, leading to overfitting.
    - *Shared:* The single network sees data from all $N$ time steps, effectively having $N \times M$ training examples. This provides much better statistical efficiency and regularization. The shared architecture implicitly assumes that the gradient structure is similar across time steps, which is a form of inductive bias.

    **(d) Training time.**

    - *Unshared:* More parameters means slower gradient computation and more iterations to converge. However, the forward pass is embarrassingly parallelizable across time steps (each sub-network is independent).
    - *Shared:* Fewer parameters means faster per-iteration cost and typically faster convergence. The network is evaluated sequentially across time steps in the forward pass.

    **Recommendation for a 30-year problem with $N = 120$ quarterly steps.**

    The **shared architecture** is strongly recommended for this problem:

    1. With $N = 120$, the unshared architecture has 120x more parameters, greatly increasing overfitting risk and training time.
    2. Over 30 years, the gradient structure changes gradually (the time scale of variation is years, not steps), so a shared network with time input can capture the variation smoothly.
    3. Statistical efficiency: each sub-network in the unshared case sees only $M$ samples, while the shared network effectively sees $120M$ samples.
    4. Memory: storing 120 separate networks' activations for backpropagation is expensive.

    An intermediate approach is to use a shared backbone with time-step-specific final layers: $Z_{t_k} = W_k \cdot \phi_\theta(t_k, X_{t_k}) + b_k$, where $\phi_\theta$ is a shared feature extractor and $(W_k, b_k)$ are per-step output weights. This captures time variation in the output layer while sharing the expensive feature extraction.

---

**Exercise 7.** A financial application of the Deep BSDE method is computing CVA for a multi-currency portfolio with $d = 20$ risk factors. The semilinear PDE includes the nonlinear driver $f(v) = \lambda_C \cdot \text{LGD} \cdot v^+$. Explain why this is intractable with grid-based PDE methods. Describe how you would set up the Deep BSDE problem: define the forward process, the BSDE driver, and the terminal condition. What does $Y_0$ represent financially, and what does $Z_0$ represent?

??? success "Solution to Exercise 7"
    **Why grid-based methods are intractable.**

    The CVA problem has $d = 20$ risk factors (e.g., interest rates in multiple currencies, FX rates, credit spreads). A finite difference or finite element method would require a grid in $\mathbb{R}^{20}$. With $M = 10$ grid points per dimension, the total number of grid points is $M^d = 10^{20}$. At 8 bytes per point, this requires $8 \times 10^{20}$ bytes $= 8 \times 10^8$ TB of storage. This is completely impossible. Even $M = 3$ points per dimension gives $3^{20} \approx 3.5 \times 10^9$ points, which is barely feasible in terms of storage but requires solving a system of $3.5 \times 10^9$ equations at each time step.

    **Setting up the Deep BSDE problem.**

    *Forward process.* The $d = 20$ risk factors $X_t = (X_t^{(1)}, \ldots, X_t^{(20)})$ evolve under the risk-neutral measure:

    $$
    dX_t^{(i)} = \mu^{(i)}(t, X_t) \, dt + \sum_{j=1}^{m} \sigma^{(i,j)}(t, X_t) \, dW_t^{(j)}
    $$

    where $\mu$ and $\sigma$ depend on the specific models for each risk factor (e.g., Hull-White for interest rates, GBM for FX rates). The Brownian motions $W^{(1)}, \ldots, W^{(m)}$ may be correlated.

    *BSDE driver.* The CVA adjustment enters as a nonlinear driver:

    $$
    f(t, X_t, Y_t, Z_t) = -rY_t + \lambda_C(t, X_t) \cdot \text{LGD} \cdot (Y_t)^+
    $$

    where:

    - $r$ is the risk-free rate (or a short rate model value)
    - $\lambda_C(t, X_t)$ is the counterparty default intensity, which may depend on the risk factors
    - $\text{LGD}$ is the loss given default (e.g., 0.6)
    - $(Y_t)^+ = \max(Y_t, 0)$ reflects that credit loss only occurs when the portfolio has positive value to us (the counterparty owes us money)

    The nonlinearity arises from $(Y_t)^+$: the CVA depends on whether the portfolio value is positive or negative, which is itself the unknown.

    *Terminal condition.* At maturity $T$ of the portfolio:

    $$
    Y_T = g(X_T) = \text{Portfolio value at time } T
    $$

    For a portfolio of derivatives, this is the sum of the terminal payoffs.

    *BSDE discretization:*

    $$
    Y_{t_{k+1}} = Y_{t_k} - f(t_k, X_{t_k}, Y_{t_k}, Z_{t_k}) \, \Delta t_k + Z_{t_k}^\top \Delta W_k
    $$

    $$
    = Y_{t_k}(1 + r\Delta t_k) - \lambda_C \cdot \text{LGD} \cdot (Y_{t_k})^+ \Delta t_k + Z_{t_k}^\top \Delta W_k
    $$

    **Financial interpretation of $Y_0$ and $Z_0$.**

    - $Y_0 = u(0, X_0)$ is the **CVA-adjusted portfolio value** at time 0. The CVA itself is the difference between the risk-free portfolio value and $Y_0$: $\text{CVA} = V_{\text{risk-free}} - Y_0$, representing the expected loss due to counterparty default.

    - $Z_0 = \sigma^\top(0, X_0) D_x u(0, X_0) \in \mathbb{R}^{20}$ represents the **sensitivity of the CVA-adjusted value to all 20 risk factors**, scaled by the diffusion coefficients. Dividing by the appropriate $\sigma$ components recovers the deltas: $\partial u / \partial X^{(i)} = Z_0^{(i)} / \sigma^{(i,i)}$. These sensitivities are essential for hedging the CVA exposure -- they tell the bank how much each risk factor affects the credit-adjusted value, enabling construction of a hedge portfolio that manages both market risk and counterparty credit risk simultaneously.
