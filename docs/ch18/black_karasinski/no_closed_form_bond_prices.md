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

Recall (see [§ Trinomial Tree Implementation](trinomial_tree_implementation.md)) that a tree is built in log-rate space with $\Delta x = \sigma\sqrt{3\Delta t}$, branching probabilities match the conditional mean and variance, and $\theta(t_k)$ is calibrated by forward induction. Bond prices follow by backward induction

$$
g(t_k, x_j) = e^{-e^{x_j}\Delta t}\left[p_u\,g(t_{k+1}, x_{j+1}) + p_m\,g(t_{k+1}, x_j) + p_d\,g(t_{k+1}, x_{j-1})\right]
$$

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

Recall (see [§ Monte Carlo Simulation](monte_carlo_simulation.md)) that exact OU simulation of $x_t = \ln r_t$ is available and the bond price estimator averages $\exp(-\int_t^T r_s\,ds)$ over $M$ paths via trapezoidal integration.

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

---

## Exercises

**Exercise 1.** Starting from the bond pricing PDE in the log-rate variable,

$$
g_t + [\theta(t) - ax]\,g_x + \frac{1}{2}\sigma^2\,g_{xx} - e^x\,g = 0
$$

attempt the affine ansatz $g(t,x) = \exp(A(t) + B(t)\,x)$ and show that it fails. Specifically, substitute the ansatz and demonstrate that the resulting equation cannot be separated into terms depending only on $t$ and terms depending only on $x$.

??? success "Solution to Exercise 1"
    We try the affine ansatz $g(t,x) = \exp(A(t) + B(t)\,x)$ in the PDE

    $$
    g_t + [\theta(t) - ax]\,g_x + \frac{1}{2}\sigma^2\,g_{xx} - e^x\,g = 0
    $$

    Computing the partial derivatives of the ansatz:

    $$
    g_t = (\dot{A} + \dot{B}\,x)\,g, \qquad g_x = B\,g, \qquad g_{xx} = B^2\,g
    $$

    Substituting into the PDE and dividing by $g$ (which is positive):

    $$
    \dot{A} + \dot{B}\,x + [\theta(t) - ax]\,B + \frac{1}{2}\sigma^2 B^2 - e^x = 0
    $$

    Collecting terms:

    $$
    \underbrace{\left(\dot{A} + \theta(t)B + \frac{1}{2}\sigma^2 B^2\right)}_{\text{function of } t \text{ only}} + \underbrace{(\dot{B} - aB)}_{\text{function of } t \text{ only}} x - e^x = 0
    $$

    For this equation to hold for all $x$, each functionally independent term must vanish separately. The functions $1$, $x$, and $e^x$ are linearly independent over any interval in $x$. Therefore we would need:

    - Coefficient of $e^x$: $-1 = 0$ --- a contradiction

    This is immediate and definitive. The discounting term $e^x g$ produces an $e^x$ that is not in the span of $\{1, x\}$ and cannot be absorbed by any choice of $A(t)$ and $B(t)$. The affine ansatz fails because the exponential discounting rate $e^x$ is incommensurate with the linear state variable $x$ used in the ansatz. In an affine model, the discounting term would be $x \cdot g$ (linear in the state), which integrates naturally with the ansatz.

---

**Exercise 2.** On a BK trinomial tree with $\Delta t = 0.5$ year, the log-rate at a node is $x_j = \ln(0.06)$, and the three successor node bond values are $g_{j+1} = 0.945$, $g_j = 0.950$, $g_{j-1} = 0.955$, with branching probabilities $p_u = 0.1667$, $p_m = 0.6667$, $p_d = 0.1667$. Compute the bond price $g(t_k, x_j)$ using the backward induction formula.

??? success "Solution to Exercise 2"
    The backward induction formula is

    $$
    g(t_k, x_j) = e^{-e^{x_j}\Delta t}\left[p_u\,g(t_{k+1}, x_{j+1}) + p_m\,g(t_{k+1}, x_j) + p_d\,g(t_{k+1}, x_{j-1})\right]
    $$

    Given values: $x_j = \ln(0.06)$, $\Delta t = 0.5$, $g_{j+1} = 0.945$, $g_j = 0.950$, $g_{j-1} = 0.955$, $p_u = p_d = 0.1667$, $p_m = 0.6667$.

    **Step 1**: Compute the expected continuation value:

    $$
    p_u \cdot g_{j+1} + p_m \cdot g_j + p_d \cdot g_{j-1} = 0.1667 \times 0.945 + 0.6667 \times 0.950 + 0.1667 \times 0.955
    $$

    $$
    = 0.15753 + 0.63337 + 0.15920 = 0.95010
    $$

    **Step 2**: Compute the one-period discount factor. The short rate at this node is $r = e^{x_j} = 0.06$:

    $$
    e^{-e^{x_j}\Delta t} = e^{-0.06 \times 0.5} = e^{-0.03} = 0.97045
    $$

    **Step 3**: Compute the bond price:

    $$
    g(t_k, x_j) = 0.97045 \times 0.95010 = 0.92200
    $$

    The bond price at this node is approximately $0.9220$.

