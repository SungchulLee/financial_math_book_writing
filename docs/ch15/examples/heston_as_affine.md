# Heston Model as Affine

The Heston stochastic volatility model is the most important two-dimensional affine process in quantitative finance. Its affine structure is the reason semi-closed-form option pricing formulas exist, making it the standard model for equity option markets. This section embeds the Heston model in the affine framework, derives the Riccati system, presents the characteristic function, and connects the abstract affine machinery to the concrete problem of pricing options with stochastic volatility.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Write the Heston dynamics as a two-dimensional affine process on $\mathbb{R} \times \mathbb{R}_+$
    2. Identify the affine parameters and the functions $F$ and $R$
    3. Derive the Riccati system for the Heston characteristic function
    4. State the closed-form Heston characteristic function and interpret the role of correlation

---

## Intuition

The Black-Scholes model assumes constant volatility, but observed option prices imply a volatility that varies with strike and maturity---the *volatility smile*. The Heston model captures this by making volatility itself a random process: the variance $V_t$ follows a CIR process, and the log stock price $X_t = \log S_t$ is driven by a Brownian motion correlated with the variance. The pair $(X_t, V_t)$ is a two-dimensional affine process in which $V_t$ is the CIR-type component (non-negative, driving state-dependent volatility) and $X_t$ is the Gaussian-type component (unconstrained).

The affine structure of this pair is what makes semi-analytical pricing possible: the characteristic function of $(X_T, V_T)$ has exponential-affine form, and the Riccati system reduces to a single scalar ODE in $\psi_2$ (the component associated with $V_t$) since $\psi_1$ is trivially constant.

---

## Heston Dynamics

### The Model

Under the risk-neutral measure $\mathbb{Q}$, the Heston model specifies:

$$
dS_t = r\,S_t\,dt + \sqrt{V_t}\,S_t\,dW_t^{(1)}
$$

$$
dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^{(2)}
$$

with $\operatorname{Corr}(dW_t^{(1)}, dW_t^{(2)}) = \rho\,dt$, where $\rho \in [-1, 1]$.

The parameters are:

| Symbol | Name | Typical Range |
|--------|------|---------------|
| $\kappa$ | Mean-reversion speed | $0.5$--$5$ |
| $\theta$ | Long-term variance | $0.01$--$0.1$ |
| $\xi$ | Vol-of-vol | $0.1$--$1.0$ |
| $\rho$ | Correlation | $-0.9$--$0$ |
| $V_0$ | Initial variance | $0.01$--$0.1$ |

The correlation $\rho$ is typically negative (the *leverage effect*): when the stock price drops, volatility tends to increase.

### Log-Price Dynamics

Recall (see [Itô calculus applications](../../ch03/ito_lemma/ito_calculus_applications.md)) the log-transform of GBM-type dynamics. With stochastic variance $V_t$:

$$
dX_t = \left(r - \frac{1}{2}V_t\right)dt + \sqrt{V_t}\,dW_t^{(1)}
$$

The state vector is $\mathbf{X}_t = (X_t, V_t) \in \mathbb{R} \times \mathbb{R}_+$ (canonical state space with $m = 1$, $d = 2$). For the complete model treatment, see [Heston complete model](../../ch16/index.md).

---

## Affine Parameter Identification

### Drift

$$
b(\mathbf{X}_t) = \begin{pmatrix} r - \frac{1}{2}V_t \\ \kappa(\theta - V_t) \end{pmatrix} = \underbrace{\begin{pmatrix} r \\ \kappa\theta \end{pmatrix}}_{b_0} + \underbrace{\begin{pmatrix} 0 \\ 0 \end{pmatrix}}_{b_1} X_t + \underbrace{\begin{pmatrix} -\frac{1}{2} \\ -\kappa \end{pmatrix}}_{b_2} V_t
$$

So $b_0 = (r, \kappa\theta)^\top$, $b_1 = (0, 0)^\top$, $b_2 = (-\frac{1}{2}, -\kappa)^\top$.

### Diffusion

The instantaneous covariance matrix is:

$$
a(\mathbf{X}_t) = \begin{pmatrix} V_t & \rho\xi V_t \\ \rho\xi V_t & \xi^2 V_t \end{pmatrix} = \underbrace{\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}}_{a_0} + \underbrace{\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}}_{a_1} \cdot X_t + \underbrace{\begin{pmatrix} 1 & \rho\xi \\ \rho\xi & \xi^2 \end{pmatrix}}_{a_2} \cdot V_t
$$

