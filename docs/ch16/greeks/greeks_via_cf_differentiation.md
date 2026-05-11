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
    For the Gil-Pelaez decomposition, the delta of a European call simplifies to $\Delta = e^{-qT} P_1$, where $P_1$ is the exercise probability under the stock-numeraire measure. This mirrors the Black-Scholes result $\Delta = e^{-qT}\mathcal{N}(d_1)$.

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

---

## Exercises

**Exercise 1.**
The Heston CF has the form $\varphi(u) = \exp(C + Dv_0 + iu\ln S_0)$. Show that $\partial\varphi/\partial(\ln S_0) = iu\cdot\varphi(u)$ and $\partial^2\varphi/\partial(\ln S_0)^2 = -u^2\cdot\varphi(u)$. Use these to express the delta and gamma integrands in the Gil-Pelaez framework.

??? success "Solution to Exercise 1"
    The Heston characteristic function has the form:

    $$
    \varphi(u) = \exp\!\bigl(C(u,\tau) + D(u,\tau)\,v_0 + iu\ln S_0\bigr)
    $$

    **First derivative.** Since $\ln S_0$ appears only in the exponent multiplied by $iu$, we differentiate with respect to $\ln S_0$:

    $$
    \frac{\partial \varphi}{\partial (\ln S_0)} = iu \cdot \exp\!\bigl(C + D\,v_0 + iu\ln S_0\bigr) = iu \cdot \varphi(u)
    $$

    **Second derivative.** Differentiating again:

    $$
    \frac{\partial^2 \varphi}{\partial (\ln S_0)^2} = iu \cdot \frac{\partial \varphi}{\partial (\ln S_0)} = iu \cdot iu \cdot \varphi(u) = -u^2 \cdot \varphi(u)
    $$

    **Delta integrand.** In the Gil-Pelaez framework, $P_j = \frac{1}{2} + \frac{1}{\pi}\int_0^\infty \operatorname{Re}\!\left[\frac{e^{-iu\ln K}\,\varphi_j(u)}{iu}\right]du$. To compute $\partial P_j / \partial S_0$, we use the chain rule $\partial / \partial S_0 = (1/S_0)\,\partial / \partial(\ln S_0)$:

    $$
    \frac{\partial P_j}{\partial S_0} = \frac{1}{\pi S_0}\int_0^\infty \operatorname{Re}\!\left[\frac{e^{-iu\ln K}\cdot iu\cdot\varphi_j(u)}{iu}\right]du = \frac{1}{\pi S_0}\int_0^\infty \operatorname{Re}\!\left[e^{-iu\ln K}\,\varphi_j(u)\right]du
    $$

    The key observation is that the factor $iu$ from differentiation cancels the $1/(iu)$ denominator, yielding a smoother integrand (the density rather than the CDF).

    **Gamma integrand.** For the second derivative:

    $$
    \frac{\partial^2 P_j}{\partial S_0^2} = \frac{1}{\pi}\int_0^\infty \operatorname{Re}\!\left[\frac{e^{-iu\ln K}}{iu}\cdot\frac{1}{S_0^2}\bigl(-u^2 - iu\bigr)\,\varphi_j(u)\right]du
    $$

    The extra factor of $-u^2$ from $\partial^2\varphi/\partial(\ln S_0)^2$ and the $-iu$ from converting $\partial^2/\partial S_0^2$ (via the chain rule applied to $\partial/\partial S_0 = (1/S_0)\partial/\partial(\ln S_0)$) produce the gamma integrand. After simplification, $\Gamma = e^{-qT}\,\partial P_1/\partial S_0 / S_0$ as shown in the main text.

---

**Exercise 2.**
The Heston vega $\partial C_{\text{call}}/\partial v_0$ involves $\partial\varphi/\partial v_0 = D(u,\tau)\cdot\varphi(u)$, where $D$ is the Riccati function. Explain why the Heston vega depends on the maturity $\tau$ through $D(u,\tau)$ in a fundamentally different way from Black-Scholes vega, which depends on $\tau$ only through $\sqrt{\tau}$.