---

**Exercise 3.** Write out the Crank-Nicolson finite difference equation for the interior node $j$ at time step $k \to k+1$, using the spatial operator $\mathcal{L}^k$ defined in the text. If $\Delta x = 0.05$, $\Delta t = 0.01$, $a = 0.10$, $\sigma = 0.20$, $\theta(t_k) = -0.25$, and $x_j = \ln(0.05)$, compute the coefficients of $g_{j-1}^{k+1}$, $g_j^{k+1}$, and $g_{j+1}^{k+1}$ on the implicit side of the scheme.

??? success "Solution to Exercise 3"
    The Crank-Nicolson scheme is

    $$
    \frac{g_j^{k+1} - g_j^k}{\Delta t} = \frac{1}{2}(\mathcal{L}^k g^k + \mathcal{L}^{k+1} g^{k+1})
    $$

    The spatial operator at time step $k$ is

    $$
    \mathcal{L}^k g_j = [\theta_k - ax_j]\frac{g_{j+1} - g_{j-1}}{2\Delta x} + \frac{\sigma^2}{2}\frac{g_{j+1} - 2g_j + g_{j-1}}{\Delta x^2} - e^{x_j}g_j
    $$

    With $\Delta x = 0.05$, $\Delta t = 0.01$, $a = 0.10$, $\sigma = 0.20$, $\theta_k = -0.25$, $x_j = \ln(0.05) \approx -2.9957$:

    Compute the drift coefficient:

    $$
    \alpha_j = \theta_k - ax_j = -0.25 - 0.10 \times (-2.9957) = -0.25 + 0.29957 = 0.04957
    $$

    Compute the auxiliary coefficients:

    $$
    \frac{\alpha_j}{2\Delta x} = \frac{0.04957}{0.10} = 0.4957
    $$

    $$
    \frac{\sigma^2}{2\Delta x^2} = \frac{0.04}{2 \times 0.0025} = \frac{0.04}{0.005} = 8.000
    $$

    $$
    e^{x_j} = 0.05
    $$

    The operator acting on node $j$ gives coefficients for $g_{j-1}$, $g_j$, $g_{j+1}$:

    $$
    c_{j-1} = -\frac{\alpha_j}{2\Delta x} + \frac{\sigma^2}{2\Delta x^2} = -0.4957 + 8.000 = 7.504
    $$

    $$
    c_j = -\frac{\sigma^2}{\Delta x^2} - e^{x_j} = -16.000 - 0.05 = -16.050
    $$

    $$
    c_{j+1} = \frac{\alpha_j}{2\Delta x} + \frac{\sigma^2}{2\Delta x^2} = 0.4957 + 8.000 = 8.496
    $$

    Rearranging Crank-Nicolson to isolate the implicit (time $k+1$) side:

    $$
    g_j^{k+1} - \frac{\Delta t}{2}\mathcal{L}^{k+1}g^{k+1} = g_j^k + \frac{\Delta t}{2}\mathcal{L}^k g^k
    $$

    The implicit-side coefficients for $g_{j-1}^{k+1}$, $g_j^{k+1}$, $g_{j+1}^{k+1}$ are:

    $$
    -\frac{\Delta t}{2}c_{j-1} = -\frac{0.01}{2}(7.504) = -0.03752
    $$

    $$
    1 - \frac{\Delta t}{2}c_j = 1 - \frac{0.01}{2}(-16.050) = 1 + 0.08025 = 1.08025
    $$

    $$
    -\frac{\Delta t}{2}c_{j+1} = -\frac{0.01}{2}(8.496) = -0.04248
    $$

    The implicit-side equation at node $j$ is

    $$
    -0.03752\,g_{j-1}^{k+1} + 1.08025\,g_j^{k+1} - 0.04248\,g_{j+1}^{k+1} = \text{(explicit-side terms)}
    $$

---

**Exercise 4.** Using the short-maturity expansion

$$
P(t,T) \approx 1 - r_t\,\tau + \frac{1}{2}\left(r_t^2 + r_t\left[\theta(t) - a\ln r_t + \frac{1}{2}\sigma^2\right]\right)\tau^2
$$

compute $P(t,T)$ for $r_t = 5\%$, $\tau = 0.25$ year, $\theta(t) = -0.25$, $a = 0.10$, and $\sigma = 0.20$. Compare this with the naive approximation $e^{-r_t \tau}$ and quantify the difference.