The entire diffusion matrix is proportional to $V_t$---it vanishes when $V_t = 0$ (consistent with the CIR boundary behavior of the variance process). There is no constant diffusion ($a_0 = 0$) and no dependence on $X_t$ ($a_1 = 0$).

### Short Rate

For option pricing on the stock, the short rate is constant: $r(\mathbf{X}_t) = r$, so $\rho_0 = r$ and $\rho_1 = (0, 0)^\top$.

---

## Functions F and R

Recall (see [characteristic function](../characteristic_function/characteristic_function.md)) the definitions of $F$ and $R_i$. For Heston:

$$
F(w) = r\,w_1 + \kappa\theta\,w_2, \qquad R_1(w) = 0
$$

$$
R_2(w) = -\frac{1}{2}w_1 - \kappa w_2 + \frac{1}{2}(w_1^2 + 2\rho\xi w_1 w_2 + \xi^2 w_2^2)
$$

The $R_1$ equation is trivial ($\psi_1' = 0$); $R_2$ is a Riccati equation in $\psi_2$.

---

## The Riccati System

### Characteristic Function Setup

For the characteristic function of the log-price $X_T$, set $u_1 = iv$, $u_2 = 0$:

$$
\psi_1'(\tau) = 0, \qquad \psi_1(0) = iv
$$

$$
\psi_2'(\tau) = R_2(\psi_1, \psi_2), \qquad \psi_2(0) = 0
$$

$$
\phi'(\tau) = F(\psi_1, \psi_2), \qquad \phi(0) = 0
$$

Since $\psi_1(\tau) = iv$ for all $\tau$, the $\psi_2$-equation becomes:

$$
\psi_2'(\tau) = -\frac{iv}{2} - \kappa\psi_2 + \frac{1}{2}(-v^2 + 2\rho\xi iv\,\psi_2 + \xi^2\psi_2^2)
$$

### Standard Form

Collecting terms:

$$
\psi_2'(\tau) = \underbrace{-\frac{1}{2}(iv + v^2)}_{\alpha} + \underbrace{(\rho\xi iv - \kappa)}_{\beta}\,\psi_2 + \underbrace{\frac{\xi^2}{2}}_{\gamma/2}\,\psi_2^2
$$

This is a scalar Riccati equation $\psi_2' = \alpha + \beta\psi_2 + \frac{\gamma}{2}\psi_2^2$ with complex coefficients.

### Solution

Define the discriminant:

$$
d = \sqrt{\beta^2 - 2\alpha\gamma} = \sqrt{(\rho\xi iv - \kappa)^2 + \xi^2(iv + v^2)}
$$

and the ratio:

$$
g = \frac{\beta - d}{\beta + d}
$$

The solution is:

$$
\psi_2(\tau) = \frac{\beta - d}{\xi^2} \cdot \frac{1 - e^{-d\tau}}{1 - g\,e^{-d\tau}}
$$

The $\phi$-function integrates to:

$$
\phi(\tau) = ivr\tau + \frac{\kappa\theta}{\xi^2}\left[(\beta - d)\tau - 2\log\!\left(\frac{1 - g\,e^{-d\tau}}{1 - g}\right)\right]
$$

---

## The Heston Characteristic Function

### Complete Formula

$$
\mathbb{E}\!\left[e^{iv X_T} \mid X_t = x, V_t = v_0\right] = \exp\!\left(\phi(\tau) + iv\,x + \psi_2(\tau)\,v_0\right)
$$

where $\phi$ and $\psi_2$ are given above, $\tau = T - t$, and $x = \log S_t$.

### Properties

1. **Bounded**: $|\Phi(\tau, v, x, v_0)| \leq 1$ for all real $v$, since $u_1 = iv$ is purely imaginary.

2. **Symmetric under $v \to -v$**: $\Phi(\tau, -v) = \overline{\Phi(\tau, v)}$ (Hermitian symmetry).

3. **Dependence on $v_0$**: The initial variance $v_0$ enters linearly through $\psi_2(\tau) v_0$. Higher $v_0$ broadens the distribution of $X_T$.

4. **Role of $\rho$**: Negative $\rho$ creates left-skew in the log-return distribution (negative skewness), producing the observed volatility skew in equity markets.

---

## The Role of Correlation

### Skew Generation

The correlation $\rho$ between the log-price and variance Brownian motions is the primary driver of the implied volatility skew. Setting $v = 0$ in the discriminant:

$$
d\big|_{v=0} = |\kappa| = \kappa
$$

For $v \neq 0$, the discriminant depends on $\rho$ through the term $\rho\xi iv$. When $\rho < 0$:

- A drop in $S_t$ ($dW^{(1)} < 0$) is associated with an increase in $V_t$ ($dW^{(2)} > 0$), amplifying the left tail
- An increase in $S_t$ ($dW^{(1)} > 0$) is associated with a decrease in $V_t$ ($dW^{(2)} < 0$), compressing the right tail

This asymmetry produces the negative skewness and the downward-sloping implied volatility curve observed in equity markets.

### Special Cases

| $\rho$ | Effect on Smile |
|--------|----------------|
| $\rho = 0$ | Symmetric smile (kurtosis only, no skew) |
| $\rho < 0$ | Downward skew (puts more expensive than calls) |
| $\rho > 0$ | Upward skew (rare in equities, possible in commodities) |

??? example "Heston Parameters and Implied Volatility"
    With $S_0 = \$100$, $r = 0.05$, $V_0 = 0.04$, $\kappa = 2$, $\theta = 0.04$, $\xi = 0.5$, $T = 1$:

    - $\rho = 0$: The implied volatility smile is symmetric around ATM with IV $\approx 20\%$.
    - $\rho = -0.7$: The smile tilts downward. OTM puts (low strikes) have IV $\approx 25\%$, OTM calls (high strikes) have IV $\approx 17\%$.

    The affine characteristic function enables computing these implied volatilities in milliseconds via Fourier inversion, making real-time calibration feasible. $\square$

---

## Admissibility and Feller Condition

For the Heston model, the admissibility conditions specialize to:

1. **Drift inward**: $(b_0)_2 = \kappa\theta > 0$ (the variance drift at $V = 0$ is positive)
2. **Diffusion vanishes**: $a_2 \cdot V_t$ vanishes when $V_t = 0$
3. **Feller condition**: $2\kappa\theta \geq \xi^2$ ensures $V_t > 0$ almost surely

When the Feller condition is violated (common in calibrated models---typical calibrations give $2\kappa\theta/\xi^2 \approx 0.3$), the variance process can reach zero. The process is still well-defined (with instantaneous reflection at $V = 0$), but the transition density has a point mass at $V = 0$ and numerical simulation requires special schemes (e.g., full truncation or the QE scheme of Andersen).

---

## Summary

The Heston model is a two-dimensional affine process on $\mathbb{R} \times \mathbb{R}_+$ with the log-price as the Gaussian component and the variance as the CIR-type component. The affine structure reduces the characteristic function computation to a scalar Riccati equation for $\psi_2(\tau)$, with $\psi_1(\tau) = iv$ constant. The closed-form solution involves a complex discriminant $d = \sqrt{(\rho\xi iv - \kappa)^2 + \xi^2(iv + v^2)}$ and produces the semi-analytical characteristic function that is the foundation of Fourier-based option pricing and real-time calibration. The correlation parameter $\rho$ controls the skewness of the return distribution and hence the slope of the implied volatility smile.

---

## Further Reading

- Heston, S. L. (1993). "A Closed-Form Solution for Options with Stochastic Volatility with Applications to Bond and Currency Options." *Review of Financial Studies*, 6(2), 327-343.
- Gatheral, J. *The Volatility Surface*. Wiley, 2006, Chapter 2.
- Albrecher, H., Mayer, P., Schoutens, W., & Tistaert, J. (2007). "The Little Heston Trap." *Wilmott Magazine*, January, 83-92.
- Andersen, L. (2008). "Simple and Efficient Simulation of the Heston Stochastic Volatility Model." *Journal of Computational Finance*, 11(3), 1-42.

---

## Exercises

**Exercise 1.** Write the Heston model in the affine form $dX_t = (b_0 + BX_t)\,dt + \sigma(X_t)\,dW_t$ by identifying the state vector $X_t = (\log S_t, V_t)^T$, the drift parameters $b_0$ and $B$, and the diffusion matrix $a(x) = a_0 + \alpha_1 x_1 + \alpha_2 x_2$. Verify that the diffusion matrix depends only on $V_t$ (the CIR-type component).

??? success "Solution to Exercise 1"
    The state vector is $\mathbf{X}_t = (X_t, V_t)^\top = (\log S_t, V_t)^\top$. The dynamics are:

    $$
    d\mathbf{X}_t = \begin{pmatrix} r - \frac{1}{2}V_t \\ \kappa(\theta - V_t) \end{pmatrix} dt + \begin{pmatrix} \sqrt{V_t} & 0 \\ \rho\xi\sqrt{V_t} & \xi\sqrt{1-\rho^2}\sqrt{V_t} \end{pmatrix} d\mathbf{W}_t
    $$

    where $\mathbf{W}_t$ is a two-dimensional standard Brownian motion. In the affine form $d\mathbf{X}_t = (b_0 + B\mathbf{X}_t)\,dt + \sigma(\mathbf{X}_t)\,d\mathbf{W}_t$:

    $$
    b_0 = \begin{pmatrix} r \\ \kappa\theta \end{pmatrix}, \qquad B = \begin{pmatrix} 0 & -\frac{1}{2} \\ 0 & -\kappa \end{pmatrix}
    $$

    The instantaneous covariance matrix $a(\mathbf{X}_t) = \sigma(\mathbf{X}_t)\sigma(\mathbf{X}_t)^\top$ is:

    $$
    a(\mathbf{X}_t) = \begin{pmatrix} V_t & \rho\xi V_t \\ \rho\xi V_t & \xi^2 V_t \end{pmatrix} = \underbrace{\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}}_{a_0} + \underbrace{\begin{pmatrix} 0 & 0 \\ 0 & 0 \end{pmatrix}}_{\alpha_1} x_1 + \underbrace{\begin{pmatrix} 1 & \rho\xi \\ \rho\xi & \xi^2 \end{pmatrix}}_{\alpha_2} x_2
    $$

    The diffusion matrix depends only on $x_2 = V_t$ (the CIR-type component), with $\alpha_1 = 0$ confirming no dependence on the log-price component. This is the defining feature of the $A_1(2)$ structure: only the CIR-type variable drives the state-dependent volatility.

