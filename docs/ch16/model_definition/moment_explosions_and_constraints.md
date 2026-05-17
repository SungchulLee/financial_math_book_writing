# Moment Explosions and Parameter Constraints

In the Black-Scholes model, $\mathbb{E}[S_T^p] < \infty$ for every real $p$ and every $T > 0$ because the log-normal distribution has finite moments of all orders. The Heston model is fundamentally different: for sufficiently large $p$, the expectation $\mathbb{E}[S_T^p]$ explodes to infinity. This phenomenon -- **moment explosion** -- arises from the stochastic variance amplifying the tails of the return distribution. The threshold value $p^*$ above which moments are infinite is called the **critical moment**, and it depends on the Heston parameters and the time horizon.

Moment explosions are not merely a mathematical curiosity. They determine the domain of the characteristic function in the complex plane, which in turn determines whether Fourier pricing methods (Gil-Pelaez, Carr-Madan, COS) converge. This section derives the critical moment formula, presents the Andersen-Piterbarg result, and draws the practical implications for pricing and calibration.

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - Define the critical moment $p^*$ and explain its financial meaning
    - State the Andersen-Piterbarg formula for $p^*$ in the Heston model
    - Connect moment explosions to the strip of analyticity of the characteristic function
    - Derive the critical moment from the Riccati ODE blow-up condition
    - Explain the implications for Fourier pricing integrability conditions

---

## Moment Explosions in Stochastic Volatility Models

### Intuition

Under stochastic volatility, the asset price can experience periods of very high variance. During these periods, the exponential growth $S_T = S_0 \exp(\int_0^T \sqrt{v_t}\,dW_t - \frac{1}{2}\int_0^T v_t\,dt)$ can produce extremely large values of $S_T$. For low powers $p$, the probability of these extreme events is small enough that $\mathbb{E}[S_T^p]$ remains finite. But as $p$ increases, the $S_T^p$ factor amplifies these rare events until the expectation diverges.

The critical moment $p^*$ is the largest exponent for which $\mathbb{E}[S_T^p]$ is finite. For $p < p^*$, all moments exist; for $p > p^*$, the $p$-th moment is infinite.

### Formal Definition

!!! info "Definition: Critical Moment"
    The **upper critical moment** of $S_T$ under the Heston model is:

    $$
    p^*_+(T) = \sup\{p > 1 : \mathbb{E}^{\mathbb{Q}}[S_T^p] < \infty\}
    $$

    Similarly, the **lower critical moment** is:

    $$
    p^*_-(T) = \inf\{p < 0 : \mathbb{E}^{\mathbb{Q}}[S_T^{p}] < \infty\}
    $$

    The **moment explosion** occurs at the boundary: $\mathbb{E}^{\mathbb{Q}}[S_T^p] = \infty$ for $p > p^*_+(T)$ and for $p < p^*_-(T)$.

---

## Connection to the Characteristic Function

The $p$-th moment of $S_T$ is related to the characteristic function of $x_T = \ln S_T$ evaluated at a complex argument. Specifically:

$$
\mathbb{E}[S_T^p] = \mathbb{E}[e^{p\,x_T}] = \phi(-ip, T)
$$

where $\phi(u, T)$ is the characteristic function of $x_T$. The moment $\mathbb{E}[S_T^p]$ is finite if and only if $\phi(u, T)$ is well-defined (finite) at $u = -ip$.

!!! success "Proposition: Strip of Analyticity"
    The characteristic function $\phi(u, T) = \mathbb{E}[e^{iu\,x_T}]$ is analytic (well-defined and finite) in the **strip of analyticity**:

    $$
    \{u \in \mathbb{C} : p^*_-(T) < -\text{Im}(u) < p^*_+(T)\}
    $$

    The moment explosions occur precisely at the boundaries of this strip.

This means $\phi(u, T)$ is defined for $u \in \mathbb{R}$ (the real line, corresponding to $\text{Im}(u) = 0$, which lies inside the strip since $p^*_- < 0 < 1 < p^*_+$). But the Fourier pricing formulas sometimes require evaluating $\phi$ at complex values of $u$, and the strip of analyticity determines whether this is possible.

---

## The Andersen-Piterbarg Formula

### Derivation via Riccati Blow-Up

The moment $\mathbb{E}[S_T^p] = \phi(-ip, T) = \exp(C(T, -ip) + D(T, -ip)\,v_0 + p\,x_0)$ is finite if and only if the Riccati ODE for $D(\tau, u)$ does not blow up before time $\tau = T$ at the point $u = -ip$.