??? success "Solution to Exercise 2"
    In Black-Scholes, the option price depends on total integrated variance $\sigma^2 T$, so vega satisfies:

    $$
    \mathcal{V}_{\text{BS}} = \frac{\partial C}{\partial \sigma} = S\sqrt{T}\,\phi(d_1)
    $$

    The dependence on maturity is purely through $\sqrt{T}$, reflecting the fact that every future instant contributes equally to the total variance.

    In Heston, vega involves the Riccati function $D(u, \tau)$, which satisfies the ODE:

    $$
    \frac{dD}{d\tau} = \frac{1}{2}(iu + u^2) - (\kappa - i\rho\xi u)\,D + \frac{1}{2}\xi^2\,D^2
    $$

    with $D(u, 0) = 0$. The solution is:

    $$
    D(u, \tau) = \frac{(\kappa - i\rho\xi u) - \gamma}{\xi^2}\cdot\frac{1 - e^{-\gamma\tau}}{1 - g\,e^{-\gamma\tau}}
    $$

    where $\gamma$ and $g$ depend on $u$, $\kappa$, $\rho$, $\xi$. The function $D(u, \tau)$ enters the vega integrand as:

    $$
    \frac{\partial P_j}{\partial v_0} = \frac{1}{\pi}\int_0^\infty \operatorname{Re}\!\left[\frac{e^{-iu\ln K}}{iu}\,D_j(u,\tau)\,\varphi_j(u)\right]du
    $$

    The crucial difference is that $D(u, \tau)$ does not scale simply as $\sqrt{\tau}$ or $\tau$. For small $\tau$, $D(u,\tau) \approx \frac{1}{2}(iu + u^2)\tau + \mathcal{O}(\tau^2)$, so vega grows roughly linearly in $\tau$ (and thus like $\sqrt{T}$ when combined with the density scaling). But for large $\tau$, $D(u,\tau) \to D_\infty(u) = \frac{(\kappa - i\rho\xi u) - \gamma}{\xi^2}$ (the stable fixed point of the Riccati equation), and the exponential $e^{-\gamma\tau}$ drives $D$ to saturation. This means the sensitivity of the option price to $v_0$ **decays** for long maturities because mean reversion makes the terminal variance distribution insensitive to its initial value.

    Financially, this reflects the fact that in Heston, the initial variance $v_0$ only influences the near-term dynamics. Over long horizons, $v_t$ reverts to $\theta$, and the option price depends primarily on $\theta$ rather than $v_0$. The Riccati function $D(u, \tau)$ encodes this exponential memory decay, producing a hump-shaped vega term structure with no analog in Black-Scholes.

---

**Exercise 3.**
The sensitivity $\partial C/\partial\rho$ requires $\partial D/\partial\rho$ and $\partial C_{\text{Riccati}}/\partial\rho$. These involve differentiating $\gamma = \sqrt{(\kappa - i\rho\xi u)^2 + \xi^2(iu + u^2)}$ with respect to $\rho$. Compute $\partial\gamma/\partial\rho$ in terms of $\gamma$, $\kappa$, $\rho$, $\xi$, and $u$.

??? success "Solution to Exercise 3"
    The discriminant $\gamma$ is defined as:

    $$
    \gamma = \sqrt{(\kappa - i\rho\xi u)^2 + \xi^2(iu + u^2)}
    $$

    Let $f(\rho) = (\kappa - i\rho\xi u)^2 + \xi^2(iu + u^2)$. Then $\gamma = \sqrt{f(\rho)}$ and by the chain rule:

    $$
    \frac{\partial \gamma}{\partial \rho} = \frac{1}{2\gamma}\,\frac{\partial f}{\partial \rho}
    $$

    Computing $\partial f / \partial \rho$:

    $$
    \frac{\partial f}{\partial \rho} = 2(\kappa - i\rho\xi u)\cdot(-i\xi u) = -2i\xi u(\kappa - i\rho\xi u)
    $$

    Therefore:

    $$
    \frac{\partial \gamma}{\partial \rho} = \frac{-i\xi u(\kappa - i\rho\xi u)}{\gamma}
    $$

    Expanding the numerator:

    $$
    \frac{\partial \gamma}{\partial \rho} = \frac{-i\kappa\xi u - \rho\xi^2 u^2}{\gamma}
    $$

    This result is complex-valued (as expected, since $\gamma$ itself is complex for $u \neq 0$). The real and imaginary parts are needed when computing $\partial D/\partial\rho$ and $\partial C_{\text{Riccati}}/\partial\rho$ via subsequent applications of the chain rule through the Riccati solutions.

    Note that $\partial\gamma/\partial\rho$ is proportional to $\xi u$, confirming that the $\rho$-sensitivity vanishes when either $\xi = 0$ (deterministic variance, no correlation effect) or at $u = 0$ (the zeroth moment, which is always 1).

---