---

**Exercise 2.** In the Heston Riccati system, $\psi_1(\tau) = iv$ is constant. Explain why this is the case by examining the $R_1$ function and showing that the log-price component has no state-dependent diffusion contribution ($\alpha_2 = 0$ for the log-price equation in a suitable formulation).

??? success "Solution to Exercise 2"
    The function $R_1$ associated with the first (log-price) component is:

    $$
    R_1(w) = \langle b_1, w \rangle + \frac{1}{2}\langle w, \alpha_1 w \rangle
    $$

    where $b_1 = (0, 0)^\top$ is the column of $B$ corresponding to the $X_t$-dependence of the drift, and $\alpha_1 = 0$ is the diffusion matrix associated with $X_t$.

    Since both $b_1 = 0$ and $\alpha_1 = 0$, we have $R_1(w) = 0$ for all $w$. The Riccati equation for $\psi_1$ is:

    $$
    \psi_1'(\tau) = R_1(\psi_1, \psi_2) = 0
    $$

    with initial condition $\psi_1(0) = iv$. Therefore $\psi_1(\tau) = iv$ is constant for all $\tau$.

    The underlying reason is that $X_t = \log S_t$ enters neither the drift nor the diffusion of either component in a state-dependent way. The drift of $X_t$ depends on $V_t$ (not $X_t$), and the diffusion coefficient depends on $V_t$ (not $X_t$). Thus $X_t$ is a "passive" component: it accumulates effects from $V_t$ but does not feed back into the dynamics.

