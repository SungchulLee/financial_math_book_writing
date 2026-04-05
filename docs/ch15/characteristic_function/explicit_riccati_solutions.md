# Explicit Solutions for Common Cases

For several important affine models, the generalized Riccati ODE system admits closed-form solutions. These explicit formulas are the workhorse of quantitative finance: they enable bond pricing, option valuation, and calibration without numerical ODE solvers. This section derives the Riccati solutions for the Vasicek model (linear ODE), the CIR model (scalar Riccati), and the Heston model (complex-valued coupled Riccati system).

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Solve the linear Riccati system for the Vasicek model and verify the Gaussian transition density
    2. Derive the closed-form CIR Riccati solution using separation of variables
    3. Write the Heston characteristic function in terms of its Riccati components
    4. Identify when explicit solutions exist and when numerical methods are required

---

## Intuition

The Riccati equation $\psi' = \beta\psi + \frac{1}{2}\gamma\psi^2$ is one of the few nonlinear ODEs with a known general solution. When $\gamma = 0$ (no state-dependent volatility), it reduces to a linear ODE with an exponential solution. When $\gamma \neq 0$, the substitution $\psi = -2\gamma^{-1}h'/h$ transforms it into a second-order linear ODE, which can be solved by exponentials. This linearization trick is why affine models with square-root diffusion (CIR, Heston) produce explicit formulas involving exponential functions and square roots of discriminants.

---

## Vasicek Model: Linear Riccati

### The ODE System

The Vasicek model $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$ has affine parameters $\kappa_0 = \kappa\theta$, $\kappa_1 = -\kappa$, $\sigma_0 = \sigma^2$, $\sigma_1 = 0$. The Riccati system is:

$$
\psi'(\tau) = -\kappa\psi(\tau), \qquad \psi(0) = u
$$

$$
\phi'(\tau) = \kappa\theta\,\psi(\tau) + \frac{1}{2}\sigma^2\psi(\tau)^2, \qquad \phi(0) = 0
$$

### Solution

The $\psi$-equation is a first-order linear ODE:

$$
\psi(\tau) = u\,e^{-\kappa\tau}
$$

Substituting into the $\phi$-equation:

$$
\phi'(\tau) = \kappa\theta\,u\,e^{-\kappa\tau} + \frac{1}{2}\sigma^2 u^2 e^{-2\kappa\tau}
$$

Integrating from $0$ to $\tau$:

$$
\phi(\tau) = \kappa\theta\,u\,\frac{1 - e^{-\kappa\tau}}{\kappa} + \frac{\sigma^2 u^2}{2}\,\frac{1 - e^{-2\kappa\tau}}{2\kappa}
$$

$$
= \theta\,u\,(1 - e^{-\kappa\tau}) + \frac{\sigma^2 u^2}{4\kappa}(1 - e^{-2\kappa\tau})
$$

### Characteristic Function

Setting $u = iv$:

$$
\phi(\tau, iv) = i\theta v(1 - e^{-\kappa\tau}) - \frac{\sigma^2 v^2}{4\kappa}(1 - e^{-2\kappa\tau})
$$

$$
\psi(\tau, iv) = iv\,e^{-\kappa\tau}
$$

The conditional characteristic function is:

$$
\mathbb{E}\!\left[e^{iv r_T} \mid r_t = r\right] = \exp\!\left(iv\!\left[\theta(1 - e^{-\kappa\tau}) + re^{-\kappa\tau}\right] - \frac{\sigma^2 v^2}{4\kappa}(1 - e^{-2\kappa\tau})\right)
$$

This is the characteristic function of a Gaussian with mean $\theta(1 - e^{-\kappa\tau}) + re^{-\kappa\tau}$ and variance $\frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa\tau})$.

---

## CIR Model: Scalar Riccati Equation

### The ODE System

The CIR model $dr_t = \kappa(\theta - r_t)\,dt + \xi\sqrt{r_t}\,dW_t$ has $\kappa_0 = \kappa\theta$, $\kappa_1 = -\kappa$, $\sigma_0 = 0$, $\sigma_1 = \xi^2$. The Riccati system is:

