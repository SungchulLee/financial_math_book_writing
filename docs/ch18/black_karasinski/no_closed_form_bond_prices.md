# No Closed-Form Bond Prices

In the Vasicek, Hull-White, and CIR models, zero-coupon bond prices can be written as explicit functions of the model parameters and the current short rate. The Black-Karasinski model offers no such luxury. As established in the non-affine structure section, the $r\ln r$ drift and $r^2$ diffusion terms in the BK dynamics prevent the bond pricing PDE from admitting an exponential-affine solution. This section examines the numerical methods required to compute BK bond prices, compares their accuracy and computational cost, and presents asymptotic approximations that provide useful intuition even without exact formulas.

---

## The bond pricing problem

Under the risk-neutral measure, the BK zero-coupon bond price is

$$
P(t,T) = \mathbb{E}^{\mathbb{Q}}\!\left[\exp\!\left(-\int_t^T r_s\,ds\right)\,\bigg|\,\mathcal{F}_t\right]
$$

where $r_s = e^{x_s}$ and $x_s$ solves $dx_s = [\theta(s) - ax_s]\,dt + \sigma\,dW_s$. The expectation cannot be evaluated in closed form because the integral $\int_t^T e^{x_s}\,ds$ couples the exponential nonlinearity of $r = e^x$ with the stochastic path of $x_s$.

In the log-rate variable $x = \ln r$, the bond pricing PDE is

$$
g_t + [\theta(t) - ax]\,g_x + \frac{1}{2}\sigma^2\,g_{xx} - e^x\,g = 0, \qquad g(T, x) = 1
$$

The term $e^x g$ --- the discounting term --- is the fundamental obstruction. There is no transformation that linearizes $e^x$ and simultaneously maintains the Gaussian structure of the $x$-dynamics.

---

## Numerical method 1: trinomial tree

The most widely used method for BK bond pricing is the **trinomial tree** (Hull-White tree adapted for log-normal rates). The tree discretizes both time and the log-rate space.

### Construction

1. Build a tree for $x = \ln r$ with time steps $\Delta t$ and log-rate steps $\Delta x = \sigma\sqrt{3\Delta t}$
2. At each node, compute branching probabilities (up, middle, down) that match the conditional mean and variance of $x_{t+\Delta t}$
3. Calibrate $\theta(t_k)$ at each time step to match the observed discount factor $P^{\text{mkt}}(0, t_k)$

### Bond pricing on the tree

To price a bond maturing at $T$:

1. Set all terminal nodes at time $T$ to value $1$
2. Roll backward through the tree: at each node $(t_k, x_j)$, the bond price is the discounted expected value

$$
g(t_k, x_j) = e^{-e^{x_j}\Delta t}\left[p_u\,g(t_{k+1}, x_{j+1}) + p_m\,g(t_{k+1}, x_j) + p_d\,g(t_{k+1}, x_{j-1})\right]
$$

where $p_u, p_m, p_d$ are the branching probabilities and $e^{x_j}$ is the short rate at node $j$.

**Convergence**: $O(\Delta t)$ for standard trees, $O(\Delta t^2)$ with Richardson extrapolation.

---

## Numerical method 2: finite differences

The PDE in the log-rate variable can be solved by standard finite difference methods.

### Crank-Nicolson scheme

Discretize the spatial domain $x \in [x_{\min}, x_{\max}]$ with $N_x$ points and time with $N_t$ steps. The Crank-Nicolson (implicit-explicit average) scheme for the BK PDE is

$$
\frac{g_j^{k+1} - g_j^k}{\Delta t} = \frac{1}{2}\left(\mathcal{L}^k g^k + \mathcal{L}^{k+1} g^{k+1}\right)
$$

where $\mathcal{L}^k$ is the spatial operator at time step $k$:

$$
\mathcal{L}^k g_j = [\theta(t_k) - ax_j]\frac{g_{j+1} - g_{j-1}}{2\Delta x} + \frac{\sigma^2}{2}\frac{g_{j+1} - 2g_j + g_{j-1}}{\Delta x^2} - e^{x_j}g_j
$$

**Boundary conditions**: At $x_{\min}$ (very low rates), $P \approx 1$; at $x_{\max}$ (very high rates), $P \approx 0$.

**Convergence**: $O(\Delta t^2 + \Delta x^2)$ for Crank-Nicolson, unconditionally stable.