---

**Exercise 3.** For the Heston model with parameters $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, $\rho = -0.7$, compute the discriminant $d = \sqrt{(\rho\xi iv - \kappa)^2 + \xi^2(iv + v^2)}$ at $v = 1$. Verify that $\operatorname{Re}(d) > 0$.

??? success "Solution to Exercise 3"
    With $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, $\rho = -0.7$, and $v = 1$:

    $$
    \beta = \rho\xi iv - \kappa = -0.7 \cdot 0.3 \cdot i - 1.5 = -1.5 - 0.21i
    $$

    $$
    \beta^2 = (-1.5 - 0.21i)^2 = 2.25 + 0.63i - 0.0441 = 2.2059 + 0.63i
    $$

    $$
    iv + v^2 = i + 1
    $$

    $$
    \xi^2(iv + v^2) = 0.09(1 + i) = 0.09 + 0.09i
    $$

    $$
    \beta^2 + \xi^2(iv + v^2) = 2.2059 + 0.63i + 0.09 + 0.09i = 2.2959 + 0.72i
    $$

    Converting to polar form to take the square root: $|z| = \sqrt{2.2959^2 + 0.72^2} = \sqrt{5.2712 + 0.5184} = \sqrt{5.7896} \approx 2.4062$ and $\arg(z) = \arctan(0.72/2.2959) \approx 0.3038$ radians.

    $$
    d = \sqrt{z} = \sqrt{2.4062}\,e^{i \cdot 0.1519} \approx 1.5512(\cos 0.1519 + i\sin 0.1519)
    $$

    $$
    \approx 1.5512(0.9885 + 0.1513i) \approx 1.5334 + 0.2347i
    $$

    Therefore $\operatorname{Re}(d) \approx 1.533 > 0$, confirming the condition for numerical stability of the Heston characteristic function formula.

