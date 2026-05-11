# Affine Term Structure


Many short-rate models (including Vasicek and CIR) belong to the **affine term structure** class. Affine structure explains why bond prices have closed forms and provides a framework for multi-factor generalizations.

---

## Affine bond prices


A term structure model is affine if zero-coupon bond prices can be written as

$$
P(t,T) = \exp\big(A(t,T) - B(t,T)^{\top}X_t\big)
$$


where:

- $X_t$ is a state vector (often including the short rate),
- $A$ and $B$ are deterministic functions.

In the one-factor case, $X_t=r_t$.

---

## Why affine models are tractable


Affine models lead to:

- exponential-affine characteristic functions,
- Riccati-type ODEs for $A$ and $B$,
- closed-form bond prices and efficient option pricing in many cases.

This is analogous to affine stochastic volatility (e.g., Heston).

---

## Examples


- **Vasicek:** Gaussian affine model.
- **CIR:** square-root affine model.
- **Multi-factor affine models:** sums of OU/CIR factors.

These models are widely used for curve and swaption pricing (often with shifts).

---

## Fitting the initial yield curve


A common practical extension is **time-dependent drift** (e.g., Hull–White):

- preserves affine structure,
- fits today’s yield curve exactly,
- retains analytical tractability.

---

## Key takeaways


- Affine structure yields exponential-affine bond prices.
- Vasicek and CIR are key affine examples.
- Affine term structure theory supports scalable multi-factor extensions.

---

## Further reading


- Duffie & Kan, affine term structure models.
- Filipović, *Term-Structure Models*.
- Brigo & Mercurio, affine short-rate modeling.

---

## Exercises

**Exercise 1.** For the affine bond price $P(t,T) = e^{A(t,T) - B(t,T)r_t}$, compute the yield $R(t,T) = -\ln P(t,T)/(T-t)$ and the instantaneous forward rate $f(t,T) = -\partial_T \ln P(t,T)$. Express both in terms of $A$ and $B$ and their derivatives.

??? success "Solution to Exercise 1"
    Starting from the affine bond price $P(t,T) = e^{A(t,T) - B(t,T)r_t}$, we have

    $$
    \ln P(t,T) = A(t,T) - B(t,T)r_t
    $$

    **Yield.** By definition,

    $$
    R(t,T) = -\frac{\ln P(t,T)}{T-t} = \frac{-A(t,T) + B(t,T)r_t}{T-t}
    $$

    Hence the yield is an affine (linear) function of $r_t$ with slope $B(t,T)/(T-t)$ and intercept $-A(t,T)/(T-t)$.

    **Instantaneous forward rate.** By definition,

    $$
    f(t,T) = -\frac{\partial}{\partial T}\ln P(t,T) = -\frac{\partial A}{\partial T}(t,T) + \frac{\partial B}{\partial T}(t,T)\,r_t
    $$

    This confirms that the forward rate is also affine in $r_t$. The slope is $\partial_T B(t,T)$ and the intercept is $-\partial_T A(t,T)$. In particular, $f(t,t) = r_t$ requires $\partial_T B(t,T)\big|_{T=t} = 1$ and $\partial_T A(t,T)\big|_{T=t} = 0$, which are consistent with the boundary conditions $A(t,t) = 0$ and $B(t,t) = 0$.

---

---

**Exercise 2.** Verify that the Vasicek model with $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$ is affine by showing that the Riccati equations for $A$ and $B$ have the required form $\partial_T B = -1 + \kappa B$ and $\partial_T A = \kappa\theta B - \frac{1}{2}\sigma^2 B^2$ with $A(T,T) = 0$, $B(T,T) = 0$.