Recall (see [§ Affine Structure and Riccati System](affine_structure_and_riccati.md)) the Riccati ODE $D' = \tfrac{1}{2}\sigma_v^2 D^2 + (\rho\sigma_v\,iu - \kappa)D + \tfrac{1}{2}(iu - u^2)$. Substituting $u = -ip$ (so $iu = p$ and $u^2 = -p^2$):

$$
D' = \tfrac{1}{2}\sigma_v^2\,D^2 + (\rho\sigma_v\,p - \kappa)\,D + \tfrac{1}{2}(p + p^2)
$$

$$
= \tfrac{1}{2}\sigma_v^2\,D^2 + (\rho\sigma_v\,p - \kappa)\,D + \tfrac{1}{2}p(1 + p)
$$

This is a real-valued Riccati ODE with real coefficients (all quantities are real when $u = -ip$). The solution $D(\tau)$ starts at $D(0) = 0$ and increases. If the discriminant of the quadratic on the right-hand side is positive, $D(\tau)$ reaches a pole (blows up to $+\infty$) at a finite time $\tau^*$. The moment $\mathbb{E}[S_T^p]$ is finite if and only if $T < \tau^*(p)$.

### The Critical Time

The discriminant of the quadratic $\frac{1}{2}\sigma_v^2 D^2 + (\rho\sigma_v p - \kappa)D + \frac{1}{2}p(1+p)$ is:

$$
\gamma^2(p) = (\kappa - \rho\sigma_v\,p)^2 - \sigma_v^2\,p(1 + p)
$$

$$
= \kappa^2 - 2\kappa\rho\sigma_v\,p + \rho^2\sigma_v^2\,p^2 - \sigma_v^2\,p - \sigma_v^2\,p^2
$$

$$
= \kappa^2 - (2\kappa\rho + \sigma_v)\sigma_v\,p + (\rho^2 - 1)\sigma_v^2\,p^2
$$

When $\gamma^2(p) > 0$, the Riccati ODE has a solution that exists for all $\tau \geq 0$ (no blow-up). When $\gamma^2(p) \leq 0$, the solution blows up at a finite time.

!!! success "Theorem: Andersen-Piterbarg Critical Moment (Long-Maturity Limit)"
    As $T \to \infty$, the critical moment converges to:

    $$
    p^*_+ = \frac{1}{2} - \frac{\kappa}{\sigma_v(|\rho| + \sqrt{1 - \rho^2}\,\cdot\,\text{sgn}(\text{terms}))} + \frac{1}{2}\sqrt{\left(\frac{2\kappa}{\sigma_v(1 - \rho^2)} - \frac{1}{1-\rho^2}\right)^2 + \frac{1}{(1-\rho^2)}}
    $$

    More precisely, $p^*_+(T)$ is the largest positive root of $\gamma^2(p) = 0$ that satisfies $\kappa - \rho\sigma_v p > 0$. Solving $\gamma^2(p) = 0$ for $p$ as a quadratic in $p$:

    $$
    (1 - \rho^2)\sigma_v^2\,p^2 + (2\kappa\rho + \sigma_v)\sigma_v\,p - \kappa^2 = 0
    $$

    The positive root is:

    $$
    p^*_+ = \frac{-(2\kappa\rho + \sigma_v)\sigma_v + \sqrt{(2\kappa\rho + \sigma_v)^2\sigma_v^2 + 4(1-\rho^2)\sigma_v^2\kappa^2}}{2(1-\rho^2)\sigma_v^2}
    $$

    which simplifies to:

    $$
    p^*_+ = \frac{-(2\kappa\rho + \sigma_v) + \sqrt{(2\kappa\rho + \sigma_v)^2 + 4\kappa^2(1-\rho^2)}}{2(1-\rho^2)\sigma_v}
    $$

!!! warning "Finite-Maturity Correction"
    The formula above gives the long-maturity limit $p^*_+(\infty)$. For finite $T$, the critical moment $p^*_+(T)$ is larger (more moments exist for shorter horizons). The exact finite-$T$ value requires solving for the blow-up time of the Riccati ODE, which does not have a simpler closed form. In practice, the long-maturity formula provides a conservative bound for the integrability constraints.

---

## Implications for Fourier Pricing

### The Integrability Condition

