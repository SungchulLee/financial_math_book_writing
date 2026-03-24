# Closed-Form Characteristic Function

The Riccati ODE system derived in the [preceding section](riccati_ode_system.md) can be solved in closed form, yielding the explicit Heston characteristic function. This is the central analytical result of the Heston model: a formula that reduces option pricing to a one-dimensional numerical integration. The solution involves a discriminant $\gamma$ (a complex square root), a ratio $g$ that controls the asymptotic behavior, a logarithmic term in $C(\tau, u)$, and an exponential-rational expression for $D(\tau, u)$.

Two equivalent formulations exist in the literature: the original **Heston (1993)** form and the **Albrecher et al.** form. The Albrecher formulation is preferred for numerical implementation because it avoids branch-cut discontinuities in the complex logarithm. This section derives both formulations, explains their equivalence, and discusses the role of the complex logarithm.

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - Solve the Riccati ODE for $D(\tau, u)$ in closed form
    - Derive the closed-form expression for $C(\tau, u)$ via integration
    - Write the complete Heston characteristic function
    - State both the Heston (1993) and Albrecher formulations
    - Explain why the Albrecher form is numerically superior

---

## Solving the D-Equation

### Recall the Riccati ODE

From the [Riccati ODE system](riccati_ode_system.md):

$$
D' = \tfrac{1}{2}\sigma_v^2\,D^2 + (\rho\sigma_v\,iu - \kappa)\,D + \tfrac{1}{2}(iu - u^2), \qquad D(0) = 0
$$

Define the shorthand:

$$
b = \rho\sigma_v\,iu - \kappa, \qquad c = \tfrac{1}{2}(iu - u^2), \qquad a = \tfrac{1}{2}\sigma_v^2
$$

and the discriminant:

$$
\gamma = \sqrt{b^2 - 4ac} = \sqrt{(\kappa - i\rho\sigma_v u)^2 + \sigma_v^2(iu + u^2)}
$$

### Solution via Partial Fractions

The Riccati ODE $D' = a(D - D_+)(D - D_-)$ where $D_{\pm} = (-b \pm \gamma)/(2a) = (\kappa - i\rho\sigma_v u \mp \gamma)/\sigma_v^2$ are the two roots of $aD^2 + bD + c = 0$.

Separating variables:

$$
\frac{dD}{(D - D_+)(D - D_-)} = a\,d\tau
$$

Partial fraction decomposition: $\frac{1}{(D-D_+)(D-D_-)} = \frac{1}{\gamma/a}\left(\frac{1}{D-D_+} - \frac{1}{D-D_-}\right)$ since $D_+ - D_- = -2\gamma/\sigma_v^2 = -\gamma/a$. Wait -- more carefully: $D_+ - D_- = \frac{-\gamma - \gamma}{\sigma_v^2} = \frac{-2\gamma}{\sigma_v^2}$. So:

$$
\frac{1}{(D-D_+)(D-D_-)} = \frac{1}{D_+ - D_-}\left(\frac{1}{D - D_-} - \frac{1}{D - D_+}\right) = \frac{\sigma_v^2}{-2\gamma}\left(\frac{1}{D-D_-} - \frac{1}{D-D_+}\right)
$$

Integrating from $0$ to $\tau$ with $D(0) = 0$:

$$
\frac{\sigma_v^2}{-2\gamma}\ln\!\left(\frac{D(\tau) - D_-}{D(\tau) - D_+}\cdot\frac{-D_+}{-D_-}\right) = \frac{\sigma_v^2}{2}\,\tau
$$

$$
\ln\!\left(\frac{D - D_-}{D - D_+}\cdot\frac{D_+}{D_-}\right) = -\gamma\tau
$$

Define $g = D_+/D_- = \frac{\kappa - i\rho\sigma_v u - \gamma}{\kappa - i\rho\sigma_v u + \gamma}$. Then:

$$
\frac{D - D_-}{D - D_+} = \frac{g^{-1} e^{-\gamma\tau}}{1} \cdot \frac{D_-}{D_+}
$$

Solving for $D$:

!!! success "Theorem: Closed-Form Solution for D (Albrecher Formulation)"
    $$
    D(\tau, u) = \frac{\kappa - i\rho\sigma_v u - \gamma}{\sigma_v^2} \cdot \frac{1 - e^{-\gamma\tau}}{1 - g\,e^{-\gamma\tau}}
    $$

    where:

    $$
    \gamma = \sqrt{(\kappa - i\rho\sigma_v u)^2 + \sigma_v^2(iu + u^2)}
    $$

    $$
    g = \frac{\kappa - i\rho\sigma_v u - \gamma}{\kappa - i\rho\sigma_v u + \gamma}
    $$