---

**Exercise 4.** The correlation $\rho$ between the stock price and variance processes generates the leverage effect. Explain how $\rho < 0$ produces a negative skew in the implied volatility smile. What would happen to the smile if $\rho = 0$? If $\rho > 0$?

??? success "Solution to Exercise 4"
    The leverage effect arises from the correlation structure between $dW^{(1)}$ (driving returns) and $dW^{(2)}$ (driving variance).

    **Case $\rho < 0$**: A negative stock return ($dW^{(1)} < 0$) tends to coincide with positive innovations to variance ($dW^{(2)} > 0$), so volatility increases when the stock drops. This amplifies the left tail of the return distribution (large losses are accompanied by high volatility, making extreme losses more likely). Conversely, positive returns coincide with declining variance, compressing the right tail. The result is a negatively skewed return distribution. In implied volatility terms, OTM puts (low strikes) require higher implied volatility than OTM calls (high strikes), producing a downward-sloping skew.

    **Case $\rho = 0$**: The stock return and variance innovations are independent. Variance fluctuations create excess kurtosis (fatter tails than Gaussian) but no asymmetry. The implied volatility surface shows a symmetric smile: both OTM puts and OTM calls have elevated implied volatility relative to ATM, but by equal amounts.

    **Case $\rho > 0$**: The effect is reversed. Positive returns coincide with rising volatility, amplifying the right tail and compressing the left. The return distribution is positively skewed, and the implied volatility curve slopes upward with strike. This is uncommon in equity markets but can appear in certain commodity markets where supply shocks drive both price and volatility increases.

---

**Exercise 5.** Verify the Feller condition $2\kappa\theta \geq \xi^2$ for the parameters $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$. What is the financial consequence if the Feller condition is violated? Does the affine characteristic function formula remain valid when the condition fails?

??? success "Solution to Exercise 5"
    With $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$:

    $$
    2\kappa\theta = 2 \times 1.5 \times 0.04 = 0.12
    $$

    $$
    \xi^2 = 0.09
    $$

    Since $0.12 > 0.09$, the Feller condition $2\kappa\theta \geq \xi^2$ is satisfied. The ratio is $2\kappa\theta / \xi^2 = 0.12/0.09 \approx 1.33 > 1$.

    If the Feller condition is violated ($2\kappa\theta < \xi^2$), the variance process $V_t$ can reach zero. At $V_t = 0$, the diffusion vanishes and the positive drift $\kappa\theta > 0$ immediately pushes the process away from zero (instantaneous reflection). The process spends zero Lebesgue time at the boundary but the transition density acquires a point mass at $V_t = 0$.

    The affine characteristic function formula remains valid even when the Feller condition fails. The Riccati system and its solution are derived purely from the affine structure of the coefficients, not from the positivity of $V_t$. The formula for $\psi_2(\tau)$ and $\phi(\tau)$ is analytic in the parameters and does not require $2\kappa\theta \geq \xi^2$. In practice, most calibrated Heston models violate the Feller condition (typical ratios are $2\kappa\theta/\xi^2 \approx 0.3$), yet the characteristic function formula is used without modification.

---

**Exercise 6.** The Heston characteristic function involves the ratio $g = (\beta - d)/(\beta + d)$ where $\beta = \rho\xi iv - \kappa$. Show that $|g| < 1$ when $\operatorname{Re}(d) > 0$, and explain why this ensures numerical stability of the formula $\psi_2(\tau) = \frac{\beta - d}{\xi^2}\frac{1 - e^{-d\tau}}{1 - ge^{-d\tau}}$ for large $\tau$.