??? success "Solution to Exercise 4"
    With $r_t = 0.05$, $\tau = 0.25$, $\theta(t) = -0.25$, $a = 0.10$, $\sigma = 0.20$:

    **Short-maturity expansion**:

    $$
    P(t,T) \approx 1 - r_t\tau + \frac{1}{2}\left(r_t^2 + r_t\left[\theta(t) - a\ln r_t + \frac{1}{2}\sigma^2\right]\right)\tau^2
    $$

    Computing the bracketed terms:

    $$
    \ln r_t = \ln(0.05) = -2.9957
    $$

    $$
    \theta(t) - a\ln r_t + \frac{1}{2}\sigma^2 = -0.25 - 0.10 \times (-2.9957) + 0.02 = -0.25 + 0.29957 + 0.02 = 0.06957
    $$

    $$
    r_t \times 0.06957 = 0.05 \times 0.06957 = 0.003479
    $$

    $$
    r_t^2 = 0.0025
    $$

    $$
    r_t^2 + r_t[\cdots] = 0.0025 + 0.003479 = 0.005979
    $$

    Now assembling the expansion:

    $$
    P \approx 1 - 0.05 \times 0.25 + \frac{1}{2}(0.005979)(0.0625)
    $$

    $$
    = 1 - 0.01250 + 0.000187 = 0.98769
    $$

    **Naive approximation**:

    $$
    e^{-r_t\tau} = e^{-0.0125} = 0.98758
    $$

    **Difference**:

    $$
    P_{\text{expansion}} - e^{-r_t\tau} = 0.98769 - 0.98758 = 0.00011
    $$

    The model-specific correction adds approximately 1.1 basis points to the bond price. This correction arises from the drift and volatility terms in the BK dynamics and represents the convexity adjustment for the stochastic path of rates over the short period $[t, T]$. For a 3-month maturity, the difference is small, validating the use of the naive approximation $e^{-r_t\tau}$ as a quick estimate.

---

**Exercise 5.** A cap with 40 quarterly caplets must be calibrated. Each calibration iteration requires pricing all 40 caplets, and convergence takes 100 iterations. If one trinomial tree bond price takes $1$ ms and one affine-model bond price takes $1$ ns, compute the total calibration time for both the BK model and an affine model (e.g., CIR). Express the ratio.

??? success "Solution to Exercise 5"
    A cap with 40 quarterly caplets requires pricing 40 caplet payoffs. Each caplet pricing involves a bond price computation (for the LIBOR rate at the reset date) and the backward induction of the caplet payoff. Each calibration iteration prices all 40 caplets, and convergence requires 100 iterations.

    **Total number of bond price evaluations**: $40 \times 100 = 4{,}000$.

    **BK model (trinomial tree)**: Each bond price takes 1 ms.

    $$
    \text{Time}_{BK} = 4{,}000 \times 1\text{ ms} = 4{,}000\text{ ms} = 4\text{ seconds}
    $$

    **Affine model (e.g., CIR)**: Each bond price takes 1 ns.

    $$
    \text{Time}_{\text{affine}} = 4{,}000 \times 1\text{ ns} = 4{,}000\text{ ns} = 4 \times 10^{-6}\text{ seconds} = 4\text{ microseconds}
    $$

    **Ratio**:

    $$
    \frac{\text{Time}_{BK}}{\text{Time}_{\text{affine}}} = \frac{4\text{ s}}{4 \times 10^{-6}\text{ s}} = 10^6
    $$

    The BK calibration is approximately one million times slower than the affine model calibration. In absolute terms, the BK calibration takes 4 seconds, which is acceptable for a daily calibration but would be prohibitive if repeated thousands of times (e.g., in a nested simulation for CVA). The affine model calibration at 4 microseconds is essentially instantaneous and can be run in real time.

---

**Exercise 6.** In the log-normal approximation, $P(t,T) \approx \exp(-\mu_Y + \frac{1}{2}\sigma_Y^2)$ where $Y = \int_t^T r_s\,ds$. Show that this approximation is exact when $Y$ is Gaussian (as would be the case if $r_s$ were a Gaussian process). For the BK model, explain why $Y$ is not Gaussian and discuss the sign of the error introduced by this approximation for typical parameter values.

