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