??? success "Solution to Exercise 2"
    In the Vasicek model, $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$, so $\mu^{\mathbb{Q}}(r) = \kappa(\theta - r)$ and $\sigma(r) = \sigma$ (constant). The drift is affine in $r$ and the squared diffusion $\sigma^2$ is constant (trivially affine in $r$).

    Substituting the ansatz $P(t,T) = e^{A(\tau) - B(\tau)r}$ with $\tau = T - t$ into the bond pricing PDE

    $$
    \frac{\partial P}{\partial t} + \kappa(\theta - r)\frac{\partial P}{\partial r} + \frac{1}{2}\sigma^2\frac{\partial^2 P}{\partial r^2} = rP
    $$

    yields (after dividing by $P$):

    $$
    -A'(\tau) + B'(\tau)r - \kappa(\theta - r)B(\tau) + \frac{1}{2}\sigma^2 B(\tau)^2 = r
    $$

    where primes denote derivatives with respect to $\tau$. Collecting powers of $r$:

    - **Coefficient of $r$:** $B'(\tau) + \kappa B(\tau) = 1$, equivalently $\partial_T B = -1 + \kappa B$ (since $\partial_T = -\partial_\tau$).
    - **Constant term:** $-A'(\tau) - \kappa\theta B(\tau) + \frac{1}{2}\sigma^2 B(\tau)^2 = 0$, equivalently $\partial_T A = \kappa\theta B - \frac{1}{2}\sigma^2 B^2$.

    The boundary conditions at $\tau = 0$ (i.e., $T = t$) come from $P(T,T) = 1$, giving $A(T,T) = 0$ and $B(T,T) = 0$. These are Riccati-type ODEs (linear in $B$, then linear in $A$ once $B$ is known), confirming that Vasicek is affine.

---

---

**Exercise 3.** Explain why the CIR model is affine but the Black-Karasinski model is not. What specific structural property of the drift and diffusion is required for affine structure?

??? success "Solution to Exercise 3"
    An affine term structure model requires that the risk-neutral drift $\mu^{\mathbb{Q}}(t,r)$ and the squared diffusion $\sigma(t,r)^2$ are both **affine functions of the state variable** $r$. Specifically, they must take the form

    $$
    \mu^{\mathbb{Q}}(t,r) = a(t) + b(t)\,r, \qquad \sigma(t,r)^2 = c(t) + d(t)\,r
    $$

    for deterministic functions $a, b, c, d$.

    **CIR model:** $\mu^{\mathbb{Q}} = \kappa(\theta - r) = \kappa\theta - \kappa r$ (affine in $r$) and $\sigma^2 = \sigma^2 r$ (affine in $r$ with $c = 0$, $d = \sigma^2$). Both conditions are satisfied, so CIR is affine.

    **Black-Karasinski model:** The dynamics are $d\ln r_t = [\theta(t) - a(t)\ln r_t]\,dt + \sigma(t)\,dW_t$, meaning $r_t$ is lognormal. By Ito's lemma, the SDE for $r_t$ itself involves terms like $r\ln r$, which is **not** affine in $r$. Moreover, the squared diffusion for $r_t$ is $\sigma(t)^2 r_t^2$, which is quadratic (not affine) in $r$. When one substitutes into the bond pricing PDE, the coefficients are not polynomial of degree one in $r$, so the PDE cannot be separated into Riccati ODEs. Therefore Black-Karasinski is not affine.

    The key structural requirement is: both drift and squared volatility must be at most linear (affine) in the state.

---

---

**Exercise 4.** In a two-factor affine model with state $X_t = (r_t, v_t)$, the bond price is $P(t,T) = e^{A(t,T) - B_1(t,T)r_t - B_2(t,T)v_t}$. Discuss the advantage of having a second factor $v_t$ for fitting the yield curve and its volatility structure.

??? success "Solution to Exercise 4"
    In a two-factor affine model, the bond price $P(t,T) = e^{A(t,T) - B_1(t,T)r_t - B_2(t,T)v_t}$ depends on two state variables. The advantages of the second factor $v_t$ include:

    **Yield curve fitting.** With a single factor $r_t$, the yield at any maturity is $R(t,T) = -A/(T-t) + B_1 r_t/(T-t)$, so all yields move in lockstep with $r_t$ (perfect correlation across maturities). A second factor $v_t$ adds a second degree of freedom: $R(t,T) = -A/(T-t) + B_1 r_t/(T-t) + B_2 v_t/(T-t)$, allowing yields at different maturities to move partially independently.

    **Volatility structure.** If $v_t$ governs the volatility of $r_t$ (as in stochastic volatility models), the model captures time-varying yield volatility. This is critical for pricing interest rate options, which depend on the volatility term structure.

    **Richer dynamics.** The two-factor model can generate yield curve steepening, flattening, and twist movements that a one-factor model cannot reproduce. Empirically, the first three principal components of yield changes (level, slope, curvature) explain over 99% of variation, so at least two or three factors are needed for realistic dynamics.

    **Calibration.** The additional parameters allow simultaneous calibration to the yield curve and the volatility surface (caps, swaptions), whereas a single-factor model typically cannot fit both.