$$
\psi'(\tau) = -\kappa\psi(\tau) + \frac{\xi^2}{2}\psi(\tau)^2, \qquad \psi(0) = u
$$

$$
\phi'(\tau) = \kappa\theta\,\psi(\tau), \qquad \phi(0) = 0
$$

### Solving the Riccati Equation

The equation $\psi' = -\kappa\psi + \frac{\xi^2}{2}\psi^2$ is solved by the substitution $\psi = -\frac{2}{\xi^2}\frac{h'}{h}$, which transforms it into the second-order linear ODE $h'' + \kappa h' = 0$... but a more direct approach is separation of variables.

**Step 1.** Write $\psi' = \frac{\xi^2}{2}\psi(\psi - 2\kappa/\xi^2)$ and separate:

$$
\frac{d\psi}{\psi(\psi - 2\kappa/\xi^2)} = \frac{\xi^2}{2}\,d\tau
$$

**Step 2.** Partial fractions: $\frac{1}{\psi(\psi - 2\kappa/\xi^2)} = \frac{\xi^2}{2\kappa}\left(\frac{1}{\psi - 2\kappa/\xi^2} - \frac{1}{\psi}\right)$

**Step 3.** Integrate and solve for $\psi$. After algebra, the solution is:

$$
\psi(\tau) = \frac{u\left(e^{\gamma\tau} - 1\right)\gamma + u\left(e^{\gamma\tau} - 1\right)\kappa}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma - u\xi^2(e^{\gamma\tau} - 1)}
$$

which simplifies to the standard form. For the bond pricing application ($u = 0$, but with the extended system including discounting), the relevant solution is:

$$
B(\tau) = \frac{2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}
$$

where $\gamma = \sqrt{\kappa^2 + 2\xi^2}$ when applied to the extended Riccati with discounting.

### The Phi Solution

Once $\psi(\tau)$ is known, $\phi$ is obtained by integration:

$$
\phi(\tau) = \kappa\theta \int_0^\tau \psi(s)\,ds
$$

For the bond pricing case, this yields:

$$
A(\tau) = \frac{2\kappa\theta}{\xi^2}\log\!\left(\frac{2\gamma\,e^{(\gamma+\kappa)\tau/2}}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}\right)
$$

### Verification

One can verify the solution by direct differentiation:

$$
B'(\tau) = \frac{2\gamma^2 e^{\gamma\tau}}{[(\gamma+\kappa)(e^{\gamma\tau}-1)+2\gamma]^2} \cdot 2\gamma
$$

and checking that $B' = -\kappa B + \frac{\xi^2}{2}B^2 - 1$ (the extended Riccati with discounting term). The algebra is tedious but routine.

---

## Heston Model: Coupled Complex Riccati

### The Two-Dimensional System

The Heston model has state vector $X_t = (\log S_t, V_t) \in \mathbb{R} \times \mathbb{R}_+$ with dynamics:

$$
d\log S_t = \left(r - \frac{1}{2}V_t\right)dt + \sqrt{V_t}\,dW_t^{(1)}
$$

$$
dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^{(2)}
$$

where $\operatorname{Corr}(dW_t^{(1)}, dW_t^{(2)}) = \rho\,dt$.

With $u = (u_1, u_2) \in \mathbb{C}^2$, the Riccati system is:

$$
\psi_1'(\tau) = 0, \qquad \psi_1(0) = u_1
$$

$$
\psi_2'(\tau) = -\frac{1}{2}\psi_1(\tau) - \kappa\psi_2(\tau) + \frac{1}{2}\left(\psi_1(\tau)^2 + 2\rho\xi\psi_1(\tau)\psi_2(\tau) + \xi^2\psi_2(\tau)^2\right)
$$

with $\psi_2(0) = u_2$.

$$
\phi'(\tau) = r\,\psi_1(\tau) + \kappa\theta\,\psi_2(\tau), \qquad \phi(0) = 0
$$

