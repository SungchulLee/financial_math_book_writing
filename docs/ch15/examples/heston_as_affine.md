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

Applying Ito's lemma to $X_t = \log S_t$:

$$
dX_t = \left(r - \frac{1}{2}V_t\right)dt + \sqrt{V_t}\,dW_t^{(1)}
$$

The state vector is $\mathbf{X}_t = (X_t, V_t) \in \mathbb{R} \times \mathbb{R}_+$, which is the canonical state space $D = \mathbb{R}^1_+ \times \mathbb{R}^1$ with $m = 1$ (one CIR-type component: $V_t$) and $d = 2$.

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

Using the identified parameters:

$$
F(w) = \langle b_0, w \rangle = r\,w_1 + \kappa\theta\,w_2
$$

(No quadratic term since $a_0 = 0$.)

$$
R_1(w) = \langle b_1, w \rangle = 0
$$

$$
R_2(w) = \langle b_2, w \rangle + \frac{1}{2}\langle w, a_2 w \rangle = -\frac{1}{2}w_1 - \kappa w_2 + \frac{1}{2}(w_1^2 + 2\rho\xi w_1 w_2 + \xi^2 w_2^2)
$$

The $R_1$ equation is trivial ($\psi_1' = 0$), and the $R_2$ equation is a Riccati equation in $\psi_2$ with coefficients depending on $\psi_1$.

---

## The Riccati System

### Characteristic Function Setup

For the characteristic function of the log-price $X_T$ (marginal in the first component), set $u_1 = iv$ and $u_2 = 0$:

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