---

---

**Exercise 5.** Show that in an affine model, the yield $R(t,T) = -A(t,T)/(T-t) + B(t,T)r_t/(T-t)$ is linear (affine) in the short rate $r_t$. Why does this property make calibration and pricing computationally efficient?

??? success "Solution to Exercise 5"
    From $\ln P(t,T) = A(t,T) - B(t,T)r_t$, the yield is

    $$
    R(t,T) = -\frac{\ln P(t,T)}{T-t} = \frac{-A(t,T) + B(t,T)r_t}{T-t} = \frac{B(t,T)}{T-t}\,r_t - \frac{A(t,T)}{T-t}
    $$

    This is manifestly affine (linear) in $r_t$. For fixed $t$ and $T$, the coefficients $B(t,T)/(T-t)$ and $-A(t,T)/(T-t)$ are deterministic constants.

    **Computational efficiency.** This linearity has several important consequences:

    1. **Calibration:** Fitting the model to observed yields reduces to a regression-type problem. Since yields are linear in $r_t$, one can use least-squares or maximum likelihood with Gaussian (or chi-squared) transition densities efficiently.

    2. **Pricing:** Bond prices, and hence yields, can be computed without Monte Carlo simulation or numerical PDE methods. One only needs to evaluate the deterministic functions $A$ and $B$ (via Riccati ODEs or closed-form solutions) and plug in the current $r_t$.

    3. **Portfolio analytics:** Sensitivities of bond prices with respect to $r_t$ (duration, convexity) are immediate from the affine form. The dollar duration of a zero-coupon bond is simply $B(t,T) \cdot P(t,T)$.

    4. **Filtering:** In state estimation (e.g., Kalman filtering), the linear relationship between observations (yields) and the latent state ($r_t$) is exactly the structure required for the standard Kalman filter to be optimal.

---

---

**Exercise 6.** The Riccati ODEs in affine models can be solved in closed form for Vasicek and CIR. For a general affine model, these ODEs may require numerical integration. Describe a numerical method (e.g., Runge-Kutta) for solving the Riccati system, and discuss the accuracy requirements for bond pricing applications.

??? success "Solution to Exercise 6"
    For a general affine model, the Riccati system takes the form

    $$
    B'(\tau) = 1 + b\,B(\tau) + \tfrac{1}{2}d\,B(\tau)^2, \quad B(0) = 0
    $$

    $$
    A'(\tau) = -a\,B(\tau) - \tfrac{1}{2}c\,B(\tau)^2, \quad A(0) = 0
    $$

    where the drift is $\mu = a + br$ and the squared diffusion is $c + dr$. When $d \neq 0$ (as in CIR), the $B$-equation is a genuine Riccati ODE (quadratic in $B$). For Vasicek ($d = 0$), it reduces to a linear ODE.

    **Numerical method.** The classical fourth-order Runge-Kutta (RK4) method is well suited:

    1. Discretize $[0, \tau_{\max}]$ with step size $h$.
    2. At each step, compute $B_{n+1}$ from $B_n$ using the RK4 update with the right-hand side $g(B) = 1 + bB + \frac{1}{2}dB^2$.
    3. Once $B(\tau)$ is known on the grid, integrate the $A$-equation (which is linear in $A$ given $B$) by the same RK4 scheme or by quadrature.

    The global error of RK4 is $O(h^4)$, so moderate step sizes (e.g., $h = 0.001$ years) yield errors well below $10^{-8}$ in $A$ and $B$, which translates to sub-basis-point bond price accuracy.

    **Accuracy requirements.** Bond prices enter option pricing formulas (e.g., in the numerator and denominator of forward rates), so relative errors in $P(t,T)$ should be at most $10^{-6}$ to $10^{-8}$. Since $P = e^{A - Br}$ and typical values of $Br$ are of order 0.1 to 1, an absolute error of $10^{-8}$ in $A$ and $B$ suffices. Adaptive step-size control (e.g., Dormand-Prince RK45) can be used to meet a prescribed tolerance automatically. For multi-factor models, the system becomes a coupled vector Riccati ODE and the same methods apply with the state vector $(B_1, \ldots, B_n, A)$.