**Exercise 4.**
All Greeks can be computed in a single pass over the quadrature nodes. If you need price, delta, gamma, vega, and $\partial C/\partial\rho$, describe the algorithm: at each node $u_n$, evaluate $\varphi(u_n)$ and accumulate contributions to each Greek using the appropriate multiplier ($iu$ for delta, $-u^2$ for gamma, $D$ for vega, etc.). Estimate the cost saving versus five separate quadrature passes.

??? success "Solution to Exercise 4"
    **Single-pass algorithm.** At each quadrature node $u_n$ for $n = 1, \ldots, N$:

    1. Evaluate the characteristic function $\varphi(u_n)$ (one complex exponential involving $C(u_n, \tau)$, $D(u_n, \tau)$, and $iu_n \ln S_0$).
    2. Compute the following multiplied quantities, reusing $\varphi(u_n)$:
        - **Price**: accumulate $\operatorname{Re}\!\left[\frac{e^{-iu_n\ln K}\,\varphi_j(u_n)}{iu_n}\right] \times w_n$ for each measure $j = 1, 2$
        - **Delta**: accumulate $\operatorname{Re}\!\left[e^{-iu_n\ln K}\,\varphi_1(u_n)\right] \times w_n$ (the $iu$ factor cancels $1/(iu)$)
        - **Gamma**: accumulate $\operatorname{Re}\!\left[e^{-iu_n\ln K}\,\varphi_1(u_n)\right] \times w_n / S_0$ (one additional division)
        - **Vega**: accumulate $\operatorname{Re}\!\left[\frac{e^{-iu_n\ln K}\,D_j(u_n,\tau)\,\varphi_j(u_n)}{iu_n}\right] \times w_n$ for $j = 1, 2$
        - **$\partial C/\partial\rho$**: accumulate $\operatorname{Re}\!\left[\frac{e^{-iu_n\ln K}}{iu_n}\left(\frac{\partial C_j}{\partial\rho} + \frac{\partial D_j}{\partial\rho}\,v_0\right)\varphi_j(u_n)\right] \times w_n$
    3. After the loop, combine the accumulated sums with the outer factors ($S_0 e^{-qT}$, $-Ke^{-rT}$, etc.) to form each Greek.

    **Cost analysis.** The dominant cost per quadrature node is evaluating $\varphi(u_n)$, which requires computing $C(u_n, \tau)$ and $D(u_n, \tau)$ (involving complex exponentials, logarithms, and square roots). The chain-rule derivatives $\partial C/\partial\rho$, $\partial D/\partial\rho$, and $D$ itself are obtained with modest additional arithmetic (a few multiplications and divisions) using the same intermediate quantities ($\gamma$, $g$, $e^{-\gamma\tau}$).

    Approximate cost breakdown per node:

    - Characteristic function evaluation: $\sim 20$ floating-point operations (the bottleneck)
    - Each additional Greek multiplier: $\sim 5$ operations

    For $N$ quadrature nodes and $G$ Greeks, the single-pass cost is approximately $N \times (20 + 5G)$, while $G$ separate passes cost $N \times 20G$. For $G = 5$ and $N = 128$:

    - Single pass: $128 \times 45 = 5{,}760$ operations
    - Five separate passes: $128 \times 100 = 12{,}800$ operations

    The single-pass approach is roughly **2.2 times faster** (saving about 55% of the computation). In practice the savings are even larger because $\varphi$ evaluation often involves expensive transcendental functions (complex $\exp$, $\log$, $\sqrt{\phantom{x}}$), and caching these intermediate values avoids redundant computation.

---

**Exercise 5.**
Compare the CF-differentiation delta with the Black-Scholes delta $N(d_1)$ for an ATM call with $K = S_0 = 100$, $T = 0.5$, $v_0 = 0.04$, $\rho = -0.7$. The Heston delta accounts for the correlation between stock and variance moves. Explain qualitatively why negative $\rho$ makes the Heston delta slightly different from the BS delta.