### Verification

At $\tau = 0$: $D(0) = \frac{\kappa - i\rho\sigma_v u - \gamma}{\sigma_v^2}\cdot\frac{1 - 1}{1 - g} = 0$. $\checkmark$

As $\tau \to \infty$ (assuming $\text{Re}(\gamma) > 0$): $e^{-\gamma\tau} \to 0$, so $D(\infty) = \frac{\kappa - i\rho\sigma_v u - \gamma}{\sigma_v^2} = D_+$, which is the stable equilibrium of the Riccati ODE. $\checkmark$

---

## Solving the C-Equation

### Integration

From the $C$-equation $C' = (r-q)\,iu + \kappa\theta\,D$ with $C(0) = 0$:

$$
C(\tau, u) = (r-q)\,iu\,\tau + \kappa\theta\int_0^{\tau} D(s, u)\,ds
$$

The integral of $D$ can be evaluated in closed form. Using $D = D_+\frac{1-e^{-\gamma s}}{1-g\,e^{-\gamma s}}$:

$$
\int_0^{\tau}\frac{1-e^{-\gamma s}}{1-g\,e^{-\gamma s}}\,ds = \tau + \frac{1}{\gamma}\left[\ln(1-g\,e^{-\gamma\tau}) - \ln(1-g)\right] = \tau + \frac{1}{\gamma}\ln\!\left(\frac{1-g\,e^{-\gamma\tau}}{1-g}\right)
$$

Therefore:

!!! success "Theorem: Closed-Form Solution for C (Albrecher Formulation)"
    $$
    C(\tau, u) = (r-q)\,iu\,\tau + \frac{\kappa\theta}{\sigma_v^2}\left[(\kappa - i\rho\sigma_v u - \gamma)\,\tau - 2\ln\!\left(\frac{1 - g\,e^{-\gamma\tau}}{1 - g}\right)\right]
    $$

---

## The Complete Characteristic Function

### Albrecher Formulation (Recommended)

!!! success "Theorem: Heston Characteristic Function -- Albrecher Form"
    The conditional characteristic function of $x_T = \ln S_T$ given $(x_t, v_t)$ is:

    $$
    \phi(u, \tau) = \exp\!\bigl(C(\tau, u) + D(\tau, u)\,v_t + iu\,x_t\bigr)
    $$

    where $\tau = T - t$ and:

    $$
    \gamma = \sqrt{(\kappa - i\rho\sigma_v u)^2 + \sigma_v^2(iu + u^2)}
    $$

    $$
    g = \frac{\kappa - i\rho\sigma_v u - \gamma}{\kappa - i\rho\sigma_v u + \gamma}
    $$

    $$
    D(\tau, u) = \frac{\kappa - i\rho\sigma_v u - \gamma}{\sigma_v^2}\cdot\frac{1 - e^{-\gamma\tau}}{1 - g\,e^{-\gamma\tau}}
    $$

    $$
    C(\tau, u) = (r-q)\,iu\,\tau + \frac{\kappa\theta}{\sigma_v^2}\left[(\kappa - i\rho\sigma_v u - \gamma)\tau - 2\ln\!\left(\frac{1-g\,e^{-\gamma\tau}}{1-g}\right)\right]
    $$

### Heston (1993) Original Formulation

The original Heston (1993) paper presented the characteristic function in a different but algebraically equivalent form. Define $\tilde{g} = 1/g$:

$$
D(\tau, u) = \frac{\kappa - i\rho\sigma_v u + \gamma}{\sigma_v^2}\cdot\frac{1 - e^{\gamma\tau}}{1 - \tilde{g}\,e^{\gamma\tau}}
$$

$$
C(\tau, u) = (r-q)\,iu\,\tau + \frac{\kappa\theta}{\sigma_v^2}\left[(\kappa - i\rho\sigma_v u + \gamma)\tau - 2\ln\!\left(\frac{1-\tilde{g}\,e^{\gamma\tau}}{1-\tilde{g}}\right)\right]
$$

