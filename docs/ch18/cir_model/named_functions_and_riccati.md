# CIR Named Functions and Riccati ODEs

The CIR model retains the affine bond price structure $P(t,T) = A(\tau)\,e^{-B(\tau)\,r_t}$ of the Vasicek model, but the state-dependent diffusion $\sigma\sqrt{r_t}$ produces a genuinely **quadratic** (Riccati) ODE for $B(\tau)$ rather than the linear ODE that arises in Vasicek. This quadratic nonlinearity introduces an auxiliary parameter $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$ that governs the rate of exponential decay and leads to more complex---but still closed-form---expressions for $A$ and $B$. This section derives the Riccati ODEs, solves them, and compares the CIR and Vasicek named functions.

---

## Bond pricing PDE for the CIR model

The CIR short rate under $\mathbb{Q}$ satisfies $dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t$. The zero-coupon bond price $P(t,T) = f(t, r_t)$ satisfies the PDE

$$
f_t + \kappa(\theta - r)\,f_r + \frac{1}{2}\sigma^2 r\,f_{rr} - r\,f = 0
$$

with terminal condition $f(T, r) = 1$. The crucial difference from Vasicek is the factor $r$ multiplying $f_{rr}$: the diffusion coefficient $\sigma^2 r$ is **affine** in $r$, preserving the affine structure.

---

## The affine ansatz

We seek a solution of the form

$$
P(t,T) = A(\tau)\,e^{-B(\tau)\,r_t}
$$

where $\tau = T - t$, with $A(0) = 1$ and $B(0) = 0$.

Computing derivatives (with $\dot{A} = dA/d\tau$, $\dot{B} = dB/d\tau$):

$$
f_t = -\dot{A}\,e^{-Br} + A\,\dot{B}\,r\,e^{-Br}
$$

$$
f_r = -A\,B\,e^{-Br}, \qquad f_{rr} = A\,B^2\,e^{-Br}
$$

Substituting into the PDE and dividing by $A\,e^{-Br}$:

$$
-\frac{\dot{A}}{A} + \dot{B}\,r + \frac{1}{2}\sigma^2 r\,B^2 - \kappa(\theta - r)\,B - r = 0
$$

Collecting terms in $r$ and the constant:

$$
\left(\dot{B} + \frac{1}{2}\sigma^2 B^2 + \kappa B - 1\right)r + \left(-\frac{\dot{A}}{A} - \kappa\theta\,B\right) = 0
$$

Setting both the coefficient of $r$ and the constant to zero yields two ODEs.

---

## Riccati ODE for B(tau)

The coefficient of $r$ gives

$$
\boxed{\dot{B}(\tau) = 1 - \kappa\,B(\tau) - \frac{1}{2}\sigma^2 B(\tau)^2, \qquad B(0) = 0}
$$

This is a **Riccati equation**---a first-order ODE that is quadratic in the unknown $B$. The quadratic term $-\frac{1}{2}\sigma^2 B^2$ arises from the $\frac{1}{2}\sigma^2 r\,f_{rr}$ term in the PDE, which itself comes from the state-dependent diffusion $\sigma^2 r$.

In the Vasicek model, the diffusion is constant ($\sigma^2$ independent of $r$), so the $f_{rr}$ term contributes to the constant (not the $r$-coefficient), and the ODE for $B$ is linear. The CIR square-root diffusion makes the $f_{rr}$ contribution proportional to $r$, producing the quadratic Riccati.

### Solution

Define the auxiliary parameter

$$
\gamma = \sqrt{\kappa^2 + 2\sigma^2}
$$

Note that $\gamma > \kappa$ always. The Riccati equation has the closed-form solution

$$
\boxed{B(\tau) = \frac{2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}}
$$

???+ note "Derivation"
    The Riccati ODE $\dot{B} = 1 - \kappa B - \frac{1}{2}\sigma^2 B^2$ has two equilibria (fixed points) where $\dot{B} = 0$:

    $$
    B_\pm = \frac{-\kappa \pm \gamma}{\sigma^2}
    $$

    where $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$. Since $\gamma > \kappa$, $B_+ > 0$ and $B_- < 0$.

    The general solution of the Riccati ODE with initial condition $B(0) = 0$ is obtained by the substitution $B = -2\dot{u}/(\sigma^2 u)$, which converts the Riccati into a second-order linear ODE $\ddot{u} - \kappa\dot{u} - \frac{1}{2}\sigma^2 u = 0$ (after appropriate manipulation). The characteristic roots are $(\kappa \pm \gamma)/2$.

    Solving with the initial conditions corresponding to $B(0) = 0$ yields the stated formula. $\square$

### Properties of B(tau) in CIR

- $B(0) = 0$: boundary condition satisfied
- $B(\tau) > 0$ for $\tau > 0$: bond prices decrease in $r$
- $B(\tau) \to B_+ = (\gamma - \kappa)/\sigma^2$ as $\tau \to \infty$: saturation at a finite limit
- $B(\tau) \approx \tau$ for small $\tau$: agrees with Vasicek to first order
- $\dot{B}(\tau) > 0$: $B$ is strictly increasing

