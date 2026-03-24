# Zero-Coupon Bond Pricing Under CIR

The Cox-Ingersoll-Ross model belongs to the affine class of short-rate models, which means zero-coupon bond prices admit an exponential-affine closed-form solution. This analytical tractability is one of the main reasons the CIR model remains widely used in practice. Unlike the Vasicek model, the CIR bond price formula involves a square-root characteristic that prevents negative rates from appearing in the discount factor. This section derives the closed-form bond price formula from first principles, starting from the bond pricing PDE, introducing the affine ansatz, solving the resulting Riccati ordinary differential equations, and verifying the solution.

---

## Risk-neutral pricing framework

Under the risk-neutral measure $\mathbb{Q}$, the CIR short rate satisfies

$$
dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t^{\mathbb{Q}}
$$

where $\kappa > 0$ is the speed of mean reversion, $\theta > 0$ is the long-run mean, and $\sigma > 0$ is the volatility parameter. The zero-coupon bond price at time $t$ for maturity $T$ is defined by the conditional expectation

$$
P(t,T) = \mathbb{E}^{\mathbb{Q}}\!\left[\exp\!\left(-\int_t^T r_s\,ds\right)\,\bigg|\,\mathcal{F}_t\right]
$$

Because the short rate is Markovian, this price depends only on the current rate $r_t$ and the time to maturity $\tau = T - t$, so we write $P(t,T) = f(t, r_t)$.

---

## Bond pricing PDE

Applying Ito's lemma to $f(t, r_t)$ and requiring the discounted bond price $e^{-\int_0^t r_s\,ds}f(t,r_t)$ to be a $\mathbb{Q}$-martingale yields the fundamental PDE

$$
f_t + \kappa(\theta - r)f_r + \frac{1}{2}\sigma^2 r\,f_{rr} - r\,f = 0
$$

with the terminal condition $f(T, r) = 1$ for all $r \geq 0$. The key feature distinguishing this PDE from the Vasicek case is the factor of $r$ multiplying both $f_{rr}$ (from the square-root diffusion) and $f$ (from discounting). This state-dependent structure is precisely what makes the CIR model affine.

---

## Exponential-affine ansatz

The affine structure of the CIR PDE suggests searching for a solution of the form

$$
f(t, r) = A(\tau)\exp\!\big(-B(\tau)\,r\big)
$$

where $\tau = T - t$ is the time to maturity, $A(\tau)$ is a deterministic function, and $B(\tau)$ determines the rate sensitivity. The terminal condition $f(T, r) = 1$ translates to

$$
A(0) = 1, \qquad B(0) = 0
$$

Computing the required partial derivatives (noting $\partial_t = -\partial_\tau$):

$$
f_t = \left(-A'(\tau) + A(\tau)B'(\tau)\,r\right)\exp\!\big(-B(\tau)\,r\big)
$$

$$
f_r = -A(\tau)B(\tau)\exp\!\big(-B(\tau)\,r\big)
$$

$$
f_{rr} = A(\tau)B(\tau)^2\exp\!\big(-B(\tau)\,r\big)
$$

---

## Deriving the Riccati system

Substituting the ansatz into the PDE and dividing through by $A(\tau)\exp(-B(\tau)\,r)$ yields