??? success "Solution to Exercise 6"
    The approximation $P(t,T) \approx \exp(-\mu_Y + \frac{1}{2}\sigma_Y^2)$ is the moment-generating function of $Y$ evaluated at $\lambda = 1$, under the assumption that $Y$ is Gaussian.

    **Exactness for Gaussian $Y$**: If $Y \sim \mathcal{N}(\mu_Y, \sigma_Y^2)$, then by the standard Gaussian MGF:

    $$
    \mathbb{E}[e^{-Y}] = \exp\!\left(-\mu_Y + \frac{1}{2}\sigma_Y^2\right)
    $$

    This is exact, not an approximation. In the Vasicek/Hull-White model, $r_s$ is Gaussian, so $Y = \int_t^T r_s\,ds$ (an integral of a Gaussian process) is Gaussian, and the formula gives the exact bond price.

    **Why $Y$ is not Gaussian in BK**: In the BK model, $r_s = e^{x_s}$ where $x_s$ is Gaussian. The integral $Y = \int_t^T e^{x_s}\,ds$ is a sum of log-normal random variables. The sum (integral) of log-normal random variables is not log-normal, and certainly not Gaussian. The distribution of $Y$ has:

    - A heavier right tail than Gaussian (inherited from the log-normal $r_s$)
    - Right skewness (since $e^{x_s}$ is right-skewed)
    - A support bounded below (since $Y > 0$)

    **Sign of the error**: The log-normal approximation uses only the first two moments ($\mu_Y$, $\sigma_Y^2$) and assumes Gaussian tails. For the bond price $\mathbb{E}[e^{-Y}]$, the function $e^{-Y}$ is convex and decreasing. The true distribution of $Y$ has a heavier right tail than the Gaussian with the same mean and variance. Paths with very large $Y$ (high integrated rates) contribute negligibly to $\mathbb{E}[e^{-Y}]$ (since $e^{-Y} \approx 0$ for large $Y$), while the heavier right tail of the true distribution moves probability mass away from moderate values of $Y$ where $e^{-Y}$ is significant. The net effect is that the Gaussian approximation typically **overestimates** the bond price (underestimates the integrated rate's impact), because it underweights the heavy-tailed scenarios. The error is small for short maturities and moderate volatilities but grows with $\sigma$ and $T$.

---

**Exercise 7.** Compare the boundary conditions for the finite difference PDE solver: $g \approx 1$ at $x_{\min}$ (very low rates) and $g \approx 0$ at $x_{\max}$ (very high rates). Justify these conditions economically. What happens to the bond price as $r_t \to 0$? What happens as $r_t \to \infty$? How should $x_{\min}$ and $x_{\max}$ be chosen relative to the model parameters $a$, $\sigma$, and $\theta(t)$ to ensure negligible truncation error?

??? success "Solution to Exercise 7"
    **Boundary condition at $x_{\min}$ ($g \approx 1$)**: When $x = x_{\min}$ is very negative, the short rate is $r = e^{x_{\min}} \approx 0$. With near-zero interest rates, there is essentially no discounting between $t$ and $T$:

    $$
    P(t,T) = \mathbb{E}\!\left[\exp\!\left(-\int_t^T r_s\,ds\right)\right] \approx \mathbb{E}[e^0] = 1
    $$

    Economically, a zero interest rate means money has no time value, so a bond paying \$1 at maturity is worth \$1 today. Furthermore, with strong mean reversion, even if the rate starts very low, it will revert toward the mean, but the discounting effect during the period when $r$ is near zero contributes negligibly to $\int r_s\,ds$.

    **Boundary condition at $x_{\max}$ ($g \approx 0$)**: When $x = x_{\max}$ is very large, the short rate $r = e^{x_{\max}}$ is enormous. The discount factor $\exp(-\int_t^T r_s\,ds)$ is dominated by the initial high rate:

    $$
    \int_t^T r_s\,ds \geq r_t \cdot \epsilon \text{ for some positive duration}
    $$

    For very high $r_t$, this integral is huge, and $e^{-\int r_s\,ds} \approx 0$. Economically, extremely high interest rates mean money has enormous time value, so a future payment of \$1 is worth essentially nothing today.

    **Choosing $x_{\min}$ and $x_{\max}$**: The boundaries should be placed where the probability of the log rate reaching them is negligible. The long-run distribution of $x_t$ is approximately $\mathcal{N}(\theta/a, \sigma^2/(2a))$, with standard deviation $\sigma/\sqrt{2a}$. A standard choice is

    $$
    x_{\min} = \frac{\theta}{a} - n_{\text{sd}} \cdot \frac{\sigma}{\sqrt{2a}}, \qquad x_{\max} = \frac{\theta}{a} + n_{\text{sd}} \cdot \frac{\sigma}{\sqrt{2a}}
    $$

    where $n_{\text{sd}}$ is the number of standard deviations (typically 4--6). With $n_{\text{sd}} = 5$, the probability of reaching the boundary is less than $3 \times 10^{-7}$ per time step, ensuring negligible truncation error. If $\theta(t)$ varies, use the extremes of $\theta(t)/a$ over the time horizon and add the appropriate volatility buffer. The grid should also be wide enough that the boundary condition errors (from approximating $g$ as exactly 0 or 1 at the boundary) do not propagate significantly into the interior solution region.