The Gil-Pelaez inversion formula for a European call option requires evaluating the characteristic function $\phi(u, T)$ along the real line $u \in \mathbb{R}$, which is always inside the strip of analyticity. However, the **Carr-Madan** formulation with damping parameter $\alpha$ requires evaluating $\phi(u - i(\alpha + 1), T)$, which shifts the imaginary part to $\text{Im}(u) = -(\alpha + 1)$. For this to be finite, we need $\alpha + 1 < p^*_+(T)$.

!!! info "Definition: Damping Parameter Constraint"
    In the Carr-Madan FFT pricing method, the damping parameter $\alpha > 0$ must satisfy:

    $$
    \alpha + 1 < p^*_+(T)
    $$

    If this condition is violated, the modified call price $c_T(k)\,e^{\alpha k}$ is not integrable and the FFT method fails.

Similarly, for put options, the lower critical moment imposes $\alpha > -p^*_-(T)$.

### The Lewis (2000) Formulation

Lewis (2000) observed that the call price can be written as a single integral involving the characteristic function evaluated on the line $\text{Im}(u) = -\frac{1}{2}$:

$$
C = S_0 e^{-qT} - \frac{\sqrt{S_0 K}\,e^{-(r+q)T/2}}{\pi}\int_0^\infty \text{Re}\!\left[\frac{\phi(u - i/2, T)}{u^2 + 1/4}\right]du
$$

This requires $\frac{1}{2} < p^*_+(T)$, which is always satisfied (since $p^*_+ > 1$). The Lewis formulation is therefore robust to moment explosions.

---

## Worked Example: Critical Moment Calculation

??? example "Computing p* for Typical Parameters"
    Consider $\kappa = 2.0$, $\sigma_v = 0.5$, $\rho = -0.7$.

    The quadratic $\gamma^2(p) = 0$ becomes:

    $$
    (1 - 0.49)(0.25)\,p^2 + (2(2)(-0.7) + 0.5)(0.5)\,p - 4 = 0
    $$

    $$
    0.1275\,p^2 + (-2.8 + 0.5)(0.5)\,p - 4 = 0
    $$

    $$
    0.1275\,p^2 - 1.15\,p - 4 = 0
    $$

    Using the quadratic formula:

    $$
    p = \frac{1.15 \pm \sqrt{1.3225 + 4(0.1275)(4)}}{2(0.1275)} = \frac{1.15 \pm \sqrt{1.3225 + 2.04}}{0.255}
    $$

    $$
    = \frac{1.15 \pm \sqrt{3.3625}}{0.255} = \frac{1.15 \pm 1.834}{0.255}
    $$

    The positive root is:

    $$
    p^*_+ = \frac{1.15 + 1.834}{0.255} = \frac{2.984}{0.255} \approx 11.7
    $$

    This means $\mathbb{E}[S_T^p] < \infty$ for $p < 11.7$ as $T \to \infty$. For the Carr-Madan method, the damping parameter must satisfy $\alpha < 10.7$, which is easily met (typical values are $\alpha = 1.5$).

    The negative root gives $p^*_- = (1.15 - 1.834)/0.255 \approx -2.68$, meaning moments of order $p > -2.68$ from below are finite.

---

## Parameter Sensitivity of the Critical Moment

The critical moment $p^*_+$ depends on the parameters in intuitive ways:

| Change | Effect on $p^*_+$ | Explanation |
|:---|:---:|:---|
| Increase $\sigma_v$ | Decreases $p^*_+$ | Higher vol-of-vol creates heavier tails |
| $\rho$ more negative | Decreases $p^*_+$ | Leverage effect amplifies downside tails |
| Increase $\kappa$ | Increases $p^*_+$ | Stronger mean-reversion constrains variance excursions |
| $\rho = 0$ | Maximizes $p^*_+$ (for given $\kappa, \sigma_v$) | No leverage amplification |

!!! warning "Calibration Constraint"
    When calibrating the Heston model, one must verify that the calibrated parameters yield a critical moment $p^*_+ > \alpha + 1$ for the chosen damping parameter. If calibration produces parameters with a low $p^*_+$ (e.g., very high $\sigma_v$ or extreme $\rho$), the Fourier pricing integrals may not converge, leading to spurious prices. This constraint should be included in the calibration objective or enforced as a hard constraint.

---

## Summary