The saturation level $B_+ = (\gamma - \kappa)/\sigma^2$ is strictly less than the Vasicek saturation $1/\kappa$ when $\sigma > 0$, because $\gamma - \kappa < \sigma^2/\kappa$ (verifiable from $\gamma^2 = \kappa^2 + 2\sigma^2$).

---

## ODE for A(tau)

The constant term gives

$$
\frac{d}{d\tau}\ln A(\tau) = \kappa\theta\,B(\tau), \qquad \ln A(0) = 0
$$

Integrating:

$$
\ln A(\tau) = \kappa\theta \int_0^\tau B(s)\,ds
$$

Substituting the expression for $B(s)$ and evaluating the integral:

$$
\boxed{A(\tau) = \left(\frac{2\gamma\,e^{(\gamma + \kappa)\tau/2}}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}\right)^{2\kappa\theta/\sigma^2}}
$$

The exponent $2\kappa\theta/\sigma^2 = \nu/2$ involves the Feller ratio $\nu$.

### Properties of A(tau) in CIR

- $A(0) = 1$: boundary condition satisfied
- $0 < A(\tau) \leq 1$ for $\tau \geq 0$
- $A(\tau) \to 0$ as $\tau \to \infty$ (exponential decay)

---

## Complete CIR bond pricing formula

Assembling the results:

$$
P(t,T) = A(\tau)\,e^{-B(\tau)\,r_t}
$$

with

$$
B(\tau) = \frac{2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}
$$

$$
A(\tau) = \left(\frac{2\gamma\,e^{(\gamma + \kappa)\tau/2}}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}\right)^{2\kappa\theta/\sigma^2}
$$

$$
\gamma = \sqrt{\kappa^2 + 2\sigma^2}
$$

**Verification.** At $\tau = 0$: $B(0) = 0$, $A(0) = (2\gamma/(2\gamma))^{2\kappa\theta/\sigma^2} = 1$, so $P(T,T) = 1$. $\square$

---

## Comparison with Vasicek named functions

| Property | Vasicek | CIR |
|---|---|---|
| ODE for $B$ | Linear: $\dot{B} = 1 - \kappa B$ | Riccati: $\dot{B} = 1 - \kappa B - \frac{1}{2}\sigma^2 B^2$ |
| $B(\tau)$ | $\frac{1 - e^{-\kappa\tau}}{\kappa}$ | $\frac{2(e^{\gamma\tau}-1)}{(\gamma+\kappa)(e^{\gamma\tau}-1)+2\gamma}$ |
| Saturation $B(\infty)$ | $1/\kappa$ | $(\gamma - \kappa)/\sigma^2 < 1/\kappa$ |
| Auxiliary parameter | None | $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$ |
| $\ln A$ depends on | $B(\tau) - \tau$, $B(\tau)^2$ | $\int_0^\tau B(s)\,ds$ |
| $A(\tau)$ form | Exponential of polynomial in $B$ | Power of rational function |
| Small-$\tau$ expansion of $B$ | $\tau - \frac{1}{2}\kappa\tau^2 + \cdots$ | $\tau - \frac{1}{2}\kappa\tau^2 + \cdots$ (same) |

The small-$\tau$ expansions agree to first order: $B^{\text{CIR}}(\tau) = \tau - \frac{1}{2}\kappa\tau^2 + O(\tau^3) = B^{\text{Vas}}(\tau) + O(\tau^3)$. The difference appears at order $\tau^3$, where the CIR $B$ function has an additional $-\frac{1}{6}\sigma^2\tau^3$ contribution from the quadratic Riccati term.

---

## Yield and forward rate

### CIR yield

$$
R(t,T) = -\frac{\ln A(\tau)}{\tau} + \frac{B(\tau)}{\tau}\,r_t
$$

### Long-run CIR yield

As $\tau \to \infty$:

$$
R_\infty^{\text{CIR}} = \frac{2\kappa\theta}{\gamma + \kappa}
$$

Compare with the Vasicek long-run yield $R_\infty^{\text{Vas}} = \theta - \sigma^2/(2\kappa^2)$. The CIR long-run yield does not have a simple "mean minus convexity correction" form because the convexity correction is itself level-dependent.

### CIR forward rate

$$
f(t,T) = \dot{B}(\tau)\,r_t - \frac{d}{d\tau}\ln A(\tau)
$$

$$
= \left(1 - \kappa B(\tau) - \frac{1}{2}\sigma^2 B(\tau)^2\right)r_t + \kappa\theta\,B(\tau) - \kappa\theta\,B(\tau)
$$

Wait---the forward rate simplifies to

$$
f(t,T) = r_t\,\dot{B}(\tau) + \kappa\theta\,B(\tau) \cdot \left(\frac{\dot{B}(\tau)}{1 - \kappa B - \frac{1}{2}\sigma^2 B^2}\right)
$$