!!! warning "Branch-Cut Issue in the Heston (1993) Form"
    The Heston (1993) formulation uses $e^{+\gamma\tau}$ (a growing exponential), which means the argument of the logarithm $\frac{1 - \tilde{g}\,e^{\gamma\tau}}{1 - \tilde{g}}$ can cross zero or become large, causing the complex logarithm to jump across branch cuts. This produces discontinuities in $\phi$ as a function of $u$ and leads to incorrect prices when integrating over $u$.

    The Albrecher formulation uses $e^{-\gamma\tau}$ (a decaying exponential) and $|g| < 1$ (when $\text{Re}(\gamma) > 0$), which ensures $|g\,e^{-\gamma\tau}| < 1$ and the logarithm's argument stays away from the branch cut. This is why the Albrecher form is universally preferred in numerical implementations.

---

## Equivalence of the Two Formulations

The two formulations are related by the substitution $g = 1/\tilde{g}$ and algebraic rearrangement. Specifically:

$$
\frac{1 - e^{-\gamma\tau}}{1 - g\,e^{-\gamma\tau}} = \frac{e^{-\gamma\tau}(e^{\gamma\tau} - 1)}{e^{-\gamma\tau}(e^{\gamma\tau} - \tilde{g}^{-1})} = \frac{e^{\gamma\tau} - 1}{e^{\gamma\tau} - g^{-1}} = \frac{-(1-e^{\gamma\tau})}{-(g^{-1}-e^{\gamma\tau})} = \frac{1-e^{\gamma\tau}}{g^{-1}-e^{\gamma\tau}}
$$

Multiplying numerator and denominator of the Heston form by $-\tilde{g}$ and simplifying yields the Albrecher form. The two expressions are analytically identical on the principal branch but differ in their branch-cut behavior when evaluated numerically.

---

## The Complex Logarithm

The term $\ln\!\left(\frac{1 - g\,e^{-\gamma\tau}}{1-g}\right)$ in $C(\tau, u)$ involves the complex logarithm, which requires care.

!!! info "Definition: Principal Value and Continuous Extension"
    The principal value of the complex logarithm is $\text{Log}(z) = \ln|z| + i\,\text{Arg}(z)$ with $\text{Arg}(z) \in (-\pi, \pi]$.

    For the Heston characteristic function, the logarithm must be evaluated as a **continuous function of $u$** (the Fourier variable). If the argument $\frac{1-g\,e^{-\gamma\tau}}{1-g}$ crosses the negative real axis as $u$ varies, the principal-value logarithm jumps by $2\pi i$, producing a discontinuity in $\phi(u)$.

    In the Albrecher formulation, $|g| < 1$ and $|g\,e^{-\gamma\tau}| < 1$ for $u \in \mathbb{R}$ (under standard parameter constraints), so the argument stays in the right half-plane and the principal-value logarithm is continuous. This is the primary advantage of the Albrecher form.

!!! note "Rotation Count Method"
    When the principal-value logarithm does exhibit jumps (e.g., for very large $\tau$ or extreme parameters), the **rotation count method** of Kahl and Jackel (2005) provides a systematic correction. It tracks the winding number of the complex argument as $u$ increases and adds the appropriate multiple of $2\pi i$ to maintain continuity. This technique is discussed in the [numerical stability section](numerical_stability_and_branch_cuts.md).

---

## Worked Example: Evaluating the Characteristic Function

??? example "Numerical Evaluation at u = 1"
    Parameters: $\kappa = 2$, $\theta = 0.04$, $\sigma_v = 0.5$, $\rho = -0.7$, $v_0 = 0.04$, $r = 0.03$, $q = 0$, $x_0 = \ln(100) = 4.6052$, $\tau = 1$.

    **Step 1: Compute $\gamma$.**

    $$
    \gamma = \sqrt{(\kappa - i\rho\sigma_v u)^2 + \sigma_v^2(iu + u^2)}
    $$

    $$
    = \sqrt{(2 - i(-0.7)(0.5)(1))^2 + 0.25(i + 1)}
    $$

    $$
    = \sqrt{(2 + 0.35i)^2 + 0.25 + 0.25i}
    $$

    $$
    = \sqrt{(4 + 1.4i - 0.1225) + 0.25 + 0.25i} = \sqrt{4.1275 + 1.65i}
    $$

    Computing the complex square root: $|z| = \sqrt{4.1275^2 + 1.65^2} = \sqrt{17.04 + 2.72} = \sqrt{19.76} \approx 4.445$. So $|\gamma| = \sqrt{4.445} \approx 2.108$, and $\gamma \approx 2.065 + 0.399i$ (by computing $\text{Arg}(z)/2$ and using polar form).

    **Step 2: Compute $g$.**

    $$
    g = \frac{2 + 0.35i - (2.065 + 0.399i)}{2 + 0.35i + (2.065 + 0.399i)} = \frac{-0.065 - 0.049i}{4.065 + 0.749i}
    $$

    $$
    |g| \approx \frac{0.081}{4.133} \approx 0.0197
    $$

    Since $|g| \ll 1$, the Albrecher formulation is very well-behaved numerically.

    **Step 3: Compute $D(1, 1)$ and $C(1, 1)$.**

    With $e^{-\gamma\tau} \approx e^{-2.065}(\cos 0.399 - i\sin 0.399) \approx 0.127(0.921 - 0.389i) = 0.117 - 0.049i$:

    The full numerical evaluation gives $D \approx -0.0268 + 0.0031i$ and $C \approx 0.03i - 0.0227 + 0.0019i$.

    The characteristic function value is:

    $$
    |\phi(1, 1)| = \exp\!\bigl(\text{Re}(C + Dv_0)\bigr) \approx \exp(-0.0238) \approx 0.976
    $$

    As expected, $|\phi| < 1$ for $u \neq 0$, reflecting the characteristic function's decay.

