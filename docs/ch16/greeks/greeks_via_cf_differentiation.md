# Greeks via Characteristic Function Differentiation

In the Black-Scholes model, Greeks have closed-form expressions involving the normal CDF and its density. The Heston model lacks such simple formulas, but its characteristic function is known in closed form, and every Greek can be computed by **differentiating the Fourier inversion integral** with respect to the relevant parameter. This approach produces Greeks with the same accuracy as the option price itself---no finite difference approximation, no bump-size sensitivity---making it the method of choice for production-quality risk computation.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive delta and gamma by differentiating the Gil-Pelaez inversion with respect to $S_0$
    2. Compute vega (sensitivity to $v_0$) by differentiating through the characteristic function
    3. Compute sensitivities to model parameters $\kappa$, $\theta$, $\xi$, $\rho$
    4. Evaluate the resulting integrals numerically with appropriate quadrature

!!! tip "Prerequisites"
    This section requires the [Gil-Pelaez inversion](../european_pricing/gil_pelaez_inversion.md) and the [characteristic function](../heston_cf/closed_form_characteristic_function.md).

---

## The Gil-Pelaez Framework

Recall that the European call price under Heston is:

$$
C = S_0 e^{-qT} P_1 - K e^{-rT} P_2
$$

where the exercise probabilities are:

$$
P_j = \frac{1}{2} + \frac{1}{\pi} \int_0^\infty \text{Re}\!\left[\frac{e^{-iu \ln K} \phi_j(u)}{iu}\right] du, \qquad j = 1, 2
$$

Here $\phi_1(u)$ is the characteristic function under the stock-numeraire measure $\mathbb{Q}^S$ and $\phi_2(u) = \phi(u)$ is the characteristic function under the money-market measure $\mathbb{Q}$. Both have the exponential-affine form:

$$
\phi(u) = \exp\!\left(C(\tau, u) + D(\tau, u) v_0 + iu \ln S_0\right)
$$

where $C$ and $D$ are the Riccati solutions depending on $\kappa, \theta, \xi, \rho$ but not on $S_0$ or $v_0$.

---

## Delta

**Delta** $\Delta = \partial C / \partial S_0$ measures the sensitivity of the option price to the stock price.

### Derivation

Since $\phi(u)$ contains $S_0$ only through the term $iu \ln S_0$:

$$
\frac{\partial \phi}{\partial S_0} = \frac{iu}{S_0} \phi(u)
$$

Differentiating the call price formula:

$$
\Delta = e^{-qT} P_1 + S_0 e^{-qT} \frac{\partial P_1}{\partial S_0} - K e^{-rT} \frac{\partial P_2}{\partial S_0}
$$

The derivative of each $P_j$ involves:

$$
\frac{\partial P_j}{\partial S_0} = \frac{1}{\pi} \int_0^\infty \text{Re}\!\left[\frac{e^{-iu \ln K}}{iu} \cdot \frac{iu}{S_0} \phi_j(u)\right] du = \frac{1}{\pi S_0} \int_0^\infty \text{Re}\!\left[e^{-iu \ln K} \phi_j(u)\right] du
$$

The factor $iu$ from the differentiation cancels the $1/(iu)$ in the integrand, producing a simpler integral (the density rather than the CDF).

The final delta formula is:

$$
\Delta = e^{-qT} \left[P_1 + \frac{1}{\pi}\int_0^\infty \text{Re}\!\left[e^{-iu\ln K}\phi_1(u)\right]du\right] - \frac{Ke^{-rT}}{\pi S_0}\int_0^\infty \text{Re}\!\left[e^{-iu\ln K}\phi_2(u)\right]du
$$

In practice, a cleaner approach is to directly differentiate the combined call price integral.

!!! note "Delta as a Probability"
    For the Gil-Pelaez decomposition, the delta of a European call simplifies to $\Delta = e^{-qT} P_1$, where $P_1$ is the exercise probability under the stock-numeraire measure. This mirrors the Black-Scholes result $\Delta = e^{-qT}\Phi(d_1)$.

---

## Gamma

**Gamma** $\Gamma = \partial^2 C / \partial S_0^2$ measures the convexity of the option price.

Differentiating delta:

$$
\Gamma = \frac{\partial \Delta}{\partial S_0} = e^{-qT} \frac{\partial P_1}{\partial S_0}
$$

Using the result above:

$$
\Gamma = \frac{e^{-qT}}{\pi S_0} \int_0^\infty \text{Re}\!\left[e^{-iu\ln K} \phi_1(u)\right] du
$$

This integral converges because $\phi_1(u) \to 0$ rapidly as $u \to \infty$ (the characteristic function of a continuous distribution decays). The integrand is the risk-neutral density of $\ln S_T$ under $\mathbb{Q}^S$, evaluated at $\ln K$.

---

## Vega (Sensitivity to Initial Variance)

In the Heston model, the natural "vega" is $\mathcal{V} = \partial C / \partial v_0$, the sensitivity to the **initial variance** (not implied volatility). Since $v_0$ appears only in $\phi$ through the term $D(\tau, u) v_0$:

$$
\frac{\partial \phi}{\partial v_0} = D(\tau, u) \, \phi(u)
$$

The vega is:

$$
\mathcal{V} = S_0 e^{-qT} \frac{\partial P_1}{\partial v_0} - K e^{-rT} \frac{\partial P_2}{\partial v_0}
$$

where:

$$
\frac{\partial P_j}{\partial v_0} = \frac{1}{\pi}\int_0^\infty \text{Re}\!\left[\frac{e^{-iu\ln K}}{iu} D_j(\tau, u) \phi_j(u)\right] du
$$

Here $D_j$ is the Riccati function $D$ evaluated with the parameters appropriate for measure $j$.

!!! warning "Vega vs Black-Scholes Vega"
    The Heston $\mathcal{V} = \partial C / \partial v_0$ has units of price per variance, not price per volatility. To convert to Black-Scholes-like vega (per unit of volatility), divide by $2\sqrt{v_0}$: $\text{vega}_{\text{BS-like}} = \mathcal{V} / (2\sqrt{v_0})$. However, in the Heston context, reporting $\mathcal{V}$ directly is more natural because $v_0$ (not $\sigma_0$) is the model parameter.

---

## Parameter Sensitivities

### Sensitivity to Vol-of-Vol

The sensitivity $\partial C / \partial \xi$ requires differentiating $C(\tau, u)$ and $D(\tau, u)$ with respect to $\xi$. Since the Riccati solutions $C$ and $D$ depend on $\xi$ through:

$$
\gamma = \sqrt{(\kappa - i\rho\xi u)^2 + \xi^2(iu + u^2)}
$$

the derivatives $\partial C / \partial \xi$ and $\partial D / \partial \xi$ can be computed using the chain rule, although the expressions are lengthy. The option sensitivity is:

$$
\frac{\partial C_{\text{option}}}{\partial \xi} = S_0 e^{-qT}\frac{\partial P_1}{\partial \xi} - Ke^{-rT}\frac{\partial P_2}{\partial \xi}
$$

with:

$$
\frac{\partial P_j}{\partial \xi} = \frac{1}{\pi}\int_0^\infty \text{Re}\!\left[\frac{e^{-iu\ln K}}{iu}\left(\frac{\partial C_j}{\partial \xi} + \frac{\partial D_j}{\partial \xi}v_0\right)\phi_j(u)\right]du
$$

### Sensitivity to Correlation

Similarly, $\partial C_{\text{option}} / \partial \rho$ requires $\partial C / \partial \rho$ and $\partial D / \partial \rho$, computed through the dependence of $\gamma$ on $\rho$.

### Sensitivity to Mean-Reversion Parameters

The sensitivities $\partial C_{\text{option}} / \partial \kappa$ and $\partial C_{\text{option}} / \partial \theta$ follow the same pattern: differentiate the Riccati solutions with respect to the parameter and integrate.

---

## Numerical Integration

### Integrand Behavior

The differentiated integrands decay at the same rate as the undifferentiated ones because the $D$ function grows at most polynomially in $u$ while $\phi$ decays exponentially. However, the differentiated integrands may oscillate more rapidly, requiring slightly more quadrature points.

### Practical Implementation

1. Use **adaptive Gauss-Kronrod** or **Clenshaw-Curtis** quadrature with a truncation at $u_{\max} \approx 200$--$500$
2. For delta and gamma, the cancellation of $iu$ in the integrand produces a smoother function that converges faster
3. For parameter sensitivities ($\xi$, $\rho$, $\kappa$, $\theta$), the integrands are more oscillatory and may require $u_{\max} \approx 500$ or higher

!!! tip "Efficiency"
    All Greeks can be computed in a **single integration pass**: evaluate $\phi$, $D\phi$, $\partial_\xi C \cdot \phi$, $\partial_\xi D \cdot \phi$, etc., at each quadrature point $u_k$, then combine. The cost is one characteristic function evaluation per quadrature point (plus chain-rule derivatives), compared to multiple full repricing passes for finite difference Greeks.

---

## Worked Example

For a European call with $S_0 = \$100$, $K = \$100$, $T = 1$, $r = 0.05$, $q = 0$ and Heston parameters $v_0 = 0.04$, $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, $\rho = -0.7$:

| Greek | CF Differentiation | Finite Difference ($h = 10^{-4}$) |
|-------|:-----------------:|:---------------------------------:|
| Price | $\$10.36$ | $\$10.36$ |
| Delta | $0.617$ | $0.617$ |
| Gamma | $0.0189$ | $0.0189$ |
| Vega ($\partial C/\partial v_0$) | $21.4$ | $21.4$ |
| $\partial C / \partial \xi$ | $5.82$ | $5.82$ |
| $\partial C / \partial \rho$ | $-7.14$ | $-7.14$ |

??? example "Integration Details"
    Using 128-point Gauss-Kronrod quadrature on $[0, 300]$:

    - Price integral converges to 12 significant digits
    - Delta integral (smoother) converges to 14 significant digits
    - $\partial C / \partial \xi$ integral converges to 10 significant digits (more oscillatory)
    - Total computation time: approximately 2 ms for all Greeks simultaneously

---

## Summary

Differentiating the Fourier inversion integral with respect to model parameters produces exact Greeks for the Heston model. Delta and gamma follow from the simple dependence of $\phi$ on $\ln S_0$; vega follows from the linear dependence on $v_0$ through the Riccati function $D$; parameter sensitivities ($\xi$, $\rho$, $\kappa$, $\theta$) require chain-rule differentiation of the Riccati solutions. All Greeks can be computed in a single quadrature pass, making this approach both more accurate and more efficient than [finite difference Greeks](greeks_via_finite_differences.md). The method is limited to European options priced via Fourier inversion; for American or exotic options, finite differences or pathwise Monte Carlo sensitivities are needed.