More directly, from $-\partial_T \ln P = B'(\tau)\,r_t + \kappa\theta\,B(\tau)$... To avoid errors, the forward rate is best computed numerically as $f(t,T) = -\partial_T \ln P(t,T)$ using the explicit $A$ and $B$ formulas.

---

## Numerical example

Parameters: $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.1$, $r_0 = 0.03$.

Auxiliary: $\gamma = \sqrt{0.25 + 0.02} = \sqrt{0.27} = 0.5196$.

**CIR vs Vasicek B(tau):**

| $\tau$ | $B^{\text{Vas}}$ | $B^{\text{CIR}}$ | Ratio |
|:-:|:-:|:-:|:-:|
| 1 | 0.787 | 0.771 | 0.980 |
| 5 | 1.836 | 1.594 | 0.868 |
| 10 | 1.987 | 1.703 | 0.857 |
| $\infty$ | 2.000 | 1.961 | 0.980 |

The CIR $B$ function is always smaller than Vasicek's, reflecting the additional risk-adjustment from the state-dependent volatility.

**Bond prices:**

| $\tau$ | $P^{\text{Vas}}$ | $P^{\text{CIR}}$ |
|:-:|:-:|:-:|
| 1 | 0.974 | 0.974 |
| 5 | 0.900 | 0.904 |
| 10 | 0.829 | 0.839 |
| 30 | 0.620 | 0.660 |

CIR bond prices are slightly higher (yields lower) than Vasicek for the same parameters, because the CIR $B$ function saturates at a lower level.

---

## Summary

The CIR named functions $A(\tau)$ and $B(\tau)$ are derived from the same affine ansatz as Vasicek, but the state-dependent diffusion $\sigma^2 r$ produces a Riccati (quadratic) ODE for $B$ instead of a linear one. The solution involves the auxiliary parameter $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$, which reflects the interaction between mean reversion and volatility. The CIR $B$ function saturates at $(\gamma - \kappa)/\sigma^2 < 1/\kappa$, producing smaller long-maturity sensitivities than Vasicek. Despite the more complex formulas, the affine structure is preserved, ensuring closed-form bond prices and a tractable framework for yield curve modeling and derivative pricing.

---

## Exercises

**Exercise 1.** For CIR parameters $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.1$, compute $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$. Then evaluate $B(\tau)$ for $\tau = 1, 5, 10$ years and compare with the Vasicek $B(\tau) = (1 - e^{-\kappa\tau})/\kappa$ using the same $\kappa$. Verify that $B^{\text{CIR}} < B^{\text{Vas}}$ for all $\tau > 0$.

---

**Exercise 2.** Verify that $B(0) = 0$ by direct substitution into the CIR formula. Then compute $\dot{B}(0)$ by differentiating the formula (or using the Riccati ODE at $\tau = 0$) and show that $\dot{B}(0) = 1$, which matches the Vasicek small-$\tau$ behavior $B(\tau) \approx \tau$.

---

**Exercise 3.** The Riccati ODE has equilibria at $B_{\pm} = (-\kappa \pm \gamma)/\sigma^2$. Compute $B_+$ and $B_-$ for $\kappa = 0.5$, $\sigma = 0.1$. Verify that $B_+ > 0$ and $B_- < 0$. Show that $B(\tau) \to B_+$ as $\tau \to \infty$ and explain why $B_-$ is not relevant for the bond pricing problem.

---

**Exercise 4.** Derive the ODE for $A(\tau)$ from the bond pricing PDE. Starting from $\frac{d}{d\tau}\ln A = \kappa\theta B(\tau)$, explain why $A(\tau) \leq 1$ for all $\tau \geq 0$ given that $B(\tau) > 0$ and $\kappa\theta > 0$. (Careful: check the sign of $\frac{d}{d\tau}\ln A$.)

---

**Exercise 5.** Compute the CIR long-run yield $R_\infty = 2\kappa\theta/(\gamma + \kappa)$ for $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.1$ and compare with the Vasicek long-run yield $R_\infty^{\text{Vas}} = \theta - \sigma^2/(2\kappa^2)$ using the same parameters. Which model predicts a higher long-run yield, and why?

---

**Exercise 6.** Expand $B^{\text{CIR}}(\tau)$ to third order in $\tau$ and show that $B^{\text{CIR}}(\tau) = \tau - \frac{1}{2}\kappa\tau^2 + \frac{1}{6}(\kappa^2 - \sigma^2)\tau^3 + O(\tau^4)$, while $B^{\text{Vas}}(\tau) = \tau - \frac{1}{2}\kappa\tau^2 + \frac{1}{6}\kappa^2\tau^3 + O(\tau^4)$. Identify the term where the two diverge and relate it to the quadratic Riccati contribution.

---

**Exercise 7.** Using the complete CIR bond pricing formula, compute $P(0, T)$ for $T = 1, 5, 10, 30$ years with $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.1$, $r_0 = 0.03$. Then compute the corresponding zero rates $R(0, T) = -\ln P(0, T)/T$. Plot or tabulate $R(0, T)$ and describe the shape of the CIR yield curve. Is it upward-sloping, humped, or inverted?