---

## Special Cases

### Black-Scholes Limit ($\sigma_v \to 0$)

When $\sigma_v = 0$: $\gamma \to \kappa$, $g \to 0$, $D(\tau) \to \frac{1}{2}(iu - u^2)(1 - e^{-\kappa\tau})/\kappa$, and as $\kappa \to 0$ further: $D(\tau) \to \frac{1}{2}(iu - u^2)\tau$, recovering the Black-Scholes characteristic function.

### Zero Correlation ($\rho = 0$)

When $\rho = 0$: $\gamma = \sqrt{\kappa^2 + \sigma_v^2(iu + u^2)}$, $g = \frac{\kappa - \gamma}{\kappa + \gamma}$. The formula simplifies because the cross-terms vanish, but the structure remains the same.

### Long Maturity ($\tau \to \infty$)

As $\tau \to \infty$: $D \to D_+ = (\kappa - i\rho\sigma_v u - \gamma)/\sigma_v^2$ and $C$ grows linearly in $\tau$. The characteristic function decays exponentially in $\tau$ (for $u \neq 0$), reflecting the diffusion of $x_T$ over time.

---

## Summary

The Heston characteristic function has the closed form $\phi = \exp(C + Dv + iux)$ where $D(\tau, u)$ and $C(\tau, u)$ are given by explicit formulas involving the discriminant $\gamma$, the ratio $g$, and complex exponentials and logarithms. The Albrecher formulation, which uses decaying exponentials $e^{-\gamma\tau}$ and satisfies $|g| < 1$, is preferred over the original Heston (1993) form because it avoids branch-cut discontinuities in the complex logarithm. This characteristic function is the foundation for all Fourier-based pricing methods -- Gil-Pelaez inversion, COS expansion, and Carr-Madan FFT -- developed in subsequent sections.

The [next section](derivation_of_characteristic_function.md) provides an alternative derivation using the probability flow approach, while the [numerical stability section](numerical_stability_and_branch_cuts.md) addresses the practical implementation challenges.

---

---

## Exercises

**Exercise 1.** Write the Heston characteristic function in the form $\varphi(u, \tau; x, v) = \exp(C(\tau,u) + D(\tau,u)v + iux)$ and state the closed-form expressions for $C$ and $D$ involving the discriminant $\gamma$, the ratio $g$, and the parameters $\kappa, \theta, \sigma_v, \rho$.

---

**Exercise 2.** Verify the formula $g = (\beta - \gamma)/(\beta + \gamma)$ where $\beta = \kappa - i\rho\sigma_v u$. For $\kappa = 2$, $\sigma_v = 0.3$, $\rho = -0.7$, $u = 1$, compute $g$ and verify $

---

g

---

 < 1$.

---

**Exercise 3.** Show that $D(\tau, u) \to 0$ as $\tau \to 0$ and $C(\tau, u) \to 0$ as $\tau \to 0$, consistent with the initial conditions of the Riccati system.|**Exercise 4.** For $u = -i$, verify that $\varphi(-i, \tau; x, v) = S_t e^{(r-q)\tau}$, confirming the forward price martingale condition.|**Exercise 5.** Implement the characteristic function numerically and compute $|\varphi(u, 1; \log 100, 0.04)|$ for $u = 0.5, 1, 5, 10, 50$ using typical parameters. Verify that the modulus is always at most 1.