Moment explosions are an intrinsic feature of the Heston model: for each maturity $T$, there exists a critical moment $p^*_+(T)$ beyond which $\mathbb{E}[S_T^p] = \infty$. The critical moment is determined by the blow-up condition of the Riccati ODE evaluated at a real argument and can be computed from a quadratic equation involving $\kappa$, $\sigma_v$, and $\rho$. The strip of analyticity of the characteristic function, which governs the convergence of Fourier pricing methods, is directly determined by the critical moments. In practice, the Andersen-Piterbarg long-maturity formula provides the binding constraint, and calibrated parameters must be checked to ensure that the Fourier integrability conditions are satisfied.

The [variance dynamics](../variance_dynamics/cir_variance_process_solution.md) section next examines the exact solution and transition density of the CIR variance process.

---

## Exercises

**Exercise 1.** For Heston parameters $\kappa = 2$, $\sigma_v = 0.3$, $\rho = -0.7$, compute the long-maturity critical moment $p^*_+$ using the Andersen-Piterbarg formula. Verify that $p^*_+ > 2$, which is needed for the second moment of $S_T$ to be finite.

??? success "Solution to Exercise 1"
    For $\kappa = 2$, $\sigma_v = 0.3$, $\rho = -0.7$, the long-maturity critical moment is the positive root of $\gamma^2(p) = 0$:

    $$
    (1 - \rho^2)\sigma_v^2\,p^2 + (2\kappa\rho + \sigma_v)\sigma_v\,p - \kappa^2 = 0
    $$

    Substituting the parameters:

    $$
    (1 - 0.49)(0.09)\,p^2 + (2(2)(-0.7) + 0.3)(0.3)\,p - 4 = 0
    $$

    $$
    (0.51)(0.09)\,p^2 + (-2.8 + 0.3)(0.3)\,p - 4 = 0
    $$

    $$
    0.0459\,p^2 - 0.75\,p - 4 = 0
    $$

    Applying the quadratic formula:

    $$
    p = \frac{0.75 \pm \sqrt{0.5625 + 4(0.0459)(4)}}{2(0.0459)} = \frac{0.75 \pm \sqrt{0.5625 + 0.7344}}{0.0918}
    $$

    $$
    = \frac{0.75 \pm \sqrt{1.2969}}{0.0918} = \frac{0.75 \pm 1.1389}{0.0918}
    $$

    The positive root is:

    $$
    p^*_+ = \frac{0.75 + 1.1389}{0.0918} = \frac{1.8889}{0.0918} \approx 20.6
    $$

    **Verification that $p^*_+ > 2$:** Since $p^*_+ \approx 20.6 \gg 2$, the second moment $\mathbb{E}[S_T^2]$ is finite. This is important because finiteness of the second moment guarantees that $S_T \in L^2$, which is needed for the variance of the asset price to be well-defined and for mean-variance hedging to make sense.

    Compared to the worked example in the text ($\sigma_v = 0.5$ gave $p^*_+ \approx 11.7$), the lower vol-of-vol $\sigma_v = 0.3$ produces a much higher critical moment, as expected: lower $\sigma_v$ means lighter tails.

---

**Exercise 2.** Explain the connection between the critical moment $p^*_+$ and the strip of analyticity of the characteristic function. If $p^*_+ = 8$, what is the maximal damping parameter $\alpha$ in the Carr-Madan FFT method?

??? success "Solution to Exercise 2"
    The $p$-th moment of $S_T$ is:

    $$
    \mathbb{E}[S_T^p] = \mathbb{E}[e^{p\,x_T}] = \phi(-ip, T)
    $$

    where $\phi(u, T)$ is the characteristic function of $x_T = \ln S_T$. The moment is finite if and only if the CF is well-defined at $u = -ip$, i.e., at imaginary part $\text{Im}(u) = -p$.

    The strip of analyticity of $\phi$ is:

    $$
    \mathcal{S} = \{u \in \mathbb{C} : p^*_- < -\text{Im}(u) < p^*_+\}
    $$

    The moment $\mathbb{E}[S_T^p]$ is finite for $p^*_- < p < p^*_+$ and infinite for $p > p^*_+$ or $p < p^*_-$.

    **Connection to the Carr-Madan FFT method:** The Carr-Madan formula computes the call price via:

    $$
    c(k) = \frac{e^{-\alpha k}}{\pi}\int_0^\infty e^{-iuk}\,\frac{e^{-rT}\phi(u - i(\alpha + 1), T)}{\alpha^2 + \alpha - u^2 + iu(2\alpha + 1)}\,du
    $$

    This requires evaluating $\phi$ at $u - i(\alpha + 1)$, where $\text{Im}(u - i(\alpha+1)) = -(\alpha + 1)$. For this to lie inside the strip of analyticity, we need:

    $$
    \alpha + 1 < p^*_+
    $$

    **For $p^*_+ = 8$:** The maximal damping parameter is:

    $$
    \alpha < p^*_+ - 1 = 8 - 1 = 7
    $$

    Any $\alpha \in (0, 7)$ is valid. The typical choice $\alpha = 1.5$ satisfies $1.5 < 7$ easily. However, if $p^*_+$ were close to 2 (e.g., $p^*_+ = 2.5$), then $\alpha < 1.5$ would be required, and the integrand would decay more slowly, requiring more quadrature points for accurate evaluation.