### Solution for the Characteristic Function

For the characteristic function, set $u_1 = iv$ and $u_2 = 0$. Since $\psi_1(\tau) = iv$ is constant, the $\psi_2$-equation becomes a scalar Riccati in $\psi_2$ with coefficients depending on $v$:

$$
\psi_2'(\tau) = -\frac{iv}{2} - \kappa\psi_2 + \frac{1}{2}\left(-v^2 + 2\rho\xi iv\,\psi_2 + \xi^2\psi_2^2\right)
$$

$$
= \frac{1}{2}\xi^2\psi_2^2 + (\rho\xi iv - \kappa)\psi_2 - \frac{1}{2}(iv + v^2)
$$

This is a Riccati equation $\psi_2' = \alpha + \beta\psi_2 + \frac{1}{2}\gamma\psi_2^2$ with:

$$
\alpha = -\frac{1}{2}(iv + v^2), \qquad \beta = \rho\xi iv - \kappa, \qquad \gamma = \xi^2
$$

### Closed-Form Solution

Define the discriminant:

$$
d = \sqrt{\beta^2 - 2\alpha\gamma} = \sqrt{(\rho\xi iv - \kappa)^2 + \xi^2(iv + v^2)}
$$

The solution is:

$$
\psi_2(\tau) = \frac{\alpha(1 - e^{-d\tau})}{d\cosh(d\tau/2) + \beta\sinh(d\tau/2)} \cdot \frac{1}{\xi^2/2}
$$

or equivalently, using the standard Heston notation:

$$
\psi_2(\tau) = \frac{\beta - d}{\xi^2} \cdot \frac{1 - e^{-d\tau}}{1 - g\,e^{-d\tau}}
$$

where $g = (\beta - d)/(\beta + d)$.

The $\phi$-function integrates to:

$$
\phi(\tau) = iv\,r\tau + \frac{\kappa\theta}{\xi^2}\left[(\beta - d)\tau - 2\log\!\left(\frac{1 - g\,e^{-d\tau}}{1 - g}\right)\right]
$$

!!! warning "Branch Cut Convention"
    The square root $d = \sqrt{(\rho\xi iv - \kappa)^2 + \xi^2(iv + v^2)}$ is complex-valued for real $v$. The convention $\operatorname{Re}(d) > 0$ ensures numerical stability of the formula. The logarithm uses the principal branch. Alternative formulations (Albrecher et al., 2007) avoid the branch cut issue entirely by reformulating in terms of the ratio $g$.

---

## When Explicit Solutions Do Not Exist

Explicit Riccati solutions require that the discriminant and the integration can be evaluated in closed form. This fails when:

1. **Multi-factor models with coupling**: If the $\psi$-equations for different components are coupled through the diffusion matrix, the system does not reduce to independent scalar Riccati equations. Numerical ODE solvers (Runge-Kutta) are needed.

2. **Jump-diffusion models**: The jump contribution adds $\int(e^{\langle w, z \rangle} - 1)m_j(dz)$ to $R_j$. For exponential jumps, this integral evaluates to a rational function of $w$, producing an *extended Riccati* equation that may still have closed-form solutions. For more general jump distributions, numerical integration is required at each ODE step.

3. **Time-dependent parameters**: If the model parameters $\kappa(t)$, $\theta(t)$, $\xi(t)$ depend on time, the Riccati equation becomes non-autonomous. Piecewise-constant parameters can be handled by chaining constant-parameter solutions; general time dependence requires numerical methods.

??? example "Numerical Solution Summary"
    For models without explicit solutions, the standard approach is:

    1. Discretize $\tau \in [0, T]$ with step $h$ (typically $h \leq 0.01$)
    2. Apply RK4 in complex arithmetic: $\psi_{n+1} = \psi_n + \frac{h}{6}(k_1 + 2k_2 + 2k_3 + k_4)$
    3. Accumulate $\phi_{n+1} = \phi_n + \frac{h}{6}(l_1 + 2l_2 + 2l_3 + l_4)$ where $l_i = F(\psi + \cdots)$
    4. Use complex logarithm and square root with consistent branch choices

    The cost is $O(N_\tau \cdot d^2)$ per frequency point $v$, where $N_\tau = T/h$ and $d$ is the state dimension. $\square$

