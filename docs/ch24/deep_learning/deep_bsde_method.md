# Deep BSDE Method

The **Deep BSDE method**, introduced by E, Han, and Jentzen (2017), reformulates the numerical solution of high-dimensional partial differential equations as a stochastic optimization problem. By exploiting the connection between parabolic PDEs and backward stochastic differential equations (BSDEs) via the Feynman-Kac theorem, and parameterizing the unknown gradient process with neural networks, this approach solves problems in 100+ dimensions that are completely intractable for grid-based methods.

---

## From PDEs to BSDEs: The Feynman-Kac Connection

### The Semilinear Parabolic PDE

Consider the semilinear parabolic PDE on $[0,T] \times \mathbb{R}^d$:

$$
\frac{\partial u}{\partial t}(t,x) + \frac{1}{2}\operatorname{tr}\!\left[\sigma\sigma^\top(t,x)\,D^2_x u(t,x)\right] + \mu(t,x)^\top D_x u(t,x) + f\!\left(t, x, u(t,x), \sigma^\top(t,x)\,D_x u(t,x)\right) = 0
$$

with terminal condition $u(T,x) = g(x)$, where $D_x u$ denotes the gradient and $D^2_x u$ the Hessian.

This PDE arises throughout quantitative finance:

- **Black-Scholes PDE** for multi-asset derivatives ($d$ assets)
- **Hamilton-Jacobi-Bellman equations** for optimal control
- **Pricing under counterparty risk** (CVA/DVA computations)

### The Associated BSDE

**Theorem (Nonlinear Feynman-Kac).** Under regularity conditions, the PDE solution $u(t,x)$ is connected to the BSDE:

$$
Y_t = g(X_T) + \int_t^T f(s, X_s, Y_s, Z_s) \, ds - \int_t^T Z_s^\top \, dW_s
$$

where the forward process satisfies:

$$
dX_s = \mu(s, X_s) \, ds + \sigma(s, X_s) \, dW_s, \quad X_t = x
$$

The relationship is:

$$
Y_s = u(s, X_s), \quad Z_s = \sigma^\top(s, X_s) \, D_x u(s, X_s)
$$

The pair $(Y, Z)$ is the unknown. $Y$ gives the PDE solution along the forward path, and $Z$ gives the (scaled) gradient. Solving the BSDE is equivalent to solving the PDE.

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

---

**Exercise 2.** The Deep BSDE loss function is $\mathcal{L}(\Theta) = \mathbb{E}[|Y_{t_N}^\Theta - g(X_{t_N})|^2]$. Explain why minimizing this loss over parameters $\Theta = (Y_0, \theta_0, \ldots, \theta_{N-1})$ produces both the PDE solution $u(0, x_0) = Y_0$ and the gradient process $Z_{t_k} = \mathcal{Z}_{\theta_k}(t_k, X_{t_k})$. What value should the loss converge to if the neural networks can perfectly represent the true gradient?

---

**Exercise 3.** The convergence bound states $|\hat{u}(0,x_0) - u(0,x_0)|^2 \le C(\Delta t + \delta^2)$ where $\Delta t$ is the time step and $\delta$ the network approximation error. If $T = 1$ year and $N = 50$ time steps, compute $\Delta t$. Discuss qualitatively how increasing the network width affects $\delta$ (via universal approximation), and why neither error term depends exponentially on dimension $d$. Why is this dimension independence the key advantage over finite difference methods?

---

**Exercise 4.** Consider using the Deep BSDE method for a 10-asset basket option pricing problem. The forward SDE in log-coordinates is $dX_t^{(i)} = (r - \sigma_i^2/2)dt + \sigma_i dW_t^{(i)}$ for $i = 1,\ldots,10$. Describe the input and output dimensions of the neural network $\mathcal{Z}_{\theta_k}$ at each time step. If each hidden layer has 20 neurons and there are 2 hidden layers, estimate the total number of parameters per sub-network. With $N = 50$ time steps and unshared networks, how many total parameters are there?

---

**Exercise 5.** The Deep BSDE method for a nonlinear PDE with driver $f(t, x, y, z) = y - y^3$ (Allen-Cahn equation) involves the update $Y_{t_{k+1}} = Y_{t_k} - (Y_{t_k} - Y_{t_k}^3)\Delta t_k + Z_{t_k}^\top \Delta W_k$. Explain why standard Monte Carlo cannot solve this PDE (since it requires an expectation under a nonlinear Feynman-Kac formula). How does the Deep BSDE method handle the nonlinearity through the forward simulation? In what financial application does a similar nonlinear driver arise?

---

**Exercise 6.** Compare the shared and unshared network architectures for the Deep BSDE method. In the shared architecture, a single network $\mathcal{Z}_\theta(t, x)$ is used for all time steps with time $t$ as an additional input. In the unshared architecture, each time step has its own network $\mathcal{Z}_{\theta_k}(x)$. Discuss the tradeoffs in terms of: (a) total number of parameters, (b) ability to capture time-varying gradient structure, (c) generalization performance, and (d) training time. Which architecture would you recommend for a long-dated (30-year) problem with $N = 120$ quarterly steps?

---

**Exercise 7.** A financial application of the Deep BSDE method is computing CVA for a multi-currency portfolio with $d = 20$ risk factors. The semilinear PDE includes the nonlinear driver $f(v) = \lambda_C \cdot \text{LGD} \cdot v^+$. Explain why this is intractable with grid-based PDE methods. Describe how you would set up the Deep BSDE problem: define the forward process, the BSDE driver, and the terminal condition. What does $Y_0$ represent financially, and what does $Z_0$ represent?