---

**Exercise 3.** For $\rho = 0$ (no leverage), show that the critical moment formula simplifies and $p^*_+$ is maximized. Why does negative $\rho$ decrease $p^*_+$ and thus make moment explosions more restrictive?

??? success "Solution to Exercise 3"
    For $\rho = 0$, the quadratic $\gamma^2(p) = 0$ becomes:

    $$
    (1 - 0)\sigma_v^2\,p^2 + (0 + \sigma_v)\sigma_v\,p - \kappa^2 = 0
    $$

    $$
    \sigma_v^2\,p^2 + \sigma_v^2\,p - \kappa^2 = 0
    $$

    $$
    p^2 + p - \frac{\kappa^2}{\sigma_v^2} = 0
    $$

    By the quadratic formula:

    $$
    p = \frac{-1 + \sqrt{1 + 4\kappa^2/\sigma_v^2}}{2}
    $$

    (taking the positive root). This is maximized over $\rho$ because:

    The general formula for $p^*_+$ depends on $\rho$ through the coefficient $(2\kappa\rho + \sigma_v)\sigma_v$ and the leading term $(1 - \rho^2)\sigma_v^2$. To see that $\rho = 0$ maximizes $p^*_+$, consider the discriminant:

    $$
    \gamma^2(p) = \kappa^2 - (2\kappa\rho + \sigma_v)\sigma_v\,p + (\rho^2 - 1)\sigma_v^2\,p^2
    $$

    For fixed $p > 1$, the last term $(\rho^2 - 1)\sigma_v^2 p^2 \leq 0$ is most negative when $\rho = 0$ (i.e., $|\rho^2 - 1|$ is maximized). The middle term $-(2\kappa\rho + \sigma_v)\sigma_v p$ is minimized (most negative, hence most restrictive) when $\rho < 0$ (since $2\kappa\rho < 0$ makes the overall coefficient more negative for $p > 0$).

    **Why negative $\rho$ decreases $p^*_+$:** When $\rho < 0$, large downward moves in $x_t$ are correlated with increases in $V_t$. Higher variance leads to even larger moves, creating a feedback loop that fattens the left tail. For the right tail (which determines $p^*_+$), negative $\rho$ means that large upward moves are associated with *decreasing* variance. However, the overall effect of the correlation is to create asymmetry in the tails and, for the standard parametrization with $\rho < 0$, the upper critical moment is reduced. Intuitively, the leverage effect amplifies extreme events in both directions (through the second-order interaction of variance randomness and correlation), making higher moments explode at a lower threshold.

---

**Exercise 4.** The Lee moment formula relates the slope of the implied volatility smile at extreme strikes to the critical moment: $\lim_{k \to \infty} \sigma^2(k)\tau / k = 2 - 4(\sqrt{p^*_+(p^*_+ - 1)} - p^*_+)$ where $k = \log(K/F)$. For $p^*_+ = 10$, compute the right-wing slope and interpret it as the decay rate of the right tail of the return distribution.