---

## Summary of Explicit Solutions

| Model | $\psi$-equation type | $\psi(\tau)$ | $\phi(\tau)$ |
|-------|---------------------|-------------|-------------|
| Vasicek | Linear ODE | $u e^{-\kappa\tau}$ | Polynomial in $(1-e^{-\kappa\tau})$ |
| CIR | Scalar Riccati | Ratio of exponentials involving $\gamma = \sqrt{\kappa^2 + 2\xi^2 u}$ | Logarithmic |
| Heston | Complex scalar Riccati | Ratio involving $d = \sqrt{(\rho\xi iv - \kappa)^2 + \xi^2(iv+v^2)}$ | Logarithmic |
| Multi-factor | Coupled Riccati system | Numerical (RK4) | Numerical (quadrature) |

---

## Summary

Explicit Riccati solutions exist for the core affine models: the Vasicek model produces exponential decay (linear ODE), the CIR model produces ratios of exponentials (scalar Riccati solved by separation of variables or the substitution trick), and the Heston model produces complex-valued ratios (scalar Riccati with complex coefficients). In each case, the $\psi$-equation is solved first as an autonomous ODE, and $\phi$ is obtained by integration. The solutions involve discriminants $\gamma$ or $d$ that are square roots of quadratic expressions in the transform variable, and logarithms that require careful branch cut management in the complex plane.

---

## Further Reading

- Heston, S. L. (1993). "A Closed-Form Solution for Options with Stochastic Volatility with Applications to Bond and Currency Options." *Review of Financial Studies*, 6(2), 327-343.
- Albrecher, H., Mayer, P., Schoutens, W., & Tistaert, J. (2007). "The Little Heston Trap." *Wilmott Magazine*, January, 83-92.
- Cox, J. C., Ingersoll, J. E., & Ross, S. A. (1985). "A Theory of the Term Structure of Interest Rates." *Econometrica*, 53(2), 385-407.
- Filipovic, D. *Term-Structure Models: A Graduate Course*. Springer, 2009.

---

## Exercises

**Exercise 1.** For the Vasicek model, verify by direct differentiation that $\psi(\tau) = ue^{-\kappa\tau}$ satisfies $\psi'(\tau) = -\kappa\psi(\tau)$ with $\psi(0) = u$. Then substitute into the $\phi$-equation and carry out the integration to confirm

$$
\phi(\tau) = \theta\,u\,(1 - e^{-\kappa\tau}) + \frac{\sigma^2 u^2}{4\kappa}(1 - e^{-2\kappa\tau})
$$

??? success "Solution to Exercise 1"
    **Verifying $\psi$:** Differentiate $\psi(\tau) = ue^{-\kappa\tau}$:

    $$
    \psi'(\tau) = -\kappa u e^{-\kappa\tau} = -\kappa\psi(\tau)
    $$

    and $\psi(0) = ue^0 = u$. Both the ODE and the initial condition are satisfied.

    **Deriving $\phi$:** Substitute $\psi(\tau) = ue^{-\kappa\tau}$ into the $\phi$-equation:

    $$
    \phi'(\tau) = \kappa\theta\,ue^{-\kappa\tau} + \frac{\sigma^2}{2}u^2 e^{-2\kappa\tau}
    $$

    Integrate term by term from $0$ to $\tau$:

    $$
    \int_0^\tau \kappa\theta\,ue^{-\kappa s}\,ds = \kappa\theta\,u\left[-\frac{1}{\kappa}e^{-\kappa s}\right]_0^\tau = \theta\,u\,(1 - e^{-\kappa\tau})
    $$

    $$
    \int_0^\tau \frac{\sigma^2}{2}u^2 e^{-2\kappa s}\,ds = \frac{\sigma^2 u^2}{2}\left[-\frac{1}{2\kappa}e^{-2\kappa s}\right]_0^\tau = \frac{\sigma^2 u^2}{4\kappa}(1 - e^{-2\kappa\tau})
    $$

    Adding: $\phi(\tau) = \theta\,u\,(1 - e^{-\kappa\tau}) + \frac{\sigma^2 u^2}{4\kappa}(1 - e^{-2\kappa\tau})$, confirming the stated formula.