$$
-\frac{A'(\tau)}{A(\tau)} + B'(\tau)\,r - \kappa\theta\,B(\tau) + \kappa\,B(\tau)\,r + \frac{1}{2}\sigma^2 B(\tau)^2\,r - r = 0
$$

Collecting terms by powers of $r$:

- **Coefficient of $r$**: $B'(\tau) + \kappa\,B(\tau) + \frac{1}{2}\sigma^2 B(\tau)^2 - 1 = 0$
- **Constant term**: $-\frac{A'(\tau)}{A(\tau)} - \kappa\theta\,B(\tau) = 0$

Since these must hold for all $r \geq 0$, each coefficient must vanish separately, producing the system:

**Riccati ODE for $B$:**

$$
B'(\tau) = 1 - \kappa\,B(\tau) - \frac{1}{2}\sigma^2 B(\tau)^2, \qquad B(0) = 0
$$

**Linear ODE for $A$:**

$$
\frac{A'(\tau)}{A(\tau)} = -\kappa\theta\,B(\tau), \qquad A(0) = 1
$$

equivalently $\ln A(\tau) = -\kappa\theta\int_0^\tau B(s)\,ds$.

---

## Solving the Riccati ODE

The Riccati equation for $B$ is a quadratic ODE. Define the discriminant

$$
\gamma = \sqrt{\kappa^2 + 2\sigma^2}
$$

This quantity $\gamma$ plays a central role analogous to $\kappa$ in the Vasicek model but incorporates the volatility through the square-root diffusion. The solution is

$$
B(\tau) = \frac{2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}
$$

???+ note "Derivation of $B(\tau)$"

    The Riccati ODE $B' = 1 - \kappa B - \frac{1}{2}\sigma^2 B^2$ with $B(0) = 0$ can be solved by factoring the right-hand side. Write

    $$
    B' = -\frac{\sigma^2}{2}(B - B_+)(B - B_-)
    $$

    where $B_\pm = \frac{-\kappa \pm \gamma}{\sigma^2}$ are the roots of $1 - \kappa B - \frac{1}{2}\sigma^2 B^2 = 0$. Using partial fractions and separating variables:

    $$
    \frac{dB}{(B - B_+)(B - B_-)} = -\frac{\sigma^2}{2}\,d\tau
    $$

    $$
    \frac{1}{B_+ - B_-}\ln\frac{B - B_+}{B - B_-} = -\frac{\sigma^2}{2}\tau + C
    $$

    Applying $B(0) = 0$ to determine $C$, then solving for $B(\tau)$, yields the stated formula after algebraic simplification using $B_+ - B_- = \frac{2\gamma}{\sigma^2}$. $\square$

**Verification of initial condition**: At $\tau = 0$, the numerator $2(e^0 - 1) = 0$, so $B(0) = 0$. $\checkmark$

**Behavior as $\tau \to \infty$**: As $\tau \to \infty$, $B(\tau) \to \frac{2}{\gamma + \kappa} = B_+$, which is the positive equilibrium of the Riccati ODE.

---

## Solving for A

Substituting $B(\tau)$ into the ODE for $A$ and integrating:

$$
\ln A(\tau) = -\kappa\theta\int_0^\tau B(s)\,ds
$$

After evaluating the integral (which requires careful manipulation of the exponential terms), the result is

$$
A(\tau) = \left(\frac{2\gamma\,e^{(\kappa + \gamma)\tau/2}}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}\right)^{2\kappa\theta/\sigma^2}
$$

???+ note "Derivation of $A(\tau)$"

    Define $D(\tau) = (\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma$. Then $B(\tau) = \frac{2(e^{\gamma\tau} - 1)}{D(\tau)}$ and

    $$
    D'(\tau) = \gamma(\gamma + \kappa)e^{\gamma\tau}
    $$

    One can verify that

    $$
    B(\tau) = \frac{2}{\sigma^2}\left(\frac{D'(\tau)}{D(\tau)} - \frac{\gamma + \kappa}{2}\right)
    $$

    so the integral becomes

    $$
    \int_0^\tau B(s)\,ds = \frac{2}{\sigma^2}\left[\ln\frac{D(\tau)}{D(0)} - \frac{(\gamma + \kappa)\tau}{2}\right]
    $$

    Since $D(0) = 2\gamma$, this gives

    $$
    \ln A(\tau) = -\kappa\theta\cdot\frac{2}{\sigma^2}\left[\ln\frac{D(\tau)}{2\gamma} - \frac{(\gamma + \kappa)\tau}{2}\right] = \frac{2\kappa\theta}{\sigma^2}\left[\frac{(\gamma + \kappa)\tau}{2} - \ln\frac{D(\tau)}{2\gamma}\right]
    $$

    Exponentiating yields the stated formula. $\square$

**Verification of initial condition**: At $\tau = 0$, the denominator equals $2\gamma$ and the exponential equals $1$, giving $A(0) = 1$. $\checkmark$

---

## Complete bond price formula

Combining both components, the CIR zero-coupon bond price is

$$
P(t,T) = A(\tau)\,e^{-B(\tau)\,r_t}
$$

where $\tau = T - t$ and

$$
A(\tau) = \left(\frac{2\gamma\,e^{(\kappa + \gamma)\tau/2}}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}\right)^{2\kappa\theta/\sigma^2}
$$

$$
B(\tau) = \frac{2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}
$$

$$
\gamma = \sqrt{\kappa^2 + 2\sigma^2}
$$

!!! tip "Interpreting the formula"
    The bond price has two components: $A(\tau)$ captures the effect of mean reversion and long-run mean on accumulated discounting, while $e^{-B(\tau)r_t}$ captures the sensitivity to the current short rate. Higher current rates $r_t$ reduce the bond price through the exponential factor, with the sensitivity governed by $B(\tau)$.

---

## Properties of the bond price

### Monotonicity in the short rate

Since $B(\tau) > 0$ for $\tau > 0$, the bond price is strictly decreasing in $r_t$:

$$
\frac{\partial P}{\partial r_t} = -B(\tau)\,P(t,T) < 0
$$

This confirms the economic intuition that higher current interest rates reduce the present value of future cash flows.

### Short-maturity limit

As $\tau \to 0^+$:

$$
B(\tau) \approx \tau - \frac{1}{2}(\kappa + \frac{1}{2}\sigma^2)\tau^2 + O(\tau^3)
$$

so for very short maturities, $P(t,T) \approx e^{-r_t\tau}$, which matches the instantaneous discounting rate.

### Long-maturity limit

As $\tau \to \infty$:

$$
B(\tau) \to B_\infty = \frac{2}{\gamma + \kappa}
$$

$$
\ln A(\tau) \sim \frac{2\kappa\theta}{\sigma^2}\left[\frac{\gamma + \kappa}{2} - \gamma\right]\tau = -\frac{\kappa\theta(\gamma - \kappa)}{\sigma^2}\,\tau
$$

Therefore the long-maturity yield is

$$
R_\infty = \lim_{\tau \to \infty}\frac{-\ln P(t,T)}{\tau} = \frac{2\kappa\theta}{\gamma + \kappa}
$$

This long rate is independent of the current short rate $r_t$ and depends only on the model parameters $\kappa$, $\theta$, and $\sigma$.

---

## Comparison with the Vasicek formula

| Feature | Vasicek | CIR |
|---------|---------|-----|
| **Ansatz** | $P = A(\tau)e^{-B(\tau)r}$ | $P = A(\tau)e^{-B(\tau)r}$ |
| **$B(\tau)$ ODE** | $B' = 1 - \kappa B$ (linear) | $B' = 1 - \kappa B - \frac{1}{2}\sigma^2 B^2$ (Riccati) |
| **$B(\tau)$ solution** | $\frac{1 - e^{-\kappa\tau}}{\kappa}$ | $\frac{2(e^{\gamma\tau} - 1)}{(\gamma+\kappa)(e^{\gamma\tau}-1)+2\gamma}$ |
| **Discriminant** | $\kappa$ (trivial) | $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$ |
| **Rate dependence of vol** | None ($\sigma$ constant) | $\sigma\sqrt{r}$ (state-dependent) |
| **Negative rates possible** | Yes | No (if Feller condition holds) |

The additional quadratic term $\frac{1}{2}\sigma^2 B^2$ in the CIR Riccati ODE arises from the state-dependent volatility $\sigma\sqrt{r}$, which introduces an $r$-dependent contribution to $f_{rr}$ in the PDE. When $\sigma \to 0$, both models converge to pure mean-reversion discounting.

---

## Numerical example

Consider CIR parameters $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.1$, and current rate $r_0 = 0.04$.

**Step 1**: Compute the discriminant:

$$
\gamma = \sqrt{0.5^2 + 2(0.1)^2} = \sqrt{0.25 + 0.02} = \sqrt{0.27} \approx 0.5196
$$

**Step 2**: For $\tau = 5$ years, compute $B(5)$:

$$
e^{\gamma \cdot 5} = e^{2.598} \approx 13.44
$$

$$
B(5) = \frac{2(13.44 - 1)}{(0.5196 + 0.5)(13.44 - 1) + 2(0.5196)} = \frac{24.88}{12.68 + 1.039} = \frac{24.88}{13.72} \approx 1.813
$$

**Step 3**: Compute $A(5)$:

$$
A(5) = \left(\frac{2(0.5196)\,e^{(0.5 + 0.5196)(2.5)}}{13.72}\right)^{2(0.5)(0.06)/(0.01)}
$$

$$
= \left(\frac{1.039 \cdot e^{2.549}}{13.72}\right)^{6} = \left(\frac{1.039 \cdot 12.80}{13.72}\right)^{6} \approx (0.969)^6 \approx 0.828
$$

**Step 4**: Bond price:

$$
P(0, 5) = 0.828 \cdot e^{-1.813 \times 0.04} = 0.828 \cdot e^{-0.0725} \approx 0.828 \cdot 0.930 \approx 0.770
$$

The corresponding continuously compounded yield is $R(0, 5) = -\ln(0.770)/5 \approx 0.0523$, or about 5.23%.

---

## Summary

The CIR model produces zero-coupon bond prices of the exponential-affine form $P(t,T) = A(\tau)e^{-B(\tau)r_t}$, where the functions $A$ and $B$ solve a coupled system of ordinary differential equations. The Riccati ODE for $B(\tau)$ --- quadratic rather than linear as in Vasicek --- arises from the state-dependent volatility $\sigma\sqrt{r}$ and is solved in closed form using the discriminant $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$. The resulting formula preserves non-negativity of rates (when the Feller condition holds), provides the long-run yield $R_\infty = 2\kappa\theta/(\gamma + \kappa)$, and reduces to instantaneous discounting at short maturities. This closed-form solution is the foundation for yield curve fitting, bond option pricing, and calibration procedures developed in subsequent sections.

---

## Exercises

**Exercise 1.** Substitute the exponential-affine ansatz $f(t,r) = A(\tau)e^{-B(\tau)r}$ into the CIR bond pricing PDE and derive the two ODEs for $A$ and $B$ by collecting powers of $r$. Show each step explicitly.

---

**Exercise 2.** For $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.08$, compute the discriminant $\gamma$, then evaluate $B(\tau)$ for $\tau = 1, 5, 10, 30$. What is the limiting value $B_\infty = 2/(\gamma + \kappa)$? How close is $B(30)$ to $B_\infty$?

---

**Exercise 3.** Factor the Riccati ODE as $B' = -\frac{\sigma^2}{2}(B - B_+)(B - B_-)$ where $B_{\pm} = (-\kappa \pm \gamma)/\sigma^2$. For $\kappa = 0.5$ and $\sigma = 0.1$, compute $B_+$ and $B_-$. Verify that $B_+ > 0$ is the stable equilibrium and $B_- < 0$ is the unstable equilibrium.

---

**Exercise 4.** Compute the complete CIR bond price $P(0, 10)$ for $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.10$, $r_0 = 0.05$. Show each intermediate step: $\gamma$, $e^{\gamma \cdot 10}$, $B(10)$, the denominator $D(10)$, $A(10)$, and finally $P = A \cdot e^{-Br_0}$.

---

**Exercise 5.** The bond price sensitivity to the short rate is $\partial P/\partial r_t = -B(\tau)P(t,T)$. For a \$1,000,000 face value 10-year zero-coupon bond with the parameters from Exercise 4, compute the DV01 (dollar value of a one-basis-point change in $r_t$). Compare with the Vasicek DV01 using $B^{\text{Vas}}(10) = (1 - e^{-\kappa \cdot 10})/\kappa$.

---

**Exercise 6.** Show that in the limit $\sigma \to 0$, the CIR bond price formula reduces to pure deterministic discounting: $P(t,T) = \exp(-\int_t^T r_s\,ds)$ where $r_s = \theta + (r_t - \theta)e^{-\kappa(s-t)}$. Verify by showing $\gamma \to \kappa$, $B(\tau) \to (1 - e^{-\kappa\tau})/\kappa$, and computing $\lim_{\sigma \to 0} A(\tau)$.

---

**Exercise 7.** Compare the CIR and Vasicek bond prices for $\tau = 1, 5, 10, 30$ using $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.10$, $r_0 = 0.04$. For which maturities is the difference largest? Explain why the CIR price is higher than Vasicek for long maturities by relating the difference to the saturation levels $B_\infty^{\text{CIR}}$ versus $B_\infty^{\text{Vas}} = 1/\kappa$.