!!! tip "Finite differences vs trees"
    Finite differences offer higher-order convergence and systematic grid refinement. Trees are simpler to implement and naturally handle the calibration of $\theta(t)$ through forward induction. For production systems, finite differences with adaptive grids are often preferred; for teaching and prototyping, trees are more transparent.

---

## Numerical method 3: Monte Carlo

Monte Carlo simulation generates paths of $x_t = \ln r_t$ (which is Gaussian, making simulation straightforward) and averages the discounted payoffs.

### Path simulation

Since $x_t$ follows an OU process, exact simulation is available:

$$
x_{t+\Delta t} = x_t\,e^{-a\Delta t} + \frac{\theta(t)}{a}(1 - e^{-a\Delta t}) + \sigma\sqrt{\frac{1 - e^{-2a\Delta t}}{2a}}\,Z
$$

where $Z \sim \mathcal{N}(0,1)$. The short rate is then $r_t = e^{x_t}$.

### Bond price estimator

$$
\hat{P}(t,T) = \frac{1}{M}\sum_{m=1}^M \exp\!\left(-\sum_{k=0}^{N-1}\frac{e^{x_{t_k}^{(m)}} + e^{x_{t_{k+1}}^{(m)}}}{2}\,\Delta t_k\right)
$$

**Convergence**: $O(1/\sqrt{M})$ statistical error plus $O(\Delta t^2)$ discretization error (with trapezoidal rule).

---

## Asymptotic approximations

Although no exact formula exists, useful approximations can be derived.

### Short-maturity expansion

For small $\tau = T - t$, expand $P(t,T)$ in powers of $\tau$:

$$
P(t,T) = 1 - r_t\,\tau + \frac{1}{2}\left(r_t^2 + r_t\left[\theta(t) - a\ln r_t + \frac{1}{2}\sigma^2\right]\right)\tau^2 + O(\tau^3)
$$

The first two terms match the general short-rate expansion $P \approx e^{-r_t\tau}$. The third term introduces model-specific corrections from the drift and volatility.

### Log-normal approximation

For moderate maturities, one can approximate the bond price by assuming the integral $\int_t^T r_s\,ds$ is approximately log-normal. If $Y = \int_t^T r_s\,ds$ has mean $\mu_Y$ and variance $\sigma_Y^2$, then

$$
P(t,T) = \mathbb{E}[e^{-Y}] \approx \exp\!\left(-\mu_Y + \frac{1}{2}\sigma_Y^2\right)
$$

The moments $\mu_Y$ and $\sigma_Y^2$ can be computed from the conditional moments of the CIR or BK process. This approximation captures the convexity correction but is only accurate for moderate maturities and volatilities.

---

## Computational cost comparison

| Method | Cost per bond price | Accuracy | Calibration |
|--------|:------------------:|:--------:|:-----------:|
| Affine formula (Vasicek/CIR) | $O(1)$ | Exact | Analytical |
| Trinomial tree | $O(N_t \cdot N_x)$ | $O(\Delta t)$ | Forward induction |
| Finite differences | $O(N_t \cdot N_x)$ | $O(\Delta t^2 + \Delta x^2)$ | Iterative |
| Monte Carlo | $O(M \cdot N_t)$ | $O(1/\sqrt{M})$ | Iterative |

The computational cost of BK bond pricing is orders of magnitude higher than for affine models. A single bond price that takes nanoseconds with the CIR formula requires milliseconds on a tree. This cost multiplies for derivative pricing (which requires many bond prices) and calibration (which requires many derivative prices).

!!! warning "The speed penalty is real"
    For a cap with 40 caplets, each requiring a bond price, and calibration requiring 100 iterations of 40 cap prices: the total is $\sim 4000$ bond prices per calibration. With trees this takes seconds; with CIR formulas, microseconds. For real-time risk management, this speed difference matters.

---

## Summary

The Black-Karasinski model requires numerical methods for bond pricing because the non-affine structure prevents closed-form solutions. The three standard approaches --- trinomial trees, finite differences, and Monte Carlo --- offer different tradeoffs between accuracy, speed, and ease of calibration. Trees are the most common in practice due to their natural integration with the forward-induction calibration of $\theta(t)$. Finite differences provide higher-order convergence, while Monte Carlo handles path-dependent products. Asymptotic approximations offer quick estimates for short maturities but lack the accuracy needed for precision pricing. The computational cost of BK bond pricing, while manageable with modern hardware, is orders of magnitude higher than for affine models and represents the practical price of non-negativity and exact term structure fitting.
