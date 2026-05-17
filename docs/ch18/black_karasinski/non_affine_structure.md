# Non-Affine Structure and Consequences

The Vasicek, Hull-White, and CIR models all belong to the **affine** class of term structure models, where zero-coupon bond prices take the exponential-affine form $P(t,T) = A(\tau)e^{-B(\tau)r_t}$. This structure enables closed-form pricing of bonds, bond options, caps, and swaptions. The Black-Karasinski model breaks this pattern: the nonlinear dependence of the drift on $\ln r$ prevents the bond pricing PDE from admitting an exponential-affine solution. Understanding precisely why the affine structure fails --- and what consequences follow --- is essential for appreciating both the limitations and the compensating advantages of the BK model.

---

## Definition of affine term structure models

A short-rate model is called **affine** if the drift and squared diffusion coefficient are both affine (linear plus constant) functions of the state variable $r_t$:

$$
\mu(t, r) = \alpha_0(t) + \alpha_1(t)\,r
$$

$$
\sigma^2(t, r) = \beta_0(t) + \beta_1(t)\,r
$$

where $\alpha_0, \alpha_1, \beta_0, \beta_1$ are deterministic functions of time. Under this condition, the bond pricing PDE

$$
f_t + \mu(t,r)\,f_r + \frac{1}{2}\sigma^2(t,r)\,f_{rr} - r\,f = 0
$$

admits a solution of the form $f(t,r) = A(\tau)\,e^{-B(\tau)\,r}$, and the functions $A(\tau)$ and $B(\tau)$ satisfy ordinary differential equations.

### Examples of affine models

| Model | $\mu(t,r)$ | $\sigma^2(t,r)$ | Affine? |
|-------|------------|------------------|:-------:|
| Vasicek | $\kappa(\theta - r)$ | $\sigma^2$ | Yes |
| Hull-White | $\theta(t) - ar$ | $\sigma^2$ | Yes |
| CIR | $\kappa(\theta - r)$ | $\sigma^2 r$ | Yes |
| Black-Karasinski | $r[\theta(t) - a\ln r + \frac{1}{2}\sigma^2]$ | $\sigma^2 r^2$ | **No** |

---

## Why Black-Karasinski is not affine

Recall (see [§ Log-Normal Short Rate SDE](log_normal_short_rate_sde.md)) the BK short rate dynamics

$$
dr_t = r_t\!\left[\theta(t) - a\ln r_t + \frac{1}{2}\sigma^2\right]dt + \sigma\,r_t\,dW_t
$$

Comparing with the affine requirements:

**Drift**: $\mu(t, r) = r\!\left[\theta(t) - a\ln r + \frac{1}{2}\sigma^2\right]$. This contains the term $r\ln r$, which is not affine in $r$. No choice of $\alpha_0(t)$ and $\alpha_1(t)$ can represent $r\ln r$ as $\alpha_0 + \alpha_1 r$.

**Squared diffusion**: $\sigma^2(t,r) = \sigma^2 r^2$. This is quadratic in $r$, not affine. The affine condition requires $\sigma^2(t,r) = \beta_0(t) + \beta_1(t)\,r$, which cannot accommodate $r^2$.

Both conditions fail simultaneously. The BK model is therefore **doubly non-affine**: both the drift and the diffusion violate the affine requirements.

---

## The BK bond pricing PDE

Substituting the BK dynamics into the general bond pricing PDE:

$$
f_t + r\!\left[\theta(t) - a\ln r + \frac{1}{2}\sigma^2\right]f_r + \frac{1}{2}\sigma^2 r^2\,f_{rr} - r\,f = 0
$$

with terminal condition $f(T, r) = 1$.

### Attempting the affine ansatz

Suppose we try $f(t,r) = A(\tau)\,e^{-B(\tau)\,r}$. Then $f_r = -B\,f$ and $f_{rr} = B^2\,f$. Substituting:

$$
\left[-\frac{A'}{A} + B'\,r\right] + r\!\left[\theta(t) - a\ln r + \frac{1}{2}\sigma^2\right](-B) + \frac{1}{2}\sigma^2 r^2\,B^2 - r = 0
$$

This expression contains terms $r\ln r$ (from the drift) and $r^2$ (from the diffusion), neither of which can be absorbed into the coefficient-matching structure that separates powers of $r$. The ansatz fails --- there is no way to split the equation into independent functions of $\tau$ and $r$.

!!! warning "No exponential-affine solution exists"
    The failure of the affine ansatz is not a matter of insufficient cleverness. The $r\ln r$ and $r^2$ terms create a fundamental obstruction: the PDE cannot be reduced to a system of ODEs for any ansatz of the form $A(\tau)\,e^{-B(\tau)\,g(r)}$ with $g$ polynomial in $r$.

---

## Alternative PDE formulation in log-rate

Working in the log-rate variable $x = \ln r$ simplifies the PDE. Setting $g(t, x) = f(t, e^x)$:

$$
g_t + \left[\theta(t) - ax + \frac{1}{2}\sigma^2\right]g_x - \frac{1}{2}\sigma^2\,g_x + \frac{1}{2}\sigma^2\,g_{xx} - e^x\,g = 0
$$

which simplifies to

$$
g_t + \left[\theta(t) - ax\right]g_x + \frac{1}{2}\sigma^2\,g_{xx} - e^x\,g = 0
$$

The obstruction is now concentrated in the single term $e^x g$: the discounting rate $r = e^x$ is a nonlinear function of the state variable $x$. In an affine model (Vasicek or Hull-White), the discounting term would be $x\,g$ (linear in $x$), which is compatible with the exponential-affine ansatz. The exponential $e^x$ prevents separation.

---

## Consequences for derivative pricing

The non-affine structure has cascading consequences.

### No closed-form bond prices

The bond pricing PDE must be solved numerically (by finite differences, trees, or Monte Carlo). There is no formula analogous to $P(t,T) = A(\tau)e^{-B(\tau)r_t}$.

### No closed-form bond options

Since bond prices are not available in closed form, bond option formulas (which require the distribution of bond prices) are also unavailable. The CIR chi-squared formula and the Vasicek/Hull-White Gaussian formula have no BK analogue.

### No closed-form caps or swaptions

Caps and swaptions, which decompose into bond options, inherit the numerical requirement.

### Jamshidian decomposition still applies

Jamshidian's trick requires only that bond prices are monotone in the short rate, which holds for BK. The decomposition of a swaption into bond options remains valid, but each bond option must be priced numerically.

### Calibration is iterative

The time-dependent drift $\theta(t)$ cannot be extracted by a single analytical formula (as in Hull-White). Instead, $\theta(t)$ is calibrated iteratively, typically by forward induction on a trinomial tree.

---

## What the BK model gains

Despite losing analytical tractability, the BK model offers:

1. **Strict positivity**: Rates are always positive, which is essential for certain products and markets
2. **Exact term structure fit**: The time-dependent $\theta(t)$ matches the initial yield curve exactly
3. **Log-normal rate distribution**: The heavy right tail better captures the empirical distribution of rates in high-rate environments
4. **Flexible volatility structure**: The multiplicative noise $\sigma r$ produces rate-level-dependent volatility, matching the empirical observation that rate volatility increases with the level

!!! tip "The affine-tractability tradeoff"
    The choice between affine models (Vasicek, Hull-White, CIR) and non-affine models (Black-Karasinski) reflects a fundamental tradeoff: analytical formulas enable fast pricing and transparent calibration, while non-affine models offer richer distributional properties and positivity constraints. The "right" choice depends on the application: for vanilla products where speed matters, affine models dominate; for portfolios sensitive to the rate distribution (e.g., mortgage-backed securities), BK may be preferred.

---

## Summary

The Black-Karasinski model is non-affine because both its drift (containing $r\ln r$) and its squared diffusion (proportional to $r^2$) violate the affine conditions required for exponential-affine bond prices. The failure is visible in the bond pricing PDE, where the discounting term $e^x g$ (with $x = \ln r$) prevents the separation of variables that underlies all affine model solutions. As a consequence, no closed-form formulas exist for bonds, bond options, caps, or swaptions; all must be computed numerically. The BK model compensates for this loss with guaranteed positive rates, exact term structure calibration, and a log-normal rate distribution that better matches empirical behavior in certain market environments.

---

## Exercises

**Exercise 1.** Verify that the Vasicek model satisfies the affine conditions. Write the Vasicek SDE $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$ in the form $\mu(t,r) = \alpha_0 + \alpha_1 r$ and $\sigma^2(t,r) = \beta_0 + \beta_1 r$, and identify the four coefficients $\alpha_0, \alpha_1, \beta_0, \beta_1$.

??? success "Solution to Exercise 1"
    The Vasicek SDE is $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$, which can be rewritten as

    $$
    dr_t = (\kappa\theta - \kappa r_t)\,dt + \sigma\,dW_t
    $$

    The drift function is $\mu(t,r) = \kappa\theta - \kappa r$. Comparing with the affine form $\mu(t,r) = \alpha_0 + \alpha_1 r$:

    $$
    \alpha_0 = \kappa\theta, \qquad \alpha_1 = -\kappa
    $$

    The squared diffusion function is $\sigma^2(t,r) = \sigma^2$ (constant). Comparing with $\sigma^2(t,r) = \beta_0 + \beta_1 r$:

    $$
    \beta_0 = \sigma^2, \qquad \beta_1 = 0
    $$

    Both the drift and diffusion satisfy the affine conditions: the drift is affine in $r$ (linear with a constant intercept), and the squared diffusion is affine in $r$ (constant, which is a special case of affine with zero slope). Therefore, the Vasicek model is affine, and the bond pricing PDE admits the exponential-affine solution $P(t,T) = A(\tau)e^{-B(\tau)r_t}$.

---

**Exercise 2.** For the BK drift $\mu(t,r) = r[\theta(t) - a\ln r + \frac{1}{2}\sigma^2]$, show that no constants $\alpha_0(t)$ and $\alpha_1(t)$ exist such that $\mu(t,r) = \alpha_0(t) + \alpha_1(t)\,r$ for all $r > 0$. (Hint: evaluate $\mu(t,r)$ at three distinct values of $r$ and derive a contradiction.)

??? success "Solution to Exercise 2"
    Suppose for contradiction that constants $\alpha_0(t)$ and $\alpha_1(t)$ exist such that

    $$
    r[\theta(t) - a\ln r + \tfrac{1}{2}\sigma^2] = \alpha_0(t) + \alpha_1(t)\,r \quad \text{for all } r > 0
    $$

    Evaluate at three distinct values of $r$:

    **At $r = 1$**: $\ln 1 = 0$, so

    $$
    1 \cdot [\theta + \tfrac{1}{2}\sigma^2] = \alpha_0 + \alpha_1 \implies \alpha_0 + \alpha_1 = \theta + \tfrac{1}{2}\sigma^2
    $$

    **At $r = e$**: $\ln e = 1$, so

    $$
    e[\theta - a + \tfrac{1}{2}\sigma^2] = \alpha_0 + \alpha_1 e \implies \alpha_0 = e[\theta - a + \tfrac{1}{2}\sigma^2] - \alpha_1 e
    $$

    **At $r = e^2$**: $\ln(e^2) = 2$, so

    $$
    e^2[\theta - 2a + \tfrac{1}{2}\sigma^2] = \alpha_0 + \alpha_1 e^2
    $$

    From the first two equations, $\alpha_1 = \theta + \tfrac{1}{2}\sigma^2 - \alpha_0$ and $\alpha_0 = e(\theta - a + \tfrac{1}{2}\sigma^2) - \alpha_1 e$. Substituting the first into the second:

    $$
    \alpha_0 = e(\theta - a + \tfrac{1}{2}\sigma^2) - e(\theta + \tfrac{1}{2}\sigma^2 - \alpha_0) = -ea + e\alpha_0
    $$

    $$
    \alpha_0(1 - e) = -ea \implies \alpha_0 = \frac{ea}{e - 1}
    $$

    $$
    \alpha_1 = \theta + \tfrac{1}{2}\sigma^2 - \frac{ea}{e-1}
    $$

    Now check at $r = e^2$:

    $$
    e^2(\theta - 2a + \tfrac{1}{2}\sigma^2) = \frac{ea}{e-1} + \left(\theta + \tfrac{1}{2}\sigma^2 - \frac{ea}{e-1}\right)e^2
    $$

    The right side is $\frac{ea}{e-1} + e^2(\theta + \tfrac{1}{2}\sigma^2) - \frac{e^3 a}{e-1}$. The left side is $e^2(\theta + \tfrac{1}{2}\sigma^2) - 2ae^2$. Setting them equal:

    $$
    -2ae^2 = \frac{ea}{e-1} - \frac{e^3 a}{e-1} = \frac{a(e - e^3)}{e-1} = \frac{ae(1 - e^2)}{e-1} = \frac{-ae(e+1)(e-1)}{e-1} = -ae(e+1)
    $$

    So we need $2e^2 = e(e+1) = e^2 + e$, i.e., $e^2 = e$, i.e., $e = 1$. But $e \approx 2.718 \neq 1$. This is a contradiction. Therefore, no affine representation $\alpha_0(t) + \alpha_1(t)r$ of the BK drift exists.

---

**Exercise 3.** Substitute the affine ansatz $f(t,r) = A(\tau)\,e^{-B(\tau)\,r}$ into the BK bond pricing PDE

$$
f_t + r\!\left[\theta(t) - a\ln r + \tfrac{1}{2}\sigma^2\right]f_r + \tfrac{1}{2}\sigma^2 r^2\,f_{rr} - r\,f = 0
$$

and explicitly collect terms by their dependence on $r$. Show that you obtain terms proportional to $r\ln r$ and $r^2$ that cannot be eliminated, confirming the failure of the ansatz.

??? success "Solution to Exercise 3"
    Substituting $f = A(\tau)e^{-B(\tau)r}$ into the BK bond pricing PDE with $\tau = T - t$:

    Derivatives: $f_t = -(A'e^{-Br} - AB'r e^{-Br}) = (-A'/A + B'r)f$, $f_r = -Bf$, $f_{rr} = B^2 f$.

    (Here primes denote $d/d\tau$.) Substituting and dividing by $f$:

    $$
    -\frac{A'}{A} + B'r + r[\theta - a\ln r + \tfrac{1}{2}\sigma^2](-B) + \frac{1}{2}\sigma^2 r^2 B^2 - r = 0
    $$

    Rearranging:

    $$
    -\frac{A'}{A} + r\left[B' - B\theta - B\tfrac{1}{2}\sigma^2 - 1\right] + aBr\ln r + \frac{1}{2}\sigma^2 B^2 r^2 = 0
    $$

    The functions $1$, $r$, $r\ln r$, and $r^2$ are linearly independent over $r > 0$. For the equation to hold for all $r > 0$, the coefficient of each independent function must vanish:

    - Coefficient of $1$: $-A'/A = 0$, giving $A(\tau) = $ constant
    - Coefficient of $r$: $B' - B(\theta + \frac{1}{2}\sigma^2) - 1 = 0$
    - Coefficient of $r\ln r$: $aB = 0$, requiring $B = 0$ (since $a > 0$)
    - Coefficient of $r^2$: $\frac{1}{2}\sigma^2 B^2 = 0$, requiring $B = 0$

    But if $B = 0$, the coefficient-of-$r$ equation gives $-1 = 0$, which is a contradiction. The $r\ln r$ and $r^2$ terms force $B = 0$, which then makes it impossible to satisfy the $r$-coefficient equation. The ansatz fails irrecoverably.

---

**Exercise 4.** In the log-rate PDE formulation, the discounting term is $e^x g$ rather than $x\,g$. Consider a hypothetical model where the short rate is $r = x$ (the identity map, as in Vasicek). Write the corresponding bond pricing PDE and show that the exponential-affine ansatz $g(t,x) = A(\tau)\,e^{-B(\tau)\,x}$ succeeds by deriving the Riccati ODEs for $A(\tau)$ and $B(\tau)$.

??? success "Solution to Exercise 4"
    With $r = x$ (the identity), the bond pricing PDE becomes

    $$
    g_t + [\theta(t) - ax]\,g_x + \frac{1}{2}\sigma^2\,g_{xx} - x\,g = 0
    $$

    Note the discounting term is $xg$ (linear in $x$), not $e^x g$.

    Try $g(t,x) = A(\tau)e^{-B(\tau)x}$ with $\tau = T - t$:

    $$
    g_t = (-A'/A + B'x)g, \qquad g_x = -Bg, \qquad g_{xx} = B^2 g
    $$

    Substituting and dividing by $g$:

    $$
    -\frac{A'}{A} + B'x + [\theta(t) - ax](-B) + \frac{1}{2}\sigma^2 B^2 - x = 0
    $$

    Collecting by powers of $x$:

    - **$x^0$ terms**: $-A'/A - B\theta(t) + \frac{1}{2}\sigma^2 B^2 = 0$
    - **$x^1$ terms**: $B' + aB - 1 = 0$

    Both equations involve only $\tau$-dependent quantities. There is no $x\ln x$ or $x^2$ obstruction. We obtain two ODEs:

    **Riccati ODE for $B(\tau)$**:

    $$
    B'(\tau) = 1 - aB(\tau), \qquad B(0) = 0
    $$

    This has the solution $B(\tau) = \frac{1}{a}(1 - e^{-a\tau})$.

    **ODE for $A(\tau)$**: Writing $\ln A = \alpha$:

    $$
    \alpha'(\tau) = -B(\tau)\theta(\tau) + \frac{1}{2}\sigma^2 B(\tau)^2, \qquad \alpha(0) = 0
    $$

    This is integrated directly: $\alpha(\tau) = \int_0^\tau [-B(s)\theta(s) + \frac{1}{2}\sigma^2 B(s)^2]\,ds$.

    The ansatz succeeds because the discounting term $xg$ is linear in the state variable, allowing clean separation into $x^0$ and $x^1$ terms. This is exactly the affine structure of the Vasicek/Hull-White model.

---

**Exercise 5.** Explain why Jamshidian's decomposition of a coupon bond option into a portfolio of zero-coupon bond options remains valid in the BK model. What property of the function $P(t,T;r_t)$ as a function of $r_t$ is required, and why does BK satisfy it despite lacking closed-form bond prices?

??? success "Solution to Exercise 5"
    Jamshidian's decomposition applies to any one-factor short-rate model where the zero-coupon bond price $P(t,T;r_t)$ is a **monotone decreasing function** of the current short rate $r_t$ (for fixed $t$ and $T > t$).

    **Why monotonicity holds in BK**: The bond price is $P(t,T) = \mathbb{E}[\exp(-\int_t^T r_s\,ds) \mid r_t]$. A higher initial rate $r_t$ leads to (stochastically) higher future rates $r_s$ for $s > t$ due to the mean-reverting dynamics: if $r_t$ is higher, the OU process $x_t = \ln r_t$ starts from a higher level, and while it reverts toward $\theta(t)/a$, the entire path distribution is shifted upward. Higher rates along the path increase $\int_t^T r_s\,ds$, which decreases $\exp(-\int_t^T r_s\,ds)$. Therefore $P(t,T;r_t)$ is strictly decreasing in $r_t$.

    **How the decomposition works**: A European call on a coupon bond with coupon payments $c_i$ at times $T_i$ and exercise date $T_0$ has payoff $[\sum_i c_i P(T_0, T_i) - K]^+$. Since each $P(T_0, T_i; r_{T_0})$ is monotone decreasing in $r_{T_0}$, there exists a unique critical rate $r^*$ such that $\sum_i c_i P(T_0, T_i; r^*) = K$. For $r_{T_0} < r^*$, all bond prices are higher and the option is in the money; for $r_{T_0} > r^*$, the option is out of the money. The coupon bond option decomposes into a portfolio of zero-coupon bond options:

    $$
    \text{Call on coupon bond} = \sum_i c_i \cdot \text{Call on ZCB}(T_0, T_i, K_i)
    $$

    where $K_i = P(T_0, T_i; r^*)$. This decomposition is purely a consequence of monotonicity and does not require closed-form bond prices. However, each individual ZCB option must still be priced numerically (by tree or MC) in the BK model, unlike in Hull-White where analytical formulas are available.

---

**Exercise 6.** The CIR model has drift $\kappa(\theta - r)$ and squared diffusion $\sigma^2 r$. A practitioner proposes modifying CIR to $\sigma^2 r^2$ (keeping the CIR drift). Would the resulting model be affine? Justify your answer by checking both the drift and diffusion affine conditions. What key distributional property would change?

??? success "Solution to Exercise 6"
    The proposed model has drift $\mu(t,r) = \kappa(\theta - r) = \kappa\theta - \kappa r$ and squared diffusion $\sigma^2(t,r) = \sigma^2 r^2$.

    **Drift check**: $\mu(t,r) = \kappa\theta - \kappa r = \alpha_0 + \alpha_1 r$ with $\alpha_0 = \kappa\theta$ and $\alpha_1 = -\kappa$. The drift is affine in $r$. This condition is satisfied.

    **Diffusion check**: $\sigma^2(t,r) = \sigma^2 r^2$. The affine condition requires $\sigma^2(t,r) = \beta_0 + \beta_1 r$. But $\sigma^2 r^2$ is quadratic in $r$, not affine. There is no choice of $\beta_0$ and $\beta_1$ such that $\beta_0 + \beta_1 r = \sigma^2 r^2$ for all $r > 0$.

    **Conclusion**: The model is **not affine** because the diffusion condition fails. The drift alone being affine is insufficient; both conditions must hold simultaneously.

    **Distributional change**: The original CIR model with $\sigma^2 r$ diffusion produces a non-central chi-squared distribution for $r_t$, ensuring positivity via the Feller condition ($2\kappa\theta \geq \sigma^2$) and having a moderate right tail. The modified model with $\sigma^2 r^2$ diffusion makes volatility proportional to $r$ (rather than $\sqrt{r}$), which is the same multiplicative structure as in the BK model. The rate distribution would be heavier-tailed on the right (more similar to log-normal), and the positivity guarantee would need to be analyzed separately (the Feller condition no longer applies in its standard form). The model would also lose all closed-form bond pricing formulas, requiring numerical methods just like BK.

---

**Exercise 7.** Consider the practical tradeoff between affine and non-affine models. A trading desk prices 10,000 swaptions daily for risk management. Each BK tree-based swaption price takes 5 ms and each Hull-White analytical swaption price takes 0.005 ms. Compute the daily pricing time for each model. If the desk also needs to calibrate the model once per day using 200 swaption prices with 150 optimizer iterations, compute the total calibration time for each model. Under what circumstances might the BK model still be preferred despite this cost?

??? success "Solution to Exercise 7"
    **Daily pricing time**:

    - BK: $10{,}000 \times 5\text{ ms} = 50{,}000\text{ ms} = 50\text{ seconds}$
    - Hull-White: $10{,}000 \times 0.005\text{ ms} = 50\text{ ms} = 0.05\text{ seconds}$

    **Calibration time**: Each calibration iteration evaluates 200 swaption prices. With 150 iterations:

    - Total evaluations: $200 \times 150 = 30{,}000$
    - BK: $30{,}000 \times 5\text{ ms} = 150{,}000\text{ ms} = 150\text{ seconds} = 2.5\text{ minutes}$
    - Hull-White: $30{,}000 \times 0.005\text{ ms} = 150\text{ ms} = 0.15\text{ seconds}$

    **Total daily compute**:

    - BK: $50 + 150 = 200\text{ seconds} \approx 3.3\text{ minutes}$
    - Hull-White: $0.05 + 0.15 = 0.20\text{ seconds}$
    - Ratio: $200 / 0.20 = 1{,}000\times$

    **Circumstances where BK might still be preferred**:

    1. **Rate positivity requirement**: If the desk's risk framework or regulatory constraints require non-negative rates (e.g., certain insurance ALM applications), Hull-White's ability to produce negative rates is a disqualification.

    2. **Swaption smile calibration**: If the swaption market exhibits significant log-normal skew, BK can capture this naturally while Hull-White produces a flat normal smile. Better smile calibration leads to more accurate hedging.

    3. **Bermudan swaptions**: If the portfolio is dominated by Bermudan swaptions, the tree-based BK pricing is natural, and the incremental cost of using BK over Hull-White for the tree is modest (both require trees for early exercise).

    4. **Acceptable latency**: At 3.3 minutes total, BK is feasible for end-of-day risk reporting and daily P&L. The speed difference only becomes critical for intraday real-time pricing, Monte Carlo-based CVA, or interactive trading systems.

    5. **Parallelization**: The 10,000 swaption pricings are independent and can be parallelized across multiple cores. With 20 cores, BK pricing drops to $\sim$2.5 seconds for the daily portfolio, making it practical even for more frequent valuations.