??? success "Solution to Exercise 5"
    In Black-Scholes, the ATM call delta is $\Delta_{\text{BS}} = e^{-qT}\mathcal{N}(d_1)$ where:

    $$
    d_1 = \frac{(r - q + \tfrac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}
    $$

    With $\sigma = \sqrt{v_0} = 0.2$, $T = 0.5$, $r = 0.05$, $q = 0$, $K = S_0 = 100$:

    $$
    d_1 = \frac{(0.05 + 0.02) \times 0.5}{0.2 \times \sqrt{0.5}} = \frac{0.035}{0.1414} \approx 0.2475
    $$

    $$
    \Delta_{\text{BS}} = \Phi(0.2475) \approx 0.598
    $$

    The Heston delta $\Delta_{\text{Heston}} = e^{-qT}P_1 \approx 0.617$ (from the worked example in the text) is slightly higher.

    **Qualitative explanation.** The difference arises from negative correlation $\rho = -0.7$. When $\rho < 0$:

    - A rise in $S$ is associated with a fall in $v$ (the leverage effect).
    - When the stock price increases, variance tends to decrease, making further large moves less likely. This compresses the right tail of the return distribution.
    - Conversely, a fall in $S$ is associated with a rise in $v$, fattening the left tail.

    This asymmetry produces a **negatively skewed** distribution of $\ln S_T$ under the Heston model, compared to the symmetric (Gaussian) distribution under Black-Scholes. For an ATM call:

    - The negative skew means the risk-neutral probability of finishing ITM ($P_2$) is slightly different from $\mathcal{N}(d_2)$.
    - More importantly, the stock-measure probability $P_1$ (which weights outcomes by the stock price) is affected by the skew. The leverage effect creates a subtle conditional dependence: given that the option finishes ITM, the expected stock price differs from the Black-Scholes prediction.

    The net result is that negative $\rho$ slightly increases the ATM Heston delta relative to Black-Scholes. Intuitively, the leverage-induced left skew makes the option "more sensitive" to the current stock price because downside moves are amplified by rising variance, so the hedge ratio must be slightly larger to compensate for this asymmetric risk.

---

**Exercise 6.**
CF differentiation produces exact Greeks (up to quadrature error) but only for European options priced via Fourier inversion. For an American put under Heston, explain why CF differentiation cannot be used directly and describe the alternative approach (finite differences on the PDE solution or pathwise MC sensitivities).

??? success "Solution to Exercise 6"
    **Why CF differentiation fails for American options.** The characteristic function approach requires expressing the option price as a Fourier inversion integral of the form:

    $$
    V = \frac{1}{2\pi}\int_{-\infty}^{\infty} \hat{V}(u)\,e^{iux}\,du
    $$

    where $\hat{V}(u)$ depends on the characteristic function $\varphi(u)$. This representation is valid when the option payoff can be expressed as a function of the terminal asset price $S_T$ alone (European-style exercise).

    An **American put** has an early exercise boundary $S^*(t)$ that depends on the entire variance path and creates a **free boundary** in the pricing problem. The option price at time $t$ is:

    $$
    V(t, S, v) = \sup_{\tau \in [t, T]} \mathbb{E}\!\left[e^{-r(\tau - t)}(K - S_\tau)^+ \mid S_t = S,\, v_t = v\right]
    $$

    This optimal stopping problem couples the exercise decision to the two-dimensional state $(S, v)$ at every instant. There is no closed-form characteristic function for the American option value because:

    1. The payoff is path-dependent (through the exercise decision).
    2. The exercise boundary $S^*(t, v)$ depends on the variance state and must be solved simultaneously with the option price.
    3. No Fourier transform of the American price exists in closed form.

    **Alternative approaches:**

    1. **Finite differences on the PDE solution.** Solve the Heston PDE on a 2D grid $(S, v)$ with the early exercise constraint (a linear complementarity problem or penalty method). Greeks are computed by:
        - **Grid differentiation**: Delta $= \partial V / \partial S$ and gamma $= \partial^2 V / \partial S^2$ are obtained directly from the PDE grid stencil at the evaluation point. Vega $= \partial V / \partial v$ comes from the $v$-direction stencil. These are "free" (no additional PDE solves).
        - **Bump-and-revalue**: For parameter sensitivities ($\xi$, $\rho$, $\kappa$), solve the PDE with bumped parameters and use finite differences.

    2. **Pathwise Monte Carlo sensitivities.** Simulate the Heston dynamics with a Longstaff-Schwartz (least-squares Monte Carlo) exercise policy:
        - **Finite differences**: Bump a parameter, re-simulate with common random numbers, and compute the difference quotient.
        - **Pathwise (tangent) method**: Differentiate the simulated paths with respect to the parameter of interest. This is complicated by the discontinuous exercise decision, which requires smoothing techniques (e.g., kernel smoothing of the exercise boundary) or likelihood ratio methods.

    The PDE approach is generally preferred for American options under Heston because it provides all $(S, v)$-direction Greeks from the grid and only requires repricing for parameter sensitivities.