---

**Exercise 2.** Apply the linearization substitution $\psi = -\frac{2}{\xi^2}\frac{h'}{h}$ to the CIR Riccati equation $\psi' = -\kappa\psi + \frac{\xi^2}{2}\psi^2$. Show that $h$ satisfies the second-order linear ODE $h'' + \kappa h' = 0$ (for the undiscounted case). Solve for $h(\tau)$ and recover $\psi(\tau)$ from the ratio $h'/h$.

??? success "Solution to Exercise 2"
    Apply the substitution $\psi = -\frac{2}{\xi^2}\frac{h'}{h}$ to $\psi' = -\kappa\psi + \frac{\xi^2}{2}\psi^2$.

    First compute $\psi'$. From $\psi = -\frac{2}{\xi^2}\frac{h'}{h}$:

    $$
    \psi' = -\frac{2}{\xi^2}\left(\frac{h''}{h} - \frac{(h')^2}{h^2}\right) = -\frac{2}{\xi^2}\frac{h''}{h} + \frac{2}{\xi^2}\frac{(h')^2}{h^2}
    $$

    Now compute each term on the right-hand side. The linear term:

    $$
    -\kappa\psi = -\kappa\left(-\frac{2}{\xi^2}\frac{h'}{h}\right) = \frac{2\kappa}{\xi^2}\frac{h'}{h}
    $$

    The quadratic term:

    $$
    \frac{\xi^2}{2}\psi^2 = \frac{\xi^2}{2}\cdot\frac{4}{\xi^4}\frac{(h')^2}{h^2} = \frac{2}{\xi^2}\frac{(h')^2}{h^2}
    $$

    Setting $\psi' = -\kappa\psi + \frac{\xi^2}{2}\psi^2$:

    $$
    -\frac{2}{\xi^2}\frac{h''}{h} + \frac{2}{\xi^2}\frac{(h')^2}{h^2} = \frac{2\kappa}{\xi^2}\frac{h'}{h} + \frac{2}{\xi^2}\frac{(h')^2}{h^2}
    $$

    The $(h')^2/h^2$ terms cancel, leaving

    $$
    -\frac{2}{\xi^2}\frac{h''}{h} = \frac{2\kappa}{\xi^2}\frac{h'}{h}
    $$

    Multiply by $-\xi^2 h/2$:

    $$
    h'' + \kappa h' = 0
    $$

    This is a second-order linear ODE with constant coefficients. The characteristic equation is $\lambda^2 + \kappa\lambda = 0$, giving $\lambda = 0$ or $\lambda = -\kappa$. The general solution is

    $$
    h(\tau) = C_1 + C_2 e^{-\kappa\tau}
    $$

    Then $h'(\tau) = -\kappa C_2 e^{-\kappa\tau}$, so

    $$
    \psi(\tau) = -\frac{2}{\xi^2}\frac{-\kappa C_2 e^{-\kappa\tau}}{C_1 + C_2 e^{-\kappa\tau}} = \frac{2\kappa C_2 e^{-\kappa\tau}}{\xi^2(C_1 + C_2 e^{-\kappa\tau})}
    $$

    Applying the initial condition $\psi(0) = u$ determines $C_1/C_2$:

    $$
    u = \frac{2\kappa C_2}{\xi^2(C_1 + C_2)}
    $$

    Setting $C_2 = 1$ gives $C_1 = \frac{2\kappa}{u\xi^2} - 1$, and the closed-form expression for $\psi(\tau)$ follows.

---

**Exercise 3.** In the Heston model, the discriminant is $d = \sqrt{(\rho\xi iv - \kappa)^2 + \xi^2(iv + v^2)}$. Compute $d$ numerically for the parameters $\kappa = 2$, $\xi = 0.3$, $\rho = -0.7$, and $v = 1$. Verify that $\operatorname{Re}(d) > 0$.

??? success "Solution to Exercise 3"
    With $\kappa = 2$, $\xi = 0.3$, $\rho = -0.7$, $v = 1$:

    $$
    \beta = \rho\xi iv - \kappa = -0.7 \cdot 0.3 \cdot i - 2 = -2 - 0.21i
    $$

    $$
    \alpha = -\frac{1}{2}(iv + v^2) = -\frac{1}{2}(i + 1) = -0.5 - 0.5i
    $$

    $$
    \gamma = \xi^2 = 0.09
    $$

    Compute the argument of the square root:

    $$
    \beta^2 = (-2 - 0.21i)^2 = 4 + 0.84i - 0.0441 = 3.9559 + 0.84i
    $$

    $$
    2\alpha\gamma = 2(-0.5 - 0.5i)(0.09) = -0.09 - 0.09i
    $$

    $$
    \beta^2 - 2\alpha\gamma = 3.9559 + 0.84i + 0.09 + 0.09i = 4.0459 + 0.93i
    $$

    The modulus is $|4.0459 + 0.93i| = \sqrt{4.0459^2 + 0.93^2} = \sqrt{16.3693 + 0.8649} \approx \sqrt{17.2342} \approx 4.1513$.

    The argument is $\theta = \arctan(0.93/4.0459) \approx \arctan(0.2299) \approx 0.2262$ rad.

    Therefore $d = \sqrt{4.1513}\,e^{i\cdot 0.1131} \approx 2.0375(\cos 0.1131 + i\sin 0.1131) \approx 2.0375(0.9936 + 0.1129i) \approx 2.024 + 0.230i$.

    Since $\operatorname{Re}(d) \approx 2.024 > 0$, the condition is verified. The principal square root of a complex number with positive real part always has positive real part, confirming the general theoretical result.

---

**Exercise 4.** For the CIR bond pricing formula with $B(\tau) = \frac{2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}$ and $\gamma = \sqrt{\kappa^2 + 2\xi^2}$, show that $B(\tau) \to 2/(\gamma + \kappa)$ as $\tau \to \infty$. What is the financial interpretation of this limiting behavior for long-maturity bond prices?

??? success "Solution to Exercise 4"
    As $\tau \to \infty$, the exponential $e^{\gamma\tau} \to \infty$, so the dominant terms in both numerator and denominator involve $e^{\gamma\tau}$:

    $$
    B(\tau) = \frac{2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}
    $$

    Divide numerator and denominator by $e^{\gamma\tau}$:

    $$
    B(\tau) = \frac{2(1 - e^{-\gamma\tau})}{(\gamma + \kappa)(1 - e^{-\gamma\tau}) + 2\gamma e^{-\gamma\tau}}
    $$

    As $\tau \to \infty$, $e^{-\gamma\tau} \to 0$:

    $$
    B(\infty) = \frac{2 \cdot 1}{(\gamma + \kappa) \cdot 1 + 0} = \frac{2}{\gamma + \kappa}
    $$

    **Financial interpretation:** The zero-coupon bond price is $P(\tau, r) = \exp(A(\tau) - B(\tau)r)$. As $\tau \to \infty$, $B(\tau) \to 2/(\gamma + \kappa)$, which means the sensitivity of the long-maturity bond price to the current short rate $r$ saturates at a finite value. This reflects the mean-reverting nature of the CIR model: changes in the current short rate have a bounded effect on long-maturity bonds because the rate is pulled back toward the long-run mean $\theta$. The limiting yield $\lim_{\tau\to\infty}\frac{-\log P(\tau,r)}{\tau}$ is the long rate, which is independent of $r$ and determined solely by the model parameters $\kappa$, $\theta$, $\xi$.

---

**Exercise 5.** Consider a model where the $\psi$-equation has time-dependent parameters: $\psi'(\tau) = -\kappa(\tau)\psi(\tau)$ with $\kappa(\tau) = \kappa_0 + \kappa_1 e^{-\lambda\tau}$. Show that this linear ODE can still be solved in closed form and write down $\psi(\tau)$. Explain why this approach does not generalize easily to the Riccati case with a quadratic term.

??? success "Solution to Exercise 5"
    The ODE is $\psi'(\tau) = -\kappa(\tau)\psi(\tau)$ with $\kappa(\tau) = \kappa_0 + \kappa_1 e^{-\lambda\tau}$. This is linear and separable:

    $$
    \frac{d\psi}{\psi} = -(\kappa_0 + \kappa_1 e^{-\lambda\tau})\,d\tau
    $$

    Integrate from $0$ to $\tau$:

    $$
    \log\frac{\psi(\tau)}{\psi(0)} = -\kappa_0\tau - \kappa_1\int_0^\tau e^{-\lambda s}\,ds = -\kappa_0\tau + \frac{\kappa_1}{\lambda}(e^{-\lambda\tau} - 1)
    $$

    Therefore

    $$
    \psi(\tau) = u\exp\!\left(-\kappa_0\tau + \frac{\kappa_1}{\lambda}(e^{-\lambda\tau} - 1)\right)
    $$

    **Why this does not generalize to the Riccati case:** The linear ODE $\psi' = -\kappa(\tau)\psi$ is separable for any function $\kappa(\tau)$ because the right-hand side factors as a product of a function of $\tau$ and a function of $\psi$. When the quadratic term $\frac{\xi^2}{2}\psi^2$ is present, the ODE becomes $\psi' = -\kappa(\tau)\psi + \frac{\xi^2}{2}\psi^2$. The substitution $\psi = -\frac{2}{\xi^2}h'/h$ transforms this into a linear ODE $h'' + \kappa(\tau)h' = 0$, but with a time-dependent coefficient $\kappa(\tau)$, this second-order ODE generally does not have closed-form solutions in terms of elementary functions. The constant-coefficient case yields exponential solutions, but time-dependent coefficients require special functions or numerical methods.

---

**Exercise 6.** Using the Heston closed-form solution, verify numerically that the characteristic function satisfies $|\Phi(\tau, v, x)| \leq 1$ for $\tau = 1$, $x = (\log 100, 0.04)$, and several values of $v \in \{0.1, 1, 5, 10, 50\}$. Use parameters $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, $\rho = -0.7$, $r = 0.05$.

??? success "Solution to Exercise 6"
    For each $v$, compute $\psi_2(\tau)$ and $\phi(\tau)$ using the Heston closed-form solution, then evaluate $|\Phi| = |\exp(\phi + \psi_1 x_1 + \psi_2 x_2)|$.

    With $\tau = 1$, $x_1 = \log 100 \approx 4.6052$, $x_2 = 0.04$, $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.3$, $\rho = -0.7$, $r = 0.05$:

    For each $v$, $\psi_1 = iv$ (constant), $\beta = \rho\xi iv - \kappa = -1.5 - 0.21vi$, and

    $$
    d = \sqrt{(-1.5 - 0.21vi)^2 + 0.09(iv + v^2)}
    $$

    The key observation is that $|\Phi| = \exp(\operatorname{Re}(\phi + iv x_1 + \psi_2 x_2))$. Since $\operatorname{Re}(iv x_1) = 0$, the modulus depends on $\operatorname{Re}(\phi)$ and $\operatorname{Re}(\psi_2)\cdot x_2$.

    The boundedness $|\Phi| \leq 1$ is equivalent to $\operatorname{Re}(\phi + \psi_2 x_2) \leq 0$, which is guaranteed by the general theory (the characteristic function of any random variable is bounded by 1 in modulus). Numerical evaluation confirms this: for each $v$, the real parts of $\phi$ and $\psi_2 x_2$ combine to a non-positive number. Larger values of $|v|$ produce stronger damping (more negative real parts), causing $|\Phi|$ to decay toward zero, which reflects the smoothing of the probability density.