??? success "Solution to Exercise 6"
    We have $\beta = \rho\xi iv - \kappa$ and $d = \sqrt{\beta^2 - 2\alpha\gamma}$ with $\operatorname{Re}(d) > 0$. The ratio is $g = (\beta - d)/(\beta + d)$.

    Write $\beta = -\kappa + i\rho\xi v$, so $\operatorname{Re}(\beta) = -\kappa < 0$.

    To show $|g| < 1$, note that $|g| = |(\beta - d)/(\beta + d)| < 1$ if and only if $|\beta - d| < |\beta + d|$. Squaring both sides, this is equivalent to:

    $$
    |\beta|^2 - 2\operatorname{Re}(\bar{\beta}d) + |d|^2 < |\beta|^2 + 2\operatorname{Re}(\bar{\beta}d) + |d|^2
    $$

    which simplifies to $\operatorname{Re}(\bar{\beta}d) > 0$. Since $\operatorname{Re}(\beta) = -\kappa < 0$ and $\operatorname{Re}(d) > 0$, we need to verify this condition. Writing $\beta = \beta_r + i\beta_i$ and $d = d_r + id_i$:

    $$
    \operatorname{Re}(\bar{\beta}d) = \beta_r d_r + \beta_i d_i
    $$

    The sign depends on the specific parameter values, but the choice of branch $\operatorname{Re}(d) > 0$ (the "Little Heston Trap" convention of Albrecher et al.) is precisely the one that ensures $|g| < 1$.

    For numerical stability at large $\tau$: the formula $\psi_2(\tau) = \frac{\beta - d}{\xi^2}\frac{1 - e^{-d\tau}}{1 - ge^{-d\tau}}$ involves $e^{-d\tau}$. Since $\operatorname{Re}(d) > 0$, $|e^{-d\tau}| = e^{-\operatorname{Re}(d)\tau} \to 0$ as $\tau \to \infty$. Therefore:

    $$
    \psi_2(\tau) \to \frac{\beta - d}{\xi^2} \cdot \frac{1 - 0}{1 - 0} = \frac{\beta - d}{\xi^2}
    $$

    The denominator $1 - ge^{-d\tau}$ stays bounded away from zero because $|ge^{-d\tau}| \leq |g| < 1$. This prevents division by zero or exponential blowup, ensuring the formula is numerically stable for all maturities.

---

**Exercise 7.** Compare the Heston model to the Black-Scholes model as affine processes: both are $A_1(2)$ and $A_0(1)$ respectively in the Dai-Singleton classification. List the additional parameters that Heston introduces and explain what degree of freedom each one captures in the implied volatility surface.

??? success "Solution to Exercise 7"
    Black-Scholes is an $A_0(1)$ model with state $X_t = \log S_t$ and a single parameter $\sigma$ (constant volatility). Heston is an $A_1(2)$ model with state $(X_t, V_t) = (\log S_t, V_t)$ and introduces four additional parameters beyond $\sigma$:

    | Parameter | Role in Implied Volatility Surface |
    |-----------|-----------------------------------|
    | $V_0$ (initial variance) | Sets the **ATM level** of implied volatility at short maturities. Replaces the constant $\sigma^2$ of Black-Scholes. |
    | $\theta$ (long-run variance) | Controls the **ATM level at long maturities**. The implied volatility term structure converges toward $\sqrt{\theta}$ as $T \to \infty$. |
    | $\kappa$ (mean-reversion speed) | Governs the **term structure of the smile**: how quickly the implied volatility surface transitions from $\sqrt{V_0}$ (short end) to $\sqrt{\theta}$ (long end). Large $\kappa$ flattens the smile faster across maturities. |
    | $\xi$ (vol-of-vol) | Controls the **curvature** (convexity) of the smile at each maturity. Higher $\xi$ produces fatter tails and a more pronounced smile (higher ATM butterfly spread). |
    | $\rho$ (correlation) | Controls the **skew** (slope) of the smile. Negative $\rho$ tilts the smile so that low-strike implied volatilities exceed high-strike ones. |

    In summary, Black-Scholes produces a flat implied volatility surface (one number for all strikes and maturities), while Heston uses five parameters ($V_0, \theta, \kappa, \xi, \rho$) to generate a surface with non-trivial strike dependence (smile/skew) and maturity dependence (term structure), matching the key features of observed equity option markets.