??? success "Solution to Exercise 4"
    The Lee (2001) moment formula states that the right-wing slope of the implied volatility smile is related to the critical moment by:

    $$
    \lim_{k \to \infty} \frac{\sigma^2(k)\,\tau}{k} = \psi(p^*_+)
    $$

    where $k = \ln(K/F)$ is the log-moneyness (with $F$ the forward price) and:

    $$
    \psi(p) = 2 - 4\left(\sqrt{p(p-1)} - p\right) = 2 - 4\sqrt{p(p-1)} + 4p
    $$

    For $p^*_+ = 10$:

    $$
    \sqrt{p^*_+(p^*_+ - 1)} = \sqrt{10 \cdot 9} = \sqrt{90} = 3\sqrt{10} \approx 9.4868
    $$

    $$
    \psi(10) = 2 - 4(9.4868 - 10) = 2 - 4(-0.5132) = 2 + 2.0528 = 4.0528
    $$

    Wait -- let us recompute using the exact Lee formula. The standard form is:

    $$
    \limsup_{k \to +\infty} \frac{\sigma^2(k)\,\tau}{k} = \psi(p^*_+)
    $$

    where $\psi(p) = 2 - 4(\sqrt{p(p-1)} - p)$ for $p > 1$. We have:

    $$
    \psi(10) = 2 - 4(\sqrt{90} - 10) = 2 - 4(9.4868 - 10) = 2 + 2.0528 \approx 4.053
    $$

    However, the Lee formula is typically written as:

    $$
    \beta_R = \limsup_{k \to +\infty} \frac{\sigma_{\text{BS}}^2(k) T}{k}
    $$

    with $\beta_R = \psi(p^*_+)$ where $\psi(p) = 2 - 4(\sqrt{p(p-1)} - p)$.

    **Interpretation:** The right-wing slope $\beta_R \approx 4.05$ means that for very high strikes ($k \to +\infty$), the total implied variance $\sigma^2(k)\tau$ grows linearly in $k$ with slope approximately $4.05$. This is a relatively gentle slope, reflecting the fact that $p^*_+ = 10$ is large (many moments exist), so the right tail of the return distribution decays relatively quickly.

    If $p^*_+$ were smaller (e.g., $p^*_+ = 3$), the slope would be:

    $$
    \psi(3) = 2 - 4(\sqrt{6} - 3) = 2 - 4(2.449 - 3) = 2 + 2.204 = 4.204
    $$

    A lower $p^*_+$ gives a steeper right-wing slope, meaning the implied volatility smile rises more steeply at high strikes, consistent with heavier right tails.

    The Lee moment formula provides a model-free link between the tail behavior of option prices (observable from the smile) and the moment structure of the underlying return distribution.

---

**Exercise 5.** During calibration, the optimizer may propose parameters with very high $\sigma_v$ or very negative $\rho$, leading to $p^*_+ < 2$. Explain why this causes numerical problems in Fourier pricing and describe how to impose $p^*_+ > \alpha + 1$ as a constraint in the optimization.

??? success "Solution to Exercise 5"
    **The problem with $p^*_+ < 2$:** If the calibrated parameters yield $p^*_+ < 2$, then $\mathbb{E}[S_T^2] = \infty$, meaning the second moment of the asset price is infinite. For Fourier pricing:

    - **Carr-Madan method:** Requires $\alpha + 1 < p^*_+$. With $p^*_+ < 2$, we need $\alpha < 1$. But $\alpha$ must be positive and large enough for the integrand to decay, so $\alpha \in (0, 1)$ severely limits the method's effectiveness. For $\alpha$ close to zero, the integrand decays slowly, requiring many quadrature points and introducing numerical error.

    - **Gil-Pelaez method:** Evaluates $\phi(u, T)$ on the real line ($\text{Im}(u) = 0$), which always lies in the strip. But the decomposition into $P_1$ and $P_2$ probabilities requires evaluating $\phi(u - i, T)$ (shift by $-i$), which needs $1 < p^*_+$. If $p^*_+ < 1$, even the Gil-Pelaez formula fails.

    - **Numerical instability:** Near the boundary of the strip of analyticity, the CF oscillates violently and the Riccati solution $D(\tau, u)$ nearly blows up, causing large numerical errors in the exponent.

    **Imposing the constraint in calibration:** The constraint $p^*_+ > \alpha + 1$ can be enforced as follows:

    1. **Hard constraint:** Include $p^*_+(\kappa, \sigma_v, \rho) > \alpha + 1$ as an inequality constraint in the optimization. Since $p^*_+$ has a closed-form expression (the positive root of the quadratic), its gradient with respect to the parameters can be computed analytically, making it compatible with gradient-based optimizers.

    2. **Penalty method:** Add a barrier term to the objective:

        $$
        \mathcal{L}_{\text{total}} = \mathcal{L}_{\text{fit}} + \lambda \cdot \max(0, \alpha + 1 - p^*_+)^2
        $$

        This penalizes parameter vectors that violate the integrability condition.

    3. **Parameter bounds:** Since $p^*_+$ decreases with $\sigma_v$ and with $|\rho|$, one can impose upper bounds on $\sigma_v$ and $|\rho|$ that guarantee $p^*_+ > \alpha + 1$. For example, requiring $\sigma_v < 2\kappa / (\alpha + 1)$ (a rough sufficient condition) prevents the problem.

    In practice, most calibrated parameters give $p^*_+ \gg 2$ (values of $5$--$20$ are typical), so this constraint is rarely binding. It becomes relevant only when fitting extreme short-dated smiles that demand very high $\sigma_v$.

---

**Exercise 6.** Compare moment explosion behavior in the Heston model to the Black-Scholes model. In Black-Scholes, show that $\mathbb{E}[S_T^p] < \infty$ for all real $p$ and all $T > 0$ (because the log-normal distribution has finite moments of all orders). What structural feature of the Heston model causes the breakdown of this property?

??? success "Solution to Exercise 6"
    **Black-Scholes model:** Under Black-Scholes, $\ln S_T = \ln S_0 + (r - \frac{1}{2}\sigma^2)T + \sigma\sqrt{T}\,Z$ where $Z \sim N(0,1)$. Therefore:

    $$
    S_T^p = S_0^p \exp\!\left(p(r - \tfrac{1}{2}\sigma^2)T + p\sigma\sqrt{T}\,Z\right)
    $$

    Taking expectations:

    $$
    \mathbb{E}[S_T^p] = S_0^p \exp\!\left(p(r - \tfrac{1}{2}\sigma^2)T\right) \cdot \mathbb{E}\!\left[\exp(p\sigma\sqrt{T}\,Z)\right]
    $$

    The moment generating function of a standard normal $Z$ is $\mathbb{E}[e^{aZ}] = e^{a^2/2}$ for all real $a$. Setting $a = p\sigma\sqrt{T}$:

    $$
    \mathbb{E}[S_T^p] = S_0^p \exp\!\left(p(r - \tfrac{1}{2}\sigma^2)T + \tfrac{1}{2}p^2\sigma^2 T\right)
    $$

    $$
    = S_0^p \exp\!\left(prT + \tfrac{1}{2}p(p-1)\sigma^2 T\right) < \infty
    $$

    for all real $p$ and all $T > 0$. The log-normal distribution has finite moments of all orders. Equivalently, the strip of analyticity is the entire complex plane, and the critical moment $p^*_+ = +\infty$.

    **Heston model:** The key structural difference is that the exponent in $S_T = \exp(x_T)$ involves a stochastic integral $\int_0^T \sqrt{V_t}\,dW_t$ where the integrand $\sqrt{V_t}$ is itself random. Computing $\mathbb{E}[S_T^p]$ requires:

    $$
    \mathbb{E}[S_T^p] = \mathbb{E}\!\left[\exp\!\left(p\int_0^T \sqrt{V_t}\,dW_t - \tfrac{p}{2}\int_0^T V_t\,dt + p(r-q)T\right)\right]
    $$

    Unlike the Black-Scholes case, the "variance" of the stochastic integral $\int_0^T V_t\,dt$ is itself random and unbounded. The CIR process $V_t$ has a gamma stationary distribution with support on $[0, \infty)$, so the integrated variance $\int_0^T V_t\,dt$ can be arbitrarily large. For large $p$, the exponential amplification $e^{p\int \sqrt{V}\,dW}$ dominates, and the expectation diverges.

    More precisely, the moment $\mathbb{E}[S_T^p] = \phi(-ip, T) = \exp(C(T, -ip) + D(T, -ip)v_0 + px_0)$ is finite only when the Riccati ODE for $D(\tau, -ip)$ does not blow up before $\tau = T$. For large $p$, the quadratic coefficient $\frac{1}{2}\sigma_v^2$ and the forcing term $\frac{1}{2}p(1+p)$ in the Riccati equation cause $D$ to reach a pole in finite time, making the characteristic function infinite.

    **Summary:** The structural feature causing moment explosion in Heston is the **stochastic variance**: the randomness of $V_t$ creates a random effective volatility for the log-return, and the CIR process allows $V_t$ to take very large values. The exponential dependence of $S_T$ on the integrated variance means that rare events with persistently high variance produce extreme values of $S_T^p$ that overwhelm the averaging in the expectation. In Black-Scholes, the variance is constant, so this amplification mechanism does not exist.
